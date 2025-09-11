#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)     # ‘25’
print(type(y))    # <class ‘str’>
x = 10.8
y = F'{x}'
print(y)     # 10.8
print(type(y))    # <class ‘str’>
x = [10,20,30,40]
y = F'{x}'
print(y)    # ‘[10 , 20, 30, 40]’
print(type(y))   # <class ‘str’>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')   # 25	10.8	‘Hyd’
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')   # a = 25	b = 10.8	c = ‘Hyd’
print(F'{a=}  \t   {b=}   \t  {c=}')    # 25	10.8	Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')    # 25	10.8	‘Hyd’
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  # a = {a}	b = {b}	c = {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')   # a = a	b = b	c = c
#print(F'{x =}  \t   {y =}   \t  {z =}')   #Error x is not defined





#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')   # {{x}}
print(F'{{{{{x}}}}}')  # {{25}}
print(F'{{{{{{x}}}}}}')   # {{{x}}}
print(F'{{{{{{{x}}}}}}}')   # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')   # {{{{x}}}}


#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

#Hint:  Use  F  string  to  print  results
from math import *
a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))
result = a + b 
print(f'{a} + {b} = {result}')
result = a - b
print(f'{a} - {b} = {result}')
result = a * b
print(f'{a} * {b} = {result}') 
result = a / b 
print(f'{a} / {b} = {result}')
result = a % b 
print(f'{a} % {b} = {result}')
result = max(a,b)
print(f'max({a},{b}) = {result}')
result = min(a,b)
print(f'min({a},{b}) = {result}')
result = a ** b
print(f'{a} ^ {b} = {result}')
result = sqrt(a)
print(f'sqrt({a}) = {result}') 
result = gcd(a,b)
print(f'gcd({a},{b}) = {result}')
result = factorial(a)
print(f'fact({a}) = {result}')


#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

#Let  'x'  be  25  and  'y'  be   'Hyd'
#What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

#Hint:  Swap  references  but  not  objects

x = 25
y = 'Hyd'
x, y = y, x
print(f"x = {x}")   # Hyd
print(f"y = {y}")  # 25





#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

#1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

#2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

#3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

#4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

#5) Inputs  can  be  integers , floats , strings  and  so  on

#6) Use  nested  ternary  operator

a = eval(input("Enter 1st input: "))  # 10
b = eval(input("Enter 2nd input: "))  # 20
c = eval(input("Enter 3rd input: "))  # 15.8
largest = a if a > b and a > c else (b if b > c else c)
print(f"Largest input: {largest}")  # 20








try :
    a = input("Enter the 1st input: ")  # 20
    b = input("Enter the 2nd input: ")  # 20
    c = input("Enter the 3rd input: ")  # 20
    max = a if a>b and a>c  else b if b>c else c
except NameError:
	print('input string shoud be in quotes')
except TypeError:
	print('input can not be complex number')



#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

#1) What  is  the  result  if  input  is  -25 ?  --->  -1

#2) What  is  the  result  if  input  is  75 ?  --->  1

#3) What  is  the  result  if  input  is  0 ?  --->  0

#4) Use  nested  ternary  operator

x = int(input("Enter a number: "))  # -25
result = 1 if x > 0 else (-1 if x < 0 else 0)
print(result)  # -1






"""Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator """

x = int(input("Enter any +ve integer : "))   # 45
result = "Even number"if x % 2 == 0 else "Odd number"
print(result)   # 	Odd number





"""Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
"""


length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area of the rectangle = {area}")
print(f"Perimeter of the rectangle = {perimeter}")





"""Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
"""
import math
r = float(input("Enter the radius of the sphere: "))   # 6.7
volume = (4/3) * math.pi * r**3
print(f"Volume of the sphere with radius {r} is: {volume:f}")    # 1259.833108





"""
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
"""
p = int(input("Enter principal amount: "))   # 50000
r = int(input("Enter rate of interest (per annum): "))   # 10
t = int(input("Enter time (in years): "))  # 5
simple_interest = (p * r * t) / 100
compound_interest = p * ((1 + r / 100) ** t) - p
print(f"Simple Interest = {simple_interest}")    # 25000.0
print(f"Compound Interest = {compound_interest}")    #  30525.50000000003



"""Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
"""
x = 10
y = 25
temp = x
x = y      
y = temp   
print(f"x = {x}")  # 25
print(f"y = {y}")  # 10





"""Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions
"""
x = int(input("Enter first value: "))  # 10
y = int(input("Enter second value: "))  # 25
x = x + y   
y = x - y   
x = x - y   
print(f"x = {x }")   # x = 25 
print(f"y = {y}")    # y = 10










"""Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions
"""
x =  -200
y =  100

x = int(input("Enter first value : "))  # 100
y = int(input("Enter second value : "))  # -200
x = x * y        
y = x // y       
x = x // y      
print(f"x = {x}")  # x = -200 
print(f"y = {y}")    # y = 100


