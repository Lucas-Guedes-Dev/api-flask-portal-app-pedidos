from ast import Delete
import os
import psycopg2

class Connection:

    def __init__(self):
        super().__init__()

        self.host = 'localhost'
        self.database = 'databaseteste'
        self.user = 'postgres'
        self.password = 'postgres'

    def connect(self):

        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)

        self.cusrsor = self.connection.cursor()

        return self.cusrsor

class Querys(Connection):
    def __init__(self):
        super().__init__()

        self.cursor = self.connect()

    def select(self, table=str, fields=list, where=None, join=None):
        
        if where and not join:

            query = 'SELECT {campos} from {tabela} where {condicao} '.format(campos = ','.join(fields), tabela = table, condicao = ' and '.join(where))

        elif where and join:

            query = 'SELECT {campos} from {tabela} {join_table} where {condicao}'.format(
                campos = ','.join(fields), 
                tabela = table, 
                condicao = ' and '.join(where), 
                join_table = ''.join(join))

        else:
            query = 'SELECT {campos} from {tabela}'.format(campos = ','.join(fields), tabela = table)
        
        self.cursor.execute(query)

        fetch = self.cursor.fetchall()

        return fetch

    def insert(self, table=str, fields=list, values=list):

        query = 'INSERT INTO {tabela} ({campos}) values ({valores})'.format(tabela=table, campos=','.join(fields), valores=','.join(values))
        
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete(self, table=str, where=list):
        
        query = 'DELETE FROM {tabela} WHERE {condicao}'.format(tabela=table, condicao=' and '.join(where))

        self.cursor.execute(query)
        self.connection.commit()
    
    def update(self, table=str, set=list, where=None):
        
        if where:
            query = 'UPDATE {tabela} SET {set} WHERE {where}'.format(tabela=table, 
            set=', '.join(set), where=' and '.join(where))
        else:
            query = 'UPDATE {tabela} SET {set}'.format(table, set)

        self.cursor.execute(query)
        self.connection.commit()