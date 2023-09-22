# kills a process named killmenow using Puppet

exec { 'kill_command':
    command => "/usr/bin/pkill killmenow",
}