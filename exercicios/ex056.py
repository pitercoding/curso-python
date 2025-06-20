soma_idade = 0
media_idade = 0
maior_idade = 0
nome_velho = ''
mulher_menos_de_vinte = 0

for c in range(1, 5):
    pessoa = print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    else:
        if sexo in 'Mm' and idade > maior_idade:
            maior_idade = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_de_vinte += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é {media_idade:.0f} anos.')
print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulher_menos_de_vinte} mulheres com menos de 20 anos.')