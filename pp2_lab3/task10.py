def unique(num):
    u=[]
    for i in num:
        if i not in u:
            u.append(i)
    print(u)
a=[1,2,2,2,3,4,3]
unique(a)