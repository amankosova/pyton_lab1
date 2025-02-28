import re
a="Abb"
print(re.findall(r"[A-Z][a-z]+",a))