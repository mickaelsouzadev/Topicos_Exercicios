
con = ['b', 'c' , 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'x', 'w', 'y', 'z']

char = []
i = 0

while i < 10:
    try:
        char.append(input('Digite um caracter: '))
    except:
        print('Não consigo ler nada!')
    i+=1

count = 0
i = 0
charCon = []
while i < len(con):
    if con[i] in char:
        charCon.append(con[i])
        count+=1
    i+=1
print('Total de Consoantes: '+str(count))
print('Consoantes: '+str(charCon))

for i in range(len(con)):
    if con[i] in char:
        charCon.append(con[i])
        count+=1

