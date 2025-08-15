#  Find  outputs  (Home  work)
x = 25 # ref 'x' is assigned to int obj
y = F'{x}' # F string format --- y = 25
print(y) # 25
print(type(y)) # <class 'int'>
x = 10.8 # ref 'x' points to float obj
y = F'{x}' # F string format ---y = 10.8
print(y) # 10.8
print(type(y)) # <class 'float'>
x = [10,20,30,40] # ref 'x' points to list obj
y = F'{x}' # ref y is assigned to ref x
print(y) # [10,20,30,40]
print(type(y)) # <class 'list'>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd' # multiple assignment
print(F'{a}  \t   {b}   \t  {c}') # prints -- 25 <tab space> 10.8 <tab space> Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25 <tab space> b  =  10.8 <tab space> c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # prints same as above statement a = 25 <tab space> b  =  10.8 <tab space> c  =  Hyd
print(F'{a:}  \t   {b:}   \t  {c:}') # 25 <tab space> 10.8 <tab space> Hyd # : is ignored
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # no F format so prints as it is --- a  =  {a} <tab space> b  =  {b} <tab space> c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a <tab space> b  =  b <tab space> c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # error 


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25 -- odd braces value is printed
print(F'{{x}}')   # {x} -- even braces object is printed
print(F'{{{x}}}')  # {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{25}}
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

##### program input #####

import math
a = int(input("Enter 1st  integer  number :"))
b = int(input("Enter 2nd  integer  number :"))
print(F'{a} + {b} = {a + b}')
print(F'{a} - {b} = {a - b}')
print(F'{a} * {b} = {a * b}')
print(F'{a} / {b} = {a / b}')
print(F'{a} % {b} = {a % b}')
print(F'max({a} , {b}) = {max(a,b)}')
print(F'min({a} , {b}) = {min(a,b)}')
print(F'{a} ^ {b} = {a**b}')
print(F'sqrt{a} = {math.sqrt(a)}')
print(F'gcd({a} , {b}) = {math.gcd(a,b)}')
print(F'fact({a}) = {math.factorial(a)}')

##### Output #####
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
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
##### Swap Program #####
num1 = eval(input("Enter  1st  input :"))
num2 = eval(input("Enter  2nd  input :"))
print(F'Before  swap : x = {num1}  y = {num2}')
num1 , num2 = num2 , num1
print(F'After  swap : x = {num1}  y = {num2}')

###### output ######
Enter  1st  input :  25
Enter  2nd  input : Hyd
Before  swap :  x='25'   y='Hyd'
After  swap :  x='Hyd'   y='25'

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
###### largest input Program ######
a = eval(input("Enter 1st input :"))
b = eval(input("Enter 2nd input :"))
c = eval(input("Enter 3rd input :"))
e = a if a>b else b if b>c else c
print("Largest  Input  :", e) 

######output######
Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15.8
Largest  Input  :  20

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

###### Program ######
a = eval(input("Enter 1st input :"))
b = eval(input("Enter 2nd input :"))
e = '<' if a<b else '>' if b>a else '='
print("result :", e)

######output######
Enter 1st input : 10
Enter 2nd input : 20
Result :   <

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
###### Program ######
a = eval(input("Enter any number :"))
e = '-1' if a<0 else '+1' if a>0 else '='
print("Result :", e)

######output######
Enter any number : -25
Result :  -1

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
###### even-odd Program ######
a = int(input("Enter  any  +ve  integer :"))
e = 'even number' if a%2 == 0 else 'odd number'
print("Result :", e)

######output######
Enter  any  +ve  integer : 45
Odd  number

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

###### area  and  perimeter  of  rectangle Program ######
a = int(input("Enter Length :"))
b = int(input("Enter breadth :"))
print("area  of  rectangle :", a*b)
print("perimeter  of  rectangle :", 2*(a+b))

##### output #####
Enter Length : 2
Enter breadth : 4
area  of  rectangle : 8
perimeter  of  rectangle : 12

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
###### volume of a sphere ############

import math
a = float(input(" Enter the Radius :"))
volume = (4 / 3) * math.pi * (radius ** 3)
print("volume  of  sphere : ", volume)

#######out put########
Enter the Radius: 3
volume  of  sphere : 113.0976

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
########### simple and compound intrest ##############
principle = float(input("Enter principle amount :")
rate = float(input("Enter intrest rate :")
time = float(input("Enter the time :")

a = (principle * rate * time)/100
print("Simple  interest :", a)

b = principal * (1 + rate / 100) ** (n * time)

print("compound  interest :", b)


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
######### swap values ##########
a = eval(input("Enter 1st Value :"))
b = eval(input("Enter 2nd Value :"))

c = a
a = b
b = c
print(F"After swaping :  x = {a} and y = {b}") 

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
######### swap values ##########
a = int(input("Enter 1st Value :"))
b = int(input("Enter 2nd Value :"))
a = a + b     
b = a - b     
a = a - b
print(F"After swaping :  x = {a} and y = {b}") 

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
######### swap values ##########
a = int(input("Enter 1st Value :"))
b = int(input("Enter 2nd Value :"))
a = a * b     
b = a // b     
a = a // b
print(F"After swaping :  x = {a} and y = {b}")
