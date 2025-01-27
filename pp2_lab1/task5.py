x=7 #int type
y="a" #str type
print(x,y)
var=str(3) #will be '3'
var1=int(3) #will be 3
var2=float(3) #will be 3.0
print(var,var1,var2)
check1='5'
check2="5"
check3=5
check4=5.0
print(type(check1),type(check2),type(check3),type(check4))
a,A="a is lower,","A is upper"
print(a,A)
z=s=2
print(z+s)
massiv=['pp2','diskra','eng']
subject1,subject2,subject3=massiv
print(subject1,subject2,subject3)
global_=4.0
def find_gpa():
    local_=3.5
    print("My gpa is "+ str(local_))
find_gpa()
print("My gpa is "+ str(global_))
glob='moon'
def my_f():
    global glob
    glob="sun"
my_f()
print(glob)



