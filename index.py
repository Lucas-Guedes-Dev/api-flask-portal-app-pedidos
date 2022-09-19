from flask import Flask, request, jsonify
import json
from connection_db import Querys

app = Flask(__name__)

query  = Querys()

@app.route('/insert/produto', methods=['POST'])
def produto():
    if request.method == 'POST':

        data = request.get_json()
        
        for dt in data['produto']:
            print(dt)
            try:
                produtos_db = query.select('produtos', ['descricao', 'ativo', 'id_integracao'],
                ['id_integracao = {}'.format(str(dt['id_integracao']))])

                if produtos_db:
                    query.update('produtos', 
                        [
                            "ativo={}".format(dt['ativo']), 
                            "descricao='{}'".format(dt['descricao'])
                        ],
                        [
                            "id_integracao={}".format(dt['id_integracao'])
                        ]
                    )
                else:
                    query.insert('produtos',
                        ['descricao', 'ativo', 'id_integracao'], 
                        [
                            str("'{}'".format(dt['descricao'])),
                            str(dt['ativo']),
                            str(dt['id_integracao'])
                        ]
                    )

                message = {"Sucesso": "Produtos inseridos ou alterados com sucesso."}

            except KeyError: 
                message = {"Error": "Parametros inválidos"}
                break

        return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)