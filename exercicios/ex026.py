frase = str(input('Digite uma frase: ')).strip().upper()
nova_frase = frase.replace(" ", "")
print(f'A letra "A" aparece {nova_frase.count("A")} vezes na frase.')
print(f'A primeira letra "A" aparece na posição {nova_frase.find("A")+1}.')
print(f'A última letra "A" apareceu na posição {nova_frase.rfind("A")+1}.')


