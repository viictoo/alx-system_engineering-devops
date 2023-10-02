# using puppet to add a line in a file

exec { 'update':
  command  => 'apt-get -y update',
  provider => shell,
}

exec { 'install_nginx':
  command  => 'apt-get -y install nginx',
  provider => shell,
}

file_line { 'add_header':
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\tadd_header X-Served-By \"${hostname}\";",
  after  => 'server_name _;',
  notify => Exec['restart'],
}

exec { 'restart':
  command   => 'service nginx restart',
  provider  => shell,
  subscribe => File_line['add_header_X-Served-By'],
}
