print('='*20)
print('   GERADOR DE PA')
print('='*20)

pt = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja continuar? Quantos termos quer mostrar? '))
print(f'Progressão finalziada com {total} termos mostrados.')
