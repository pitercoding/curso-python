jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0, tot):
    partidas.append(int(input(f'    Quantos goals na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor {values}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'   => Na partida {indice}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')