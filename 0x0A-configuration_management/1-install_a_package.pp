# Description: Puppet manifest to install Flask version 2.1.0 and Werkzeug using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
