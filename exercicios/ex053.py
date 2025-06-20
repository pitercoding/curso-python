print('='*30)
print('    Detector de Palíndromo')
print('='*30)
frase = str(input('Digite uma frase: ')).strip().upper() #Espaços antes/depois eliminados + maiúscula
palavras = frase.split() #Frase separada em um vetor/lista
junto = ''.join(palavras) #Tudo junto em uma string
inverso = junto[::-1] #Inverso com fatiamento

#Teste se é palíndromo
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')