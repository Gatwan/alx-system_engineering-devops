#Add a custom HTTP header with puppet

exec { 'update':
  provider => shell,
  command  => 'sudo apt -y update',
  before   => Exec['install Nginx'],
}

exec { 'install Nginx':
  provider => shell,
  command  => 'sudo apt -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "/listen 80 default_server;/ a     add_header X-Served-By \$HOST;" /etc/nginx/sites-available/default',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
