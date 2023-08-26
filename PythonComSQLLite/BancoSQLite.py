import sqlite3


class BancoSQLite:

    def __init__(self, nomeBanco):
        self.nomeBanco = nomeBanco
        pass
    
    def consultar(self,sqlConsulta):
        conn = sqlite3.connect(self.nomeBanco)
        cursor = conn.cursor()

        cursor.execute(sqlConsulta)
        return cursor.fetchall()
        
        # return retornoConsulta


# # definindo um cursor
# cursor = conn.cursor()

# # criando a tabela (schema)
# cursor.execute("""
# CREATE TABLE clientes (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         idade INTEGER,
#         cpf     VARCHAR(11) NOT NULL,
#         email TEXT NOT NULL,
#         fone TEXT,
#         cidade TEXT,
#         uf VARCHAR(2) NOT NULL,
#         criado_em DATE NOT NULL
# );
# """)

# print('Tabela criada com sucesso.')
# desconectando...
#conn.close()

# cursor = conn.cursor()

# # inserindo dados na tabela
# cursor.execute("""
# INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
# VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08')
# """)

# cursor.execute("""
# INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
# VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '98765-4322', 'Porto Alegre', 'RS', '2014-06-09')
# """)

# cursor.execute("""
# INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
# VALUES ('Bruna', 21, '22222222222', 'bruna@email.com', '21-98765-4323', 'Rio de Janeiro', 'RJ', '2014-06-09')
# """)

# cursor.execute("""
# INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
# VALUES ('Matheus', 19, '33333333333', 'matheus@email.com', '11-98765-4324', 'Campinas', 'SP', '2014-06-08')
# """)

# # gravando no bd
# conn.commit()

# print('Dados inseridos com sucesso.')

# conn.close()

# cursor = conn.cursor()

# lendo os dados
# cursor.execute(" SELECT * FROM clientes; ")

# lista = cursor.fetchall()
# for linha in lista:
#     print(type(lista))
#     print(linha)

# conn.close()