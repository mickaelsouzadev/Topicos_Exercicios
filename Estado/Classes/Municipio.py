
class Municipio:

    def __init__(self, nome, populacao, area):
        self.__nome = nome
        self.__populacao = populacao
        self.__area = area

    def getNome(self):
        return self.__nome

    def getPopulacao(self):
        return self.__populacao

    def getArea(self):
        return self.__area