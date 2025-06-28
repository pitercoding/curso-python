dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado!'
elif dados['média'] >=5:
    dados['situação'] = 'Recuperação!'
else:
    dados['situação'] = 'Reprovado(a)!'
print('-='*30)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
