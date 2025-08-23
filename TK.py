from tkinter import *

root = TK()

root.title("new python GUI")

lebel = lebel(root, text='this is test lebel')
lebel.place(x=0, y=0)

lebel = lebel(root, text='this is second test lebel')
lebel.place(x=20, y=20)

root.mainloop()