import os
from wuappa.settings import *

if os.environ.get("POSTGRES_USER") and os.environ.get("POSTGRES_PASSWORD"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get("POSTGRES_DB", ""),
            'USER': os.environ.get("POSTGRES_USER", ""),
            'PASSWORD': os.environ.get("POSTGRES_PASSWORD", ""),
            'HOST': os.environ.get("POSTGRES_HOST", "127.0.0.1")
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get("POSTGRES_DB", ""),
            'HOST': os.environ.get("POSTGRES_HOST", "127.0.0.1")
        }
    }

STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_xIvqLjEDd3iBrGIbGWYjkqgA")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_SDcKtVxpxMlmsbUuqXVK2AEW")
STRIPE_LIVE_MODE = False
