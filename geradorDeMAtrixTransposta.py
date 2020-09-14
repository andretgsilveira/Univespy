def criaTransposta(m):
    nLinhas = len(m)
    nColunas = len(m[0])
    novaMatris = []
    for i in range(nLinhas):
        for j in range(nColunas):
            novaMatris.append(m[j][i])
    return novaMatris

matrisTeste = [[1,2,3],[4,5,6],[7,8,9]]
m = criaTransposta(matrisTeste)
print(m)