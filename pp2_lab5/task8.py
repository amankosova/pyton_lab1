import re
a="AvbSDbnGH"
print(re.findall(r"[A-Z][^A-Z]*",a))
