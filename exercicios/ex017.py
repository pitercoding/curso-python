from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')