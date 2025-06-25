times = (
    'Botafogo',         # 1º lugar
    'Palmeiras',        # 2º lugar
    'Flamengo',         # 3º lugar
    'Fortaleza',        # 4º lugar
    'Internacional',    # 5º lugar
    'São Paulo',        # 6º lugar
    'Corinthians',      # 7º lugar
    'Bahia',            # 8º lugar
    'Cruzeiro',         # 9º lugar
    'Vasco da Gama',    # 10º lugar
    'Vitória',          # 11º lugar
    'Atlético-MG',      # 12º lugar
    'Fluminense',       # 13º lugar
    'Grêmio',           # 14º lugar
    'Juventude',        # 15º lugar
    'Red Bull Bragantino', # 16º lugar
    'Athletico-PR',     # 17º lugar (rebaixado)
    'Criciúma',         # 18º lugar (rebaixado)
    'Atlético-GO',      # 19º lugar (rebaixado)
    'Cuiabá'            # 20º lugar (rebaixado)
)

print('-='*20)
print(f'Lista dos times do Brasileirão 2024: {times}')
print('-='*20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos colocados são: {times[16:20]}') #[-4:]
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'O time do Vitória está na {times.index('Vitória')+1}ª posição.')
print('-='*20)


