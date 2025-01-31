arr=[1,2,3,4,5]
for i in range(len(arr)):
    print(arr[i])
print("-"*30)
i=0
while i<len(arr):
    print(arr[i])
    i+=1
print("-"*30)
[print(i) for i in arr]