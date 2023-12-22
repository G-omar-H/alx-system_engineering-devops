# puppet manifest to execute a bash command
exec { 'kill him now':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin',],
}
