#!/usr/bin/env python

import sys
import os
import config
import re

def urls(environ):
    template = os.path.join(environ['DOCUMENT_ROOT'], 'wsgi/config/template')
    if re.match(r"/config/read", environ['PATH_INFO']):
        return config.ConfigData(environ, template).read()
    elif re.match(r"/config/update", environ['PATH_INFO']):
        return config.ConfigData(environ, template).update()
    elif re.match(r"/config/delete", environ["PATH_INFO"]):
        return config.ConfigData(environ, template).delete()
    elif re.match(r"/config/history", environ["PATH_INFO"]):
        return config.ConfigData(environ, template).history()
    elif re.match(r"/config/edit", environ["PATH_INFO"]):
        return config.ConfigHtml(environ, template).configEdit()
    else:
        return config.ConfigHtml(environ, template).configEdit()
