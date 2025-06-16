# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
mai = nome.upper()
min = nome.lower()
tot = len(nome) - nome.count(' ')
primeiro_nome = nome.split()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {mai}.')
print(f'Seu nome em minúsculas é: {min}.')
print(f'Seu nome tem ao todo {tot} letras.')
print(f'Seu primeiro nome é: {primeiro_nome[0]}. Ele tem {len(primeiro_nome[0])} letras.')
