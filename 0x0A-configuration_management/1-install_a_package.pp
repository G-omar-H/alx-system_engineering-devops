
# Installs flask and required packages

# Install Python 3.8.10
package { 'python':
  ensure => present,
}

# Install pip
package { 'python3-pip':
  ensure => present,
}

# Install Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => present,
  provider => 'pip',
  require  => Package['python3-pip'],
}
