n = (input('Digite algo: '))
print(f'Só tem espaços? \033[31m{n.isspace()}\033[m')
print(f'É numérico? \033[32m{n.isnumeric()}\033[m')
print(f'É alfabetico? {n.isalpha()}')
print(f'É alfa numérico? ? {n.isalnum()}')
print(f'Está em letras maiúsculas? {n.isupper()}')
print(f'Está em letras minúsculas? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')



