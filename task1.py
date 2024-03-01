
input("Enter name")
Enter name Athira
' Athira'
input("Enter age")
Enter age 32
' 32'


input("Enter first name")
Enter first name Athira 
' Athira '
input("Enter lastname")
Enter lastname Sukumar
' Sukumar'
print("Athira"+"sukumar")
Athirasukumar



#sum of 2  Numbers
input("Enter a number")
Enter a number10
'10'
input("Enter Second number")
Enter Second number 20
' 20'
print("sum is" (a+b))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("sum is" (a+b))
NameError: name 'a' is not defined
print("sum is" 10+20)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("sum is ",10+20)
sum is  30



#Sum,Multiplication,division operation
a=input("Enter a number")
Enter a number 10
b=input("Enter second number")
Enter second number 20
print("Sum is" ,a+b)
Sum is  10 20
a=int(input("first number"))
first number 50
b=int(input("second number"))
second number 30
print("Sum is" ,a+b)
Sum is 80
print("Multiplication result",a*b)
Multiplication result 1500
print("division ",a/b)
division  1.6666666666666667

#simple interest
p=input("Enter principal amount")
Enter principal amount 600
t=input("Enter time")
Enter time 2
r=input("Enter rate of interest")
Enter rate of interest 3
print("Result is",(p*r*t)/100)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print("Result is",(p*r*t)/100)

p=int(input("Enter principal amount")
      600
      
SyntaxError: incomplete input
p=int(input("enter principal amount"))
      
enter principal amount 600
t=int(input("Enter time"))
      
Enter time2
r=int(input("Enter rate of interest"))
      
Enter rate of interest 3
print("Result is",(p*r*t)/100)
      
Result is 36.0

#Data type
      
a=[10,20,30]
      
>>> print(type(a))
...       
<class 'list'>
>>> a=20
...       
>>> print(type(a))
...       
<class 'int'>
>>> a="athira"
...       
>>> print(type(a))
...       
<class 'str'>
>>> a=12.3
...       
>>> print(type(a))
...       
<class 'float'>
>>> 
>>> a='ammu'
...       
>>> print(typa(a))
...       
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(typa(a))
NameError: name 'typa' is not defined. Did you mean: 'type'?
>>> print(type(a))
...       
<class 'str'>
>>> #power of a number
...       
>>> x=int(input("Enter  a Number"))
...       
Enter  a Number5
>>> y=print("power is",x*x*x)
...       
power is 125
>>> #identity operator
...       
>>> p=input("Enter a number")
      
Enter a number 25
q=input("Enter second number")
      
Enter second number65
print(p is q)
      
False
print(p is not q)
      
True
#membership opertator
      
string="Helloworld"
      
print("h" not in string)
      
True
 print("h" in string)
      
SyntaxError: unexpected indent
print("h" in string)
      
False
