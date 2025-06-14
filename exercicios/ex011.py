print('==== Pintando Parede ====')
largura = float(input('Qual a largura da parede em metros(m)?'))
altura = float(input('Qual a altura da parede(m)?'))
area = largura * altura
litros_tinta = area / 2
print('Sua parede tem as dimensões: {:.2f} x {:.2f} e área de {:.2f}m². \nPara pintar essa parede, será necessário {:.2f}l de tinta.'.format(largura, altura, area, litros_tinta))

