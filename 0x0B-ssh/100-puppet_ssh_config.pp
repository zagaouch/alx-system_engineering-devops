#This script set up a client configuration file to connect to a server without a password.

exec {'ssh_config':
    path    => '/usr/bin/',
    command => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config'
}