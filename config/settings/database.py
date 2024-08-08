"""
Django database settings
"""

from django.conf import settings

# базу использовал Sqlite3. Чтобы было легко тестировать
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }
}
