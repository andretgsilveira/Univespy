'''
import random


class MyList(list):
    def choice(self):
        return random.choice(self)


p = MyList([1, 3, 4, 6, 7])
'''

class Funcionario:
    def __init__(self, nome, salario, admissao):
        self.nome = nome
        self.salario = salario
        self.admissao = admissao

    def __repr__(self):
        return self.nome + ',' + str(self.salario) + ',' + self.admissao

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario

    def setAdmissao(self, admissao):
        self.admissao = admissao

    def getAdmissao(self):
        return self.admissao

class Gerente(Funcionario):
    def __init__(self, nome, salario, admissao, bonus):
        super().__init__(nome, salario, admissao)
        self.bonus = self.salario * bonus

    def setBonus(self, bonus):
        self.bonus = self.salario * bonus

    def getBonus(self):
        return self.bonus


andre = Funcionario('Andre', 2000, '12/02/2021')
babi = Gerente('Barbara', 3000, '13/07/2021', 0.7)