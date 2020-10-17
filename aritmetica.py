def aritmetica(lst):
    nElements = len(lst)

    dif2 = 0
    for i in range(nElements):
        dif1 = lst[i] / lst[i + 1]
        if dif1 == dif2:
            return True
        dif2 = dif1

print(aritmetica([3,6,9,12,15]))
