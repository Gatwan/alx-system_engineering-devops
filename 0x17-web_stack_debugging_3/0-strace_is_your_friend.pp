# Fix 500 error when a GET HTTP request is made to an Apache server


exec {'replace':
  provider => shell
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
