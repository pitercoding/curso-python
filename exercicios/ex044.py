print('======= LOJAS GOMES =======')
total = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
condicao = int(input('Qual é a forma de pagamento? '))
if condicao == 1:
    valor = total - (total * 10 / 100) #10% desconto
elif condicao == 2:
    valor = total - (total * 5 / 100) #5% desconto
elif condicao == 3:
    valor = total #sem desconto
    parc_mensal = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parc_mensal:.2f}. SEM JUROS!')
elif condicao == 4:
    valor = total + (total * 20 / 100) #20% de juros
    parcelas = int(input('Quantas parcelas? '))
    parc_mensal = valor / parcelas
    print(f'Sua compra terá 20% DE JUROS e será parcelada em {parcelas}x de R${parc_mensal:.2f}')
else:
    valor = total
    print('OPÇÃO INVÁLIDA! Tente novamente.')
print(f'Sua compra de R${total:.2f} vai custar R${valor:.2f} no final.')
