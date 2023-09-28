#!/bin/bash
# send a get request to an input url
if [ $# -lt 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi
curl -s -L -X GET "$1" | grep -v '^<'
