def executar():
    func = Funcionario()
    func.showName()
    func.getData()

    soma_sal = func.calculaSomaSal()
    print("Soma dos salários é: " + str(soma_sal))

    media_sal = func.mediaSal()
    print("A Média dos salários é: " + str(media_sal))

    imposto_renda = func.calculaImpostoRenda(soma_sal)
    print("Seu imposto de renda é: " + str(imposto_renda))