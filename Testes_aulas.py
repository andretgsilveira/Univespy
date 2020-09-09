"""
l = ['cão', 'gato', 'coelho']
for i in l:
    print(i)

s = 'algoritmos'
for c in s:
    if c in 'aeiou':
        print(c)

x = 0
while x < 10:
    print(x)
    x += 1

num = eval(input('Digite um numero positivo '))
while num < 0:
    num = eval(input('Digite um numero positivo '))
print(num * num)

l = []
nome = input('Digite um nome: ')
while nome != '':
    l.append(nome)
    nome = input('Digite o proximo nome: ')
print(*l)
"""

