# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Django settings for team_service project in development environment.
#
# Django 4.1.1.
# -----------------------------------------------------------

from team_service.settings.common import *


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = 'django-insecure-l-6vx$ms8fu9(lir$p2r9!$^w0fupdiq)b8k#1tc1aq)m_o+17'

DEBUG = True

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
