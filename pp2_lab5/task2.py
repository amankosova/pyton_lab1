import re
a="abb"
print(re.findall("a.*bb+|abbb+",a))