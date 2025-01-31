ar1=[4,2,5,3,1]
ar2=["qqq","sss","iii","aaa","eee"]
ar1.sort()
print(ar1)
ar2.sort()
print(ar2)
ar1.sort(reverse=True)
print(ar1)
ar2.sort(reverse=True)
print(ar2)
def func(n):
    return abs(n-50)
ar3=[100,30,75,50,25]
ar3.sort(key=func)
print(ar3)
ar3.reverse()
print(ar3)
ar4=["Asd","QWE","hjk"]
ar4.sort(key=str.upper)
print(ar4)
