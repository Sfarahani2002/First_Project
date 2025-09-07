import os
import pathlib
import fnmatch
import glob
from pathlib import Path


for file_name in os.listdir('./test'):
    if fnmatch.fnmatch(file_name, '*[0-9][0-9]*'):
#   if file_name.endswith('.txt'):
#   if'data' in file_name:
        print(file_name)

print(fnmatch.fnmatch('./my_files/data-1.txt', '*.png'))

print(glob.glob('./my_files/*/*[0-9][0-9]*', recursive=True))
print(glob.glob('./my_files/*[0-9][0-9]*', recursive=True))
print(glob.glob('**/*[0-9][0-9]*', recursive=True))
path = Path('./my_files')
data = path.glob('**/*[0-9][0-9]*')
print(data)
print(list(data))