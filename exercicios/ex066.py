soma = quant = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'A soma dos {quant} valores é {soma}.')