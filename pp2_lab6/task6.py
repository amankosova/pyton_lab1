import string
import os
def gen():
    for i in string.ascii_uppercase:
        f=i+".txt"
        with open(f,"w") as fi:
            fi.write("new file")
        if os.path.exists(f):
            print(f +" exist")
        
gen()
