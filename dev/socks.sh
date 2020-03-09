#!/usr/bin/env bash
# Usage: ./socks.sh [on|off]
# `./socks.sh on` will create a socks connection, and refresh the connection if one already exists
# `./socks.sh off` will terminate the socks connection
# `./socks.sh` with no arguments will echo the current status of socks
# You can alias this script by adding `alias socks='/path/to/socks.sh'` to your `~/.bashrc` or `~/.zshrc` file.
# Override the default location of keyfile by setting VA_SOCKS_KEYFILE
set -o errexit

socks_add_key_cmd="ssh-add -K ${VA_SOCKS_KEYFILE:-~/.ssh/vetsgov_id_rsa}"
socks_del_key_cmd="ssh-add -d ${VA_SOCKS_KEYFILE:-~/.ssh/vetsgov_id_rsa}"
socks_start_cmd="ssh socks -D 2001 -N";
socks_kill_cmd="pkill -f \"$socks_start_cmd\"";
socks_ps=`ps -ef | grep "$socks_start_cmd" | grep -v grep` || true;
socks_ps_count=`ps -ef | grep "$socks_start_cmd" | grep -v grep | wc -l` || true;
[ $socks_ps_count -eq 0 ] && echo "socks are OFF" || echo "socks are ON";
if [ $# -eq 0 ]; then
    exit 0;
else
    if [ $# -eq 1 -a $1 == "on" ]; then
        echo "(re)starting socks...";
        eval $socks_kill_cmd || true;
        eval $socks_add_key_cmd;
        eval $socks_start_cmd & disown;
        exit 0;
    else
        if [ $# -eq 1 -a $1 == "off" ]; then
            echo "stopping socks...";
            eval $socks_kill_cmd;
            eval $socks_del_key_cmd;
            exit 0;
        else
            echo "Usage: socks [on|off]";
            exit 1;
        fi;
    fi;
fi
