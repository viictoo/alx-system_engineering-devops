# using puppet to add a line in a file

exec {'update':
  command => 'apt-get -y update',
  path    => ['/usr/bin', '/bin', '/usr/bin/env'],
}

package { 'nginx':
  ensure  => installed,
}

file_line { 'add_header_X-Served-By':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
  notify => Service['nginx'],
}

service {'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['add_header_X-Served-By'],
}
