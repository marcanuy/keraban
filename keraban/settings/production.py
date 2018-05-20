from .base import *



DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# customize with your owns
# better to have
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',') if os.getenv('DJANGO_ALLOWED_HOSTS') else []
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')
