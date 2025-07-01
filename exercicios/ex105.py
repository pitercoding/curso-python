def notas(*n, sit=False):
    """
    -> Função para analisar notas e situacao de aluno
    :param n: uma ou mais notas do aluno
    :param sit: valor opcional, indica se deve ser sit
    :return: dicionario com as notas e situacao
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa Principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
#help(notas)