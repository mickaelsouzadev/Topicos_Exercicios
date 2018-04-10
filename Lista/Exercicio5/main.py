def calculaPar(n):
    if n % 2 == 0:
        return True

def calculaImPar(n):
    if n % 2 != 0:
        return True

all = []
i = 0
while i < 20:

    try:
        all.append(int(input('Digite um número inteiro: ')))
    except:
        print('Digita um número inteiro disgraça!')
    i+=1

i = 0
par = []
impar = []

while i < 20:

    if calculaPar(all[i]):
        par.append(all[i])

    if calculaImPar(all[i]):
        impar.append(all[i])

    i+=1


print('Total: '+str(all))
print('Pares: '+str(par))
print('Impares: '+str(impar))
