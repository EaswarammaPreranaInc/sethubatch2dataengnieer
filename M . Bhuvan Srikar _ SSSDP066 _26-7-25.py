#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) # 10
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25 <tab> 10.8 <tab> Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25 <tab> b = 10.8 <tab> c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a = 25 <tab> b = 25 <tab> c = Hyd
print(F'{a:}  \t   {b:}   \t  {c:}') # 25 <tab> 10.8 <tab> Hyd : is ignored 
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}  <tab>  b  =  {b} <tab>  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a  <tab>  b  =  b  <tab>  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # error as there qre nno arguments x , y , z

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
What  is  the  factorial of 1st input? ---> 10!
'''
import math
try:
	a = int(input('Enter 1st number : '))
	b = int(input('Enter 2nd number : '))
	print(f'{a} + {b} = {a + b}')
	print(f'{a} - {b} = {a - b}')
	print(f'{a} * {b} = {a * b}')
	print(f'{a} / {b} = {a / b:.2f}')
	print(f'{a} % {b} = {a % b}')
	print(f'max({a , b}) = {max(a , b)}')
	print(f'min({a , b}) = {min(a , b)}')
	print(f'square root of {a} = {math.sqrt(a)}')
	print(f'{a}^{b} = {pow(a , b)}')
	print(f'gcd({a , b}) = {math.gcd(a , b)}')
	print(f'fact({a}) = {math.factorial(a)}')
except:
	print('Enter only Integer value')



'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:Swap references but not objects

Enter  1st  input :  25
Enter  2nd  input : Hyd
Before swap : x='25' y='Hyd'
After swap : x='Hyd' y='25'
'''
try:
	x = eval(input('Enter value of x : '))
	y = eval(input('Enter value of y : '))
	print(f'Before swap : {x=} \t {y=}')
	x , y = y , x
	print(f'After swap : {x=} \t {y=}')
except:
	print('Enter string input in quotes')


'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use nested ternary operator

Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15.8
Largest Input : 20
'''
try:
	a = eval(input('Enter 1st input : '))
	b = eval(input('Enter 2nd input : '))
	c = eval(input('Enter 3rd input : '))
	max = a if a > b else b if b > c else c
	print(f'Largest input is {max}')
except NameError:
	print('Please enter string with in quotes ')
except TypeError:
	print('Please enter only integer or float value')


'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use ternary operator

Enter 1st input : 10
Enter 2nd input : 20
Result  : <
'''
try:
	a = eval(input('Enter 1st input : '))
	b = eval(input('Enter 2nd input : '))
	max = '>' if a > b else '<' if a < b else '='
	print(f'Result :  {max}')
except NameError:
	print('Please enter string with in quotes ')
except TypeError:
	print('Please enter only integer or float value')



'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator

Enter any number : -25
Result :  -1
'''
try:
	a = eval(input('Enter a number : '))
	result = 1 if a >= 1 else -1 if a <= -1 else 0
	print(f'Result : {result}')
except:
	print('Enter only interger or float value')


'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator

Enter  any  +ve  integer : 45
Odd  number
'''
try:
	a = int(input('Enter a positive integer : '))
	result = 'Even Number' if a % 2 == 0 else 'Odd Number'
	print(result)
except:
	print('Enter only positive integer')


'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
try:
	length = float(input('Enter length of the rectangle : '))
	breadth = float(input('Enter breadth of the rectangle : '))
	area = length * breadth
	perimeter = 2 * (length + breadth)
	print(f'Area of rectangle is {area}')
	print(f'Perimeter of the rectangle is {perimeter}')
except:
	print('Enter integer or float value only')


'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
try:
	radius = float(input('Enter radius of the sphere : '))
	volume = (4/3) * math.pi * radius**3
	print(f'Volume of the sphere is {volume}')
except:
	print('Enter integer or float value only')


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What is compound interest formula ?--->p*(1+r/100)^t-p
'''
p = float(input('Enter principle : '))
t = float(input('Enter time(in years) : '))
r = float(input('Enter rate of intrest : '))
si = (p*t*r)/100
ci = p * ((1 + r / 100) ** t) - p
print(f'Simple intrest = {si}')
print(f'Compound intrest = {ci}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
try:
	x = eval(input('Enter value of x : '))
	y = eval(input('Enter value of y : '))
	temp = x
	x = y
	y = temp
	print(f'values after swap are {x=} and {y=}')
except NameError:
	print('Enter string on quotes')



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x=25
y=10
'''
try:
	x = int(input('Enter value of x : '))
	y = int(input('Enter value of y : '))
	x = x + y # 25 + 10 = 35
	y = x - y # 35 - 10 = 25
	x = x - y # 35 - 25 = 10
	print(f'values after swap are {x=} and {y=}')
except:
	print('Enter integer values')



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x=-200
y=100
'''
try:
	x = int(input('Enter value of x : '))
	y = int(input('Enter value of y : '))
	x = x * y 
	y = x / y 
	x = x / y 
	print(f'values after swap are {x=} and {y=}')
except:
	print('Enter integer values')
