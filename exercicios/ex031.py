from time import sleep
d = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começa sua viagem de {d:.1f}Km.')
print('Calculando...')
sleep(2)
if d <= 200:
    curta = d * 0.50
    print(f'O preço da sua passagem será de R${curta:.2f}.')
else:
    longa = d * 0.45
    print(f'O preço da sua passagem será de R${longa:.2f}.')

