thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "name":"Asd",
  "year": 1964
}
for x in thisdict:
  print(x,thisdict[x])
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():
  print(x, y)