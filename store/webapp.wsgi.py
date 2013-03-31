# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/frv2706/www/site1/')
sys.path.append( os.path.abspath('/home/frv2706/www/site1/public_html/') )
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()