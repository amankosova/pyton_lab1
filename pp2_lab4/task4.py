def func(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
s=func(a,b)
for i in s:
    print(i)