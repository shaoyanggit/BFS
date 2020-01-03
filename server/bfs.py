from flask import Flask, request
from flask_cors import CORS
from flask_api import status

app = Flask(__name__)
CORS(app)

list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    list.append(request.data)
    content = {'data': 'send'}
    return content, status.HTTP_200_OK

@app.route('/done', methods=['GET', 'POST'])
def done():
    print(list)
    content = {'congradulations': 'you are done'}
    return content, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(port=2020)