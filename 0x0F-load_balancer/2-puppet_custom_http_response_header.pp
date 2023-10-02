# using puppet to add a line in a file
exec { 'update':
  command  => '/usr/bin/apt-get -y update',
  provider => shell,
}

exec { 'install nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}


file_line { 'add_header_X-Served-By':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\tadd_header X-Served-By \"${hostname}\";",
  after  => 'server_name _;',
  # notify => Service['nginx'],
}

# service { 'nginx':service nginx status

#   ensure    => 'running',
#   enable    => true,
#   subscribe => File_line['add_header_X-Served-By'],
# }
exec { 'command':
  command  => 'service nginx restart',
  provider => shell,
}
