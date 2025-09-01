'Gopi Chandu'
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''
year=int(input("enter a year:"))
if(year%4==0 and (year%100!=0 or year%400==0)):
    print("leap year")
else:
    print("not leap year")
	
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a=eval(input("enter a 1st value:"))
b=eval(input("enter a 2nd value:"))
c=eval(input("enter a 3rd value:"))
if (a>b and a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

n=int(input("enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :"))
match n:
    case 1:
        temp=int(input("Enter  celsius  temperature : "))
        print(1.8 * temp + 32)
    case 2:
        temp=int(input("Enter  celsius  temperature : "))
        print(round((temp - 32) / 1.8,2))
    case _:
        print("Invalid")

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
x=int(input("enter x axis:"))
y=int(input("enter y axis:"))
if(x==0 and (y>0 or y<0)):
    print("'x'  is  0  and  'y'  is  non-zero")
elif(y==0 and (x>0 or x<0)):
    print("'y'  is  0  and  'x'  is  non-zero")
elif(x==0 and y==0):
    print("Both  are  zeroes")
elif( x>0 and y>0):
    print("Both  are  +ve")
elif(x<0 and y<0):
    print("Both  are  -ve")    
elif(x<0 and y>0):
    print("'x'  is  -ve  and  'y'  is  +ve")
elif(x>0 and y<0):
    print("'x'  is  +ve  and  'y'  is  -ve")

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
a= eval(input("Enter  first  input   :))
b = eval(input("Enter  second   input   :))
c = eval(input("Enter  third   input   :))
max_val =  a
min_val =  a
if(b>c and b>max_val):
    max_val=b
elif(c>max_val):
    max_val=c
if(b<min_val and b<c):
    min_val=b
elif(c<min_val):
    min_val=c

mid = ((a+b+c) - (max_val+min_val))
print("Largest number : ",max_val) 
print("Smallest number : ",min_val)
print("Mid number : ",mid)

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
from math import *
x=int(input("enter first side of triangle:"))
y=int(input("enter secong side of triangle:"))
z=int(input("enter third side of triangle:"))
if (x + y > z) and (x + z > y) and (y + z > x):
    if(x==y and y==z):
        print("equilateral  triangle  All  the  three  sides  should  be  same")
        print(" area  of  equilateral  triangle ",  sqrt(3) / 4 * x ** 2)
    elif(x==y or y==z or x==z):
        print("isoscles  triangle Any  two  sides  are  same")
        print(" perimeter    of  isoscles  triangle ",  x+y+z)
    elif(x!=y and y!=z and x!=z):
        print("scalene    triangle Any  two  sides  are  same")
        s = (x+y+z) / 2
        print("area  of  scalene  triangle",sqrt(s * (s - x) * (s - y) * (s - z)))
        print(" perimeter    of  scalene    triangle ",  x+y+z)
else:
    print("Not a valid triangle – the sum of any two sides must be greater than the third.")

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
from math import *
a=int(input("enter value:"))
b=int(input("enter value:"))
c=int(input("enter value:"))
if a==0:
    print("x should not be 0 in quadratic equation")
else:
    disc= b **2 -(4*a*c)
    print(disc)
    if(disc>0):
        print("  Real  and  distinct")
        root1=(-b + sqrt(disc)) / (2*a)
        root2=(-b -sqrt(disc)) / (2*a)
        print(f"root1:{root1} and root2:{root2} ")
    elif(disc==0):
        print("Real  and  same")
        root= -b / (2*a)
        print("root value",root)
    else:
        print("Complex  (or)  Imaginary  roots")
        real_part= -b / (2*a)
        imag_part= sqrt(-disc) / (2*a)
        print("Root 1:", complex(real_part, imag_part))
        print("Root 2:", complex(real_part, -imag_part))
        
        
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)
2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
from math import *
x=int(input("enter x value:"))
y=int(input("enter x value:"))
raidus= float(input("Enter radius of circle: "))
distance = sqrt(x ** 2 + y ** 2)
print("Distance between origin and point (x, y):", distance)
if distance < raidus:
    print("inside the circle")
elif(distance==raidus):
    print("on the circle")
else:
    print("outside of the circle")

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')   # Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') # _ not write it in between

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')  # Hello <nxt line> End

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')  #Hyd <nxt line> Bye

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
print('Bye')  #Book <nxt line> Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->#Hyd <NL> Sec <NL> Cyb <NL> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> #One <NL> Two <NL> Three <NL> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> #India <NL> China <NL> Usa <NL> Bye
4) What  are  the  outputs  if  input  is  0  ?  --->#Hyd <NL> Sec <NL> Cyb <NL> Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> #One <NL> Two <NL> Three <NL> Bye
6) What  are  the  outputs  if  input  is  7  ?  --->#Hyd <NL> Sec <NL> Cyb <NL> Bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> # Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> # x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> #y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> #Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> #Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> # Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> #y - axis
8) What  is  the  output  when  input  is  ()  ?  --->#Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---># Quadrant
10) What  is  the  output  when  input  is  (25,) ?  ---> #Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> # Not  a  point
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
		print(cost)
	case 1:
	    cost=100 * 3.00 + (units - 100) * 3.50
	    print(units,cost)
	case 2:
	    cost=100 * 3.00 + 100 * 3.50 +  (units-200) * 4.00
	    print(units,cost)
	case 3:
	    cost=100 * 3.00 + 100 * 3.50 +  100 * 4.00 + (units-400) * 4.50
	    print(cost)
	case 3:
	    cost=100 * 3.00 + 100 * 3.50 +  100 * 4.00 + 100 * 4.50+(units-700)*5.00
	    print(cost)
	case _:
	    print("empty invalid")
				
				
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
n=int(input("enter value"))
if(n==0 or n==1):
    print(n)
else:
    a,b,=0,1
    print(a,end=" ")
    print(b,end=" ")
    c=a+b
    while(c<n):

        print(c,end=" ")
        c=a+b
        a=b
        b=c

#  Find  outputs
while  True:
	print('Hello')
print('Bye')  # infinite Hello

#  Find  outputs
while  False:
	print('Hello')
print('Bye')  # Bye

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
a=[10 , 20 , 15 , 18]  
for i in a:
	print(i)# 10 <next line> 20 <next line> 15 <next line> 18

How  to  print  each  character  of   string  'Hyd'  with  for  loop
a='Hyd'
for i in a:
	print(i)  # H<next line> Y <next line> d  
How  to  print  each  element  of   range(5)  with  for  loop

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)     # 10<next line> 30<next line>50<next line> empty
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20<next line> 40<next line>60<next line> empty
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10,20)<next line> (30,40)<next line>(50,60)<next line> empty
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)  # 10<next line> 30<next line>50
	
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20<next line> 30...40<next line>50...60
for  x ,  y  in   a:
	print(x , y) # error only keys get not values
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # error

# Identify  error  (Home  work)
for  x  in   123:
        print(x) # error not iterable
		
# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # empty
for  x   in  []:
        print(x) # empty
for  x   in   {}:
        print(x) # empty
for  x   in   set():
        print(x) # empty
for  x   in   '':
        print(x) # empty
for  x  in  range(10 , 10):
	print(x) # empty
for  x  in   range():
	print(x) # error
for  x  in   (25):
	print(x)  # error 
	
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #     
	print('Hello')
print('Bye')

output is : 
  1,1
  1,2
  1,3
  1,4
  Hello
  2,1
  2,2
  2,3
  2,4
  Hello
  3,1
  3,2
  3,3
  3,4
  Hello
  Bye
  
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
	print("index is",i)
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
for i in a:
	print(i)
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

for item in enumerate(a):
    print("Index:", item[0], "Element:", item[1])
	
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)-1,-1,-1):
	print(i)
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
a=a[::-1]
for i in a:
print(i)

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
a= [10 , 20 , 15 , 18]

b= [30 , 40 , 35 , 12 , 100 , 200 , 300]
c=min(len(a),len(b))
d=[]
for i in range(c):
	d.append(a[i]+b[i])
    
print(d)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
a = [10, 20, 15, 18]
b = [30, 40, 35, 12, 100, 200, 300]

c = []

for item in enumerate(a):
    c.append(item[1] + b[item[0]])

print("Result list c:", c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2, 5):  
    print(a[i])
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
a=a[2:5]
for i in (a):
    print(i)

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)
a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]
