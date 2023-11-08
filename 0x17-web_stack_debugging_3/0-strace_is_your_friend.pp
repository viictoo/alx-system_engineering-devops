# using puppet to fix error in wordpress settings file

exec { 'replace':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/bin',
}

exec { 'restart':
  path    => '/usr/bin/',
  command => 'sudo service apache2 restart',
}
