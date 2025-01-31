thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y=thisdict.get("model")
print(x,"\n",y)
z=thisdict.keys()
print(z)
w=thisdict.values()
print(w)
thisdict["name"]="jor"
print(z)
print(thisdict)
u= thisdict.items()

print(u)