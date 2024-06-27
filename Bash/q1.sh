#!/bin/bash

while IFS= read -r line
do

if [[ ${#line} -le 4 ]]; then
    echo "$line">> q1_output.txt
else 
   echo -n ${line:0:4}>> q1_output.txt
   for ((i=0;i<$((${#line} - 4));i++)); do
   echo -n "#">> q1_output.txt
   done
 echo>> q1_output.txt
 fi

  
done < "$1"
