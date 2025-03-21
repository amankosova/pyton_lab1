import os
def c(path):
    if os.path.exists(path):
        print("path exist")
        print(os.path.basename(path))
        print(os.path.dirname(path))
path="C:/Users/zenbo/OneDrive/Рабочий стол/pp2"
c(path)
