META = 2000
cadastro = 'S'

while cadastro == 'S':
    nome = input('Nome do vendedor: ')
    valor_vendido = float(input('Valor da venda: '))
    atigimento = (valor_vendido/META)*100
    

    if atigimento >= 100:
        atigimento = atigimento + 500
        print(f'Nome: {nome}')
        print(f'Atigimento atualizado: {atigimento}')
        cadastro = input('Deseja continuar?[S/N]: ').upper

    elif atigimento >= 70 and atigimento < 100:
        atigimento = atigimento + 200
        print(f'Nome: {nome}')
        print(f'Atigimento atualizado: {atigimento}')
        cadastro = input('Deseja continuar?[S/N]: ').upper
    else:
        print(f'Nome: {nome}')
        print(f'Atigimento sem bonus: {atigimento}')

        


