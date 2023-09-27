#using Puppet to make changes to our configuration file

file_line{'Turn off password auth':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}

file_line{'use the private key':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school'

}