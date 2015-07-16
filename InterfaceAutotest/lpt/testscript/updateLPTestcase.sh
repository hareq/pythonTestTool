#!/bin/sh

testservice=$1
thread_num=$2
durnation=$3
testcaseTemplate=$4
testcasedir=`dirname ${testcaseTemplate}`
newtestcasedir=$5
csv_file=$6

now=`date +%s`
starttime=`echo $now"000"`
end=`date -d "+${durnation}minute" +%s`
endtime=`echo $end"000"`



echo $now
echo $starttime
echo $durnation
echo $endtime


if [ ! -d {newtestcasedir} ]; then
	mkdir -p ${newtestcasedir}
else
	rm -rf ${newtestcasedir}
	mkdir -p ${newtestcasedir}
fi

#copy other files
files=`ls ${testcasedir}`

for file in $files
do
	echo $file
	echo $file | grep "\.jmx" >/dev/null
	if [ $? -eq 1 ];then
		cp ${testcasedir}/$file ${newtestcasedir}
	fi
done


#update thread number
echo "update thread number....."
tmp_thread_file="${newtestcasedir}/thread_tmp.jmx"
sed -e "s/threads\">[0-9]*</threads\">${thread_num}</" $4 > ${tmp_thread_file}

#update start time
echo "update start time....."
start_time_file="${newtestcasedir}/start_time_tmp.jmx"
sed -e "s/start_time\">[0-9]*</start_time\">${starttime}</" ${tmp_thread_file} > ${start_time_file}

#update end time
echo "update end time....."
end_time_file="${newtestcasedir}/end_time_tmp.jmx"
sed -e "s/end_time\">[0-9]*</end_time\">${endtime}</" ${start_time_file} > ${end_time_file}

#update csv file
echo "update csv file....."
testcase_file="${newtestcasedir}/${testservice}_${thread_num}.jmx"
if [ "X${csv_file}" != "X" ];then
	#echo "------------------"${csv_file}
	#echo "------------------"${testcase_file}
	sed -e "s%filename\">.\+<%filename\">${csv_file}<%" ${end_time_file} > ${testcase_file}
else
	mv ${end_time_file} ${testcase_file}
fi
#clear update 

if [ -f ${tmp_thread_file} ]; then
	rm ${tmp_thread_file}
fi

if [ -f ${start_time_file} ]; then
	rm ${start_time_file}
fi

if [ -f ${end_time_file} ]; then
	rm ${end_time_file}
fi