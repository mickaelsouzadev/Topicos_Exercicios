
class Funcionario:

    def __init__(self, nome, sobrenome, sal_mens):
        self.__nome = nome
        self.__sobrenome = sobrenome
        if(sal_mens < 0):
            self.__sal_mens = 0.0
        self.__sal_mens = sal_mens

    def getNome(self):
        return self.__nome

    def getSobrenome(self):
        return self.__sobrenome

    def getSal_mens(self):
        return  self.__sal_mens

    def setNome(self, nome):
        self.__nome = nome

    def setSobrenome(self, sobrenome):
         self.__sobrenome = sobrenome

    def setSal_mens(self, sal_mens):
        if (sal_mens < 0):
            self.__sal_mens += 0.0
        self.__sal_mens += sal_mens
    def getAnual(self):
        self.__sal_anual = self.__sal_mens
        self.__sal_anual = self.__sal_anual + self.__sal_anual * 0.11
        return self.__sal_anual
