# -*- coding: utf-8 -*-
'''
U must add it to .gitignore file
and set Unix file change mode and owner
'''

import os


DEBUG = True

TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['.{{ project_name }}.com', '.{{ project_name }}.ru',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '%DB_PWD%',
        'HOST': os.environ['DB_PORT_5432_TCP_ADDR'],
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ['DB_PORT_11211_TCP_ADDR'] + ':11211',
    }
}

# one year
CACHE_TIMEOUT = 60 * 60 * 24 * 30 * 12

# cache key prefix
KEY_PREFIX = '{{ project_name }}'

REDIS_CONNECTION = {
    'host': os.environ['DB_PORT_6379_TCP_ADDR'],
    'port': 6379,
    'db': 1,
}
