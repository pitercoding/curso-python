soma = 0 #acumulador
count = 0 #contador
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma += n
        count += 1
print(f'Você informou {count} valores PARES. A soma deles é {soma}')