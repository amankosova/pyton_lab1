import os
def delete(file_path):
    if os.path.exists(file_path):
        if os.access(file_path,os.W_OK):
            os.remove(file_path)
            print(file_path +" deleted")
        else:
            print(file_path +" don`t writeable")
    else:
        print(file_path +" don`t exist")
delete("jk.txt")
