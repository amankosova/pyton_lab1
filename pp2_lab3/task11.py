def pal(a):
    a=a.lower()
    b=""
    for i in a:
        if i.isalpha():
            b+=i
    return b==b[::-1]
print(pal("A man a plan a canal Panama"))