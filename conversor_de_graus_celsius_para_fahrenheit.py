def convertTemp(temp):
    c_temp = eval(temp)
    f = 1.8 * c_temp + 32
    return f

c = '';
while c != 's':
    print('\nA qualquer momento pressione "s" para sair\n')
    c = input('Informe a temperatura em graus Celsius:');
    if c != 's':
        f = convertTemp(c)
    print('A temperatura é:', f, 'graus Fahrenheit')


