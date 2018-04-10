
def calculaMedia(notas):
    media = (notas[0] + notas[1] + notas[2] + notas[3])
    media = media/4
    return media

i = 0
notas = []

while i < 4:

    try:
        notas.append(float(input('Digite a Nota: ')))
    except:
        print('Somente números reais!')

    i+=1

media = calculaMedia(notas)
print('Media: '+str(media))
