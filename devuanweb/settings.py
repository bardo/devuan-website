"""
Django settings for devuanweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g@y=01c6%^amofpkz)(ke$lqrujn1)#3uyqrs%)jgwd@sy4l21'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
    'pipeline',
    'website',
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'devuanweb.urls'

WSGI_APPLICATION = 'devuanweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'local.db'),
    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT =  'deploy_static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'website/scss'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


# Bower configuration

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components/')

BOWER_INSTALLED_APPS = (
    'bootstrap-sass-official#3.3.3',
    'jquery#2.1.1',
)


# Pipeline configuration

PIPELINE_CSS_COMPRESSOR = None

PIPELINE_JS_COMPRESSOR = None

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_SASS_BINARY = os.path.join(os.getenv('VIRTUAL_ENV'), 'bin/sassc')

PIPELINE_SASS_ARGUMENTS = '-I ' + os.path.join(BASE_DIR, 'components/bower_components/bootstrap-sass-official/assets/')

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'devuan.scss',
        ),
        'output_filename': 'css/devuan.css',
    },
}
