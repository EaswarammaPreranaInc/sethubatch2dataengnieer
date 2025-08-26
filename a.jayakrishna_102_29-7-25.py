
"""#Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
"""
year = int(input("Enter year: "))   # 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")  # Leap tear
else:
    print("Not a leap year")



##Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

#Hint:  Write  multiple  conditions
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest =c
print("The largest number is:", largest)


"""	#Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
"""
a= input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius: ")
if a == '1':
    celsius = float(input("Enter Celsius temperature: "))
    fahrenheit = (1.8 * celsius) + 32
    print("Fahrenheit Equivalent:", fahrenheit)
elif a == '2':
    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Celsius Equivalent:", celsius)
else:
    print("Invalid input")




'''
#Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
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
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))
if x > 0 and y > 0:
    print("The point lies in the 1st quadrant")
elif x < 0 and y > 0:
    print("The point lies in the 2nd quadrant")
elif x < 0 and y < 0:
    print("The point lies in the 3rd quadrant")
elif x > 0 and y < 0:
    print("The point lies in the 4th quadrant")
elif x != 0 and y == 0:
    print("The point lies on the x-axis")
elif x == 0 and y != 0:
    print("The point lies on the y-axis")
else:
    print("The point is at the origin")


'''
#Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

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
a = 10
b = 20
c = 7
max_val = a
min_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
mid_val = (a + b + c) - (max_val + min_val)
print("Largest number is:", max_val)
print("Smallest number is:", min_val)
print("Middle number is:", mid_val)

'''
#Write  a  program  to  determine  three  sides  form  a  triangle  or  not

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
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)
if is_triangle(a, b, c):
    if a == b == c:
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Triangle is equilateral")
        print(f"Area of equilateral triangle: {area:.2f}")
    elif a == b or b == c or a == c:
        perimeter = a + b + c
        print("Triangle is isosceles")
        print(f"Perimeter of isosceles triangle: {perimeter:.2f}")
    else:
        perimeter = a + b + c
        s = perimeter / 2  # semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
        print("Triangle is scalene")
        print(f"Area of scalene triangle: {area:.2f}")
        print(f"Perimeter of scalene triangle: {perimeter:.2f}")
else:
    print("The given sides do not form a triangle")


'''
#Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

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
a = float(input("Enter coefficient a (non-zero): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c 
    print("Discriminant:", discriminant)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Roots are real and distinct.")
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("Roots are real and same.")
        print("Root:", root)
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        print("Roots are complex (imaginary).")
        print(f"Root 1: {real_part} + {imag_part}j")
        print(f"Root 2: {real_part} - {imag_part}j")



'''
#Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math
r = float(input("Enter the radius of the circle: "))
x = float(input("Enter the x coordinate of the point: "))
y = float(input("Enter the y coordinate of the point: "))
distance = math.sqrt(x**2 + y**2)
if distance < r:
    print("The point lies inside the circle.")
elif distance > r:
    print("The point lies outside the circle.")
else:
    print("The point lies on the circle.")




## Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
"""o/p:
Bye"""



# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
#	case  _:     # Error  wildcard is last case
		print('None of   the  above')
	case  2:
		print('Two')  # Two
print('Bye')  #Bye


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
#	case  _:
		print('Hello')
	case  _:  # Error due to to wildcards
		print('Bye')
print('End')
"""o/p:
Hello
End"""



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
"""o/p:
Hyd
Bye
"""
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
"""o/p:
Book
Bye"""



"""#1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd
Sec
Cyb
Bye

2) What  are  the  outputs  if  input  is  15  ?  ---> Hyd
Sec
Cyb
Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India
China
Usa
Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd
Sec
Cyb
Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One
Two
Three
Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd
Sec
Cyb
Bye
"""
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





"""#1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Not  a  point
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> Not  a  point
8) What  is  the  output  when  input  is  ()  ?  ---> Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Not  a  point
"""
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


"""#Write  a  program  to  determine  bill  amount  and  input  is  units

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
"""
units = int(input('Enter  units :   '))  #  75
match  units // 100:
	case  0:
				cost = units * 3.00


units = int(input('Enter units: '))  # For example, 1200
cost = 0.0
match units // 100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = (100 * 3.00) + ((units - 100) * 3.50)

    case 2 | 3:
        cost = (100 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00)
    case 4 | 5 | 6:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + ((units - 400) * 4.50)
    case _:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + ((units - 700) * 5.00)
print(f"Bill amount for {units} units is: Rs. {cost:.2f}")



"""#Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop

"""
x = int(input("Enter the limit (x): "))
a, b = 0, 1
print("Fibonacci series up to", x, "is:")
while a <= x:
    print(a, end=" ")
    a, b = b, a + b
print()  # for newline



#  Find  outputs
while  True:
	print('Hello')  # Hello is print in loop
print('Bye')  # not executed


#  Find  outputs
while  False:
	print('Hello')
print('Bye')   # Bye

# Find  outputs  (Home  work)
for x in [10,20,30,40]:
    Print(x)
print() 
for ch in Hyd:   #How  to  print  each  character  of   string  'Hyd'  with  for  loop
    print(ch) 
print()
#How  to  print  each  element  of   range(5)  with  for  loop




# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)   
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
"""o/p:
10
20
30
<empty >
20
40
60
<empty>
(10,20)
(30,40)
(50,60)
<empty>
10
30
50
"""
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  # 10…20	30…40	50…60
#for  x ,  y  in   a:     # Error due to no expression
	print(x , y )
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')  # 10…20	30…40	50…60


# Identify  error  (Home  work)
for  x  in   123:   # Error for loop can not iterate non sequence 
        print(x)   


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)   # empty tuple
for  x   in  []:
        print(x)  # empty list
for  x   in   {}:
        print(x)  # empty dict
for  x   in   set():
        print(x)  # empty set
for  x   in   '':
        print(x)  # empty string
for  x  in  range(10 , 10):
	print(x)  # empty 
for  x  in   range():
	print(x)  #Error 
for  x  in   (25):
	print(x)  #error


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')
"""o/p:
1 1 
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
"""

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for I in range(len(a)) :  #How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
    print(i , a[i])
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)   # not possible



#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
a = [25, 10.8, 'Hyd', True]
print('Indexed for loop (reverse order)')
for i in range(len(a) - 1, -1, -1):  # from last index to 0
    print(a[i])




"""#Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
"""
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

a = eval(input('Enter 1st list : '))    # e.g. [10, 20, 15, 18]
b = eval(input('Enter 2nd list : '))    # e.g. [30, 40, 35, 12, 100, 200, 300]
c = []
min_len = min(len(a), len(b))
for i in range(min_len):
    c.append(a[i] + b[i])
print('3rd list :', c)




#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
print('Indexed for loop')
for i in range(2, 5):  # indexes 2, 3, 4
    print(a[i])





#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)   # [11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)   # [10,20,15,18]