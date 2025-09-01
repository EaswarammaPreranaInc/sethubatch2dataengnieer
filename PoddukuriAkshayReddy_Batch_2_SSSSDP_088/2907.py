Poddukuri Akshay Reddy
2907

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''
year = int (input("Enter a Number:"))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f'{year} is leap year')
else:
    print(f'{year} is  not  leap year')


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
x = int(input("Enter 1st Number:"))
y = int(input("Enter 2nd Number:"))
z = int(input("Enter 3rd Number:"))
if( x > y and x > z):
    print(f'{x} is the largest')
elif(y > z):
    print(f'{y} is the largest')
else:
    print(f'{z} is the largest')



'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
cel = int(input("Enter celsius temp:"))
far = int(input("Enter farenheit temp:"))
x = cel * 1.8 + 32
y = (far-32)/1.8
print(f'farenheit of {cel}c is {x}') 
print(f'celsius of {far}f is {y}') 



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
x = eval(input("Enter x value:"))
y = eval(input("Enter y value:"))
if (x>0 and y>0):
    print(f'{x,y} belongs to 1st quradeant')
elif(x<0 and y>0):
    print(f'{x,y} belongs to 2nd quradeant')
elif(x<0 and y<0):
    print(f'{x,y} belongs to 3rd quradeant')
elif(x>0 and y <0):
    print(f'{x,y} belongs to 4th quradeant')


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

Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0

# Get input from user
a = float(input("Enter first input   : "))
b = float(input("Enter second input  : "))
c = float(input("Enter third input   : "))

max_num = a
min_num = a

if b > max_num:
    max_num = b
if c > max_num:
    max_num = c

if b < min_num:
    min_num = b
if c < min_num:
    min_num = c

mid_num = (a + b + c) - (max_num + min_num)

print("Largest number   :", max_num)
print("Smallest number  :", min_num)
print("Middle number    :", mid_num)



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

# Input 3 sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if sides form a triangle
if (a + b > c) and (b + c > a) and (c + a > b):
    print("These sides form a triangle.")

    if a == b and b == c:
        print("It is an Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area =", round(area, 2))

    elif a == b or b == c or c == a:
        print("It is an Isosceles Triangle.")
        perimeter = a + b + c
        print("Perimeter =", perimeter)

    else:
        print("It is a Scalene Triangle.")
        perimeter = a + b + c
        s = perimeter / 2  # semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Perimeter =", perimeter)
        print("Area =", round(area, 2))
else:
    print("These sides do NOT form a triangle.")



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
a = float(input("Enter value of a (a ≠ 0): "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Check if a is not zero
if a == 0:
    print("This is not a quadratic equation because a = 0.")
else:
    # Calculate discriminant
    disc = b ** 2 - 4 * a * c
    print("Discriminant =", disc)

    if disc > 0:
        print("Roots are Real and Distinct")
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Root 1 =", root1)
        print("Root 2 =", root2)

    elif disc == 0:
        print("Roots are Real and Same")
        root = -b / (2 * a)
        print("Root =", root)

    else:
        print("Roots are Complex (or) Imaginary")
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-disc) / (2 * a)
        print("Root 1 =", complex(real_part, imag_part))
        print("Root 2 =", complex(real_part, -imag_part))




'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
# Bye



# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
# None of   the  above
# Bye



# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')
#  Hello
# End


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
# Hyd
# Bye

# Find  outputs  (Home  work)
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

# Book
#Bye



'''
1) What  are  the  outputs  if  input  is  -6 ? --->  
# Hyd
Sec
Cyb
Bye
2) What  are  the  outputs  if  input  is  15  ?  --->
# One
Two
Three
Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->
# India
China
Usa
Bye
4) What  are  the  outputs  if  input  is  0  ?  --->
# Hyd
Sec
Cyb
Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->
# One
Two
Three
Bye

6) What  are  the  outputs  if  input  is  7  ?  --->
# Hyd
Sec
Cyb
Bye
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


'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->#  Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> #  x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> # y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> # Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> # Quadrant 
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> # y - axis
8) What  is  the  output  when  input  is  ()  ?  ---> # Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> # Quadrant
10) What  is  the  output  when  input  is  (25,) ?  ---> # Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> # Quadrant
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print(' ')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')


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
[

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

Enter  value  of  x  :  10
Fibonacci  Series
0
1
1
2
3
5
8


#  Find  outputs
while  True:
	print('Hello')
print('Bye')
# Hello
Bye


#  Find  outputs
while  False:
	print('Hello')
print('Bye')
Bye


# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
list = [10 , 20 , 15 , 18]
# for a in list:
print(a)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
a = "Hyd"
for i in a:
print(i) 
How  to  print  each  element  of   range(5)  with  for  loop
for i in range(5):
print(i)



# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()

# 10
30
50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
# 20
40
60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
(10, 20)
(30, 40)
(50, 60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
# 10
30
50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
10...20
30...40
50...60

for  x ,  y  in   a:
	print(x , y)
# error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
# error


# Identify  error  (Home  work)
for  x  in   123:
        print(x)
# int is not iterable

`# Find  outputs  (Home  work)
for  x   in   ():
        print(x)  # Empty
for  x   in  []:
        print(x) # Empty
for  x   in   {}:
        print(x) # Empty
for  x   in   set():
        print(x) # Empty
for  x   in   '':
        print(x) # Empty
for  x  in  range(10 , 10):
	print(x)  # Empty
for  x  in   range():
	print(x)   # Error
for  x  in   (25):
	print(x)  # Error


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
# 1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye


# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')

for i in range(len(a)):
	print(a[i],i)
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
for i in range(len(a)):
	print(a[i],i)

How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)-1,-1,-1):
	print(a[i])
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)-1,-1,-1):
	print(a[i],i)
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for i in range(len(a)-1,-1,-1):
	print(a[i])


'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

a = eval(input('Enter 1st list: '))
b = eval(input('Enter 2nd list: '))
c = []

for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list using index-based for loop:', c)



#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2, 5):  # 2 to 4 (inclusive)
    print(a[i])

How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
index = 0 
for value in a"
	if 2<= index <4:
		print(value)
	index +=1


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
a :   [11, 21, 16, 19]


b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)
b :   [10, 20, 15, 18]