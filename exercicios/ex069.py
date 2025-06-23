quant = masc = fem = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]

    if idade >= 18:
        quant += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1

    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if parar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {quant}')
print(f'Ao todo temos {masc} homens cadastrados.')
print(f'E temos {fem} mulheres com menos de 20 anos.')