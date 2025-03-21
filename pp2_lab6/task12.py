import math
import time
def res(a,b):
    time.sleep(a/ 1000)
    res1=math.sqrt(b)
    print(f"Square root of {b} after {a} miliseconds is {res1}")
wait=int(input("time : "))
number=int(input("number : "))
res(wait,number)
