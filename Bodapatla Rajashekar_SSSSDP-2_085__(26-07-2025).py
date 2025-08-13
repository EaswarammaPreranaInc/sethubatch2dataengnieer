Find  outputs  (Home  work)

x = 25
y = F'{x}'		# F'{x}'=F'{25}=25
print(y)		# output: 25
print(type(y))		# output: <class 'str'>
x = 10.8
y = F'{x}'		# F'{x}'=F'{10.8}=10.8
print(y)		# output: 10.8
print(type(y))		# output: <class 'str'>
x = [10,20,30,40]
y = F'{x}'		# F'{x}'=F'{[10, 20, 30, 40]}=[10, 20, 30, 40]
print(y)		# output: [10, 20, 30, 40]
print(type(y))		# output: <class 'str'>




#Find  outputs  (Home  work)

a, b, c = 25, 10.8, 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')			# output: 25   	   10.8   	  Hyd 			: inserts object values directly
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')		# output: a = 25  	  b = 10.8  	  c = Hyd 	: labels printed with values
print(F'{a=}  \t   {b=}   \t  {c=}')			# output: a=25  	  b=10.8  	  c='Hyd' 	: f-string shows object name and value automatically
print(F'{a:}  \t   {b:}   \t  {c:}')			# output: 25  	  10.8  	  Hyd 			: same as {a}, {b}, {c}, ':' is just a format specifier
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')	# output: a = {a} 	  b = {b} 	  c = {c} 	: no 'f' before string, so prints as it is
print(F'a  =  a  \t  b  =  b  \t  c  =  c')		# output: a = a 	  b = b 	  c = c 
print(F'{x =}  \t   {y =}   \t  {z =}')			# Error as x, y, z are not defined yet



#  Find  outputs  (Home  work)

print(F'{x}')			# 25 
print(F'{{x}}')			# {x} 		: for even no. of opening braces prints only object with no. of braces//2 braces
print(F'{{{x}}}')		# {25}  	: for odd no. of opening braces prints only object value with no. of braces//2 braces
print(F'{{{{x}}}}')		# {{x}} 	: for even no. of opening braces prints only object with no. of braces//2 braces
print(F'{{{{{x}}}}}')		# {{25}} 	: for odd no. of opening braces prints only object value with no. of braces//2 braces
print(F'{{{{{{x}}}}}}')		# {{{x}}}	: for even no. of opening braces prints only object with no. of braces//2 braces
print(F'{{{{{{{x}}}}}}}')	# {{{25}}} 	: for odd no. of opening braces prints only object value with no. of braces//2 braces
print(F'{{{{{{{{x}}}}}}}}')	# {{{{x}}}}	: for even no. of opening braces prints only object with no. of braces//2 braces




# Write  a  program  to  determine  sum , difference , product , quotient , largest  and smallest  of  two  numbers. also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input


import math

try:
    a = int(input('Enter 1st integer number : '))
    b = int(input('Enter 2nd integer number : '))

    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b}')
    print(f'{a} % {b} = {a % b}')
    print(f'max({a} , {b}) = {max(a, b)}')
    print(f'min({a} , {b}) = {min(a, b)}')
    print(f'{a} ^ {b} = {a ** b}')
    print(f'sqrt({a}) = {math.sqrt(a)}')
    print(f'gcd({a} , {b}) = {math.gcd(a, b)}')
    print(f'fact({a}) = {math.factorial(a)}')

except ValueError:
    print("Please enter valid integers only.")


output:


Enter 1st integer number : 10
Enter 2nd integer number : 7
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




# Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

a = input('Enter 1st input: ')
b = input('Enter 2nd input: ')

print(f"Before swap : x = '{a}'    y = '{b}'")

a, b = b, a

print(f"After swap  : x = '{a}'    y = '{b}'")

outputs:

Enter  1st  input :  25
Enter  2nd  input : Hyd
Before  swap :  x='25'            y='Hyd'
After  swap :  x='Hyd'            y='25'




# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

try:
    a= eval(input('Enter 1st input :'))
    b= eval(input('Enter 2nd input :'))
    c= eval(input('Enter 3rd input :'))

    max=a if a>b else b if b>c else c
    print('largest input:',max)

exceptt NameError:
    print('input should be in quotes')

except TypeError:
    print('input should not be a complex number')


outputs:

Enter 1st input :10
Enter 2nd input :20
Enter 3rd input :15
largest input: 20

Enter 1st input :35.8
Enter 2nd input :42.8
Enter 3rd input :27.9
largest input: 42.8

Enter 1st input :'RAMA' 
Enter 2nd input :'RAKESH'
Enter 3rd input :'RAJESH'
largest input: 'RAMA'

Enter 1st input :[10 , 20 , 15 , 18]  
Enter 2nd input :[10 , 20 , 32 , 19] 
Enter 3rd input :[10 , 20 , 25 , 17]
largest input: [10 , 20 , 32 , 19] 



# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input, '<'  if  1st  input <  2nd  input  and '='  if  inputs  are  same

try:
    a = eval(input('Enter 1st input: '))
    b = eval(input('Enter 2nd input: '))

    result = '>' if a > b else '<' if a < b else '='
    print('Result:', result)

except NameError:
    print('Input should be in quotes for strings')

except TypeError:
    print('Input should not be a complex number')

outputs:

enter 1st input :10
enter 2nd input :20
Result: <

enter 1st input :70
enter 2nd input :60
Result: >

enter 1st input :25
enter 2nd input :25
Result: =



# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

a= eval(input('Enter 1st input :'))
result= 1 if a>0 else '-1' if a<0 else '0'
print('Result :',result)


outputs:

Enter 1st input :-25
Result : -1

Enter 1st input :75
Result : 1

Enter 1st input :0
Result : 0



# Write  a  program  to  test  input  is  even  number  or  odd  number

a = eval(input('Enter any +ve number: '))
  
result = 'Even number' if a //2 else 'Odd number'
print('Result:', result)

outputs:

Enter  any  +ve  integer : 45
Odd  number

Enter  any  +ve  integer : 36
Evenn  number



#(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object
Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10

# Homework: Swap using 3rd object (temporary variable)

x = 10
y = 25

print(f"Before swap: x = {x}, y = {y}")


z = x   # z stores x (10)
x = y   # x gets value of y (25)
y = z   # y gets value of z (10)

print(f"After swap : x = {x}, y = {y}")





# Write  a  program  to  determine  area  and  perimeter  of  rectangle


length = float(input('Enter length of rectangle: '))
breadth = float(input('Enter breadth of rectangle: '))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f'Area of rectangle = {area}')
print(f'Perimeter of rectangle = {perimeter}')

output:

Enter length of rectangle: 10
Enter breadth of rectangle: 5
Area of rectangle = 50.0
Perimeter of rectangle = 30.0




# Write  a  program  to  determine  volume  of  a  sphere

import math

radius = float(input('Enter radius of sphere: '))

volume = (4 / 3) * math.pi * (radius ** 3)

print(f'Volume of sphere = {volume}')

output:

Enter radius of sphere: 3
Volume of sphere = 113.09733552923255




# Write  a  program  to  determine  simple  interest  and  compound  interest


principal = float(input('Enter principal amount: '))
rate = float(input('Enter rate of interest: '))
time = float(input('Enter time in years: '))

simple_interest = (principal * time * rate) / 100
compound_interest = principal * ((1 + rate / 100) ** time) - principal

print(f'Simple Interest = {simple_interest}')
print(f'Compound Interest = {compound_interest}')

output:

Enter principal amount: 10000
Enter rate of interest: 5
Enter time in years: 2
Simple Interest = 1000.0
Compound Interest = 1025.0



# (Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions


x = int(input('Enter 1st integer number : '))
y = int(input('Enter 2nd integer number : '))

print(f'Before swap: x = {x}, y = {y}')

x = x + y      # x = 25 + 10 = 35
y = x - y      # y = 35 - 10 = 25 (y now becomes original x)
x = x - y      # x = 35 - 25 = 10 (x now becomes original y)

print(f'After swap : x = {x}, y = {y}')

output:

Enter 1st integer number : 25
Enter 2nd integer number : 10
Before swap: x = 25, y = 10
After swap : x = 10, y = 25



# (Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x = int(input('Enter 1st integer number : '))
y = int(input('Enter 2nd integer number : '))

print(f'Before swap: x = {x}, y = {y}')

x = x * y      # x = (-200) * 100 = -20000
y = x / y      # y = (-20000) / 100 = -200 
x = x / y      # x = (-20000) / (-200) = 100 

print(f'After swap : x = {x}, y = {y}')

output:

Enter 1st integer number : -200
Enter 2nd integer number : 100
Before swap: x = -200, y = 100
After swap : x = 100.0, y = -200.0