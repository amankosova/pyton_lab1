import os
path="C:/Users/zenbo/OneDrive/Рабочий стол/pp2"
d=[i for i in os.listdir(path) if os.path.isdir(os.path.join(path , i))]
print("directory:")
for i in d:
    print(i)
f=[i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]
print("files:")
for i in f:
    print(i)
all=os.listdir(path)
print("all files anf dir:")
for i in all:
    print(i)