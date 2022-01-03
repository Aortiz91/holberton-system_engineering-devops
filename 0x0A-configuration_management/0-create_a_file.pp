# Using Puppet, creates a file in /tmp. | File path is /tmp/school | permission is 0744 | owner is www-data | group is www-data
file { '/tmp/school':
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
  content => 'I love Puppet',
}
