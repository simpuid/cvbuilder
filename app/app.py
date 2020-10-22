from flask import Flask, Response
from typing import List, Dict
import simplejson as json
import db

app = Flask(__name__)
db.initialize('citiesData', 'init.sql')


def cities_import() -> List[Dict]:
    db.execute('SELECT * FROM tblCitiesImport')
    result = db.fetch()
    return result


@app.route('/')
def home():
    js = json.dumps(cities_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp
