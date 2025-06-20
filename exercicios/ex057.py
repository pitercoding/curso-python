#Fatiamento: strip(). upper() joga para maiúscula. [0] Só pega a primeira letra
sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe o sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')