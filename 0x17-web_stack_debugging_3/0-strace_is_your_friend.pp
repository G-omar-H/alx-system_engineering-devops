# Puppet script to fix the Wordpress internal server error

exec { 'sed -ir "s/class-wp-locale.phpp/class-wp-locale.php/g" wp-settings.php':
  cwd  => '/var/www/html/',
  path => '/bin/',
}
