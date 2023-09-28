#!/bin/bash
# make a request to 0:5000/catch_me to make server respond with message
curl -sLX PUT -d 'user_id=98' -H "Origin:School" "0.0.0.0:/catch_me"
