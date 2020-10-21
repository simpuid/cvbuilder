from flask import Flask, Response
from typing import List, Dict
import mysql.connector
import simplejson as json

app = Flask(__name__)
config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'port': '3306',
    'database': 'citiesData',
}
connection = mysql.connector.connect(**config)


def cities_import() -> List[Dict]:
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()
    cursor.close()
    return result


@app.route("/")
def home():
    js = json.dumps(cities_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp
