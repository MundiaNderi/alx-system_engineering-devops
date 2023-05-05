# Create a file in /tmp with various attributes

file { '/tmp/school':
  ensure  => directory,
  path    => '/tmp/school',
  mode    => '0755',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
  }
