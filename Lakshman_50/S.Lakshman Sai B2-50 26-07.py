#  Find  outputs  (Home  work)
x = 25
y = F'{x}' #25
print(y) #25
print(type(y)) #<class str>
x = 10.8
y = F'{x}' #10.8
print(y)# 10.8
print(type(y)) #<class Str>
x = [10,20,30,40]
y = F'{x}' #[10,20,30,40]
print(y)# [10,20,30,40]
print(type(y))#<class Str>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#25   10.8  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25   b=10.8   c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}') #25  10.8  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#a={a}  b={b} c={c}
#print(F'{x =}  \t   {y =}   \t  {z =}') #Error

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}

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
'''

import math
x=eval(input("Enter 1st interger number: "))
y=eval(input("Enter 2st interger number: "))
print(F'{x} + {y} = {x+y}')
print(F'{x} - {y} = {x-y}')
print(F'{x} * {y} = {x*y}')
print(F'{x} / {y} = {x/y}')
print(F'{x} % {y} = {x%y}')
print(F'max({x} , {y}) = {max(x,y)}')
print(F'min({x} , {y}) = {min(x,y)}')
print(F'{x} ^ {y} = {x**y}')
print(F'sqrt({x} = {math.sqrt(10)}')
print(F'gcd({x} , {y}) = {math.gcd(x,y)}')
print(F'fact({x} = {math.factorial(x)}')

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects

Enter  1st  input :  25
Enter  2nd  input : Hyd
Before  swap :  x='25'            y='Hyd'
After  swap :  x='Hyd'            y='25'
'''
y=eval(input("Enter 2nd input : "))
x=eval(input("Enter 1st input : "))
print(f"Before swapping : x={x}      y={y}")
x,y=y,x
print(f"after swapping : x={x}       y={y}")


'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator

Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15.8
Largest  Input  :  20
'''
a=eval(input("Enter 1st input: "))
b=eval(input("Enter 2nd input: "))
c=eval(input("Enter 3rd input: "))
Large_num= a if a>b and a>c else b if b>c and b>a else c
print("largest_input : ",Large_num)

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator

Enter 1st input : 10
Enter 2nd input : 20
Result :   <
'''
a=eval(input("enter 1st number: "))
b=eval(input("enter 2nd number: "))
result=">" if a>b else "<" if b>a else "="
print("Result : ",result)


'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator

Enter any number : -25
Result :  -1
'''
a=eval(input("enter any number: "))
result="-1" if a<0 else "1" if a>0 else "0"
print("Result : ",result)

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator

Enter  any  +ve  integer : 45
Odd  number
'''
a=eval(input("enter any number: "))
result="Even number" if a%2==0 else "Odd" 
print("Result : ",result)

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
length=eval(input("Enter the length: "))
breadth=eval(input("Enter the Breadth: "))
area=length*breadth
perimeter=2*(length*breadth)
print("Area of Rectangle: ",area)
print("perimeter of Rectangle: ",perimeter)


'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math
radius=eval(input("enter radius: "))
volume=((4/3)*math.pi*(radius**3))
print(f"volume of spere: {volume:.2f}")


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''


p=eval(input("enter principle ammount: "))
t=eval(input("enter rate of time: "))
r=eval(input("enter rate of interest: "))
sim_int=(p*t*r)/100
com_int=(p*(1+r/100)**t)-p
print(f'Simple interest is: {sim_int}')
print(f'Compound interest is: {com_int:.2f}')



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(f'Before swapping x:{x}  y:{y}')
z=x
x=y
y=z
print(f'After swapping x:{x}  y:{y}')

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(f'Before swapping x:{x}  y:{y}')
x=x+y
y=x-y
x=x-y
print(f'After swapping x:{x}  y:{y}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(f'Before swapping {x= }  {y=}')
x=x*y
y=x/y
x=x/y
print(f'After swapping x:{x:.0f}  y:{y:.0f}')
