class Ponto:
    x = 0
    y = 0

p = Ponto()
Ponto.x = 1
p.x = 2
p.y = 3

print(Ponto.x)
print(p.x)
print(Ponto.x)
print(p.y)