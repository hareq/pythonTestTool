#!/bin/sh

send_ip="10.2.5.153"

send_ssh_port="1022"

loadtest_ssh_port="1022"

load_test_ip=""
test_service=$1
thread_num=$2
durnation=$3
interval="5"


remote_testcase_dir="/home/deploy/test/jmetertestcase/${test_service}";
remote_monitor_dir="/home/deploy/test/tool/${test_service}";

testcase_template_dir="../${test_service}"

local_jmx_file=""

testcase_name=""

csv_file_name=""

new_testcase_dir="../${test_service}/tmp/${thread_num}"

lp_testcase_tar="${test_service}_${thread_num}.tar"

jmeter_sh="/home/deploy/test/apache-jmeter-2.6/bin/jmeter.sh"

remote_jmx_file=""

jtl_file="${remote_testcase_dir}/${thread_num}/${test_service}_${thread_num}.jtl"

function startup(){
	 jmx_file_number=`ls -l ${testcase_template_dir} | grep "\.jmx" | awk '{print $9}' |wc -l`
	
	if [ ${jmx_file_number} -ne 1 ];then
		echo "Error: jmx file error"
		exit 1
	else
		testcase_name=`ls -l ${testcase_template_dir} | grep "\.jmx" | awk '{print $9}'`
	fi
	
	local_jmx_file="../${test_service}/${testcase_name}"
	remote_jmx_file="${remote_testcase_dir}/${thread_num}/${test_service}_${thread_num}.jmx"
	
	 csv_file_number=`ls -l ${testcase_template_dir} | grep -v "\.jmx" | grep ^[^d] | grep -v total | wc -l`
	 
	 if [ ${csv_file_number} -eq 1 ];then
		csv_file_name=`ls -l ${testcase_template_dir} | grep -v "\.jmx" | grep ^[^d] | grep -v total | awk '{print $9}'`

	 elif [ ${csv_file_number} -gt 1 ];then
		echo "Error: CSV file error"
	 fi
}
#get load test IP

function getLoadTestIP(){
	ipstring=`grep -i domain ${local_jmx_file} 2>/dev/null`
	
	if [ "X${ipstring}" != "X" ];then
		echo "get ip"
		load_test_ip=`grep -i domain ${local_jmx_file} 2>/dev/null | awk -F'>' '{print $2}' |awk -F'<' '{print $1}' | head -1`
		#load_test_ip=`grep -i domain ${local_jmx_file} 2>/dev/null | awk -F'>' '{print$2}' | awk -F'<' '{print $1}'`
	else
		echo "Error: can't get the load test ip"
		exit 1
	fi
	
}

#check for dir for load test machine
function checkDirForLoadTest(){
	ssh -p${loadtest_ssh_port} deploy@${load_test_ip} "if [ ! -d ${remote_monitor_dir} ];then mkdir -p ${remote_monitor_dir}; fi"
}

function checkDirForCaseSender(){
	ssh -p${send_ssh_port} deploy@${send_ip} "if [ ! -d ${remote_testcase_dir} ];then mkdir -p ${remote_testcase_dir}; fi"
}

function scpTestMonitorTool(){
	scp -P${loadtest_ssh_port} cpu_mem.sh deploy@${load_test_ip}:${remote_monitor_dir}
}

function updateTestcase(){
	update_testCase_script="./updateLPTestcase.sh"
	
	csv_file_dir="${remote_testcase_dir}/${thread_num}/${csv_file_name}"
	
	if [ -f ${update_testCase_script} ];then
		./updateLPTestcase.sh ${test_service} ${thread_num} ${durnation} ${local_jmx_file} ${new_testcase_dir} ${csv_file_dir}
	else
		echo "Can't update the testcase template"
	fi
	if [ -f ${lp_testcase_tar} ];then
		rm -rf ${lp_testcase_tar}
	fi
	
	tar cvf ${lp_testcase_tar} ${new_testcase_dir}
	
}

function scpLPTestcase(){
	new_testcase="${new_testcase_dir}/${test_service}_${thread_num}.jmx"
	
	if [ -f ${new_testcase} ];then	
		cd ${new_testcase_dir}; cd ..
		tar cvf ${test_service}_${thread_num}.tar ${thread_num}
	else
		echo "Error: Can't find the LP test case"
	fi
	
	scp -P${send_ssh_port} ${lp_testcase_tar}  deploy@${send_ip}:${remote_testcase_dir}
		
}

function runLPTestcase(){
	#tar the test case
	ssh -p${send_ssh_port} deploy@${send_ip} "if [  -d ${remote_testcase_dir}/${thread_num} ];then rm -rf ${remote_testcase_dir}/${thread_num}; fi; cd ${remote_testcase_dir}; tar xvf ${lp_testcase_tar}"
	
	#run the testcase

}

function runMonitorTool(){
	ssh -p${loadtest_ssh_port} deploy@${load_test_ip} "${remote_monitor_dir}/cpu_mem.sh ${test_service} ${interval} ${durnation} ${thread_num} ${remote_monitor_dir} &"
	
	ssh -p${send_ssh_port} deploy@${send_ip} "nohup ${jmeter_sh} -n -t ${remote_jmx_file} -l ${jtl_file} &"
}

startup

getLoadTestIP

checkDirForLoadTest

checkDirForCaseSender

scpTestMonitorTool

updateTestcase

scpLPTestcase

runLPTestcase

runMonitorTool


