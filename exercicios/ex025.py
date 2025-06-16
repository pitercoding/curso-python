#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é seu nome completo? ')).strip()
teste = 'SILVA' in nome.upper()
print(f'Seu nome tem Silva? {teste}')
