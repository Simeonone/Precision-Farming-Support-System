"""
Django settings for version1 project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eg5)!7ezcx^tdq6q2%@*$$i=z-k9lpacne)z2ra&^78d(++#u@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #the code below deletes old profile pictures when new ones are updated - but its bringing errors
    #'django-cleanup',
    'users.apps.UsersConfig',
    #'opencv.apps.OpencvConfig',
    'convert',
    #'opencvproj.apps.OpencvProjConfig'
    'cropimage.apps.CropimageConfig',
    'blog.apps.BlogConfig',
    'store.apps.StoreConfig',
    'notifications',
    #check your spelling. My initial error:
    #blogs.apps.Blogconfig
    'crispy_forms',
    #above, is a crispy forms app that i installed
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customerpdf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'version1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'version1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
      #  'ENGINE': 'django.db.backends.sqlite3',
      # 'NAME': BASE_DIR / 'db.sqlite3',
    'ENGINE': 'django.db.backends.postgresql',
    'NAME' : 'simeon',
    'USER' : 'postgres',
    'PASSWORD' : 'pass1234',
    'HOST' : 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#the code below is for the profile picture directory
MEDIA_ROOT = os.path.join(BASE_DIR,'media') #this is the full path to a directory where
#i would like django to store uploaded files
MEDIA_URL = '/media/'

#below, we are telling crisy forms what version of bootstrap we are using-because by default, it uses bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap4' #remember to load this in to the template to use it(register.html)


LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
DEFAULT_FROM_EMAIL = 'precision farming with Simeon <noreply>'
