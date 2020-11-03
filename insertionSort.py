def insertion_sort(lst):
    for i in range(1, len(lst)):
        elem = lst[i]
        cont = i - 1
        while cont >= 0 and elem < lst[cont]:
            lst[cont + 1] = lst[cont]
            cont -= 1
        lst[cont + 1] = elem


lista = [1, 5, 4, 2, 3, 1, 7, 9, 33, 12]
insertion_sort(lista)
print(lista)