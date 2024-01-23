# create a manifest that kills a process named killmenow.
exec {'killmenow':
    path    => '/usr/bin/',
    command => 'pkill -f killmenow'
}
