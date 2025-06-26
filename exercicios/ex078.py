valores = []
for i in range(0, 5):
    while True:
        try:
            valor = int(input(f'Digite um valor para a posição {i}: '))
            valores.append(valor)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

print('=-'*30)
print(f'Você digitou os valores: {valores}')

# Encontrando o maior e o menor valor de forma otimizada
maior = max(valores)
menor = min(valores)

# Encontrando as posições do(s) maior(es) valor(es)
posicoes_maior = []
for i, v in enumerate(valores):
    if v == maior:
        posicoes_maior.append(i)

# Encontrando as posições do(s) menor(es) valor(es)
posicoes_menor = []
for i, v in enumerate(valores):
    if v == menor:
        posicoes_menor.append(i)

print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições: {posicoes_maior}')
print(f'O menor valor digitado foi {menor} nas posições: {posicoes_menor}')
