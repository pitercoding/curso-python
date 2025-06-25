from random import randint
numeros = (randint(1,10), #Sorteio 1
           randint(1,10), #Sorteio 2
           randint(1,10), #Sorteio 3
           randint(1,10), #Sorteio 4
           randint(1,10)  #Sorteio 5
           )
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')