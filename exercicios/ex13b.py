p = float(input('Qual o valor do produto? R$'))
p_avista = p - (p * 12 / 100)
p_juros = p + (p * 8 / 100)
print('O preço do produto é R${:.2f}. \nÀ vista e com 12% de desconto sairá por R${:.2f}. \nParcelado terá 8% de juros, resultando no preço final de R${:.2f}.' .format(p, p_avista, p_juros))