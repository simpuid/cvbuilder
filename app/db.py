import mysql.connector as sql
from config import db_config

connection = sql.connect(**db_config)
cursor = connection.cursor(dictionary=True)


def execute(command: str, data = ()):
    global cursor
    print('execute "' + command + '",', data, flush=True)
    cursor.execute(command, data)


def fetch():
    global cursor
    return cursor.fetchall()


def commit():
    global connection
    connection.commit()


def check_database(name: str):
    execute('SHOW DATABASES', ())
    for element in fetch():
        if element['Database'] == name:
            return True
    return False


def execute_file(path: str):
    file = open(path)
    commands = file.read().split(';')
    file.close()
    for command in commands:
        strip = command.strip()
        if strip != '':
            execute(strip, ())


def initialize(name: str, path: str):
    global connection
    global cursor
    if not check_database(name):
        execute_file(path)
        commit()
    connection.close()
    db_config['database'] = name
    connection = sql.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
