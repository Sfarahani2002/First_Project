import os
import re

for item in os.walk('./my_files'):
    for file in item[2]:
        if re.search('./txt', file):
            print(file)111
