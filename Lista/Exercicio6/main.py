
count = 0
notas = []
alunos = {}
medias = {}


while count < 10:
    nome = input('Digite o nome do aluno: ')
    for i in range(4):
        try:
            notas.append(float(input('Digite a nota'+str(i+1)+' do aluno: ')))
        except:
            print('Valor invalido!')
    alunos[nome] = notas
    count+=1
    notas = []

count = 0

for nome in alunos:
    media = sum(alunos[nome]) /len(alunos[nome])
    medias[nome] = media



for nome in medias:

    if medias[nome] >= 7.0:
        count += 1

print(count)