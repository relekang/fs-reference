import os.path

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LFS_URL = ''

ADMINS = ()
MANAGERS = ADMINS

TEST_RUNNER = 'fs_ref.test_runner.TestSuiteRunner'
TEST_EXCLUDE = ['django']

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'project.db',
        }
    }

TIME_ZONE = 'Europe/Oslo'

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'Engelsk'),
    ('no', 'Norsk'),
    ('dk', 'Dansk'),
    ('se', 'Svensk'),
)
LANGUAGES_FOR_DOMAIN = {
    'lekang.com': 'no',
    'filterteknik.se': 'se',
    'filterteknik.dk': 'dk',
    #    'filtersystem.no': 'en',
}

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(BASE_PATH, 'files/media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_PATH, 'files/static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm%ly)xctv^5vckv3*p+(iwo)a+grz7x2i0f9@rw-3dxwdbcmj4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'fs_ref.middleware.LanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fs_ref.core.auth.LocalUserMiddleware'
)

AUTHENTICATION_BACKENDS = (
    'fs_ref.core.auth.LfsAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#STATICFILES_FINDERS = (
#'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#)

ROOT_URLCONF = 'fs_ref.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_PATH, 'templates'),
)
LOCALE_PATHS = (
    os.path.join(BASE_PATH, '../locale'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    #    'django.contrib.staticfiles',
    'django.contrib.messages',

    'sorl.thumbnail',

    'fs_ref.core',
    'fs_ref.core.profiles',

    'fs_ref.api',

    'fs_ref.app.users',
    'fs_ref.app.fs_admin',
    'fs_ref.app.references',
    'fs_ref.app.comments',
)
