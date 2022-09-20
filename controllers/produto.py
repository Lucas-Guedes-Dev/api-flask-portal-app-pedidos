from connection_db import Querys

query = Querys()

class Produto:
    def __init__(self):
        super().__init__()
    
    def isert_or_update(self, data):
        for dt in data['produto']:

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

        return message