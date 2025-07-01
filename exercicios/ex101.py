def votacao(a):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

#Programa Principal
print(votacao(int(input('Em que ano você nasceu? '))))
