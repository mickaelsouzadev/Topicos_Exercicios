from math import *

A = []
soma = 0

for i in range(10):
    try:
        A.append(int(input('Digite um valor inteiro: ')))
    except:
        print('Valor invalido!')

for i in range(10):
    soma+= pow(A[i], 2)

print('Soma: '+str(soma))