thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "name":"Asd",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["brand"]
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict