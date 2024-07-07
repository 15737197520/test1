"""
WSGI config for djangoProject1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from main.views import loop_monitor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')

application = get_wsgi_application()

print("启动定时任务")
loop_monitor()
print("执行wsgi")
