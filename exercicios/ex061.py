print('='*20)
print('   GERADOR DE PA')
print('='*20)

pt = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')