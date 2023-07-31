"""
WSGI config for journal_set project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
#C:\JournalSite\venv\lib\python3.6\site-packages
sys.path.append('C:/JournalSite/journal_set')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'journal_set.settings')

application = get_wsgi_application()

