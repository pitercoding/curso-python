frase = 'Curso em Vídeo Python'
#print(frase[3]) Índice 3
#print(frase[3:13]) Inicia índice 3 e termina índice 12
#print(frase[:13]) início ao 12
#print(frase[1:15:2]) Início 1, fim 14, pulando de 2 em 2
#print(frase[::2]) Toda string pulando de 2 em 2
print(frase.upper().count('O'))
print(len(frase))
#print(frase.replace('Python', 'Android'))
print(frase.find('Vídeo'))
dividido = frase.split()
print(dividido[0]) #mostra só o primeiro iten da lista
print(dividido[2][3]) #pega o item 2 e mostra o que tem na 3 posição
