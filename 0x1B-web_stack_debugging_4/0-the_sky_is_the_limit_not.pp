#Fix limit connections 

exec { 'fix limit connections':
        command => 'sed -i \'s/http {/http {\n  open_file_cache max=1024 inactive=10s;\n    open_file_cache_valid 120s;/g\' /etc/nginx/nginx.conf && service nginx restart',
        path => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
