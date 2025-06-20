from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    nasc = int(input(f'Digite o {c}° ano de nascimento: '))
    idade = ano_atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas MAIORES de idade!')
print(f'Além de {totmenor} pessoas MENORES de idade!')