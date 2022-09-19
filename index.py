from flask import Flask, request
import json
from connection_db import Querys

app = Flask(__name__)

@app.route('/insert/produto', methods=['POST'])
def produto():
    if request.method == 'POST':

        data = request.get_json()
        print(data['produto'])
        return data

if __name__ == '__main__':
    app.run(debug=True)