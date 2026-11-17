# contador = 1
# while contador <= 10:
#     print(contador)
#     #contador = contador + 1   #posso também trocar 4 pelo 3, mas teria que começar com 0, pois iria esconder o 1 e mostrar o 11.
#     contador += 1

contador = 1
soma = 0

while contador <=5: #quantidade de vezes precisar girar esse laço
    #soma = 0 #aqui ele só recebe zero e vai somar apenas com número que digitar, ou seja, 1+0 e 2+0
    n = float(input('Digite um valor: '))
    soma = soma + n
    contador += 1
    print(f'total {soma}') #printa a cada soma que digitar

print(f'total {soma}') #mostra resultado final