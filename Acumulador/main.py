from Classes.Acumulador import *

acumulador = Acumulador()

for i in range(100):
    acumulador.incrementar()

print(acumulador.retornar())

acumulador.zerar()

print(acumulador.retornar())
