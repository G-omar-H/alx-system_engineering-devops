exec { 'fix the wordpress':
  command => 'sed -r "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php'
}
