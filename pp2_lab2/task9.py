arr=[1,2,3,4,5]
ar1=[1 for x in arr]
print(ar1)
ar2=[i if i!=2 else 11 for i in arr]
print(ar2)