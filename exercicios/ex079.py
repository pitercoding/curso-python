valores = []

while True:
    try:
        valor = int(input('Digite um valor: ')) # Pede um número

        if valor not in valores: # Verifica se o valor já está na lista
            valores.append(valor) # Adiciona se não for duplicado
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado! Não vou adicionar.') # Informa se for duplicado

        # --- Início da validação para "Quer continuar?" ---
        while True: # Loop para garantir uma resposta válida (S ou N)
            resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
            if resp in "SN": # Se a resposta for S ou N, é válida
                break # Sai do loop de validação de 'resp'
            else:
                print("Resposta inválida! Digite apenas 'S' para sim ou 'N' para não.")
        # --- Fim da validação para "Quer continuar?" ---

        if resp == "N": # Só sai do loop principal 'while True' se a resposta final for 'N'
            break

    except ValueError: # Captura erro se o usuário não digitar um número
        print("Entrada inválida. Por favor, digite um número inteiro.")

print('-=' * 30)
valores.sort() # Ordena os valores no final
print(f'Você digitou os valores: {valores}')
print('Fim do programa!')
