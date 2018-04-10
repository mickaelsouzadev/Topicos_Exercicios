i = 0
vetor = []

while i < 5:

    try:
         vetor.append(int(input('Digite um número: ')))
    except:
        print('Digite um número inteiro')
    i += 1

print(vetor)