from BancoSQLite import BancoSQLite


banco = BancoSQLite('ArquivoBanco.db')

retornoConsulta = banco.consultar('SELECT * FROM CLIENTES')

print(retornoConsulta)