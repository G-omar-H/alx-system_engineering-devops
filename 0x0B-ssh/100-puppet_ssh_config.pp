# puppet script to setup client SSH configuration file to disable password authentification
file_line { 'PasswordAuthentication':
  ensure => absent,
  path   => '~/.ssh/school',
}
