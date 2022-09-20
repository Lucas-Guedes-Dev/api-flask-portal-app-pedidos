from connection_db import Querys
import psycopg2

query = Querys()

class Pedido:
    def __init__(self):
        super().__init__()
    
    def insert_or_update(self, data):

        try:    
            
            select_pedido = query.select('pedidos',
                fields=['id_pedido'], 
                where=['id_integracao={}'.format(data['id_integracao'])] 
                )

            if select_pedido:
                for dt in data['produto']:

                    query.update("pedidos", 
                    [
                        "id_integracao={}".format(data['id_integracao']),
                        "valor_total_pedido={}".format(data['valor_pedido']),
                        "quantidade={}".format(dt['quantidade']),
                        "id_produto={}".format(dt['id_produto']),
                        "valor_produto={}".format(dt['valor_produto']),
                        "observacao='{}'".format(dt["obs"]),
                        "data_pedido='{}'".format(data['data_pedido'])
                    ],
                    [
                        "id_integracao={}".format(data['id_integracao'])
                    ]
                    )

                    message = {"Sucesso": "Pedido feito com sucesso."}

            else:
                for dt in data['produto']:
                    try: 
                        query.insert("pedidos", 
                        [
                            "id_integracao",
                            "valor_total_pedido",
                            "quantidade",
                            "id_produto",
                            "valor_produto",
                            "observacao",
                            "data_pedido"
                        ],
                        [
                            "'{}'".format(data['id_integracao']),
                            "'{}'".format(data['valor_pedido']),
                            "'{}'".format(dt['quantidade']),
                            "'{}'".format(dt['id_produto']),
                            "'{}'".format(dt['valor_produto']),
                            "'{}'".format(dt["obs"]),
                            "'{}'".format(data['data_pedido'])
                        ]
                        )

                        message = {"Sucesso": "Pedido feito com sucesso."}

                    except psycopg2.errors.ForeignKeyViolation:

                        message = {"Error": "Este produto {} não está cadastrado".format(dt['id_produto'])}

                        break

        except KeyError:

            message = {"Error": "Parametros inválidos."}

        return message