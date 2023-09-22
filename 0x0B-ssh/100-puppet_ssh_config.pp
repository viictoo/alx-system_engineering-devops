# set up your client SSH configuration file so that you can connect to a server without typing a password
# include stdlib
file_line { 'use the private key ~/.ssh/school':
  line    => '    IdentityFile ~/.ssh/school',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

file_line { 'refuse to authenticate using a password':
  line    => '    PasswordAuthentication no',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
