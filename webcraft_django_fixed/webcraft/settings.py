
SECRET_KEY = 'example'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['channels', 'django.contrib.staticfiles']
ASGI_APPLICATION = 'server.application'
ROOT_URLCONF = 'webcraft.urls'
MIDDLEWARE = []
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}
