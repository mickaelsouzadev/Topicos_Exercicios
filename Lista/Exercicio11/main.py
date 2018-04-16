def intercalar(lG):
    lI = []
    for i in range(len(lG)):
        for j in range(len(lG)):
            lI.append(lG[j][i])
    return lI

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor1.append(input("Digite um valor pro vetor 1: "))
    vetor2.append(input("Digite um valor por vetor 2: "))
    vetor3.append(input("Digite um valor por vetor 3: "))

lG = []
lG.append(vetor1)
lG.append(vetor2)
lG.append(vetor3)

vetorIntecalado = intercalar(lG)

print(vetorIntecalado)