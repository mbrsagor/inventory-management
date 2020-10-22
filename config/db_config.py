# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory',
        'USER': 'macair',
        'PASSWORD': 'inventory',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
