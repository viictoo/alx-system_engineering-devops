# using puppet to add a line in a file
file_line { 'add_header_X-Served-By':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  match  => '^server\s*{',
  after  => 'matched',
}
