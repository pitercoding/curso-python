produtos_supermercado = (
    "Arroz 5kg", 28.50,
    "Feijão Carioca 1kg", 8.99,
    "Açúcar Refinado 1kg", 4.20,
    "Óleo de Soja 900ml", 7.65,
    "Leite Integral 1L", 5.80,
    "Café Torrado e Moído 500g", 15.90,
    "Pão de Forma Tradicional", 7.10,
    "Manteiga com Sal 200g", 12.50,
    "Ovos Brancos Dúzia", 9.90,
    "Frango Congelado Inteiro 2kg", 22.00,
    "Carne Moída (Patinho) 500g", 18.75,
    "Macarrão Espaguete 500g", 3.50,
    "Molho de Tomate 340g", 2.80,
    "Sabão em Pó 1kg", 11.20,
    "Amaciante de Roupas 500ml", 6.90,
    "Detergente Líquido 500ml", 2.30,
    "Papel Higiênico 12 rolos", 19.90,
    "Creme Dental 90g", 4.50,
    "Shampoo 350ml", 14.00,
    "Refrigerante Cola 2L", 8.00
)
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
'''for produto, preco in produtos_supermercado:
    print(f"- {produto}: R$ {preco:.2f}")'''
for pos in range(0, len(produtos_supermercado)):
    if pos % 2 == 0:
        print(f'{produtos_supermercado[pos]:.<30}', end='')
    else:
        print(f'R${produtos_supermercado[pos]:>7.2f}')
print('-'*40)

