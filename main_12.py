import os
import time
from pathlib import Path

# print(os.listdir('./my_files'))
# print(os.path.isfile('./my_files/doc.txt'))
# print(os.path.isdir('./my_files/pictures'))
#
# result = os.scandir('./my_files')
#
# for item in result:
#     if item.is_file():  #is_dir
#         print(item.stat())
#         print(f'File {item.name}: {time.ctime(item.stat().st_mtime)}')
#         print(item)
#
#
# directory = Path('./my_files')
#
# for item in directory.iterdir():
#     if item.is_dir():
#         print(item)

result = os.stat('./my_files/doc.txt')
print(result)
print(result.st_mtime)
print(time.ctime(result.st_mtime))