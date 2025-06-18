n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    binario = bin(n)
    print(f'\033[36m{n}\033[m para BINARIO: \033[31m{binario[2:]}\033[m')
elif opcao == 2:
    oct = oct(n)
    print(f'\033[36m{n}\033[m para OCTAL: \033[31m{oct[2:]}\033[m')
elif opcao == 3:
    hex = hex(n)
    print(f'\033[36m{n}\033[m para HEXADECIMAL: \033[31m{hex[2:]}\033[m')
else:
    print('Opção inválida. Digite novamente.')


