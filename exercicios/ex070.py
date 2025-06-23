print('-' * 20)
print(' Loja Super Baratão')
print('-' * 20)
total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$ '))
    cont += 1
    total += valor
    if valor >= 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra é R${total:.2f}.')
print(f'{totmil} produto(s) custam mais de R$1000.00.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')