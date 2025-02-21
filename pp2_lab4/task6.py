from datetime import datetime,timedelta
a=datetime.now()
b=datetime.now()-timedelta(5)
print(a.strftime("%Y-%m-%d"))
print(b.strftime("%Y-%m-%d"))