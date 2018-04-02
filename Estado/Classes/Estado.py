
class Estado:

    def __init__(self, nome):
        self.__nome = nome
        self.__municipios = []

    def addMunicipio(self, municipio):
        self.__municipios.append(municipio)

    def getPopulacao(self):
        self.__populacao = 0.0
        for i in range(0, len(self.__municipios)):
            self.__populacao += self.__municipios.getPopulacao()

    def getArea(self):
        self.__area = 0.0
        for i in range(0, len(self.__area)):
            self.__area += self.__municipios.getPopulacao()