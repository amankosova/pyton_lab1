from datetime import datetime,timedelta
a=input("Enter a date (YYYY-MM-DD HH:MM:SS): ")
a=datetime.strptime(a,"%y-%m-%d %H:%M:%S")
print(datetime.now()-a)