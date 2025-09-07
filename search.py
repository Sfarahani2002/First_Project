import os
import pathlib
import fnmatch

for file_name in os.listdir('./test'):
    if fnmatch.fnmatch(file_name, '*[0-9][0-9]*'):
#   if file_name.endswith('.txt'):
#   if'data' in file_name:
        print(file_name)

print(fnmatch.fnmatch('./my_files/data-1.txt', '*.png'))