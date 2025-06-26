valores = []
pares = []
impares = []

while True:
    try:
        valor = int(input('Digite um valor: '))
        valores.append(valor)
        while True:
            resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
            if resp in 'SN':
                break
            else:
                print("Resposta inválida! Digite apenas 'S' para sim ou 'N' para não.")
        if resp == 'N':
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print('=-'*30)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')