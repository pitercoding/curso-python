valores = (
    int(input('Primeiro valor: ')),
    int(input('Segundo valor: ')),
    int(input('Terceiro valor: ')),
    int(input('Quarto valor: '))
)
print(f'Você digitou os valores: {valores}.', end='')
print(f'\nO valor 9 apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
