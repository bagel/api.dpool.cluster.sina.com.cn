Config
========
config admin system

##config

#### update

	curl 10.13.32.236/config/update -d @conf.json -H "Host: api.example.com"

conf.json

	{
	    "name": "php-fpm.ini",
	    "path": "/usr/local/exmapledata/php-fpm/php-fpm.ini",
	    "owner": "root:root",
	    "perm": "0644",
	    "type": "file",
	    "module": "global",
	    "version": 1,
	    "author": "caoyu2",
	    "cmd0": "L2V0Yy9pbml0LmQvcGhwLWZwbSByZWxvYWQ=",
	    "cmd1": "L2V0Yy9pbml0LmQvcGhwLWZwbSByZWxvYWQ=",
	    "data": "dGVzdCBAQGludGlwQEAgd29ya1xuICAgIHRlc3Q="
	}

cmd0, cmd1 and data are base64 encode

#### delete

	curl 10.13.32.236/config/delete -d '{"name": "nginx.conf", "version": 2}' -H "Host: api.example.com"

delete config "nginx.conf" with version 2

	curl 10.13.32.236/config/delete -d '{"name": "nginx.conf"}' -H "Host: api.example.com"

delete config "nginx.conf" all


#### read

	curl 10.13.32.236/config/read -d '{"name": "nginx.conf", "version": 2}' -H "Host: api.example.com"

read config "nginx.conf" with version 2

	curl 10.13.32.236/config/read -d '{"name": "nginx.conf"}' -H "Host: api.example.com"

read config "nginx.conf" with the last version


#### history

	curl 10.13.32.236/config/history -d '{"name": "nginx.conf"}' -H "Host: api.example.com"

version, author and mtime history of config "nginx.conf"


##node

#### create

	curl 10.13.32.236/config/node/create -d '{"name": "node", "data": {"root": "dpool"}' -H "Host: api.example.com"

create node tree root "dpool"


#### add

	curl 10.13.32.236/config/node/add -d '{"name": "node", "parent": "dpool", "current": "web3"}' -H "Host: api.example.com"

add node "web3" to "dpool"

#### update

	curl 10.13.32.236/config/node/create -d '{"name": "node", "delete": "nginx"}' -H "Host: api.example.com"

delete a node

#### addnodes

	curl 10.13.32.236/config/node/addnodes  -d '{"name": "node", "nodes": [["10.73.48.210", {"idc": "bx"}]], "current": "nginx"}' -H 'Host: api.example.com'

add nodes to a node

#### readnodes

	curl 10.13.32.36/config/node/readnodes -d '{"name": "node", "current": "dpool"}' -H "Host: api.example.com" | python -m json.tool

	[
	    [
	        "10.13.32.235",
	        {
	            "idc": "bx",
	            "parent": "nginx"
	        }
	    ],
	    [
	        "10.73.48.210",
	        {
	            "idc": "tc",
	            "parent": ""
	        }
	    ]
	]

read nodes from a node

#### deletenodes

	curl 10.13.32.36/config/node/deletenodes -d '{"name": "node", "nodes": ["10.13.32.23", "10.13.32.26"]}' -H "Host: api.example.com"

delete nodes

#### read

	curl 10.13.32.236/config/node/read  -d '{"name": "node", "parent": "web3", "current": "nginx"}' -H 'Host: api.example.com'

	{
	    "data": {
	        "dpool": {
	            "ssoweb": {}, 
	            "web3": {
	                "nginx": {
	                    "nodes": [
	                        "10.73.48.210"
	                    ]
	                }
	            }
	        }
	    }, 
	    "mtime": 1382440967, 
	    "name": "node", 
	    "version": 61
	}


#### delete, history 

same to config file part


## 
