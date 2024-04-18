# Puppet manifest to optimize web server configuration to handle load

# Fixing the limit in the Nginx configuration file

exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
