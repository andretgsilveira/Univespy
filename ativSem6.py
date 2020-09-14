"""
list = ['a',1,'b',2]
d = dict()
for i in range(len(list)-1):
    d[list[i]] = list[i+1]

print(d['b'])


list = [1,2,[3,4]]

for i in list:
    print(i)

list = [-1,2,-3,4]
aux = 0
for i in list:
    aux += i
print(aux)

list = [1, -2, -3, 4]
aux = 0
for i in list:
    if i % 2 == 0:
        aux += 1
print(aux)

"""

for i in range(1,5):
    print(i)