def func(n):
    for i in range(1,n+1):
        yield i**2
n=int(input())
s=func(n)
for i in s:
    print(i)