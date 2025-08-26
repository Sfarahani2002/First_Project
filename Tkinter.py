from tkinter import *

root = TK()
root.title("Entry")
root.geometry("400x300")
root.resizable(width=false, height=false)

nameLanel = Label(root, text="please enter your name :")
namelabel.place(x=8, y=10)

nameInput = Entry(root)
nameInput.place(x=8, y=30)

def get_name():
    print(nameInput.get())

btn = Button(root, text="Get Name",command=lambda:get_name())
btn.place(x=10, y=60)

root.mainloop()