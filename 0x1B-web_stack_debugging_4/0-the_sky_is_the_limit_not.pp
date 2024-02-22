# Puppet script to fix overloading requests on a nginx server

exec { 'sed -rine "s/^(ULIMIT=\"-n )[0-9]+\"/\1 4096\"/" /etc/default/nginx':
  path  =>  ['/usr/bin', '/usr/sbin', '/bin/',],
}

exec { 'service nginx restart':
  path  =>  ['/usr/bin', '/usr/sbin', '/bin/',],
}

