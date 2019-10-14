#!/bin/bash
cd ~/freecode/
DATE=$( date "+%Y-%m-%d %H:%M")
file=".git/new-push.txt"
git status > $file
git add .

if [ -z "$1" ]; then  #if not yet cmd parameters
    var1=0; var2=0; var3=0;
    while IFS= read line
    do
    #modified
        if [[ ${line:1:9} == "modified:" ]]; then
    	    var1=$((var1+1));
        fi
    #deleted
        if [[ ${line:1:8} == "deleted:" ]]; then
          var2=$((var2+1))
        fi
    #new file:
    if [[ ${line:1:9} == "new file:" ]]; then
          var3=$((var3+1))
    fi
    done <"$file"
    #echo "m{${var1}}d{${var2}}n{${var3}} ";
    git commit -m"m{${var1}}d{${var2}}n{${var3}} from $HOSTNAME at ${DATE}"
else
    #echo "$1";
    git commit -m"$1";
fi
git push origin master
#echo "Push m{${var1}}d{${var2}}n{${var3}} from $HOSTNAME at ${DATE}"
