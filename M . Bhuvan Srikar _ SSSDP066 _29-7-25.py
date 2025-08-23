'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''
try:
	a = int(input('Enter a Year : '))
	if (a % 4  == 0 and a % 100 != 0 ) or a % 400 == 0:
		print('Leap Year')
	else:
		print('Not a Leap Year')
except:
	print('Please enter a integer value')

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a = int(input('Enter a Number : '))
b = int(input('Enter a Number : '))
c = int(input('Enter a Number : '))
if a > b and a > c:
	print(f'largest number is {a}')
elif b > c:
	print(f'largest number is {b}')
else:
	print(f'largest number is {c}')

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input
'''
a = int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert fahrenheit  to  celsius : '))
if a == 1:
	temp = int(input('Enter a Celcius temperature : '))
	b = 1.8 * temp + 32
	print(f'Fahrenheit Equivalent : {b}')
elif a == 2:
	temp1 = int(input('Enter  fahrenheit  temperature : '))
	c = (temp1 - 32) / 1.8
	print(f'celsius equivalent : {c}')
else:
	print('Invalid Input')


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

8) Hint:  Use  if  ..   elif
'''
x = float(input('Enter value of x : '))
y = float(input('Enter value of y : ')) 
if x > 0 and y > 0 :
	print('1st Quadrant')
elif x == 0 and y == 0:
	print('Origin')
elif x < 0 and y > 0:
	print('2nd quadrant')
elif x < 0 and y < 0:
	print('3rd quadrant')
elif x > 0 and y < 0:
	print('4th quadrant')
elif y == 0:
	print('x - axis')
elif x == 0:
	print('y - axis')



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

6) Hint : Do  not  use  else  in  the  program

Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0
'''
a = float(input('Enter 1st Number : '))
b = float(input('Enter 2nd Number : '))
c = float(input('Enter 3rd Number : '))

max = a
if b > max:
	max = b
if c > max:
	max = c
print(f'Largest Number : {max}')


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

5) Hint: Use  nested  if
'''
import math
a = float(input('Enter 1st side of the triangle : '))
b = float(input('Enter 2nd side of the triangle : '))
c = float(input('Enter 3rd side of the triangle : '))
if a + b > c and b + c > a and c + a > b:
	if a == b == c:
		print('Equilateral triangle')
		area = (math . sqrt(3) / 4) * a**2
		print(f'Area of equilateral triangle : {area}')
	elif a == b or b == c or c == a:
		print('Isoscles Triangle')
		peri = a + b + c
		print(f'Perimeter of Isoscles Triangle : {peri}')
	else:
		print('Scalen Triangle')
		s = (a + b + c) / 2
		area = math.sqrt(s * (s - a) * (s - b) * (s - c))
		print(f'Area of scalene triangle : {area}')
		print(f'Perimeter of scalene triangle : {a + b + c}')
else:
	print('It is not a Triangle')



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
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  --->  3 - 4j
'''
import math
a = float(input('Enter 1st value : '))
b = float(input('Enter 2nd value : '))
c = float(input('Enter 3rd value : '))
if a != 0:
	disc = math.pow(b , 2) -4*a*c
	if disc > 0:
		print('Real and Distinct')
		root1 = (-b + math . sqrt(disc)) / (2 * a)
		root2 = (-b - (math . sqrt(disc))) / (2 * a)
		print(root1)
		print(root2)
	elif disc == 0:
		print('Real and same')
		root = -b/(2*a)
		print(root)
	elif disc < 0:
		print('Complex (or) Imaginary roots')
		real = -b / (2*a)
		imag = math . sqrt(-disc) / (2 * a)
		print(f'root1 : {real} + {imag}j')
		print(f'root2 : {real} - {imag}j')
else:
	print('Value of a should be non-zero')

'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math
x = float(input('Enter x point : '))
y = float(input('Enter y point : '))
r = float(input('Enter Radius : '))
distance = math . sqrt(x ** 2 + y ** 2)
if distance > r :
	print('Outside the circle')
elif distance < r:
	print('Inside the circle')
elif distance == r:
	print('On the circle')


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # Bye


# Identify  Error
i = 2
match  i: 
	case  1:
		print('One')
	case  _: # error as case _ should be at last
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')


# Find  outputs  (Home  work)
m = 2
match  m: 
	case  1:
		print('One')
	case  _: # error as there are two _
		print('Hello')
	case  _:
		print('Bye')
print('End')




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

'''
Hyd
Bye
'''


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

'''
Book
Bye
'''


'''
1) What  are  the  outputs  if  input  is  -6 ? --->  Hyd <next line> Sec <next line> Cyb <next line> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One <next line> Two <next line> Three <next line> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India <next line> China <next line> Usa <next line> Bye
4) What  are  the  outputs  if  input  is  0  ?  --->  Hyd <next line> Sec <next line> Cyb<next line> Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One <next line> Two <next line> Three <next line> Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd <next line> Sec <next line> Cyb <next line> Bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> not a point
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> not a point
8) What  is  the  output  when  input  is  ()  ?  ---> not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> not a point
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
		print('Not  a  point')


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
	case 0:
		cost = units * 3.00
	case 1:
		cost = 100 * 3.00 + (units - 100) * 3.50
	case 2 | 3:
		cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
	case 4 | 5 | 6:
		cost = 100 * 3.00 + 100 * 3.5 + 200 * 4.00 + (units - 400) * 4.50
	case _:
		cost = 100 * 3.00 + 100 * 3.5 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00	
print(f'Total bill : {cost}')


'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop

Enter  value  of  x  :  10
Fibonacci  Series
0
1
1
2
3
5
8
'''
x = int(input('Till which number you want : '))
a = 0
b = 1
print('Fibanoci Series')
print(a)
print(b)
c = a + b
while x >= c:
	print(c)
	a = b
	b = c
	c = a + b


#  Find  outputs
while  True:
	print('Hello')
print('Bye')

'''
infinite loop
Hello infinite times
'''


#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye


# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in [10 , 20 , 15 , 18]:
	print(x)
print()
# How  to  print  each  character  of   string  'Hyd'  with  for  loop
for x in 'Hyd':
	print(x)
print()
# How  to  print  each  element of range(5)  with  for  loop
for x in range(5):
	print(x)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10 <next line> 30 <next line> 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 <next line> 40 <next line> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10 , 20) <next line> (30 , 40) <next line> (50 , 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 <next line> 30 <next line> 50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20 <next line> 30...40 <next line> 50...60
for  x ,  y  in   a:
	print(x , y) # error as there is y 
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # error as default method is keys


# Identify  error  (Home  work)
for  x  in   123:
        print(x) # error as int object is not iterable


# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # nothing
for  x   in  []:
        print(x) # nothing
for  x   in   {}:
        print(x) # nothing
for  x   in   set():
        print(x) # nothing
for  x   in   '': 
        print(x) # nothing
for  x  in  range(10 , 10):
	print(x) # nothing
for  x  in   range():
	print(x) # error as range must have 1 arg
for  x  in   (25): 
	print(x) # error as int object is not iterable


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

'''
1 <space> 1
1 <space> 2
1 <space> 3
1 <space> 4
Hello
2 <space> 1
2 <space> 2
2 <space> 3
2 <space> 4
Hello
3 <space> 1
3 <space> 2
3 <space> 3
3 <space> 4
Hello
Bye
'''


# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
# How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
	print(a[i])
print('For each loop')
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for i in a:
	print(i)


#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
# How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(1 , len(a) + 1):
	print(a[-i])
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for x in reversed(a):
	print(x)


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
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for i in range(min(len(a) , len(b))):
	c . append(a[i] + b[i])
print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
for x in a:
	if i < len(b):
		c . append(x + b[i])
		i += 1 
print('3rd  list : ' , c)


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2 , 5):
	print(a[i])
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice



#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # [11 , 21 , 16 , 18]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # [11 , 21 , 16 , 19]
