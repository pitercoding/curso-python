palavras = (
    "cachorro", "mesa", "telefone", "nuvem", "floresta",
    "computador", "janela", "bicicleta", "montanha", "sorvete",
    "oceano", "churrasco"
)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')