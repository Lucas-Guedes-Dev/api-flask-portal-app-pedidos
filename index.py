from flask import Flask, request, jsonify
from controllers.produto import Produto
from controllers.pedido import Pedido

app = Flask(__name__)

@app.route('/insert/produto', methods=['POST'])
def produto():
    if request.method == 'POST':

        data = request.get_json()
        
        message = Produto().isert_or_update(data)

        return jsonify(message)

@app.route('/realizar-pedido', methods=['POST'])
def pedido():
    if request.method == 'POST':

        data = request.get_json()

        message = Pedido().insert_or_update(data)

        return message 

if __name__ == '__main__':
    app.run(debug=True)