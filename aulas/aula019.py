pessoas = {'nome': 'Piter', 'idade': 34, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-'*10)
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*10)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[0]['sigla'])

print('-'*10)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')

