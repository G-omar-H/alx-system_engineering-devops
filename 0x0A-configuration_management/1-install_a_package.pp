# Puppet script manifestating to install flask from pip3
package { 'python3.8':
  ensure => '3.8.10',
}
package { 'python3-pip':
  ensure => present,
}

package {'flask':
  ensure   => '2.1.0',
  name     => flask,
  provider => 'pip3',
  require  => package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => package['python3-pip'],
  }
}

