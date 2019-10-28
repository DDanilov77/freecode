#!/bin/bash

#alias new120='~/script/new120.sh'
#run this script for send key to vagrant box

ip12=('192.168.20.120' '192.168.20.121' '192.168.20.122')
for value in ${ip12[@]};   do    
    echo "Remove ssh-key"
    ssh-keygen -f ~/.ssh/known_hosts -R $value
    echo "Send ssh-key to server"
    ssh-copy-id -i ~/.ssh/$USER.pub root@$value
    echo $value
done

