The open_file_cache parameters within the /etc/nginx/nginx.conf file are used to define how long and how many files NGINX can keep open and cached in memory.

http {
        open_file_cache max=1024 inactive=10s;
        open_file_cache_valid 120s;

ssentially these parameters allow NGINX to open our HTML files during the first HTTP request and keep those files open and cached in memory. As subsequent HTTP requests are made, NGINX can use this cache rather than reopening our source files.

In the above, we are defining the open_file_cache parameter so that NGINX can cache a maximum of 1024 open files. However, of those files, the cache will be invalidated if they are not accessed within 10 seconds. The open_file_cache_valid parameter is defining a time interval to check if currently cached files are still valid; in this case, every 120 seconds.