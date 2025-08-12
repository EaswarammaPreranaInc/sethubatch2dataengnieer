   Name: M.SaiCharan                           (Home work)
   Date: 26-07-2025.



1.#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)						#'25'
print(type(y))						#<class 'str'>
x = 10.8
y = F'{x}'
print(y)						#'10.8'
print(type(y))						#class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)						#[10, 20, 30, 40]
print(type(y))						#<class 'str'>




2.#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')			#25  	   10.8   	   Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')		#a = 25  	  b  =  10.8  	  c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')			#a=25   	   b=10.8   	   c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')			#25   	   10.8   	   Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')	#a  =  {a}  	b  =  {b}  	c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')		#a  =  a  	b  =  b  	c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')			#Error




3.#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  						#  25
print(F'{{x}}')						#  {x}
print(F'{{{x}}}')					#   {25}
print(F'{{{{x}}}}')					#{{x}}
print(F'{{{{{x}}}}}')					#{{25}}
print(F'{{{{{{x}}}}}}')					#{{{x}}}
print(F'{{{{{{{x}}}}}}}')				#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')				#{{{{x}}}}




'''
4.Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
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
code:
import math

# Input
a = eval(input("Enter 1st integer number : "))
b = eval(input("Enter 2nd integer number : "))
sum_result= a + b
diff = a - b
product = a * b
quotient = a / b
remainder = a % b
maximum = max(a, b)
minimum = min(a, b)
power = a ** b                          
sqrt_a = math.sqrt(a)
gcd = math.gcd(a,b)
factorial_a = math.factorial(a)
print(f'{a} + {b} = {sum}')
print(f'{a} - {b} = {diff}')
print(f'{a} * {b} = {product}')
print(f'{a} / {b} = {quotient}')
print(f'{a} % {b} = {remainder}')
print(f'max({a}, {b}) = {maximum}')
print(f'min({a}, {b}) = {minimum}')
print(f'{a} ** {b} = {power}')
print(f'sqrt({a}) = {sqrt_a}')
print(f'gcd({a}, {b}) = {gcd}')
print(f'fact({a}) = {factorial_a}')



5.Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects

 code:
x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
print(f"Before swap :  x='{x}'    y='{y}'")
x, y = y, x
print(f"After swap :  x='{x}'     y='{y}'")



6.Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

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

code:

try:
   a=eval(input("Enter 1st input: "))
   b=eval(input("Enter 2nd input: "))
   c=eval(input("Enter 3rd input: "))
   max=a if a>b and a>c else( b if b>c else c)
   print(f'Largest Input: {max}')
except:
    print("for string inputs, use single quotes")
'''




7.Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
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

code:

a=eval(input("Enter 1st input: "))
b=eval(input("Enter 2nd input: "))
max='>' if a>b else '<' if a<b else '='
print("Result :  ", maximum)

'''



8.Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
sample output:
Enter any number : -25
Result :  -1


code:
a = int(input("Enter any number : "))
result = 1 if a > 0 else (-1 if a < 0 else 0)
print("Result : ", result)
'''


9.Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
sample output:
Enter  any  +ve  integer : 45
Odd  number

code:

try:
   a=eval(input("Enter any number: "))
   result = 'Even Number' if a % 2 ==0 else 'Odd Number'
   print(f'{result}')
except:
   print("Input should be a positive number")
'''


(Home  work)
10.Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
code:

Length= eval(input("Enter the length of the rectangle : "))
breadth = eval(input("Enter the breadth of the rectangle : "))
area = Length * breadth
perimeter = 2 * (Length + breadth)
print("Area of rectangle      : ", area)
print("Perimeter of rectangle : ", perimeter)




'''



11.Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
code:

import math

try:
   a=eval(input("Enter Radius: "))
   pi=math.pi
   Vol=(4/3) * pi * a**3
   print(f'Volume of Sphere with Radius {a} is: {Vol:.2f} cubic units')
except:
   print("Input should be a positive number")




'''

12.Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
code:
 p = float(input("Enter the principal amount : "))
 t = float(input("Enter the time (in years)     : "))
 r = float(input("Enter the rate of interest (%) : "))
# simple interest
si = (p * t * r) / 100
# compound interest
ci = p * ((1 + r / 100) ** t) - p
print("Simple Interest   : ", si)
print("Compound Interest : ", ci)






'''

13.Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
code:

x=eval(input("Enter 1st input: "))
y=eval(input("Enter 2nd input: "))
print("Before swap:")
print("x =", x)
print("y =", y)
temp = x
x = y
y = temp
print("After swap:")
print("x =", x)
print("y =", y)



'''



14.Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
# code:
     
x=eval(input("Enter 1st input: "))
y=eval(input("Enter 2nd input: "))
print("Before swap:")
print("x =", x)
print("y =", y)
# Swapping using addition and subtraction
x = x + y  
y = x - y   
x = x - y   
print("After swap:")
print("x =", x)
print("y =", y)


'''


15.Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
#code:

x=eval(input("Enter 1st input: "))
y=eval(input("Enter 2nd input: "))
print("Before swap:")
print("x =", x)
print("y =", y)
# Swapping using multiplication and division
x = x * y   
y = x // y  
x = x // y 
print("After swap:")
print("x =", x)
print("y =", y)