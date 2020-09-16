def aritmetica(lst):
    nElementos = len(lst)
    if len(lst) == 1:
        return True
        exit(aritmetica())

    media = lst[1] - lst[0]
    for i in range(nElementos - 1):
        print(lst[i + 1] - lst[i])  # visualização do teste
        if lst[i + 1] - lst[i] != media:
            status = False
        else:
            status = True
    return status


x = aritmetica([3, 6, 9, 12, 15, 18, 22])

print(x)
