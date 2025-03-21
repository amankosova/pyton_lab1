
file="dii.txt"
with open(file,"w") as f:
    f.write("first line\n")
    f.write("second line\n")
    f.write("third line ")
with open(file,"r") as f:
    any=f.readlines()
print(len(list(any)))