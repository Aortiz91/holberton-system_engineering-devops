# Using Puppet, modify configuration file 

file_line { 'IdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^IdentityFile',
  line   => '^IdentityFile ~/.ssh/school',
}

file_line { 'PasswordAuthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^PasswordAuthentication',
  line   => 'PasswordAuthentication no',
}
