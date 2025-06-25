lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

#Se não precisar de posição
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('-'*15)

#Com posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
print('-'*15)

#Com posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('-'*15)

print('Comi muito!')