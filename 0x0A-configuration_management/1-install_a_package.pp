# Using Puppet, install flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# # install flask version 2.1.0 from pip3
# package { 'python3':
#   ensure  => '3.10.12',
# }

# package {'python3-pip':
#   ensure  => installed,
# }

# exec { 'flask':
#   command => 'pip3 install flask==2.1.0',
#   path    => '/usr/bin',
#   unless  => 'pip3 show flask',
# }
