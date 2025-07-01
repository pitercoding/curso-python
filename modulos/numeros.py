from uteis import numeros
#Programa Principal
n= int(input('Digite um número: '))
fat = numeros.fatorial(n)
print(f'O fatorial de {n} é {fat}.')
print(f'O dobro de {n} é {numeros.dobro(n)}')
print(f'O triplo de {n} é {numeros.triplo(n)}')