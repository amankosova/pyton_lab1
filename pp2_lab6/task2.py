import os
def c(path):
    #Бұл жол тексерілетін файл немесе директорийдің жолы
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
            #код жолы орындауға рұқсаттың бар-жоғын тексереді
            print("executable")
        else:
            print("don't executable")
if __name__=="__main__":
    #файлды тікелей іске қоссаңыз,импортталмаса
    p="C:/Users/zenbo/OneDrive/Рабочий стол/pp2"
    c(p)


     