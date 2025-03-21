file='dii.txt'
def a(n):
    arr=list(map(str,n.split(" ")))
    with open(file,"a") as f:
        for i in arr:
            f.write('\n' +i)
    with open(file,"r") as f:
        res=f.read()
        print(res)
ass="asd asd asd"
a(ass)