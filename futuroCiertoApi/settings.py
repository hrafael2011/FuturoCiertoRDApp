"""
Django settings for futuroCiertoApi project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&=)%5@(0p4(gqw076#8b_f0b46$&^q1&26p7)ck-g^qiqn%+w9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [#'futurociertord.azurewebsites.net',
                 #'3.12.151.15',
                 #'127.0.0.1',
                 #'localhost',
                 'draacostafit.com',
                 'www.draacostafit.com'
                 ]


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000/',
    'http://127.0.0.1:8000/',
    'http://3.12.151.15:8080',
    'http://draacostafit.com',       # Versión HTTP sin 'www'
    'https://draacostafit.com',      # Versión HTTPS sin 'www'
    'http://www.draacostafit.com',   # Versión HTTP con 'www'
    'https://www.draacostafit.com',  # Versión HTTPS con 'www'

]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'coreapi',
    'FuturoCiertoContent.apps.FuturociertocontentConfig',
    'simple_history',
    'ckeditor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]





ROOT_URLCONF = 'futuroCiertoApi.urls'

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

WSGI_APPLICATION = 'futuroCiertoApi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS':{
            'timeout': 20,
        }
    }
}

'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 20,
        }
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#CORS_ALLOWED_ORIGINS = ['http://localhost:5173', 
 #                       'http://10.0.0.58:5173',  
  #                      'https://new-page.futurociertord.org',
   #                     'http://draacostafit.com',       
    #                    'https://draacostafit.com',      
     #                   'http://www.draacostafit.com',   
      #                  'https://www.draacostafit.com' 
#
 #                       ]
CORS_ALLOW_ALL_ORIGINS = True 




REST_FRAMEWORK = {
    
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema", # Para que se autodocumente
}




#Media files
MEDIA_URL = '/media/'
#MEDIA_URL = 'https://draacostafit.com/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


from decouple import config

TRANSLATOR_API_KEY = config('API_KEY_TRANSLATOR', default=None)




# ERROR DETECTION BY LOG

# Ruta base de tu proyecto (asegúrate de que esté definida correctamente)
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta para guardar el archivo de log
LOG_DIR = BASE_DIR / "logs"

# Crear la carpeta 'logs' si no existe
if not LOG_DIR.exists():
    LOG_DIR.mkdir()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'api_errors.log',  # Aquí definimos el archivo de log
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',  # Solo registrar errores y niveles superiores
            'propagate': True,
        },
    },
}