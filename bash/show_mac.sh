#/bin/bash

var1=$(ifconfig -a | sed -n '/^lo.*/ d;s/\(^[a-z].*:\).*/\1/p; s/.*\(..:..:..:..:..:..\).*/\1/p;'|sed 'N;s/\n/ /')
echo $var1
