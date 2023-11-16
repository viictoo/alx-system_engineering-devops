# change the ulimit of nginx from 15 to 2^20

exec { 'max out':
  command => 'sed -i "s/15/41048576/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
