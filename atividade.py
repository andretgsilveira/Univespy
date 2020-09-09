print('Digite três valores e descubra se eles formam um triangulo e que triangulo seria.')
a = eval(input('Digite o primeiro valor '))
b = eval(input('Digite o segundo valor '))
c = eval(input('Digite o terceiro valor '))

lst = [a,b,c]
maior = max(lst)
lst.remove(maior)
somaLados = sum(lst)
if maior < somaLados:
    print('É um triangulo ')
    if a == b and a == c:
        print('trinagulo equilatero')
    elif a != b and a != c and b != c:
        print('triangulo escaleno')
    else:
        print('triangulo isoseles')
else:
    print('Não é um triangulo')