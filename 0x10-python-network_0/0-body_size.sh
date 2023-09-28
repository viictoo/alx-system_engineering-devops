#!/bin/bash
# print the content-length of request
curl -sI "$1" | awk '/Content-Length/ { print $2 }'
