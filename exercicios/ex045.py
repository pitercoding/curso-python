from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('====== JOKENPÔ ======')
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

# --- Início da validação da entrada do jogador ---
while True:
    try:
        jogador = int(input('Qual é sua jogada? '))
        if 0 <= jogador <= 2:
            break
        else:
            print('OPÇÃO INVÁLIDA! Por favor, escolha 0, 1 ou 2.')
    except ValueError:
        print('ENTRADA INVÁLIDA! Por favor, digite um número inteiro (0, 1 ou 2).')
# --- Fim da validação da entrada do jogador ---

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-='*10)
print(f'Computador jogou {itens[computador]}.')
print(f'Jogador jogou {itens[jogador]}')
print('-='*10)

# Lógica do jogo
if computador == 0: #PEDRA
    if jogador == 0: #PEDRA
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2: #TESOURA
        print('COMPUTADOR VENCE')
elif computador == 1: #PAPEL
    if jogador == 0: #PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 2: #TESOURA
        print('JOGADOR VENCE')
elif computador == 2: #TESOURA
    if jogador == 0: #PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2: #TESOURA
        print('EMPATE')
