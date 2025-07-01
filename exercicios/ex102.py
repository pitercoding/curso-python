def fatorial(n, show=False):
    """
        -> Calcula o fatorial do número digitado.
        :param n: O número a ser calculado.
        :param show: (opcional) mostrar ou não a conta.
        :return: Retorna o valor de n.
        """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5, show=True))
#help(fatorial)