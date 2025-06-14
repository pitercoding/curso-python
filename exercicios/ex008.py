print('==== Conversor de Medidas (Metros) ====')
# --- Pedindo um número ---
try:
    metros = float(input('Digite o valor em metros (m): '))
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    exit()

# --- Múltiplos do Metro ---
quilometros = metros / 1000
hectometros = metros / 100
decametros = metros / 10

# --- Submúltiplos do Metro ---
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000
micrometros = metros * 1_000_000
nanometros = metros * 1_000_000_000

# --- Outras Conversões ---
pes = metros * 3.28084
polegadas = metros * 39.37
jardas = metros * 1.09361

# --- Exibindo os Resultados ---
print('\n--- Conversões ---')
print(f'- {quilometros:.4f} km (quilômetros)')
print(f'- {hectometros:.4f} hm (hectômetros)')
print(f'- {decametros:.4f} dam (decâmetros)')
print(f'- {decimetros:.2f} dm (decímetros)')
print(f'- {centimetros:.2f} cm (centímetros)')
print(f'- {milimetros:.2f} mm (milímetros)')
print(f'- {micrometros:.4f} μm (micrómetros)')
print(f'- {nanometros:.4f} nm (nanómetro)')
print(f'- {pes:.4f} pés')
print(f'- {polegadas:.4f} polegadas')
print(f'- {jardas:.4f} jardas')
