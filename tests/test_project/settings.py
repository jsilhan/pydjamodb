"""
Django settings for test_project project.

Generated by "django-admin startproject" using Django 1.10a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import getpass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "lzu78x^s$rit0p*vdt)$1e&hh*)4y=xv))=@zsx(am7t=7406a"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pydjamodb",
    "test_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "test_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "test_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"

PYDJAMODB_DATABASE = {

    'HOST': 'http://localhost:8000',
    'AWS_ACCESS_KEY_ID': '_',
    'AWS_SECRET_ACCESS_KEY': '_',
    'AWS_REGION': None,


    # 'AWS_ACCESS_KEY_ID': 'ASIAVWB6PXERM5UBRXAY',
    # 'AWS_SECRET_ACCESS_KEY': 'FOIKbNUpH8kyynWap/N7Br9mldQDOwE+l4DOI/4G',
    # 'AWS_REGION': 'eu-central-1',
    # 'AWS_SESSION_TOKEN': 'IQoJb3JpZ2luX2VjEIT//////////wEaDGV1LWNlbnRyYWwtMSJHMEUCIEP/MsNLhJDoRgQJcrZBbBoDQstb/eVlUTzNceSyFA7xAiEA/ZIQN2p8oIwSIJV5ytVRezVvGpq11iDkBM5AMmG6vGUqiQMIHRAAGgwzOTA5NzMwNzc3OTQiDK8vI3fOFjxzpH2/MyrmAhxmQaYGe47z7lAJpT+ysaI8HPzDoGIR3IiOgYLbML+E9ny6IPROABSFwRXCXdWOauwJH08+RdZinFpxzsedRqYKOF3nDPachiNNo62At3dtau3t6v92QQBaaNGhn/H/+rLr1P5nHxOgGt8V1p4GVHwXj9sXwfBbaOUhMWSWgUxA5SlY4X180pSGVXk5Y/97mYULf+0y7kGqw+It6dN8hLY2SeMXh8dssC9loHpv8U3CrsV8ZmstH4KsYY/JWwd2rnpR8XbJ1+K9nGOHr60yq10Sdm8piu/lzSfW7dXVVJH8Y8dYWnuC40XDQYl6ivnZ4Ns5G9VD2D/CgvQ51IzyNCNTMRQHQ4UUfTLwWTeM250Q5/lN97OcTc0qur46/zlWjvjbl4BmutH3Rum2W42UvXPlEIZR6EZXSBObsLeDSd5hy7EQ/+eaEiEaaEG2KGM9PC9LDeHpUapyUKjfWuCO8QFZ7JXoF10wyey0/gU6pgEV6hyfFKMX91D1Zl+QXN3GPMsF9BSvd084vBfQSsYqAqzgXnF8QwF6qV3/GKdGJR/terEjedI2pVlMx/rbjF4POKg+5qTbSazftUa5tBRy6ifRY4KFs2xmWrKcoXHno+yel5wWn3+/6NMY2jLVhdUbhO1xpex6qsakGhv3ZJGfY9dprspUVH4MycHNc6mLT7dMwRYFvvbML1tGXTDRajHueAH9zh4O',
    'TABLE_PREFIX': 'pydjamodb',
    'BILLING_MODE': 'PAY_PER_REQUEST',
    'TAGS': {
        'Project': 'pydjamodb',
        'Name': '{table_name}',
    }
}

TEST_RUNNER = 'pydjamodb.test_runner.DynamoDBTestDiscoverRunner'
