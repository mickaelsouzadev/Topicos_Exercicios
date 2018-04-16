
idade = []
altura = []

for i in range(5):
    try:
        altura.append(float(input('Altura: ')))
        idade.append(int(input('Idade: ')))
    except:
        print('Valor invalido: ')

print(idade[::-1])
print(altura[::-1])
