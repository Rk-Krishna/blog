import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userend.settings')

application = get_wsgi_application()

# Alias for Vercel's expected variable
app = application
