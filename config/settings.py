import environ

ROOT_DIR = (
        environ.Path(__file__) - 3
)  # (nomad_auto_garage/config/settings/base.py - 3 = nomad_auto_garage/)
APPS_DIR = ROOT_DIR.path("nomad_auto_garage")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path(".env")))
DEBUG = env.bool("DJANGO_DEBUG", True)
TIME_ZONE = "Asia/Almaty"
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_L10N = True
USE_TZ = False
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }}

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]
THIRD_PARTY_APPS = [
    "django_filters",
    "rest_framework",
    "drf_yasg",
]
LOCAL_APPS = [
    "kiz_sushi_bot.main.apps.MainConfig",
    "kiz_sushi_bot.bot.apps.BotConfig"
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {

}

STATIC_ROOT = str(ROOT_DIR("staticfiles"))
STATIC_URL = "/static/"
MEDIA_URL = os.getenv("MEDIA_URL", "/api/media/")
MEDIA_ROOT = os.getenv("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates"))],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]
FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.handlers.mail.backends.smtp.EmailBackend"
)
ADMIN_URL = "admin/"
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    }
}
BOT_TOKEN = "1240576397:AAH-iQqaDhxy3I6BarVbuW3FHoa8emlBQTM"

DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="znui8Rfp5MGh1P3u9plp4nbXcGDxxdt69J0gKwXK2vs8uODXNN12AoGXe1RLbT7h",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "SELF_SERVICE_NAME", "*"]

CACHES = {
    "default": {
        "BACKEND": "django.handlers.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa F405

EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
# if env("USE_DOCKER") == "yes":
#     import socket
#     hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]
INSTALLED_APPS += ["django_extensions"]  # noqa F405

DOMAIN_NAME = 'https://1e6e5352bc48.ngrok.io'
