valor_casa = float(input('Valor da casa? R$'))
sal = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao =  valor_casa / (anos * 12)
print(f'Para pagar uma casa de {valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
if prestacao < sal * 30 / 100:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo NEGADO!')
