from tkinter import *

# ========================== Settings ==================
root = Tk()
root.geometry("400x300")
root.title("calculator")
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)
# ========================== Frames =====================
top_first = frame(root, width=400, height=60, bg=color)
tpo_first.pack(side=TOP)

top_second = frame(root, width=400, height=60, bg=color)
tpo_second.pack(side=TOP)

top_third = frame(root, width=400, height=60, bg=color)
tpo_third.pack(side=TOP)

top_forth = frame(root, width=400, height=60, bg=color)
tpo_forth.pack(side=TOP)

# ========================== Buttons =====================
btn_plus = Botton(top_third, text="+",width=10, highlightbackground=color)
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Botton(top_third, text="-",width=10, highlightbackground=color)
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Botton(top_third, text="*",width=10, highlightbackground=color)
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Botton(top_third, text="/",width=10, highlightbackground=color)
btn_div.pack(side=LEFT, padx=10, pady=10)

# ========================== Entries and labels =====================
Label_first_num = Label(top_first, text="Input Number 1: ", bg=color)
Label_first_num.pack(side=LEFT, padx=10, pady=10)

first_num = Entry(top_first, highlightbackground=color)
first_num.pack(side=LEFT, padx=10, pady=10)

Label_second_num = Label(top_second, text="Input Number 2: ", bg=color)
Label_second_num.pack(side=LEFT, padx=10, pady=10)

second_num = Entry(top_second, highlightbackground=color)
second_num.pack(side=LEFT, padx=10, pady=10)

res = Label(top_forth, text="Result: ", bg=color)
res.pack(side=LEFT, padx=10, pady=10)

res_num = Entry(top_forth, highlightbackground=color)
res_num.pack(side=LEFT)

root.mainloop()