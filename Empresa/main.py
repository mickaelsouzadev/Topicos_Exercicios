from Functions.functions import *
from Classes.Funcionario import *

for i in range(0, 3):
    nome = getNome()
    sobrenome = getSobrenome()
    sal_mens = getSalmens()

    funcionario = Funcionario (nome, sobrenome, sal_mens)

    for i in range(0,11):
        funcionario.setSal_mens(getSalmens())

    print(showNomecompleto(funcionario.getNome(), funcionario.getSobrenome()))
    print('Salário Anual: '+str(funcionario.getAnual()))

