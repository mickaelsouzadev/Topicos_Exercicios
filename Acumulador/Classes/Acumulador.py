
class Acumulador:

    def __init__(self):
        self.__count = 0

    def incrementar(self):
        self.__count += 1

    def zerar(self):
        self.__count = 0

    def retornar(self):
        return self.__count
