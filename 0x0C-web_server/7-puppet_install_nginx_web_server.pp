# Manifest file to install and configure Nginx on an Ubuntu machine

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'), # Use a template for Nginx configuration
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create Hello World index file
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Nginx configuration template
# This template includes both the root content and the redirect rule
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Notify service restart if Nginx configuration is modified
exec { 'nginx-restart':
  command     => '/bin/systemctl restart nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

# Template for Nginx site configuration
# This template includes both the root content and the redirect rule
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}
