1)#  Find  outputs  (Home  work)
x = 25
y = F'{x}'  
print(y)  #  25
print(type(y))  #  class 'str'
x = 10.8 
y = F'{x}'
print(y)  #   10.8
print(type(y))  #  class 'str'
x = [10,20,30,40]
y = F'{x}'
print(y)  #  [10,20,30,40]
print(type(y))  #  class 'str'

2)#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')  #  25 <tabspace> 10.8 <tab space> Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  #  a=25 <tabspace> b=10.8 <tabspace> c= Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')  #  a=25 <tabspace> b=10.8 <tabspace> c=hyd
print(F'{a:}  \t   {b:}   \t  {c:}')  #  a: <tabspace> b: <tabspace> c: 
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  #  a  =  {a}  \t  b  =  {b}  \t  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')  #  a  =  a <tabspace>b  =  b <tabspace> c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')  #  Error due to x,y,z are not defined

3)#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}')  # {{25}} 
print(F'{{{{{{x}}}}}}')  #  {{{x}}}
print(F'{{{{{{{x}}}}}}}')  #  {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')  #  {{{{x}}}}


4)Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

program: 

import math
x=eval(input("Enter the 1st number : "))
y=eval(input("Enter the 2nd number : "))
a=x+y
b=x-y
c=x*y
d=x/y
e=x%y
f=max(x,y)
g=min(x,y)
h=x**y
i=math.sqrt(x)
j=math.gcd(x,y)
k=math.factorial(x)

print(f"{x}+{y}={a}")
print(f"{x}-{y}={b}")
print(f"{x}*{y}={c}")
print(f"{x}/{y}={d}")
print(f"{x}%{y}={e}")
print(f"max({x},{y})={f}")
print(f"min({x},{y})={g}")
print(f"{x}^{y}={h}")
print(f"sqrt{x}={i}")
print(f"gcd({x},{y})={j}")
print(f"fact({x})={k}")


'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25
Hint:  Swap  references  but  not  objects
'''
Program:
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")

print(f" Before swap : x={x} , y={y}")
x,y=y,x
print(f" After swap : x={x} , y={y}")



'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator


x=eval(input("enter 1st input : "))
y=eval(input("enter 2nd input : "))
z=eval(input("enter 3rd input : "))

large = x if x >= y and x >= z else y if y >= x and y >= z else z
print(f"Largest input is : {large}")

'''


'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''

x=eval(input("enter 1st input : "))
y=eval(input("enter 2nd input : "))

k= '>' if x>y else '<' if y>x else '='
print(f"Result is : {k}")


'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''

x=int(input("enter a number : "))
k= '1' if x>0 else '-1' if x<0 else '0'

print(f" Result : {k}")


'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
x=int(input("enter any +ve integer : "))
k= 'Even number' if x%2==0 else 'Odd number'
print(f"{k}")


'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

l=int(input("enter length of rectangle : "))
b=int(input("enter breadth of rectangle : "))

x = l*b
y = 2*(l+b)

print(f" Area :{x} , Perimeter : {y}")



'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
r=int(input("enter the Radius of the Circle : "))
v=4/3*(22/7)*(r**3)
print(f" Volume : {v}")



'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''


p=eval(input("enter principle input : "))
t=eval(input("enter time input : "))
r=eval(input("enter interest input : "))

a=p*t*r/100
b=p * ((1  +  (r  /  100))**t)-p

print(f" Simple interest : {a}, Compound interest : {b}")



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x=eval(input("enter 1st input : "))
y=eval(input("enter 2nd input : "))
print(f' Before Swap  : x={x} , y={y}')
z=x
x=y
y=z
print(f' After Swap  : x={x} , y={y}')




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x=int(input("enter 1st input : "))
y=int(input("enter 2nd input : "))
print(f' Before Swap  : x={x} , y={y}')

x=x+y
y=x-y
x=x-y
print(f' After Swap  : x={x} , y={y}')



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
x=int(input("enter 1st input : "))
y=int(input("enter 2nd input : "))
print(f' Before Swap  : x={x} , y={y}')
x=x*y
y=x/y
x=x/y
print(f' After Swap  : x={x} , y={y}')


