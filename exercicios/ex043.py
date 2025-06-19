print('='*10)
print('  I M C')
print('='*10)
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida, CUIDADO!')