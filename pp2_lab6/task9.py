def multi(a):
    b=list(map(int,a.split(" ")))
    res=1
    for i in b:
        res*=i
    print(res)
a=input()
multi(a)