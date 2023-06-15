# Changes the OS configuration such that login is possible with
# the holberton user and open a file without any error message.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
