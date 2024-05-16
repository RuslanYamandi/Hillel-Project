from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-#dlv8***nlb#xf3u32a$psx#_at(@j@9(yoaonefyq7%-gw*w$"

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}


STATIC_URL = "static/"

