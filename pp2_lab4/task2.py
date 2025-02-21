def even(n):
    for i in range(n+1):
        if i!=0 and i%2==0:
            yield i
        
n=int(input())
s=even(n)
res=list(s)
print(",".join(map(str,res)))