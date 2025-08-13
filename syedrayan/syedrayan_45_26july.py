
#  Find  outputs  (Home  work)
x = 25
y = F'{x}' 
print(y) # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}' 
print(y) # "10.8"
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10,20,30,40] 
print(type(y)) # <class 'str'>



#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 23  10.8    'Hyd'
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25    b = 10.8    c = 'Hyd'
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25    b=10.8   c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') # 25   10.8    'Hyd'
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}   b  =  {b}    c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # 'a  =  a      b  =  b     c  =  c'
print(F'{x =}  \t   {y =}   \t  {z =}') #error


#  Find  outputs  (Home  work)
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
What  is  the  factorial   of  1st  input ?  ---> 10!
'''
import math
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print(F'{a} + {b} =',a+b)
print(F'{a} - {b} =',a-b)
print(F'{a} * {b} =',a*b)
print(F'{a} / {b} =',a/b)
print(F'{a} % {b} =',a%b)
print(F'max({a},{b}) =',max(a,b))
print(F'min({a},{b}) =',min(a,b))
print(F'sqrt({a})',math.sqrt(a))
print(F'{a}^{b} =',math.pow(a,b))
print(F'gcd({a},{b}) =',math.gcd(a,b))
print(F'fact({a}) =',math.factorial(10))


'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
try:
    x=eval(input("Enter first value :"))
    y=eval(input("Enter second value :"))
    print(F'Before  swap :  x={x}            y={y}')
    x,y=y,x
    print(F'After  swap :  x={x}            y={y}')
except NameError:
    print("string input should be in quotes ''")



'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
try:
    a=eval(input("Enter 1st input : "))
    b=eval(input("Enter 2nd input : "))
    c=eval(input("Enter 3rd input : "))
    res= a if a>b>c else b if b>c>a else  c
    print ('Largest Input :',res)
except:
    print("the string input should be in quotes''")



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
try:
    a=eval(input("Enter 1st  number :"))
    b=eval(input("Enter 2nd  number :"))
    res='>' if a>b else '<' if a<b else '='
    print('Result :',res)
except:
    print("input string shouldbe in quotes ''")




'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
n=int(input("Enter a number :"))
res=1 if n>0 else -1 if n<0 else 0
print('Result :',res)



'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
n = int(input("Enter any +ve number :"))
res='Even number' if n%2==0 else 'Odd number'
print(res)



'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breadth of rectangle: "))
print('Area =',l*b)
print('Perimeter',2*(l+b))




'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r=int(input("Enter the radius of circle :"))
print("Volume :",(4/3)math.pi(r**3))




'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
p=int(input("Enter principal amount :"))
t=int(input("Enter time in no of years:"))
r=int(input("Enter rate of interest:"))
print("Simple interest :",(p*t*r)/100)
print("compound interest :",p*(1+r/100)**t-p)




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x=int(input("Enter 1st value :"))
y=int(input("Enter 2nd value :"))
print(f"Before swap x={x} y={y}")
temp=x
x=y
y=temp
print(f"After swap x={x} y={y}")




Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
x=int(input("Enter 1st value :"))
y=int(input("Enter 2nd value :"))
print(f"Before swap x={x} y={y}")
x=x+y
y=x-y
x=x-y
print(f"After swap x={x} y={y}")




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
x=int(input("Enter 1st value :"))
y=int(input("Enter 2nd value :"))
print(f"Before swapping x={x} and y={y}")
x=-x*y # -20000
y=-x//y # -200
x=-x//y # 100
print(f"After swapping x={x} and y={y}") '''