import os

db_config = {
    'user': os.environ['mysql_user'],
    'password': os.environ['mysql_password'],
    'host': os.environ['mysql_host'],
    'port': os.environ['mysql_port']
}


class AppConfig(object):
    SECRET_KEY = os.urandom(16)
