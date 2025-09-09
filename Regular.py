import re

names = [
    'data.png', 'memory.txt', 'data.txt', 'image.png', 'mommy.png'
]

for item in names:
    if re.search('m.m', item):
        print(item)


# data = '#' # a-fA-F 0-9
# red = '#ff00000'
# red = '#000'