import os

# for data in os.walk('./my_files', topdown=False): az akhar b aval
for data in os.walk('./my_files'):
    print(data)


