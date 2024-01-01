# puppet script to setup client SSH configuration file to disable password authentification
file_line { 'PasswordAuthentication':
  ensure => present,
  path   => '~/.ssh/school',
  line   => '       PasswordAuthentication no',
  match  -> '/.\s+PasswordAuthentication\s+yes/gm',
}
