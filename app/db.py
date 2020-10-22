import mysql.connector as sql

connection_config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'port': '3306',
}
connection = sql.connect(**connection_config)
cursor = connection.cursor(dictionary=True)


def execute(command, parameter=()):
    global cursor
    # print('execute "' + command + '",', parameter, flush=True)
    cursor.execute(command, parameter)


def fetch():
    global cursor
    return cursor.fetchall()


def commit():
    global connection
    connection.commit()


def check_database(name):
    execute('SHOW DATABASES')
    for element in fetch():
        if element['Database'] == name:
            return True
    return False


def execute_file(path):
    file = open(path)
    commands = file.read().split(';')
    file.close()
    for command in commands:
        strip = command.strip()
        if strip != '':
            execute(strip)


def initialize(name, path):
    global connection
    global cursor
    global connection_config
    if not check_database(name):
        execute_file(path)
        commit()
    connection.close()
    connection_config['database'] = name
    connection = sql.connect(**connection_config)
    cursor = connection.cursor(dictionary=True)
