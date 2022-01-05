# Using Puppet, modify configuration file 

file_line { 'IdentityFile':
  path  => '/etc/ssh/ssh_config',
  match => '^IdentityFile',
  line  => '^IdentityFile ~/.ssh/school',
}

file_line { 'PasswordAuthentication':
  path  => '/etc/ssh/ssh_config',
  match => '^PasswordAuthentication',
  line  => 'PasswordAuthentication no',
}
