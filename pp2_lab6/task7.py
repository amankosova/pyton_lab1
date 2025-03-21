import os
file1="dii.txt"
file2="jk.txt"
with open(file1,"r") as f1:
    with open(file2,"w") as f2:
        ctrlc=f1.read()
        ctrlv=f2.write(ctrlc)