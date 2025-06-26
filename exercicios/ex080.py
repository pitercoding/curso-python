valores = []
for c in range(0, 5):  # Loop para pedir 5 valores
    while True:  # Loop para garantir que a entrada seja um número válido
        try:
            valor = int(input(f'Digite um valor para a posição {c}: '))

            # Se for o primeiro valor OU o valor é maior que o último da lista
            if c == 0 or valor > valores[-1]:
                valores.append(valor)
                print(f'Valor {valor} adicionado ao final da lista.')
            else:
                # Caso contrário, encontrar a posição correta para inserir
                pos = 0
                while pos < len(valores):
                    # Se o valor atual é menor ou igual ao valor na posição 'pos', inserir aqui
                    if valor <= valores[pos]:
                        valores.insert(pos, valor)
                        print(f'Valor {valor} adicionado na posição {pos}.')
                        break  # Sai do loop interno 'while pos < len(valores)'
                    pos += 1
                # Se o valor é maior que todos os existentes e o loop terminou (não deveria acontecer se a lógica 'valor > valores[-1]' fosse à prova de balas, mas é bom ter cobertura)
                else:  # Este 'else' pertence ao 'while pos < len(valores)', caso o loop termine sem um break
                    valores.append(valor)
                    print(f'Valor {valor} adicionado ao final da lista (caso especial).')

            # Se a entrada foi válida e o valor foi processado, sai do loop de validação
            break

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

print('=-' * 30)
print(f'Os valores digitados em ordem crescente foram: {valores}')

