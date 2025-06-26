valores = []

while True:
    try:
        valor = int(input('Digite um valor: '))  # Pede um número
        valores.append(valor)

        while True:
            resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

            if resp in 'SN':
                break
            else:
                print("Resposta inválida! Digite apenas 'S' para sim ou 'N' para não.")

        if resp == 'N':
            break

    except ValueError: # Captura erro se o usuário não digitar um número
        print("Entrada inválida. Por favor, digite um número inteiro.")

print('=-'*30)

print(f'Você digitou {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}.')

if 5 in valores:
    print(f'O valor 5 faz parte da Lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
