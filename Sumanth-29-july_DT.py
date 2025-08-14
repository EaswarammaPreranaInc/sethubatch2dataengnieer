'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''
# Program
a=int(input("Enter any year"))
if (a%4==0 and a%100 !=0) or a%400==0:
  print(a,"Is a Leap Year")
else:
  print(a,"Not a Leap Year")


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
# Program
a=eval(input("Enter 1st input"))
b=eval(input("Enter 2nd input"))
c=eval(input("Enter 3rd input"))
if a>b and a>c:
  print("Largest Value :",a)
elif b>a and b>c:
  print("Largest Value :",b)
else:
  print("Largest Value :",c)



'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
a=int(input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius :"))
if a==1:
  cel=float(input("Enter Celsius Temperature :"))
  fah=1.8 * cel + 32
  print("Fahrenheit Eqvivalent :",fah)
elif a==2:
  fah=float(input("Enter Fahrenheit Temperature :"))
  cel=(fah-32)/1.8
  print("Celsius Eqvivalent :",cel)
else:
  print("Invaild Number")
  
Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0
Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78
Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input


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
# Program 
X=float(input("Enter X-Coordinte :"))
y=float(input("Enter y-Coordinte :"))
if x>0 and y>0:
  print(x,y,"Values are in 1st Quardrant :")
elif x<0 and y>0:
   print(x,y,"Values are in 2nd Quardrant :")
elif x<0 and y<0:
   print(x,y,"Values are in 3rd Quardrant :")
elif x>0 and y <0:
   print(x,y,"Values are in 4th Quardrant :")
elif x==0 and y!=0:
   print(x,y,"Values are on Y-axis:")
elif x!=0 and y==o:
   print(x,y,"Values are on X-axis :")
elif x==0 and y==0:
   print(x,y,"Values are at the Origin :")
else:
  print("Invalid Coordinates")



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
# Program
a=float(input("Enter first input :"))
b=float(input("Enter second input :"))
c=float(input("Enter third input :"))
max_value=a
min_value=a
if b>max_val:
  max_value=b
if c>max_val:
  max_val=c
if b>min_val:
  min_val=b
if c>min_val:
  min_value=c
mid=(a+b+c)-(max_val+min-val)
print("Largest Number",max_val)
print("Smallest Number",min_val)
print("Middle Number",mid)

Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0


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
# Program
import math
a=float(input("Enter side a :"))
b=float(input("Enter side b :"))
c=float(input("Enter side c :"))
if a+b>c and b+c>a and c+a>b:
  print("The sides form a Triangle")
  if a==b==c:
    print("It is a Equilateral Triangle")
    area=(math.sqrt(3/4) * a**2
    print(F" Area={area:.2f}")
  elif a==b or b==c or c==a:
    print("It is a Isosceles Triangle")
    peri=a+b+c
    print(F" Perimeter={peri:.2f}")
  else:
    print("It is Scelene Triangle")
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    peri=a+b+c
    print(F" Area={area:.2f}")
    print(F" Perimeter={peri:.2f}")
else:
  print("The sides do not form a triangle")
    

        
        
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
# Program
import math
a=int(input("Enter co-efficient of x^2 :"))
b=int(input("Enter co-efficient of x :"))
c=int(input("Enter co-efficient of constant :"))
d=b*b-4ac
if d==0:
  print("Roots are Real and Same")
  x1=x2=-b/2a
  print("Roots are x1=",x1,"x2=",x2)
elif d>0:
  print("Roots are Real and Distinct")
  x1=(-b+math.sqrt(d))/2*a
  x2=(-b-math.sqrt(d))/2*a
  print("Roots are x1=",x1,"x2=",x2)
elif d<0:
  print("Roots are Complex or Imaginary :")
  real=-b/2*a
  imag=math.sqrt(-d)/2*a
  print("Roots are x1=",real+imag *j,"x2=",real-imag *j)
else:
  print("Invalid Number")



'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
# Program
import math
x=int(input("Enter x Value :"))
y=int(input("Enter y Value :"))
c=float(input("Enter Radius :"))
d=math.sqrt(x*x+y*y)
if d>r:
  print(x,y,"Points Outside The Circle")
elif d==r:
  print(x,y,"Points On The Circle")
elif d<r:
  print(x,y,"Points Inside The Circle")
else:
  print("Invalid Number")
  

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

# 'Bye'

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: # Error
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _: # Error
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

# 'Hyd'
# 'Bye'


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

# 'Book'
# 'Bye'


# Program
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
1) What  are  the  outputs  if  input  is  -6 ? --->
# 'Hyd'
# 'Sec'
# 'Cyb'
2) What  are  the  outputs  if  input  is  15  ?  --->
# 'One'
# 'Two'
# 'Three'
3) What  are  the  outputs  if  input  is  10.8  ?  --->
# 'India'
# 'China'
# 'Usa'
4) What  are  the  outputs  if  input  is  0  ?  --->
# 'Hyd'
# 'Sec'
# 'Cyb'
5) What  are  the  outputs  if  input  is  -10  ?  --->
# 'One'
# 'Two'
# 'Three'
6) What  are  the  outputs  if  input  is  7  ?  --->
# 'Hyd'
# 'Sec'
# 'Cyb'
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->
# 'Quadrant'
2) What  is  the  output  when  input  is  (10 , 0) ?  --->
# 'x-axis'
3) What  is  the  output  when  input  is  (0 , -20) ?  --->
# 'y-axis'
4) What  is  the  output  when  input  is  (0 , 0) ?  --->
# 'Origin'
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->
# Error
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->
# "Quadrant"
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->
# "y-axis"
8) What  is  the  output  when  input  is  ()  ?  --->
# 'Not a Quadrant'
9) What  is  the  output  when  input  is  {10 , 20} ?  --->
# "Quadrant"
10) What  is  the  output  when  input  is  (25,) ?  --->
# Error
11) What  is  the  output  when  input  is  {10 : 20} ?  --->
# Error
'''

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
# Program
units = int(input('Enter  units :   ')) 
match  units // 100:
   case  0:
				cost = 100 * 3.00
        print(units,"Bill Amount",cost)
   case 1:
        cost = 100 * 3.00 + (units-100) * 3.50
        print(units,"Bill Amount",cost)
   case 2|3:
        cost = 100 * 3.00 + 100 * 3.50 + (units-200) * 4.00
        print(units,"Bill Amount",cost)
   case 4|5|6:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50
        print(units,"Bill Amount",cost)
   case _:
         cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 400) * 4.50 + (units-700) * 5.00
         print(units,"Bill Amount",cost)

      

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
# Program
x=int(input("Enter integer Number :"))
a=0
b=1
c=a+b
print(a,b,end="")
while c<x:
  print(c,end="")
  a=b
  b=c
  c=a+b
  
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
# 'Hello'
# 'Bye'

#  Find  outputs
while  False:
	print('Hello')
print('Bye')

# 'Bye'

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
# Program
list=[10 , 20 , 15 , 18] 
for x in list:
  print(x)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
# Program
str=input("Enter any String :")
for i in range(len(str)):
     print(i)

How  to  print  each  element  of   range(5)  with  for  loop
# program
for i in range(5):
     print(i)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10,30,50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20,40,60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # {(10:20),(30:40),(50:60)}
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # {10 : 20 , 30 : 40 , 50 : 60}


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') 
for  x ,  y  in   a: # Error
	print(x , y
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}: # Error
	print(x , y , sep = '...')
# 10...20
# 30...40
# 50...60


# Identify  error  (Home  work)
for  x  in   123: # Error
        print(x)

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # ()
for  x   in  []:
        print(x) # []
for  x   in   {}:
        print(x) {}
for  x   in   set():
        print(x) # set()
for  x   in   '':
        print(x) # ''
for  x  in  range(10 , 10): # Error
	print(x)
for  x  in   range():
	print(x) # "Empty Range Elements"
for  x  in   (25): # Error
	print(x)

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
      print(i ,  j)  
	print('Hello')
print('Bye')
# 1 1
# 1 2
# 1 3
# 1 4
# Hello
# 2 1
# 2 2
# 2 3
# 2 4
# Hello
# 3 1
# 3 2
# 3 3
# 3 4
# Hello
# Bye


# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
      print(i,a[i])
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
a = [25 , 10.8 , 'Hyd' , True]
print('For each loop')
for x in a :
   print(x)
   
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable) # not possible

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(1,len(a)+1):
    print((-i),a[-i])
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice) # not possible


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
# program
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
small=min(len(a),len(b))
for i in range(small):
    c.append(a[i] + b[i])
    print("3rd list :",c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable) # not possible

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
# program
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,5):
    print(a[i])
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice # not possible

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a:[11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b:[10,20,15,18]
