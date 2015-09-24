import os
import sys

path = '/var/www/cal'
if path not in sys.path:
    sys.path.insert(0, '/var/www/cal')

os.environ['DJANGO_SETTINGS_MODULE'] = 'cal.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

