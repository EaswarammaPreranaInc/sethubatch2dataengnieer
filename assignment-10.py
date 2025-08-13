#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y)  # 10.8 
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>
-------------------------------------
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')  #  25  	   10.8   	  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25  	  b  =  10.8  	  c  =  Hyd 
print(F'{a=}  \t   {b=}   \t  {c=}')  #  a=25  	   b=10.8   	  c='Hyd' 
print(F'{a:}  \t   {b:}   \t  {c:}')  #  25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  #   a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')     #  a  =  a  	  b  =  b  	  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')  # error
-------------------------------------------------------
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {x}
print(F'{{{{{x}}}}}') # {25}
print(F'{{{{{{x}}}}}}') # {{x}}
print(F'{{{{{{{x}}}}}}}') # {{25}}
print(F'{{{{{{{{x}}}}}}}}')  # {{{x}}}
---------------------------------------------------
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

SUM;-
--------
a= int(input("enter 1st integer : ")
b=int(input("enter 2nd integer : ")
total=a+b
print(F'{a}+{b}={total}'}

Difference:-
----------------
a= int(input("enter 1st integer : ")
b=int(input("enter 2nd integer : ")
total=a-b
print(F'{a}-{b={total}'}

Product:-
------------
a= int(input("enter 1st integer : ")
b=int(input("enter 2nd integer : ")
product=a*b
print(F'{a}*{b={total}'}

Quotient:-
--------------
a= int(input("enter 1st integer : ")
b=int(input("enter 2nd integer : ")
quotient=a/b
print(F'{a}/{b={quotient}'}

Remainder:-
---------------
a= int(input("enter 1st integer : ")
b=int(input("enter 2nd integer : ")
Remainder=a%b
print(F'{a}%{b={Remainder}'}

Largest:-
----------
num1 = int(input("Enter 1st  integer  number :  "))
num2 = int(input("Enter 2nd  integer  number :  "))
maximum = max(num1, num2)
print(f"max({num1} , {num2}) = {maximum}")

Smallest:-
-------------
num1 = int(input("Enter 1st  integer  number :  "))
num2 = int(input("Enter 2nd  integer  number :  "))
minimum = min(num1, num2)
print(f"min({num1} , {num2}) = {minimum}")

Square root:-
----------------
import math
first = int(input("Enter 1st  integer  number :  "))
print("Square root of", first, "is:", math.sqrt(first))

Factorial:-
---------
first_num = int(input("Enter 1st  integer  number :  "))
second_num = int(input("Enter 2nd  integer  number :  "))
fact = factorial(first_num)
print(f"\nFactorial of {first_num} is: {fact}")
------------------------------------
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

x = input("Enter value for x: ")
y = input("Enter value for y: ")

x, y = y, x

print("After swapping:")
print("x =", x)
print("y =", y)
---------------------------
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
c = eval(input("Enter 3rd input : "))

largest = a if a > b and a > c else (b if b > c else c)

print("Largest Input  : ", largest)
---------------------------
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

a = input("Enter first input: ")
b = input("Enter second input: ")

print('>' if a > b else '<' if a < b else '=')

---------------------------
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

num = int(input("Enter a number: "))

result = 1 if num > 0 else (-1 if num < 0 else 0)

print(result)
------------------------------------
Write  a  program  to  test  input  is  even  number  or  odd  number

num = int(input("Enter a number: "))

result = "Even" if num % 2 == 0 else "Odd"

print(result)
------------------------
Write  a  program  to  determine  area  and  perimeter  of  rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
----------------------------
Write  a  program  to  determine  volume  of  a  sphere

import math

radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * math.pi * radius**3

print("Volume of the sphere:", volume)
-----------------------
Write  a  program  to  determine  simple  interest  and  compound  interest

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time (in years): "))
rate = float(input("Enter the rate of interest (in %): "))

simple_interest = (principal * time * rate) / 100

compound_interest = principal * ((1 + rate / 100) ** time) - principal

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
------------------------------
Write  a  program  to  swap  values  of  two  objects  using  3rd   object
x = 10
y = 25
print("Before swap: x =", x, ", y =", y)
temp = x
x = y
y = temp
print("After swap: x =", x, ", y =", y)
------------------------------
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

x = 25
y = 10

print("Before swap: x =", x, ", y =", y)

x = x + y      # x becomes 35
y = x - y      # y becomes 25 (original x)
x = x - y      # x becomes 10 (original y)

print("After swap: x =", x, ", y =", y)
--------------------------
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = -200
y = 100

print("Before swap: x =", x, ", y =", y)

x = x * y      # x becomes -20000
y = x // y     # y becomes -200 (original x)
x = x // y     # x becomes 100 (original y)

print("After swap: x =", x, ", y =", y)






























