#using Puppet to make changes to our configuration file
file_line{'~/.ssh/config ':
	ensure  => present,
	content => "# SSH client configuration\n\nHost *\n  PasswordAuthentication no\n",
}
