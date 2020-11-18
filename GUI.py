from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='rocket.gif').subsample(5)
image = Label(master=root, image=photo, width=200, height=200)
image.pack(side=BOTTOM)
text = Label(master = root, text='Rocket')
text.pack(side=TOP)
root.mainloop()