
def getNome():
    nome = input('Insira o nome: ')
    return  nome

def getSobrenome():
    sobrenome = input('Insira o sobrenome: ')
    return sobrenome

def getSalmens():
    sal_mens = 0.0
    while(not float(sal_mens)):
        try:
            sal_mens = float(input('Insira o salário mensal: '))
        except:
            print('Valor Invalido!')
    return sal_mens

def showNomecompleto(nome, sobrenome):
    return nome+' '+sobrenome