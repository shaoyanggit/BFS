from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.json)

if __name__ == '__main__':
    app.run(port=2020)