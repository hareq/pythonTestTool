#!/bin/sh
service_name_tmp=$1
service_name=`echo ${service_name_tmp} | awk -F'_' '{print $1}'`
service_pid=`ps -ef | grep ${service_name} | grep engine | grep -v grep | grep java | awk '{print $2}'`

interval=$2

duration=`expr $3 \* 60`

thread_num=$4

tool_dir=$5

echo "Test will  last " $duration "seconds"
times=`expr $duration \/ $2`
echo "times" $times

startime=`date +%y%m%d%H%M%S`
jstat_monitor(){
	echo "Start monitor jstat......"
	jstat_log="${tool_dir}/jstat_${thread_num}_${startime}.log"
    nohup /usr/java/latest/bin/jstat -gc ${service_pid} ${interval}s ${times} >> ${jstat_log} &
}

cpu_monitor(){
	echo "Start monitor cpu usage......"
	cpu_log="${tool_dir}/cpu_${thread_num}_${startime}_log"
	nohup top -b -p ${service_pid} -d ${interval} -n ${times} | grep ${service_pid} >> ${cpu_log} &
}

jstat_monitor

cpu_monitor
