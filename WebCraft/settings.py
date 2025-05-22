SECRET_KEY = 'django-insecure-webcraft'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'channels',
    'django.contrib.staticfiles',
]

ASGI_APPLICATION = "webcraft.asgi.application"

INSTALLED_APPS = [
    ...
    "channels",
    ...
]

# Redis или InMemoryChannelLayer для локального теста
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
