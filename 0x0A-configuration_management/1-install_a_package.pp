# Puppet script manifestating to install flask from pip3
package { 'python':
  ensure => present,
}
package { 'python3-pip':
  ensure => present,
}

package {'flask':
  ensure   => '2.1.0',
  name     => flask,
  provider => pip3,
}

package { 'Werkzeug':
  ensure   => present,
  provider => pip3,
}

