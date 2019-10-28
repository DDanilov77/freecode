#!/usr/bin/env bash

if [ ! -z "$1" ] && [ ! -z "$2" ] && [ ! -z "$3" ]
  then
    echo $1 $2 $3
    #1:make package
##    build_deb($1)

    #2:scp package to host
    scp $1.deb root@$2:$3

    #3:run package over ssh
    timeout -s 9 60 ssh -t root@$2 $3/$1.deb
  else
    echo "Not enough arguments"
fi

#run example: arg xmr 192.168.11.100 /opt/