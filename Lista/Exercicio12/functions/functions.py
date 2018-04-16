from classes.Aluno import *

def calculaMedia(alunos):

    soma = 0

    for i in range(len(alunos)):
        soma += alunos[i].getAltura()

    media = soma / len(alunos)

    return media

def menor13(alunos):

    media = calculaMedia(alunos)
    count = 0

    for i in range(len(alunos)):
        if alunos[i].getIdade() > 13 and alunos[i].getAltura() < media:
            count += 1

    return count

def addAluno():

    ok = False

    while not ok:
        try:
            nome = input('Digite o nome do aluno: ')
            idade = int(input('Digite a idade do aluno: '))
            altura = float(input('Digite a altura do aluno: '))
            ok = True
        except ValueError:
            print('Valor invalido!')

    aluno = Aluno(nome, idade, altura)

    return aluno
