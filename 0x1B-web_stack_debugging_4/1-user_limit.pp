# Puppet script to configure the OS so that being able to login as holberton user and open a file without any error

exec { 'sed -rine "s/(holberton \w+ nofile) [0-9]+/\1 978160/g" /etc/security/limits.conf':
  path => ['/usr/bin', '/usr/sbin', '/bin/',],
}
