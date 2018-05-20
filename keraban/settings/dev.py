from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cm9ud4e8od=68m*0&*a&u-rpza4q$t6p8tv1g4j0ku9eqe%92z'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Accept all hostnames, since we don't know in advance which hostname will be used for any given Heroku instance.
# IMPORTANT: Set this to a real hostname when using this in production!
# See https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(';')

try:
    from .local import *
except ImportError:
    pass
