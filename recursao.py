'''
Recursão
def fat(n):
    if n == 0:
        return 1
    else:
        res = n * fat(n - 1)
        return res

print(fat(4))
'''

'''
Memorização
m = dict()
def fib(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m.get(n)
    else:
        m[n] = fib(n - 1) + fib(n - 2)
        return m[n]


for i in range(50):
    print(fib(i))
'''

'''
Desafio
def soma_elem(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_elem(lista[1:])


lst = [1,2,3,4,5]
print(soma_elem(lst))
'''

'''
Desafio incompleto
def max_elem(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > max_elem(lista[1:]):
        return lista[0]
    else: return max_elem(lista[1:])


list = [2, 5, 9, 54, 500, 5, 72, 464, 0]
print(max_elem(list))
'''
