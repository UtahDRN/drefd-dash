#!/bin/bash
## Configuration
source /opt/drefd-dash/drefd_dash.conf

modules=( "A" "B" "C" "D" "E" )

while true; do
  for mod in ${modules[@]}; do
    grep "${DREFD_ID} ${mod}" /var/log/drefd/drefd.log | sort -r | awk -v mod="$mod" -F"[:-]" '{printf "%s %s %s:%s:%s %s\n", mod, $1, $2, $3, $4, $7}' | uniq | jq -R -n '[inputs | split(" ") | {module: .[0], date: .[1], time: .[2], callsign: .[3]}]' > /dstar/html/lastheard/assets/json/${mod,,}.json
  done
  sleep 5
done
