x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print("-"*30)
thistuple1 = ("apple", "banana", "cherry")
y = list(thistuple1)
y.append("orange")
thistuple1 = tuple(y)
print(thistuple1)
print("-"*30)
thistuple2 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple2 += y
print(thistuple2)
print("-"*30)
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)