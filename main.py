def numero_par():
    número = int(input('Digite um número, direi se é par ou ímpar:'))

    if número % 2 == 0:
        print(f'o número {número} é par.')
    else:
        print(f'o número {número} é impar.')

numero_par()