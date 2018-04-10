i = 0
vetor = []

while i < 10:

    try:
        vetor.append((float(input('Digite um número real: '))))
    except:
        print('Digite um número real!')
    i += 1

print(vetor[::-1])