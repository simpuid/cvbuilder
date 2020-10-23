import os

db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'port': '3306',
}


class AppConfig(object):
    SECRET_KEY = os.urandom(16)
