print('='*20)
print('   CADASTRO GERAL')
print('='*20)
pessoas = []
dado = []
maiorp = menorp = 0
while True:
    try:
        dado.append(str(input('Nome: ')))
        dado.append(float(input('Peso (Kg): ')))
        if len(pessoas) == 0:
            maiorp = menorp = dado[1]
        else:
            if dado[1] > maiorp:
                maiorp = dado[1]
            if dado[1] < menorp:
                menorp = dado[1]
        pessoas.append(dado[:])
        dado.clear()
        while True:
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if resp in 'SN':
                break
            else:
                print("Resposta inválida! Digite apenas 'S' para sim ou 'N' para não.")
        if resp == 'N':
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
print('='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maiorp}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {menorp}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')
print()


