#  Find  outputs  (Home  work)
x = 25 # Ref 'x' points to object 25
y = F'{x}' # Ref 'y' points to object F'{x}'
print(y) # prints 25
print(type(y)) # prints type of object i.e., <class 'str'>
x = 10.8 # Ref 'x' points to object 10.8
y = F'{x}' # Ref 'y' points to object F'{x}'
print(y) # prints 10.8
print(type(y)) # prints type of object i.e., <class 'str'>
x = [10,20,30,40] # Ref 'x' points to object to list
y = F'{x}' # Ref 'y' points to object to F'{x}'
print(y) # prints [10,20,30,40]
print(type(y)) # prints type of object i.e., <class 'str'>



#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd' # Ref 'a' points to object 25, ref 'b' points to object 10.8 and ref 'c' points to object 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # prints 25<tab>10.8<tab>Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # prints a = 25<tab>b = 10.8<tab>Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # prints a=25<tab>b=10.8<tab>c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') # prints 25<tab>10.8<tab>Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a = {a}<tab>b = {b}<tab>c = {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a = a<tab>b = b<tab>c = c
print(F'{x =}  \t   {y =}  \t  {z =}') # Error because there are no x,y and z objects 



#  Find  outputs  (Home  work)
x = 25
print(F'{x}') # prints 25
print(F'{{x}}')  # prints {x}
print(F'{{{x}}}')  # prints {25}
print(F'{{{{x}}}}') # prints {{x}}
print(F'{{{{{x}}}}}') # prints {{25}}
print(F'{{{{{{x}}}}}}') # prints {{{x}}}
print(F'{{{{{{{x}}}}}}}') # prints {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # prints {{{{x}}}}






'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17
What  is  the  difference ?  --->  3
What  is  the  product ?  ---> 70
What  is  the  quotient ?  --->  1.42
What  is  the  remainder ?  --->  3
What  is  the  largest  number ?  ---> 10
What  is  the  smallest  number ?  --->  7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power?  --->  10000000
What  is  the  gcd  of  2  numbers ?  ---> 1
What  is  the  factorial   of  1st  input ?  ---> 10!
'''
a = eval(input("Enter 1st integer number : "))
b = eval(input("Enter 2nd integer number : "))
print("10+7 =", a + b)
print("10-7 =",a - b)
print("10*7 =",a * b)
print("10/7 = ",a / b)
print("10%7 = ",a % b)
print("max(10,7) =",max(a , b))
print("min(10,7) =",min(a , b))
print("10^7 =", a ** b)
import math
print("sqrt(10) =",math.sqrt(a ** b))
print("gcd(10,7) =",math.gcd(a ,b))
print("fact(10) =",math.factorial(a , b))








'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = eval(input("Enter 1st input:"))
y = eval(input("Enter 2nd input:"))
print("Before swap: x =",x ,"\t y =", y)
x, y = y, x
print("After swap: x =",x ,"\t y =", y)







'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary operator
'''
a = eval(input("Enter 1st input:"))
b = eval(input("Enter 2nd input:"))
c = eval(input("Enter 3rd input:"))
if a > b and a > c:
    print(F'{a} is largest number')
else:
    if b > c:
        print(F'{b} is largest number')
    else:
        print(F'{c} is largest number')








'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary operator
'''
a = eval(input("Enter 1st input:"))
b = eval(input("Enter 2nd input:"))
print('>' if a > b else '<' if a < b else '=' )










'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary operator
'''
a = eval(input("Enter any number:"))
print("Result:",'1' if a >= 1 else '-1' if a <= -1 else '0')








'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary operator
'''
a = eval(input("Enter any +ve  integer:"))
print('Even number' if a % 2 == 0 else 'Odd nuber')










'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
a = eval(input("Enter length of rectangle:"))
b = eval(input("Enter breadth of rectangle:"))
area = a * b
perimeter = 2 * (a * b)
print("Area of rectangle:",area)
print("Perimeter of rectangle:", perimeter)










'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
from math import pi
r = eval(input("Enter radius of sphere:"))
volume = 4/3 * pi * r ** 3
print("Volume of sphere:",volume)









'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
p = eval(input("Enter principle of interest:"))
t = eval(input("Enter time of interest:"))
r = eval(input("Enter rate of interest:"))
s = (p * t * r )/100
c = p * (1 + r/100)**t - p
print("Simple interest:",s)
print("Compound interest:",c)









'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x = eval(input("Enter 1st input:"))
y = eval(input("Enter 2nd input:"))
print("Before swap: x ="x,"y ="y)
temp = x
x = y
y = temp
print("After swap: x =",x,"y =",y)









'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y = 10
'''
x = eval(input("Enter 1st input:"))
y = eval(input("Enter 2nd input:"))
print("Before swap: x =",x ,"\t y =", y)
x = x + y
y = x - y
x = x - y
print("After swap: x =",x ,"\t y =", y)










'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y = 100
'''
x = eval(input("Enter 1st input:"))
y = eval(input("Enter 2nd input:"))
print("Before swap: x =",x,"\t y =",y)
y = x * y 
x = y // x
y = y // x
print("After swap: x =",x ,"\t y =",y)


