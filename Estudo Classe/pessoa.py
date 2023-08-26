# pessoa.py
from datetime import datetime

class Pessoa:
    def __init__(self, nome, data_nascimento, altura):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.altura = altura
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        data_atual = datetime.now()
        idade = data_atual.year - self.data_nascimento.year - ((data_atual.month, data_atual.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade
