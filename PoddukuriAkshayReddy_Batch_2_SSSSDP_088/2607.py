

Poddukuri Akshay Reddy
2607


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) # 25
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
print(F'{a}  \t   {b}   \t  {c}') # 25	10.8	Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25	b = 10.8	c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')  # a=25	b=10.8	c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}') # 25	10.8	Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}  \t  b  =  {b}  \t  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a	b  =  b	c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # error z is not defined


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #  {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
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
Enter 1st  integer  number :  10
Enter 2nd  integer  number :  7

import math
x = 10
y= 7
print(f'{x}+{y} = {x+y}')
print(f'{x}-{y} = {x-y}')
print(f'{x}*{y} = {x*y}')
print(f'{x}/{y} = {x/y}')
print(f'{x}%{y} = {x%y}')
max_value = max(x,y)
print(f'maximum of ({x},{y}) = {max_value}')
minn = min(x,y)
print(f'minimum of ({x},{y}) = {minn}')
x1=math.sqrt(10)
print(f'square root of {x} = {x1}')
print(f'power {10} to the {7} = {10**7}')
x2 = math.gcd(10,7)
print(f'GCD of ({x},{y}) = {x2}')
x3 = math.factorial(10)
print(f'factorial of {x} = {x3}')


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


'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''

Enter  1st  input :  25
Enter  2nd  input : Hyd
Before  swap :  x='25'            y='Hyd'
After  swap :  x='Hyd'            y='25'

x=10
y=20
x = x+y
y= x-y
x= x-y
print(x,y)

or

x=25
y='Hyd'
x, y = y,x
print(x,y)


'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15.8
Largest  Input  :  20

a = eval(input("Enter a 1st input:"))
b = eval(input("Enter a 2nd input:"))
c = eval(input("Enter a 3rd input:"))
largest = a if a>b and a>c else b if b>c else c
print(f'largest is {largest}')


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
Enter 1st input : 10
Enter 2nd input : 20
Result :   <

a = eval(input("Enter a 1st input:"))
b = eval(input("Enter a 2nd input:"))
x = '>' if a>b else '<' if a<b else '='
print(x)



'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
Enter any number : -25
Result :  -1

a = int(input("Enter a 1st input:"))
x = '1' if a>0 else '-1' if a<0 else '0'
print(x)


'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''

Enter  any  +ve  integer : 45
Odd  number

x = int(input("Enter a number: "))
y = 'Even' if x%2==0 else 'Odd'
print(f'{x} is {y} Number')


'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
a = int(input("Enter a Length:"))
b = int(input("Enter a Breadth:"))
Area = a*b
Perimeter = 2*(a+b)
print(f'Area is {Area} sq Units And Perimeter is {Perimeter} Units')



'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
P = eval(input("Enter a Principle:"))
T = eval(input("Enter a Time in Years:"))
R = eval(input("Enter a 3rd Rate of interest:"))
SI = (P*T*R)/100
CI = P * ((1 + R / 100) ** T) - P
print(f'simple Interest is {SI} And Compound Interest is {CI}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
a = eval(input("Enter A 1st input:"))
b = eval(input("Enter B 2nd input:"))
temp = a
a = b
b = temp
print(f' A is {a} and B is {b}')



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
a = eval(input("Enter A 1st input"))
b = eval(input("Enter B 2nd input"))
a = a+b
b = a-b
a = a-b
print(f' A is {a} and B is {b}')




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
a = eval(input("Enter A 1st input"))
b = eval(input("Enter B 2nd input"))
a = a*b
b = a/b
a = a/b
print(f' A is {a} and B is {b}')