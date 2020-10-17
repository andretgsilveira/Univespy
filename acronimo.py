def acronimo(fraseRecebida):
    frase = str(fraseRecebida)
    frase = frase.upper()
    status = 0
    acrony = ''
    for i in range(len(frase)):

        if status == 1:
            if frase[i] == ' ':
                continue
            acrony = acrony + frase[i]
            status = 0

        if i == 0:
            if frase[i] != ' ':
                acrony = acrony + frase[i]

        if frase[i] == ' ':
            status = 1

    return acrony


print(acronimo('andre telles guimaraes silveira'))
