from .base import *


SECRET_KEY = "django-insecure-7%zrgunt4=94hs6bp1og%9@6%i@1s94tvw%m5hc(0y1q6t+4*#"

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
