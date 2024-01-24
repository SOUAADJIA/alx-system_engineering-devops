# Task 3: Puppet manifest to kill a process named "killmenow"

exec {'kill killmenow':
  command => '/usr/bin/pkill killmenow',
}
