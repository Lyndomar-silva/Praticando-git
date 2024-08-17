def operação_escolhida():
    operação = input(
        "Escolha + para adição, - para subtração, x para multiplicação, / para divisão:"
    )

    if operação not in ["+", "-", "x", "/"]:
        print("Operação invalida: tente novamente,")
        return operação_escolhida()
    else:
        return operação
