# using puppet to add a line in a file

exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'install_nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

file_line { 'add_header':
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By \"${hostname}\";",
  after  => 'server_name _;',
}

exec { 'restart':
  command   => 'service nginx restart',
  provider  => shell,
}
