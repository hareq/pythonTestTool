#!/bin/sh

thread_number=`cat ./thread.conf`

for num in ${thread_number}
do
	./runLPTest.sh $1 $num 30 
done
