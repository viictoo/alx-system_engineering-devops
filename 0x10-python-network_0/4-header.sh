#!/bin/bash
# print the content-length of request
#curl -s -X-School-User-Id -d "98" ${1} | awk '/Content-Length/ { print $2 }'
curl -sH "X-School-User-Id:98" "$1" 
