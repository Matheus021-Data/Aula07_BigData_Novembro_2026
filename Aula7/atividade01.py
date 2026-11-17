META = 2000
cadastro = 'S'

while cadastro == 'S':
    nome = input('Nome do vendedor: ')
    valor_vendido = float(input('Valor da venda: '))
    atigimento = (valor_vendido/META)*100
    cadastro = input('Deseja continuar?[S/N]: ').upper 

    print(f'Nome: {nome}\n'
      f'valor_vendido: {valor_vendido:.2f}\n'
      f'Atigimento: {atigimento}/100')

print('\nProgrma encerrado')
    

    

