import re
a="a,c,v.w.w a"
print(re.sub(r"[., ]",':',a))