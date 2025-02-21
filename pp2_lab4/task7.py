import datetime
print((datetime.datetime.now()-datetime.timedelta(1)).strftime("%y-%m-%d"))
print((datetime.datetime.now()).strftime("%y-%m-%d"))
print((datetime.datetime.now()+datetime.timedelta(1)).strftime("%y-%m-%d"))