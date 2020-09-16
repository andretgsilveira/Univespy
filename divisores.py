def divisores(numero):
    rst = 0
    div = []
    for i in range(1, numero + 1):
        rst = numero % i
        if rst == 0:
            div.append(i)
        rst = 0
    return div


for i in range(20):
    print(i , divisores(i))