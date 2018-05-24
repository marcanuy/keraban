from .base import *
import dj_database_url

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# customize with your owns
# better to have
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',') if os.getenv('DJANGO_ALLOWED_HOSTS') else []
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')

# AWS Amazon Web Services credentials
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_REGION = os.getenv('AWS_REGION', '')

# thanks bakerydemo ;)
if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_AUTO_CREATE_BUCKET = True

    INSTALLED_APPS.append('storages')
    MEDIA_URL = "https://{}/".format(AWS_S3_CUSTOM_DOMAIN)

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    #STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# https://django-analytical.readthedocs.io/
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-64047109-3'

# https://github.com/kennethreitz/dj-database-url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
