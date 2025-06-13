# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer, {:^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
divi = n1 // n2
e = n1 ** n2
print('O resultado é: \n Soma {}, \n Subtração {}, \n Multiplicação {}, \n Divisão {:.3f}, \n Divisão Inteira {}, \n Exponenciação {}'.format(s, sub, mul, div, divi, e))

