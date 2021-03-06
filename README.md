web admin
========


#Nginx

run with nginx + uwsgi

##nginx

	server {
	        listen       80 ;
	        root /data1/www/htdocs/www.example.com;
	        server_name www.example.com;
	
	        access_log  /data1/www/logs/www.example.com-access_log  main;
	        access_log  /data1/www/logs/all_items_http_log  main;
	        error_log   /data1/www/logs/www.example.com-error_log;
	
	        location ~ /static/(.*) {
	                alias /data1/www/htdocs/www.example.com/static/$1;
	                expires 1d;
	        }
	
	        location / {
	                uwsgi_pass 127.0.0.1:9002;
	                expires -1;
	        }
	}


##uwsgi

	[uwsgi]
	chdir = %(document_root)
	cpu-affinity = 1
	daemonize = %(sinasrv)/var/logs/uwsgi/%n.log
	document_root = /data1/www/htdocs/%n
	gid = www
	master = true
	pidfile = %(sinasrv)/var/run/uwsgi/%n.pid
	plugins = /usr/local/sinasrv2/lib/uwsgi/python_plugin.so
	sinasrv = /usr/local/sinasrv2
	socket = 127.0.0.1:9002
	stats = 127.0.0.1:7002
	uid = www
	workers = 8
	wsgi-file = wsgi
	env = SINASRV_APPLOGS_DIR=/data1/www/applogs/%n
	env = SINASRV_DB_HOST=10.73.48.210
	env = SINASRV_DB_PORT=3306
	env = SINASRV_MEMCACHED_SERVERS=10.13.32.22:7601


#Apache

run with apache

##apache

	<VirtualHost *:80>
	    ServerName www.example.com
	    ServerAdmin admin@localhost
	    DocumentRoot /data1/www/htdocs/www.example.com
	    ErrorLog /data1/www/logs/www.example.com-error_log
	    CustomLog /data1/www/logs/www.example.com-access_log combinedalias

	    Alias /static /data1/www/htdocs/www.example.com/static
	    WSGIScriptAlias / /data1/www/htdocs/www.example.com/wsgi
	</VirtualHost>
	

