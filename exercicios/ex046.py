from time import sleep
print('='*35)
print('Contagem regressiva para Réveillon')
print('='*35)
inicio = int(input('Digite 0 para começar! '))
if inicio == 0:
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    print('FELIZ ANO NOVO!!!')