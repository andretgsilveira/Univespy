class Fila():
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def insert(self,x):
        self.data.append(x)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def empty(self):
        return not len(self.data) > 0


filaPreferencial = Fila()
filaComum = Fila()
idade = None

fila = [20, 40, 60, 67, 70, 30, 40, 20, 50, 10]
for cliente in fila:
    if cliente > 60:
        filaPreferencial.insert(cliente)
    else:
        filaComum.insert(cliente)


count = 0

while (len(filaPreferencial) + len(filaComum)) > 0:
    if count > 1:
        print(filaPreferencial.remove())
        count = -1
    else:
        print(filaComum.remove())
    count += 1
