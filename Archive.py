import os
import zipfile

z = zipfile.ZipFile('./main.zip', 'w')
z.write('./my_files')
z.close()

z = zipfile.Zipfile('./main.zip', 'r')
print(z.filelist)
z.close()

z = zipfile.ZipFile('./main.zip', 'r')
z.extractall('./extracted')
z.close()

z = zipfile.ZipFile('./main.zip', 'w')

for item in os.walk('./my_files'):
    root_dir = item[0]
    sub_directories = item[1]
    sub_files = item[2]

    z.write(root_dir)

    for s_d in sub_directories:
        z.write(f'{root_dir}\\{s_d}')

    for f in sub_files:
        z.write(f'{root_dir}\\{f}')

z.close()

z = zipfile.Zipfile('./data.zip', 'r')
z.extractall('./extracted')
z.close()