class Funcionario:


    def __init__(self):
        print('Sistema do Funcionário: ')
        self.nome_func = input("Nome do Funcionário: ")
        self.sobrenome_func = input("Sobrenome do Funcionário: ")
        self.sal_func = []
        self.gasto_func = []
        self.poupanca = []

    def showName(self):
        print("Nome Completo: " + self.nome_func + " " + self.sobrenome_func)

    def getData(self):
        count = 0
        while count < 12:
            try:
                sal = float(input("Informe o salário do Mês " + str(count + 1) + " : "))
                self.sal_func.append(sal)

                gasto = float(input("Informe o gasto do Mês " + str(count + 1) + " : "))
                self.gasto_func.append(gasto)
                if (gasto > sal):
                    raise Exception('Gasto Demais, não pode!')

                count = count + 1

            except Exception as e:
                print(str(e))
            except:
                print("Valor Invalido.")


    def calculaSomaSal(self):
        count = 0
        soma = 0

        for i in range(0, 12):
            soma = soma + self.sal_func[count]
            count = count + 1
        return soma

    def mediaSal(self):
        media_sal = self.calculaSomaSal()
        media_sal = media_sal / 12

        return media_sal

    def calculaPoupanca(self):

        for i in range(0, 12):
            self.poupanca.append(self.sal_func[i] - self.gasto_func[i])
            self.poupanca[i] = (self.poupanca[i] + self.poupanca[i])

    def calculaImpostoRenda(self, soma_sal):

        if soma_sal <= 22847.76:
            return "Isento"
        elif soma_sal >= 22847.77 and soma_sal <= 33919.80:
            imposto_renda = soma_sal * 0.075
            return imposto_renda
        elif soma_sal >= 33919.81 and soma_sal <= 45012.60:
            imposto_renda = soma_sal * 0.15
            return imposto_renda
        elif soma_sal >= 45012.61 and soma_sal <= 55976.16:
            imposto_renda = soma_sal * 0.225
            return imposto_renda
        elif soma_sal > 55976.16:
            imposto_renda = soma_sal * 0.275
            return imposto_renda



