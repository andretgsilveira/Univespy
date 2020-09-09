def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    return i == num

"""
numero = 0
while numero <= 20:
    if primo(numero):
        print(numero)
    numero += 1
"""

for n in range(2,100):
    if not primo(n):
        continue
    print(n)