#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)		# 25
print(type(y))		# <class 'str'>
x = 10.8
y = F'{x}'
print(y)		# 10.8
print(type(y))		# <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)		# [10,20,30,40]
print(type(y))		# <class 'str'>




#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')			# 25 <tabspace> 10.8 <tabspace> Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')		# a = 25 <tabspace> b = 10.8 <tabspace> c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')			# a=25 <tabspace> b=10.8 <tabspace> c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')			# 25 <tabspace> 10.8 <tabspace> Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')	# a  =  {a} <tabspace> b  =  {b} <tabspace> c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')		# a  =  a  <tabspace>  b  =  b  <tabspace>  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')			# Error




#  Find  outputs  (Home  work)
x = 25
print(F'{x}')				# 25
print(F'{{x}}')				# {x}
print(F'{{{x}}}')			# {25}
print(F'{{{{x}}}}')			# {{x}}
print(F'{{{{{x}}}}}')			# {{25}}
print(F'{{{{{{x}}}}}}')			# {{{x}}}
print(F'{{{{{{{x}}}}}}}')		# {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')		# {{{{x}}}}




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
sample output:
Enter 1st  integer  number :  10
Enter 2nd  integer  number :  7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10 , 7) = 1
fact(10) = 3628800

# program:
import math
a = int(input("Enter 1st integer number: "))	# 10
b = int(input("Enter 2nd integer number: "))	# 7
print(f'{a} + {b} = {a + b}')			# 10 + 7 = 17
print(f'{a} - {b} = {a - b}')			# 10 - 7 = 3
print(f'{a} * {b} = {a * b}')			# 10 * 7 = 70
print(f'{a} / {b} = {a / b}')			# 10 / 7 = 1.428
print(f'{a} % {b} = {a % b}')			# 10 % 7 = 3
print(f'max({a} , {b}) = {max(a, b)}')		# max(10, 7) = 10
print(f'min({a} , {b}) = {min(a, b)}')		# min(10, 7) = 7
print(f'{a} ^ {b} = {a ** b}')			# 10^7=10000000
print(f'sqrt({a}) = {math.sqrt(a)}')		# sqrt(10)=3.162
print(f'gcd({a} , {b}) = {math.gcd(a, b)}')	# gcd(10, 7)= 1
print(f'fact({a}) = {math.factorial(a)}')	# fact(10) = 3628800




'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
sample output:
Enter  1st  input :  25
Enter  2nd  input : Hyd
Before  swap :  x='25'            y='Hyd'
After  swap :  x='Hyd'            y='25'

# program:
x = input("Enter 1st input: ")			# 25
y = input("Enter 2nd input: ")			# Hyd
print(f"Before swap: x='{x}' \t y='{y}'")	# Before  swap :  x='25' <taabspace> y='Hyd'
x, y = y, x  # Swap in a single line
print(f"After swap: x='{x}' \t y='{y}'")	# After  swap :  x='Hyd' <tabspace> y='25'





'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
sample output:
Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15.8
Largest  Input  :  20

# program:
x = eval(input("Enter 1st input: "))				# 10
y = eval(input("Enter 2nd input: "))				# 20
z = eval(input("Enter 3rd input: "))				# 15.8
largest = x if x > y and x > z else (y if y > z else z)		# 10 if 10>20 and 10>15.8 else (20 if 20>15.8 else 15.8)
print(f'Largest Input: {largest}')				# Largest Input: 20





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
sample output:
Enter 1st input : 10
Enter 2nd input : 20
Result :   <

#Program:
x = eval(input("Enter 1st input: "))			# 10
y = eval(input("Enter 2nd input: "))			# 20
result = '>' if x > y else ('<' if x < y else '=')	# '>' if 10>20 else ('<' if 10<20 else '=') 
print(f"Result: {result}")				# Result: <




'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
sample output:
Enter any number : -25
Result :  -1

# program:
x = int(input("Enter any number: "))			# 50
result = 1 if x > 0 else (-1 if x < 0 else 0)
print(f"Result: {result}")				# 1





'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
sample output:
Enter  any  +ve  integer : 45
Odd  number

# program:
x = int(input("Enter any +ve integer: "))			# 50
print("Even number" if x % 2 == 0 else "Odd number")		# Even number





'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

# program:
length = float(input("Enter length: "))		# 50
breadth = float(input("Enter breadth: "))	# 20
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area = {area}")				# 1000.0
print(f"Perimeter = {perimeter}")		# 140.0





'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

# program:
import math
r = float(input("Enter radius: "))
volume = (4 / 3) * math.pi * r**3
print(f"Volume = {volume}")




'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''

# program:
p = float(input("Enter principal: "))		# 5000
t = float(input("Enter time in years: "))	# 2
r = float(input("Enter rate of interest: "))	# 2
si = (p * t * r) / 100
ci = p * (1 + r / 100) ** t - p
print(f"Simple Interest = {si}")		# 200.0
print(f"Compound Interest = {ci}")		# 202.0





'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
# program:
x = 10
y = 25
a = x				# a=10
x = y				# x=25
y = a				# y=10
print(f"x = {x}, y = {y}")	# x=25, y=10




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
# program:
x = 25
y = 10
x = x + y  # x = 25+10= 35
y = x - y  # y = 35-10= 25
x = x - y  # x = 35-25= 10
print(f"x = {x}, y = {y}")




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
#program:
x = -200
y = 100
x = x * y    # x = -20000
y = x // y   # y = -200
x = x // y   # x = 100
print(f"x = {x}, y = {y}")