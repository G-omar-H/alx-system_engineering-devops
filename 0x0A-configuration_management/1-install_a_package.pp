# Puppet script manifestating to install flask from pip3

# install python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
}
# install pip3
package { 'python3-pip':
  ensure => present,
}
# install falsk 2.1.0
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => package['python3-pip'],
}

# install Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => package['python3-pip'],
}


