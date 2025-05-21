SECRET_KEY = 'django-insecure-webcraft'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'channels',
    'django.contrib.staticfiles',
]

ASGI_APPLICATION = 'WebCraft.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

ROOT_URLCONF = ''
MIDDLEWARE = []
