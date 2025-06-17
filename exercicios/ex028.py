from random import randint
from time import sleep
computador = randint(0, 5) # Computador sorteia um número
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print(f'Pensei no número {computador} e você também! ACERTOU!')
else:
    print(f'Pensei no número {computador} e você no número {jogador}. ERROU!')

