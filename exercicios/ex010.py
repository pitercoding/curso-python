print('==== Conversor Monetário ====')
reais = float(input('Quantos R$ você deseja converter? R$'))
dolar = reais / 5.54
euro = reais / 6.41
yuan = reais / 0.77
print('==== Resultado ====')
print('Convertendo {:.2f}R$, você terá: \nDólar: {:.2f}US$ \nEuro: {:.2f}€ \nYuan: {:.2f}¥'.format(reais, dolar, euro, yuan))
