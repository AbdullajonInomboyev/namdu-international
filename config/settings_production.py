"""
PythonAnywhere production sozlamalari
config/settings.py ni import qilib, kerakli qismlarni o'zgartiradi
"""
from .settings import *

DEBUG = False

# PythonAnywhere domeningizni kiriting
ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# SQLite — PythonAnywhere bepul tierda PostgreSQL yo'q
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Security (production da yoqish)
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
