from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime


def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%a', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was um {}'.format(date, weekday))


root = Tk()
label = Label(root, text='Digite uma data para saber o dia\n da semana(Ex.: Nov 11, 2020): ')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Click', command=clicked)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()
