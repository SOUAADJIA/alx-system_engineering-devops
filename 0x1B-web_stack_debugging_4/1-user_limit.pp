# 1-user_limit.pp

# Define a Puppet class to manage the file descriptor limit
exec {'change limits':
  command => "sed -i 's/nofile [0-9]\+$/nofile unlimited/g' /etc/security/limits.conf",
  path    => ['/bin/','/usr/bin/']
}
