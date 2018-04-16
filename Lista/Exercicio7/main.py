
vetor = []
soma = 0
mult = 1

for i in range(5):
    try:
        vetor.append(int(input('Digite um valor inteiro: ')))
    except:
        print('Valor invalido!')


for i in range(5):
    soma += vetor[i]
    mult *= vetor[i]

print('Soma: '+str(soma))
print('Multiplicação: '+str(mult))