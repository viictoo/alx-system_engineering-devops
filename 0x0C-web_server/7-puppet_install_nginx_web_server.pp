# puppet file to setup a web server and add keys
$redirect_me = '\tlocation /redirect_me {\n\t\t\treturn 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;\n\t\t}\n'
$filepath = '/etc/nginx/sites-enabled/default'
$search_str = '/^\tlocation \/ {'
$err = "\terror_page 404 /404.html;\n\n"

exec { 'update packages':
command => 'sudo apt-get -y update',
path    => '/usr/bin:/usr/local/bin',
}

package { 'nginx':
  ensure  => installed,
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

file {'/var/www/html/404.html':
  content => "Ceci n'est pas une page",
}

exec { 'Ngina Redirect Config':
  command => "sed -i '${search_str}/i \ ${redirect_me}' ${filepath}",
  path    => '/usr/bin',

}
exec { 'Ngina Error Page Config':
  command => "sed -i '${search_str}/i \ ${err}' ${filepath}",
  path    => '/usr/bin',
}

exec { 'command':
  path    => '/usr/bin:/usr/local/bin',
  command => 'sudo service nginx restart',
}
