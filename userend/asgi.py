import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userend.settings')

# Instead of just using `get_asgi_application()`, define a handler function
def handler(event, context):
    application = get_asgi_application()
    return application(event, context)
