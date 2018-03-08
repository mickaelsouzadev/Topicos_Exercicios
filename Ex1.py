def somaSal(sal_func):
    count = 0
    soma = 0

    while count < 12:
        soma = (soma + sal_func[count])
        count = count + 1

    return soma

def mediaSal(sal_func):
    media_sal = somaSal(sal_func)
    media_sal = media_sal / 12

    return media_sal

def calculaImpostoRenda(soma_sal):
    if soma_sal <=  22847.76:
        return "Isento"
    elif soma_sal >= 22847.77 and soma_sal <= 33919.80:
        imposto_renda = soma_sal * 0.075
        return imposto_renda
    elif soma_sal >= 33919.81 and soma_sal <=  45012.60:
        imposto_renda = soma_sal * 0.15
        return imposto_renda
    elif soma_sal >= 45012.61 and soma_sal <= 55976.16:
        imposto_renda = soma_sal * 0.225
        return imposto_renda
    elif soma_sal > 55976.16:
        imposto_renda = soma_sal * 0.275
        return imposto_renda

print("Sistema do Funcionário")

sal_func = []

nome_func = input("Nome do Funcionário: ")
sobrenome_func = input("Sobrenome do Funcionário: ")

count = 0

while count < 12:
    sal_func.append(int(input("Informe o salário do Mês "+str(count+1)+" : ")))
    count = count + 1

print("Nome Completo: "+nome_func+" "+sobrenome_func)

soma_sal = somaSal(sal_func)
print("Soma dos salários é: "+str(soma_sal))

media_sal = mediaSal(sal_func)
print("A Média dos salários é: "+str(media_sal))

imposto_renda = calculaImpostoRenda(soma_sal)
print("Seu imposto de renda é: "+str(imposto_renda))
