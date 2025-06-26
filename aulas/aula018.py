teste = []
teste.append('Piter')
teste.append(34)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print('='*20)
pessoal = [['Ana', 19], ['Roberto', 33], ['Sarah', 3], ['Rebeca', 0]]
print(pessoal[2][1])
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('='*20)

geral = []
dado = [] #lista temporária
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: '))) #pega os dados na lista DADO
    dado.append(int(input('Idade: '))) #pega os dados na lista DADO
    geral.append(dado[:]) #Copia a lista DADO para lista GERAL
    dado.clear() #Limpa a lista dado
print(geral)
for p in geral:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade. Possui {p[1]} anos de idade.')
        totmaior += 1 #Mostra a quantidade de maiores
    else:
        print(f'{p[0]} é menor de idade. Possui {p[1]} anos de idade.')
        totmenor += 1 #Mostra a quantidade de menores.
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')