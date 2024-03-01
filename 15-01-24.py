
#lambda function
x=lambda a,b:a+b
print("sum is",x(10,20))

#upper and lowercase
string = input('Enter any string: ')
print('In Upper Case:', string.upper())

#keyword argument
def show(a,b,c):
  print("details are" + a,b,c)
show("ammu",20,"python")

#Arbitory argument
def show(*arg):
  print("Student details..")
  for name in arg:
    print(name)
show("athira","annu","anju")


#default argument
def show(a):
  print(a)
show("gd morning")
  
#area and perimeter of circle
import math
def areaOfCircle(rad):
    ar = 3*3.14*rad*rad
    return ar
print("Enter the Radius of Circle: ", end="")
r = float(input())
a = areaOfCircle(r)
print("\nArea = ", a)

def peri(rad):
  res=2*3.14*rad
  return res
print("enter radious")
r1=float(input())
a1=peri(r1)
print("\nperimeter=",a1)

#odd or even
even=lambda x:x%2==0
number=int(input("enter a num"))
if even(number):
  print(f"{number} is even")
else:
  print(f"{number} is odd")


#cube
cube=lambda x: x**3
number =int(input("enter a number"))
result=cube(number)
print(f" the cube of{number} is: {result}")
   
           






















