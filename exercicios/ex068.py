from random import randint
v = 0
while True:
    print('=-' * 15)
    print('    P A R  O U  Í M P A R')
    print('=-' * 15)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total},', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Você venceu!.')
            v += 1
        else:
            print(f'Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Você venceu!')
            v += 1
        else:
            print(f'Você perdeu!')
            break
    print(f'vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

