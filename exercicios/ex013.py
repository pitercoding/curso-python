sal = float(input('Digite seu selário atual: R$'))
sal_reajustado = sal + (sal*15/100)
print('O seu salário atual é R${:.2f} e com o aumento de 15% passará a ser de R${:.2f}'.format(sal, sal_reajustado))