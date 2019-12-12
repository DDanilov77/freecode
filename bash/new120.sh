#!/bin/bash

#alias new120='~/script/new120.sh'
#run this script for send key to vagrant box

#!/bin/bash

#alias new120='~/script/new120.sh'

ip12=('192.168.11.120' '192.168.11.121' '192.168.11.122' '192.168.11.123' '192.168.11.124' '192.168.11.125')
FROMPATH='~/Downloads/2server/*'

#run this script for send key to vagrant box
if [ ! -f ~/.ssh/$USER.pub ]
    then
    #create key
    ssh-keygen -t rsa -b 2048 -f ~/.ssh/$USER
fi
    for value in ${ip12[@]};   do
    echo "Remove ssh-key from known_hosts"
    ssh-keygen -f ~/.ssh/known_hosts -R $value
    echo "Send ssh-key to servers"
    ssh-copy-id -i ~/.ssh/$USER.pub $USER@$value
    #echo $value
    scp -vf $FROMPATH $USER@$value:/home/$USER/
    done
echo "Servers ready for testing"
