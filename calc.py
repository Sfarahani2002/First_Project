from tkinter import *

# ==========================settings==================
root = Tk()
root.geometry("400x300")
root.title("calculator")
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)
# ==========================frames=====================
top_first = frame(root, width=400, height=60, bg='blue')
tpo_first.pack(side=TOP)

top_second = frame(root, width=400, height=60, bg='white')
tpo_second.pack(side=TOP)

top_third = frame(root, width=400, height=60, bg='red')
tpo_third.pack(side=TOP)

top_forth = frame(root, width=400, height=60, bg='yellow')
tpo_forth.pack(side=TOP)

root.mainloop()