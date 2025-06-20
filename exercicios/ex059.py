from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''MENU - Escolha uma opção: 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair ''')
    opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}.')
    elif opcao == 2:
        multi = n1 * n2
        print(f'Multiplicando {n1} e {n2} o resultado é {multi}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}.')
    elif opcao == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção invalida! Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre.')




