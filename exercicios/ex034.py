sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250:
    aumento = sal * 1.10
else:
    aumento = sal * 1.15
print(f'Quem ganhava {sal} passa a ganhar R${aumento:.2f} agora.')