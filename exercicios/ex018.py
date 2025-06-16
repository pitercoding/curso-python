from math import sin, cos, tan , radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O ângulo de {ang:.1f} tem:')
print(f'SENO de {seno:.2f}')
print(f'COSSENO de {cosseno:.2f}')
print(f'TANGENTE de {tangente:.2f}')
