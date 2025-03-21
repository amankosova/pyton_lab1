import os
def c(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return 
    else:
        print("path exist")
        if os.access(path,os.R_OK):
            print("readable")
        else:
            print("don`t readable")
        if os.access(path,os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path,os.X_OK):
            print("executable")
        else:
            print("don't executable")
if __name__=="__main__":
    p="C:/Users/zenbo/OneDrive/Рабочий стол/pp2"
    c(p)


     