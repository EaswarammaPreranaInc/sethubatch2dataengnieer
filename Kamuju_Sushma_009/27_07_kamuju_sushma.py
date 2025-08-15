# Name: Kamuju Sushma

#Home Work-1
#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)#25
print(type(y))#<class 'str'>
x = 10.8
y = F'{x}'
print(y)#10.8
print(type(y))#<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)#[10,20,30,40]
print(type(y))#<class 'str'>

#Home Work-2
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#25<tab space>10.8<tab space>Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')#a = 25<tab space>b = 10.8<tab space>c= Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')#a = 25<tab space>b = 10.8<tab space>c= Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')#25<tab space>10.8<tab space>Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#a  =  {a}  <tab space>  b  =  {b}  <tab space>  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#a  =  a  <tab space>  b  =  b  <tab space>  c  =   c
print(F'{x =}  \t   {y =}   \t  {z =}')#error, 'z' object is not present

#Home Work-3
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''

#Home Work-4
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
a=eval(input("Enter 1st integer number: "))
b=eval(input("Enter 2nd integer number: "))
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'max({a},{b})={max(a,b)}') 
print(f'min({a},{b})={min(a,b)}')
print(f'{a}^{b}={math.pow(a,b)}') 
print(f'sqrt({a})={math.sqrt(a)}') 
print(f'gcd({a},{b})={math.gcd(a,b)}') 
print(f'fact({a})={math.factorial(a)}') 

#Home Work-5
'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x=eval(input("Enter 1st input:"))
y=eval(input("Enter 2nd input:"))
print(f'Before swap x:{x}   y:{y}')
z=x
x=y
y=z
print(f'After swap x:{x}   y:{y}')

#Home Work-6
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

a=eval(input("Enter 1st input:"))
b=eval(input("Enter 2nd input:"))
c=eval(input("Enter 3rd input:"))
res=a if (a>b and a>c)  else b if (a<b and b>c) else c
print(f'Largest Input : {res}');
#Home Work-7
'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''
x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
res= '>' if x>y else '<' if x<y else '='
print(f'Result :   {res}')

#Home Work-8
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
# Enter any number : -25
# Result :  -1
x=int(input("Enter any number :"))
res=1 if x>0 else 0 if x==0 else -1
print(f'Result :  {res}')

#Home Work-9
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
x=int(input("Enter  any  +ve  integer :"))
print("Even number") if x%2==0 else print("Odd number")

#Home Work-10
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l=float(input("Enter length: "))
b=float(input("Enter breadth: "))
print(f'Perimeter of rectangle {2*(l+b)}')
print(f'Area of rectangle {l*b}')

#Home Work-11
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r=int(input("Enter radius of sphere: "))
print(f'Volume of sphere {(4/3)*math.pi*pow(r,3)}')

#Home Work-12
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
p=int(input("Enter principle : "))
t=int(input("Enter time: "))
r=int(input("Enter rate of intrest :"))
print(f'Simple intrest: {(p*t*r)/100}')
print(f'Compund intrest: {p*(1+r/100)**t-p}')

#Home Work-13
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x=eval(input("Enter 1st value: "))
y=eval(input("Enter 2nd value: "))
print(f'x = {x} and y = {y} before swap')
z=x
x=y
y=z
print(f'x = {x} and y = {y} after swap')

#Home Work-14
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
x=eval(input("Enter 1st value: "))
y=eval(input("Enter 2nd value: "))
print(f'x = {x} and y = {y} before swap')
x=x+y
y=x-y
x=x-y
print(f'x = {x} and y = {y} after swap')

#Home Work - 15
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
x=eval(input("Enter 1st value: "))
y=eval(input("Enter 2nd value: "))
print(f'x = {x} and y = {y} before swap')
x=x*y
y=x/y
x=x/y
print(f'x = {x} and y = {y} after swap')