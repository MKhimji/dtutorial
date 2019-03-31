import os

import environ
root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),) 
environ.Env.read_env() 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '35.178.71.105', 'x2udot.com']



INSTALLED_APPS = [
    'accounts',
    'home',
    'widget_tweaks',
    'psycopg2',
    'ckeditor',
    'ckeditor_uploader',
    'debug_toolbar',
    'taggit',
    'taggit_templatetags2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tutorial.middleware.LoginRequiredMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

ROOT_URLCONF = 'tutorial.urls'

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
                'django.template.context_processors.media',
                'home.context_processors.blogposts_processor',
               
                
                
            ],
        },
    },
]



WSGI_APPLICATION = 'tutorial.wsgi.application'



DATABASES = {
    'default': env.db(),
   
}

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'tutorial/backups')}



AUTH__VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
           'min_length': 8,
        }
       
    },
    
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',

    },
    {   'NAME': 'accounts.validators.CustomPasswordValidator',

    },
]




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'tutorial/media')

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CKEDITOR_UPLOAD_PATH = 'Screenshots/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'full',
        'height': 300,
        'width': 900,
        
    },
}


LOGIN_URL = '/account/login/'

LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/account/login/'

LOGIN_EXEMPT_URLS = (
    
    r'^account/ajax/validate_username/$',
    r'^account/register/$',
    r'^account/reset-password/$',
    r'^account/reset-password/done/$',
    r'^account/reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    r'^account/reset-password/complete/$'

)






