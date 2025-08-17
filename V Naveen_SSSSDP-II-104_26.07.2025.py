#1.  Find  outputs  (Home  work)
x = 25     
y = F'{x}' # y=F'{25}
print(y)   # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'    # y = F'{x}'
print(y)      # 10.8
print(type(y))# <class 'str'>
x = [10,20,30,40]
y = F'{x}'  # y=F'[10,20,30,40]'
print(y)    # [10,20,30,40]
print(type(y))# <class 'str'>

# 2.Find  outputs  (Home  work)
a,b ,c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')                # 25	10.8	Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  # a = 25  	  b  =  10.8  	  c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')             # a=25  	   b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')             # 25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')# a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')      # a  =  a  	  b  =  b  	  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')          # x is not defined

#3.  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}


'''
#4. Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
Hint:  Use  F  string  to  print  results
'''
from math import sqrt, gcd, factorial
x = eval(input("Enter the 1st integer number:"))
y = eval(input("Enter the 2nd integer number:"))
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")
print(f"max({x}, {y}) = {max(x, y)}")
print(f"min({x}, {y}) = {min(x, y)}")
print(f"{x} ^ {y} = {x ** y}")
print(f"sqrt({x}) = {sqrt(x)}")
print(f"sqrt({y}) = {sqrt(y)}")
print(f"gcd({x}, {y}) = {gcd(x, y)}")
print(f"fact({x}) = {factorial(x)}")
print(f"fact({y}) = {factorial(y)}")
'''
5. Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  
using  3rd  objectLet  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25
Hint:  Swap  references  but  not  objects
'''
x = eval(input("Enter the 1st Input:"))
y = (input("Enter the 2nd Input:"))
print("Before swap: x=",x,"and y =",y)
x, y = y, x
print("After swap: x =", x, "and y =", y)


#6. Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
a = eval(input("Enter the 1st Input:"))
b = eval(input("Enter the 2nd Input:"))
c = eval(input("Enter the 3rd Input:"))
if a>=b and a>=c:
    largest=a
if b>=a and b>=c:
   largest=b
if c>=a and c>=b:
    largest=c
largest= a if a>=b and a>=c else (b if b>=c else c)
print("Largest input:",largest)



#7. Write  a  program  to  print   '>'  if  1st  input  >  2nd  input, '<'  if  1st  input  <  2nd  input  and
#'='  if  inputs  are  same
x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
if x > y:
    result = '>'
elif x < y:
    result = '<'
else:
    result = '='
print("Result:", result)

#8. Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
x = eval(input("Enter a number: "))
if x>0:
    result=1
elif x<0:
    result=-1
elif x==0:
    result=0
print("Result:", result)


#9. Write  a  program  to  test  input  is  even  number  or  odd  number
x = int(input("Enter a number: "))
result = "Even" if x % 2 == 0 else "Odd"
print("Result:", result)

#10. Write  a  program  to  determine  area  and  perimeter  of  rectangle
l = float(input("Enter the length of the rectangle: "))
b= float(input("Enter the breadth of the rectangle: "))
area = l * b
perimeter = 2 * (l + b)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)


#11. Write  a  program  to  determine  volume  of  a  sphere
import math
radius = float(input("Enter the radius of the sphere: "))
volume = (4 / 3) * math.pi * (radius ** 3)
print("Volume of the sphere:", volume)

#12. Write  a  program  to  determine  simple  interest  and  compound  interest
p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
r = float(input("Enter the rate of interest: "))
si = (p * t * r) / 100
ci = p * ((1 + r / 100) ** t) - p

print("Simple Interest:", si)
print("Compound Interest:", ci)


#13. Write  a  program  to  swap  values  of  two  objects  using  3rd   object
x = 10
y = 25
temp = x
x = y
y = temp
print("After swap:")
print("x =", x)
print("y =", y)
#After swap:
x = 25
y = 10

'''
14. Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions
x = 25,y =  10
'''
#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = 25
y = 10
x = x + y     # x becomes 35
y = x - y     # y becomes 25 (35 - 10)
x = x - y     # x becomes 10 (35 - 25)
print("After swap:")
print("x =", x)
print("y =", y)


'''
15. Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
x =  -200,y =  100
'''
#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = -200
y = 100
x = x * y     # x = -200 * 100 = -20000
y = x // y    # y = -20000 // 100 = -200
x = x // y    # x = -20000 // -200 = 100
print("After swap:")
print("x =", x)
print("y =", y)


