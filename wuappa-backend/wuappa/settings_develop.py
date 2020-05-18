from wuappa.settings import *

CITIES_LIGHT_INCLUDE_COUNTRIES = ['CH', 'ES']

ALLOWED_HOSTS = ['*']

FACEBOOK_CLIENT_ID = '2016634975290360'
FACEBOOK_SECRET_KEY = '88c6c29e4b3f05d422ef458583af6b91'

ADMIN_EMAIL = 'team@kasfactory.net'

STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_xIvqLjEDd3iBrGIbGWYjkqgA")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_SDcKtVxpxMlmsbUuqXVK2AEW")
STRIPE_LIVE_MODE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", "wuappa"),
        'USER': os.environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "password"),
        'HOST': os.environ.get("POSTGRES_HOST", "127.0.0.1")
    }
}