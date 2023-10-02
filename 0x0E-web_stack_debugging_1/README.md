# 0x0E. Web stack debugging #1
Using debugging skills, to find out what’s keeping an Ubuntu container’s Nginx installation from listening on port 80.
Upon investigation it was determined that nginx was
configured to run on port 8080 which was in use.
I therefore wrote a Bash script to automate the fix
- set the nginx config to run on port 80
- restart nginx
