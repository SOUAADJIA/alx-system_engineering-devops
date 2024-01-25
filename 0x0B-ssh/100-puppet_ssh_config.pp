# 100-puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config', # Path to the SSH client configuration file
  line   => 'PasswordAuthentication no',
  match  => '^#?\s*PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?\s*IdentityFile',
}
