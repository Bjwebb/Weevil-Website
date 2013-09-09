import dj_database_url
import os
DATABASE =  dj_database_url.config()
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['weevil-test.herokuapp.com']
DEBUG = False

