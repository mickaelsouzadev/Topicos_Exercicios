
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas = {}

for i in range(len(meses)):
    temperaturas[meses[i]] = float(input("Digite a temperatura de " +str(meses[i])+": "))

print(temperaturas)