import os


ADMIN_USERNAME= "admin"
ADMIN_PASSWORD = "secret"
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')