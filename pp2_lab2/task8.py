arr=[1,2,3,4,5]
ar1=[]
for i in arr:
    if i%2!=0:
        ar1.append(i)

print(ar1)
print("-"*30)
ar2=[i for i in arr if i%2==1]
print(ar2)
ar2.clear()
print(ar2)
ar2=[x for x in range(10) if x!=0 and x<=5]
print(ar2)