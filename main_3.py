import pyfiglet
import termcolor2
from termcolor2 import colored
#---------------------------------------------------------
print('saleh')
print('-----------------')
print(pyfiglet.figlet_format('saleh'))
print(termcolor2.colored((pyfiglet.figlet_format('mohammad')),color= 'blue'))

#---------------------------------------------------------
valid_colors = ("red", 'green','blue', 'yellow')
message = input('what would you like to print? : ')
color= input('what color? : ')
if color not in valid_colors:
     color = "blue"
     
ascii_art = pyfiglet.figlet_format(message)
ascii_art = colored(ascii_art,color=color)
print(ascii_art)
#---------------------------------------------------------
valid_colors = ("red", 'green','blue', 'yellow')
def print_art(color,message):
    if color not in valid_colors:
        color = "blue"

    ascii_art = pyfiglet.figlet_format(message)
    ascii_art = colored(ascii_art,color=color)
    print(ascii_art)
    
message = input('what would you like to print? : ')
color = input('what color? : ')
print_art(color, message)

#---------------------------------------------------------