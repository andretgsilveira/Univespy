'''
ex 3.14
def trocaPU(lst):
    if len(lst) < 0:
        exit
    else:
        lst[0], lst[-1] = lst[-1], lst[0]


ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(ingredientes)
'''
'''
ex 3.15

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def olimpiadas(t):

    t.pensize(3)
    t.setheading(0)

    jump(t, 0, 0)
    t.circle(50)
    jump(t, -110, 0)
    t.circle(50)
    jump(t, 110, 0)
    t.circle(50)
    jump(t, -55, -50)
    t.circle(50)
    jump(t, 55, -50)
    t.circle(50)
    i = 0
    while i < 10000000:
        i +=1
        continue

import turtle

s = turtle.Screen()
t = turtle.Turtle()

olimpiadas(t)

'''
'''
ex 4.8
def palavra(arq):
    arqEntrada = open(arq, 'r')
    conteudo = arqEntrada.read()
    arqEntrada.close()
    novaPalavra = ''
    listaPalavras = conteudo.split()
    novaListaPalavras = []
    for palavra in listaPalavras:
        for letra in palavra:
            if letra not in "!,.:;?":
                novaPalavra = novaPalavra + letra
        novaListaPalavras.append(str(novaPalavra))
        novaPalavra = ''
    listaPalavras = novaListaPalavras
    print(listaPalavras)

palavra('exemplo.txt')
'''
'''
ex 4.9
def meuGrep(arq, text):
    infile = open(arq)
    linha = 1
    linhas = []
    for line in infile:
        if text in line:
            linhas.append(linha)
        linha = linha + 1
    return linhas

print(meuGrep('exemplo.txt','line'))
'''


