print('==== Pintando Parede ====')
largura = float(input('Qual a largura da parede em metros(m)?'))
altura = float(input('Qual a altura da parede(m)?'))
area = largura * altura
litros_tinta = area / 2
print('Para pintar uma parede de altura {:.2f}m e largura {:.2f}m, será necessário {:.2f}l de tinta.'.format(altura, largura, litros_tinta))

