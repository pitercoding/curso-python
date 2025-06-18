vel = float(input('Qual a velocidade do carro? '))
multa = (vel-80) * 7
if vel <= 80:
    print(f'Nesta via a velocidade de {vel:.0f}Km/h é permitida. Tenha um bom dia e continue dirijindo com segurança.')
else:
    print('MULTADO! você excedeu o limite permitido que é de 80Km/h.')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')
