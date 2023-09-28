#!/bin/bash
# send a get request to an input url
if [ $# -lt 1 ]; then
    echo "Usage $0 <url>"
    exit 1
fi
res=$(curl -sIL  --write "%{http_code}" "${1}" | tail -1)
#body=$(curl -X GET -w "%{http_code}\n" -o /dev/null -s $1)
body=$(curl -s -L -X GET "${1}" | grep -v '^<')
if [ "${res}" -eq 200 ]; then
	echo "${body}"
	exit 1
fi
