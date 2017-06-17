#!/bin/bash
#
# Start the websp.
#
WsBase=~/www/logs/websp-$(hostname)-9000
PidFile=$WsBase.pid
if [ -f $PidFile ] ; then
    Pid=$(cat $PidFile)
    if kill -0 $Pid 2>&1 >/dev/null ; then
	echo "ERROR: websp is already running, PID=$Pid"
	exit 1
    else
	# The process does not exist, remove the pid file.
	rm -f $PidFile
    fi
fi

if ! [ -d ~/www_panda ]; then mkdir -p ~/www_panda; fi
if ! [ -d ~/www_panda/logs ]; then mkdir -p ~/www_panda/logs; fi

./websp.py -H $(hostname) -p 9000 -l warning --no-dirlist -r ~/www_panda -d ~/www_panda/logs
echo "started"
