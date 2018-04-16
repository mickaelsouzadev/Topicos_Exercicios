from classes.Aluno import *
from functions.functions import *

alunos = []

for i in range(30):
    alunos.append(addAluno())

print(alunos)
count = menor13(alunos)

print("Total de alunos: "+str(count))