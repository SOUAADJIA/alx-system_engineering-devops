# install_flask.pp
# Description: Puppet manifest to install Flask version 2.1.0 and Werkzeug using pip3

package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => 'latest',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

