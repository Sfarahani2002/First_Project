import os
import shutil


# for data in os.walk('./my_files', topdown=False): az akhar b aval
# for data in os.walk('./', topdown=False):  all files
for data in os.walk('./my_files'):

    print(data)

shutil.copy('./my_files/data-1.txt','./new_my_files/new-data-1.txt')
print(os.stat('./my_files/data-1.txt'))
print(os.stat('./new_my_files/new-data-1.txt'))

shutil.copy('./my_files/data-2.txt','./new_my_files/new-data-2.txt')
print(os.stat('./my_files/data-2.txt'))
print(os.stat('./new_my_files/new-data-2.txt'))

shutil.copytree('./my_files', './backup')

shutil.move('./my_files/main_data.txt', './new_my_files/main-data.txt')

os.rename('./my_files/main_data.txt', './new_my_files/new_main_data.txt')
