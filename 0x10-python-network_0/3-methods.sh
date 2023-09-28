#!/bin/bash
# get all the allowed method by a server using curl
curl -sI "$1" | grep "Allow:" | cut -d" " -f2-
