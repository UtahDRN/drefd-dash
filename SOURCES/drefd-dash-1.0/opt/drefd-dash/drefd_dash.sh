#!/bin/bash
## Configuration
source /opt/drefd-dash/drefd_dash.conf

modules=( "A" "B" "C" "D" "E" )

while true; do
  for mod in ${modules[@]}; do
    grep "${DREFD_ID} ${mod}" ${DREFD_LOG_PATH} | sort -r | awk -v mod="$mod" -F"[:-]" '{printf "%s %s %s:%s:%s %s\n", mod, $1, $2, $3, $4, $7}' | uniq | jq -R -n '[inputs | split(" ") | {module: .[0], date: .[1], time: .[2], callsign: .[3]}]' > ${DREFD_JSON_PATH}/${mod,,}.json
    chown -R apache:apache ${DREFD_JSON_PATH}/${mod,,}.json
    chmod -R 755 ${DREFD_JSON_PATH}/${mod,,}.json
    chcon -R -t httpd_sys_content_t ${DREFD_JSON_PATH}/${mod,,}.json
  done
  sleep 5
done
