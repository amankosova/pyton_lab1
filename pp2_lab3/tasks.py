def u(a):
    return a*28.3495231
gramm=int(input())
print(u(gramm))
def cel(f):
    C = (5 / 9)*(f-32)
    print(C)
f=int(input())
cel(f)
def a(num):
    for i in num:
        print("*"*i)
a([4,9,7])