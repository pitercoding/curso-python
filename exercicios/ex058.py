from random import randint
from time import sleep
computador = randint(0, 10)
tentativas = 1

print('-='*25)
print('    Pensando entre 0 e 10. Tente adivinhar...')
print('-='*25)

jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(0.3)

while jogador != computador:
    print('Você errou. Tente novamente.')
    tentativas += 1

    if jogador < computador:
        print('Dica: É mais para CIMA!')
    else:
        print('Dica: É mais para BAIXO!')

    jogador = int(input('Qual é o seu próximo palpite? '))
    print('PROCESSANDO...')
    sleep(0.3)

print(f'PARABÉNS! Você acertou! Você precisou de {tentativas} tentativas.')

