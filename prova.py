'''
soma = 0
for i in range(1,10):
    if i % 2 == 0:
        soma += i
    else:
        soma -= i
print(soma)
'''

'''
def silaba(str):
    for i in range(len(str)):
        if str[i] in "aeiou":
            print(str[i])

silaba("univesp")
'''
lista = []
var = 0

while var != "x":
    var = input("Informe a nota ou pressione x para sair: ")
    if var == "x":
        break
    else:
        lista.append(var)


def mediaHarmonica(lst):
    acum = 0
    fat = 0
    for i in  lst:
        den = (1 / (int(i) + fat))
        acum = acum + den

    media = (len(lst) / acum) - fat
    return media

if mediaHarmonica(lista) >= 5:
    print("Aprovado")
    print(mediaHarmonica(lista))
else:
    print("Reprovado")
    print(mediaHarmonica(lista))


