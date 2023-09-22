# Using Puppet, create a file in /tmp.
file { 'school':
  path    => '/tmp/school',
  force   => 'true',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
