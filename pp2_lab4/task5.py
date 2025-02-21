def func(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
s=func(n)
for i in s:
    print(i)