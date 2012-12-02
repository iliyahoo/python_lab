#!/bin/bash
#read -n 1 -p "Do you want to run this script: [Y/n] " AMSURE
#[ $AMSURE = Y  ] || exit
#echo "" 1>&2
#echo OK

a1=myfunc.sh
source "$a1"; if [ $? -ne 0 ]; then echo "Ошибка—нет библиотеки функций $a1" 1>&2; exit 1; fi 

myAskYN $1 
echo $?
