'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")
	
	

#2
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if a>b and a>c:
    print(a,"is largest number")
elif b>a and b>c:
    print(b,"is largest number")
else:
    print(c,"is largest number")
	

#3
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

# Program to convert Celsius to Fahrenheit and vice-versa

print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F = {celsius}°C")

else:
    print("Invalid choice! Please enter 1 or 2.")
	
#3
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

# Program to convert Celsius to Fahrenheit and vice-versa

print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F = {celsius}°C")

else:
    print("Invalid choice! Please enter 1 or 2.")
	

#4
'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''



x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("Point lies in the 1st Quadrant")
elif x < 0 and y > 0:
    print("Point lies in the 2nd Quadrant")
elif x < 0 and y < 0:
    print("Point lies in the 3rd Quadrant")
elif x > 0 and y < 0:
    print("Point lies in the 4th Quadrant")
elif x != 0 and y == 0:
    print("Point lies on the X-axis")
elif x == 0 and y != 0:
    print("Point lies on the Y-axis")
elif x == 0 and y == 0:
    print("Point lies at the Origin")
	
#5
'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max =  20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program
'''

# Program to find max, min, and middle of three numbers

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))


maximum = a
minimum = a

if b > maximum:
    maximum = b
if c > maximum:
    maximum = c


if b < minimum:
    minimum = b
if c < minimum:
    minimum = c


middle = (a + b + c) - (maximum + minimum)


print("Maximum =", maximum)
print("Minimum =", minimum)
print("Middle  =", middle)


#6
'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''



import math

# Input three sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Step 1: Check triangle validity using triangle inequality rule
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a triangle.")

    # Step 2: Check for Equilateral triangle
    if a == b and b == c:
        print("It is an Equilateral Triangle")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area =", round(area, 2))

    # Step 3: Check for Isosceles triangle
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle")
        perimeter = a + b + c
        print("Perimeter =", perimeter)

    # Step 4: Else it's a Scalene triangle
    else:
        print("It is a Scalene Triangle")
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Perimeter =", perimeter)
        print("Area =", round(area, 2))
else:
    print("The given sides do NOT form a triangle.")
	

#8
'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  --->  b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  ---> (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  ---> (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  --->  3 - 4j
'''
import math

# Input coefficients
a = float(input("Enter coefficient a (a ≠ 0): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check that a is not zero
if a == 0:
    print("Invalid input: a must not be 0")
else:
    # Calculate discriminant
    disc = b**2 - 4*a*c
    print("Discriminant =", disc)

    # Case 1: Real and distinct roots (disc > 0)
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Roots are Real and Distinct")
        print("Root 1 =", root1)
        print("Root 2 =", root2)

    # Case 2: Real and same roots (disc == 0)
    elif disc == 0:
        root = -b / (2*a)
        print("Roots are Real and Same")
        print("Root =", root)

    # Case 3: Complex/Imaginary roots (disc < 0)
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        print("Roots are Complex/Imaginary")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
		
#9
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math

# Input radius and coordinates of the point
r = float(input("Enter the radius of the circle: "))
x = float(input("Enter x-coordinate of the point: "))
y = float(input("Enter y-coordinate of the point: "))

# Calculate distance from origin to point (x, y)
distance = math.sqrt(x**2 + y**2)
print("Distance from origin to point =", round(distance, 2))

# Determine the position of the point relative to the circle
if distance < r:
    print("The point lies Inside the circle.")
elif distance == r:
    print("The point lies On the circle.")
elif distance > r:
    print("The point lies Outside the circle.")
	
#10
# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')                           #Bye


#11
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')     #Case 2 has error. "_"must be end of match

#12
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')      #Wildcard must be one time.In case2 and 3 .we had 2 times,it causes an error

#13
#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')                   #Hyd
                               #Bye
							   
#14
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')     
              #Book
			  #Bye

#15
'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd  Sec Cyb Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One Two Three Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India China Usa Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd  Sec Cyb Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One Two Three Bye
6) What  are  the  outputs  if  input  is  7  ?  --->  Hyd  Sec Cyb Bye
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')


#16
'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Not  a  point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Not  a  point
8) What  is  the  output  when  input  is  ()  ?  --->Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Not  a  point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')
		
		

#17
'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''

units = int(input('Enter  units :   '))  #  75
match  units // 100:
	case  0:
				cost = units * 3.00
	case 1:
                cost=100*3.00-(100-units)*3.50	
	case 2 | 3 :
				cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
	case 4 | 5 | 6:
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
	case _:
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
print(units,'units,cost of Bill:',cost)


#18
'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop
'''
a=0
b=1
c=a+b
print(a)
print(b)
while c<=10:
     print(c)
	 a=b
	 b=c
	 c=a+b
	
#19
#  Find  outputs
while  True:
	print('Hello')
print('Bye') 

#Hello
#Hello...... Hello excute infinitely, True always True

#20
#  Find  outputs
while  False:
	print('Hello')
print('Bye')           #Bye

#21
# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
list=[10 , 20 , 15 , 18] 
for i in list:
    print(i)

print()
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
st='Hyd'
for i in st:
    print(i)
print()
#How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
    print(i)
	
#22
#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
b=[]
for i in a:
    b=i+b
print(b)

print('Indexed for loop')
for i in range(len(a)):
    print(i)
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop

a = [25, 10.8, 'Hyd', True]

print("Reverse order using indexed for loop:")
for i in range(len(a) - 1, -1, -1):
    print(a[i])
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
b = []
for i in a:
    b = [i] + b
print(b)

#23
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()  
#10
#30
#50
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
#20
#40
#50
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
#(10,20)
#(30,40)
#(50,60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
#10
#30
#50


#24
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)     #
for  x   in  []:
        print(x)    #
for  x   in   {}:
        print(x)     #
for  x   in   set():
        print(x)     #
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():    TypeError: range expected at least 1 argument
	print(x)
for  x  in   (25):
	print(x)           #NON SEQUENCES ARE NOT ITTERABLE
	
#25
# Identify  error  (Home  work)
for  x  in   123:
        print(x)        #Non-sequence are not iterable
		
#26
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]

for i in range(len(a)):
    print(i,a[i])

print('Indexed  based  for loop')
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')

for i in range(len(a)):
    print(i,a[i])
	
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
i = 0
for x in a:
    print(i, x)
    i += 1
	
#27
'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter 1st list  : '))
b = eval(input('Enter 2nd list  : '))
c = []

# Using index-based for loop
print('Using index-based for loop')
for i in range(len(a)):
    c.append(a[i] + b[i])

print('3rd list :', c)

# Resetting c to empty for second method
c = []

# Using for-each loop (without 2nd variable)
print('Using for-each loop (no 2nd variable)')
i = 0
for x in a:
    c.append(x + b[i])
    i += 1

print('3rd list :', c)

#28
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)       #a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)          #b = [10 , 20 , 15 , 18]