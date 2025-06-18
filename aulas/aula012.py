nome = str(input('Digite seu nome: '))
if nome == 'Piter':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}.')