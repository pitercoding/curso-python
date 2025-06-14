print('==== Aumentando Salário ====')
nome = input('Qual o nome do funcionário? ')
salario = float(input('Salário atual do funcionário: '))
aumento = salario * 1.15
print(f'Prazer, {nome}. O seu salário atual é de R$ {salario:,.2f}'.replace('.', ','))
print(f'Vamos aumentá-lo 15% e passará a ser R$ {aumento:,.2f}'.replace('.', ','))
