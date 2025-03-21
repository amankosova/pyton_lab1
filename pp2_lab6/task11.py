def pal(a):
    a=a.replace(" ","").lower()
    b=a[::-1]
    if a==b:
        return "palindrom"
    else:
        return "not palindrom"
a=input()
print(pal(a))