#copy lists not link
ar=[1,2,3,4,5]
ar1=ar.copy()
ar1.append(6)
print(ar1)
ar2=list(ar)
ar2.append(6)
print(ar2)
ar3=ar[:]
ar3.append(6)
print(ar3)
print(ar)
