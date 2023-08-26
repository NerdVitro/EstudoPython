from BancoSQLite import BancoSQLite


banco = BancoSQLite('ArquivoBanco.db')

banco.consultar('SELECT * FROM CLIENTES')

print(banco.retornoConsulta)