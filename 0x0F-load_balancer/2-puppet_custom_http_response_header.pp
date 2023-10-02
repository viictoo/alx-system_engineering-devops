# using puppet to add a line in a file

exec {'update':
  command => 'apt-get -y update',
  path    => '/usr/bin'
}

package { 'nginx':
  ensure  => installed,
}

file_line { 'add_header_X-Served-By':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  match  => '^server\s*{',
  after  => 'matched',
}

service {'nginx':
  ensure  => 'running'
}
