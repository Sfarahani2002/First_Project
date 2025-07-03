# print(test)
# None = 1

#raise IndexError("sa indexError")

def colorize(text, color):
    colors = ('red', 'blue', 'pink')
    if type(text) is not str:
        raise TypeError("text must be a bestring")
    elif color not in colors:
        raise ValueError(f"{color} is not in colors")
    else:
        print(f"printed {text} in {color}")
        
colorize("salehFr", 'blue')