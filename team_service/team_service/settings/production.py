# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Django settings for team_service project in production environment.
#
# Django 4.1.1.
# -----------------------------------------------------------

from team_service.settings.common import *


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = '9-+y+w!)ug^oli$2hte!(!)+yvopqbz+jko(j=4@t0nw)7@sgl'

DEBUG = False

ALLOWED_HOSTS = []

# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}