from flask import Flask, request, abort
from time import time
from json import dumps

app = Flask(__name__)
temperature = dict()


def last():
    resp = {
        'temperature': temperature[list(temperature.keys())[len(temperature.keys()) - 1]],
        'timestamp': list(temperature.keys())[len(temperature.keys()) - 1]
    }
    return resp


def day():
    resp = dict()
    for rec in temperature:
        if time() - 86400 <= rec:
            resp[rec] = temperature[rec]
    return resp


def week():
    resp = dict()
    for rec in temperature:
        if time() - 604800 <= rec:
            resp[rec] = temperature[rec]
    return resp


def month():
    resp = dict()
    for rec in temperature:
        if time() - 2628000 <= rec:
            resp[rec] = temperature[rec]
    return resp


def year():
    resp = dict()
    for rec in temperature:
        if time() - 31557600 <= rec:
            resp[rec] = temperature[rec]
    return resp


@app.route('/celsius', methods=['GET'])
def temp_page():
    return 'Hello.'


@app.route('/celsius/get', methods=['GET'])
def temp_get():
    if 'type' not in request.args:
        return temperature
    elif request.args['type'] == 'last':
        return last()
    elif request.args['type'] == 'day':
        return day()
    elif request.args['type'] == 'week':
        return week()
    elif request.args['type'] == 'month':
        return month()
    elif request.args['type'] == 'year':
        return year()


@app.route('/celsius/post', methods=['POST'])
def temp_post():
    if request.remote_addr == '127.0.0.1':
        temperature[float(request.form.get('time'))] = float(request.form.get('temperature'))
        open(f'{__file__}\\..\\celsius_db.json', 'w').write(dumps(temperature))
        return 'Ok.'
    else:
        abort(403)


app.run(host='0.0.0.0', port=7645)
