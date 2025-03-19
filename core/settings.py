from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-58xukmnoo25bf()%2#$zx14c*rzh!m)2yji$j5h&h9$hwip%1f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nomad-news.digitalforensics.kz', '127.0.0.1', 'localhost', '85.159.27.238']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'app',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Database backend (PostgreSQL in this example)
        'NAME': 'nomad_db',                       # Name of the database
        'USER': 'nomad',                   # Your database username
        'PASSWORD': 'S3cret!@#123',                   # Your database password
        'HOST': 'localhost',                        # Database host (e.g., localhost, an IP address, or domain)
        'PORT': '5555',                             # Database port (default for PostgreSQL)
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]
# CKEDITOR_5_CONFIGS = {
#     'default': {
#         'toolbar': ['undo', 'redo',
#             '|', 'heading',
#             '|', 'fontfamily', 'fontsize', 'fontColor', 'fontBackgroundColor',
#             '|', 'bold', 'italic', 'strikethrough', 'subscript', 'superscript', 'code',
#             '|', 'link', 'uploadImage', 'blockQuote', 'codeBlock',
#             '|', 'alignment',
#             '|', 'bulletedList', 'numberedList', 'todoList', 'outdent', 'indent'],
#         'shouldNotGroupWhenFull': True,
#         'language': 'ru',
#     },
# }
CKEDITOR_5_CONFIGS = {
    'default': {
        # The toolbar is defined as a dictionary with an "items" list.
        'toolbar': {
            'items': [
                # Document tools
                'heading',
                '|',
                # History and source editing
                'undo', 'redo',
                '|',
                # Font settings
                'fontfamily', 'fontsize', 'fontColor', 'fontBackgroundColor', 'highlight',
                '|',
                # Text formatting
                'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', 'code',
                '|',
                # Block level formatting
                'blockQuote',
                '|',
                # Link and media
                'link', 'uploadImage', 'insertImage', 'mediaEmbed',
                '|',
                # Alignment and indenting
                'alignment', 'indent', 'outdent', 
                '|',
                # List features
                'bulletedList', 'numberedList', 'todoList',
                '|',
                # Table tools
                'insertTable', 'tableColumn', 'tableRow', 'mergeTableCells',
                '|',
                # Special characters and other utilities
                'specialCharacters', 'horizontalLine', 'pageBreak', 'findAndReplace',
                '|',
                'sourceEditing', 'codeBlock',
            ]
        },
        # Prevent grouping of toolbar items when the toolbar is full.
        'shouldNotGroupWhenFull': True,
        # Set the UI language (adjust as needed).
        'language': 'ru',
        # Additional configuration for images.
        'image': {
            'toolbar': [
                'imageTextAlternative', 'toggleImageCaption',
                'imageStyle:inline', 'imageStyle:block', 'imageStyle:side'
            ]
        },
        # Additional configuration for tables.
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells'
            ]
        },
    }
}

CKEDITOR_5_CUSTOM_CSS = 'css/ckeditor5/admin_dark_mode_fix.css'