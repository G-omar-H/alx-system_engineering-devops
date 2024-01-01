# puppet script to setup client SSH configuration file to disable password authentification
file_line { 'PasswordAuthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '       PasswordAuthentication no',
  match  -> '/.\s+PasswordAuthentication\s+yes/gm',
}
file_line {'IdentityFile ~/.ssh/school':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => '       IdentityFile ~/.ssh/school'
  match  => '/./s+IdentityFile/s+/'
}
