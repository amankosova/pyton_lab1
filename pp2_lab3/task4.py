def prime(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def filter_prime(n):
    for i in n:
        if prime(i):
            print(i)


num=list(map(int,input().split()))

filter_prime(num)