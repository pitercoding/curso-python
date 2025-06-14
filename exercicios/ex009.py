print('==== Tabuada ====')
n = int(input('Tabuada do número: '))
for count in range(1, 11):
    print('{} x {:2} = {}'.format(n, count, n * count))