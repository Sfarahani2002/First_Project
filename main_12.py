import os
from pathlib import Path

print(os.listdir('./my_files'))
print(os.path.isfile('./my_files/doc.txt'))
print(os.path.isdir('./my_files/pictures'))

result = os.scandir('./my_files')

for item in result:
    if item.is_file():  # is_dir
        print(item)


directory = Path('./my_files')

for item in directory.iterdir():
    if item.is_dir():
        print(item)