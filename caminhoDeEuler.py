def caminhoDeEuler(matriz):
    total = 0
    i = 1
    n = len(matriz)
    while total <= 2 and i <= n:
        grau = 0
        c = 0
        for l in matriz:
            grau = grau + sum(l)
            if (grau % 2) != 0:
                total += 1

        i += 1
    if total > 2:
        print('Não há caminho de Euler')
    else:
        print('Há caminho de Euler')


matrizTesteErro = [[0, 2, 1, 0, 0],
                   [2, 0, 1, 0, 0],
                   [1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 2],
                   [0, 0, 1, 2, 0]]

caminhoDeEuler(matrizTesteErro)

matrizTesteCerto = [[0, 2, 1, 1, 0, 0, 0],
                    [2, 0, 0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 1, 0],
                    [1, 1, 0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 0, 0, 1],
                    [0, 0, 1, 1, 0, 0, 2],
                    [0, 0, 0, 1, 1, 2, 0]]

caminhoDeEuler(matrizTesteCerto)