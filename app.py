from math import trunc
from opção_selecionada import operação_escolhida

def calculadora():
    numero_1 = int(input("Digite um numero:"))
    numero_2 = int(input("Digite outro numero:"))
    
    operação = operação_escolhida()
    
    if operação == "+":

        soma = numero_1 + numero_2
        print(f"A soma dos numeros é {soma}")

    elif operação == "-":

        subtração = numero_1 - numero_2
        print(f"A subtração dos numeros é {subtração}")

    elif operação == "x":

        multiplicação = numero_1 * numero_2
        print(f"A multiplicação dos numeros é {multiplicação}")
    else:

        divisão = numero_1 / numero_2
        print(f"A divisão dos numeros é {trunc(divisão)}")

calculadora()
