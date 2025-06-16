import random
print('==== Sorteio ====')
pa = input('Nome do primeiro aluno: ')
sa = input('Nome do segundo aluno: ')
ta = input('Nome do terceiro aluno: ')
qa = input('Nome do quarto aluno: ')
sorteado = random.choice([pa, sa, ta, qa])
print(f'O aluno escolhido foi o {sorteado}')