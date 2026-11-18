contador = 0
despesa = 0
while True:
    contador += 1
    n = float(input('Qual valor do gasto: '))
    despesa = despesa + n

    print(f'\nQuantidade de despesa: {contador}')
    print(f'Valor total de despesa: {despesa}')

    resposta = input('\nQuer encerrar o sistema:[S/N]: ').upper()

    if resposta == 'S':
        print('\nSITEMA ENCERRADO')
        break

