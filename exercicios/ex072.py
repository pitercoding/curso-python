contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezesete', 'dezoito',
            'dezenove', 'vinte')
while True:
    try:
        resposta = int(input("Digite um número entre 0 e 20: "))
        if 0 <= resposta <= 20:
            print(f'Você digitou {contagem[resposta]}.')
            resposta = str(input("Deseja continuar?[S/N] ")).upper().strip()[0]
            if resposta[0] in "N":
                break
            while resposta [0] not in 'SN' :
                resposta = str(input("Resposta inválida. Deseja continuar?[S/N] ")).upper().strip()[0]
        else:
            print('Número fora do intervalo sugerido. Tente novamente.')
    except ValueError:
        print('Valor inválido, tente novamente.')
print('Fim do programa.')


