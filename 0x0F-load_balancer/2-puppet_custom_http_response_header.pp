# using puppet to add a line in a file

exec { 'update':
  command  => 'apt-get -y update; apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default; service nginx restart',
  provider => shell,
}

exec { 'test':
  command  => 'echo ""',
  provider => shell,
}
