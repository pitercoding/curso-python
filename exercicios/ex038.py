from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print(f'Números digitados: {n1} e {n2}.')
print('Comparando...')
sleep(2)
if n1 > n2:
    print(f'O primeiro valor é maior.')
elif n2 > n1:
    print(f'O segundo valor é maior.')
else:
    print('Não existe valor maior. Ambos são iguais.')