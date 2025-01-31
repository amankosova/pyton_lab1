ar1=[1,2,3,4,5]
ar2=[6,7,8,9,10]
res1=ar1+ar2
print(res1)
res3=[]
for i in ar1:
    res3.append(i)
for i in ar2:
    res3.append(i)
print(res3)
res4=list(ar1)
res4.extend(ar2)
print(res4)