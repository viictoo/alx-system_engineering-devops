#!/bin/bash
# send a req to a URL and display only status code
curl -so /dev/null -w "%{http_code}" "$1"
