# puppet script manifestation to create a /tmp/school file
file {create_school:
  ensure  => present,
  path    => '/tmp/school',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
}
