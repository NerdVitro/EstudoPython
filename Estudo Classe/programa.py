# main.py
from datetime import datetime
from pessoa import Pessoa  # Importa a classe Pessoa do arquivo pessoa.py

# Cria uma instância da classe Pessoa
pessoa = Pessoa('Fulano', datetime(1995, 5, 15), 1.75)

# Imprime os detalhes da pessoa
print(f"Nome: {pessoa.nome}")
print(f"Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
print(f"Altura: {pessoa.altura} metros")
print(f"Idade: {pessoa.idade} anos")
