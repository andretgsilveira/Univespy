def aritmetica(lst):
<<<<<<< HEAD
    nElements = len(lst)

    dif2 = 0
    for i in range(nElements):
        dif1 = lst[i] / lst[i + 1]
        if dif1 == dif2:
            return True
        dif2 = dif1

print(aritmetica([3,6,9,12,15]))
=======
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
>>>>>>> a08d58d79fa475428c4e520e9c893df46d1d6d0a
