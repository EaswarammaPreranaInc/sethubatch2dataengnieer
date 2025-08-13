'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''



year=int(input("enter  year : "))
if year%4==0 and (year%400==0 or year%100!=0):
   print(year ,"is a leap Year")
else:
   print(year ,"is not a leap year")

'''
Write  a  program  to  determine  largest  of  three  numbers 
with  if  and  else

Hint:  Write  multiple  conditions
'''

a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
c=int(input("enter 3rd num: "))
if a>b and a>c:
   print(f"{a} is largest number")
elif b>c:
   print(f"{b} is largest number")
else:
   print(f"{c} is largesrt number")

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? 
--->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  
--->  (temp - 32) / 1.8

Enter  1  to  convert  celsius  to  farenheit  
and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0
 Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2

Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78
[29-07-2025 11:10 AM] +91 99482 50500: Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input
'''

value=eval(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))
if value==1:
   cel=eval(input("enter celsius teperture: "))
   far=(1.8*cel)+32
   print(f"fahrenheit equvalent: {far:.2f}")
elif value==2:
   far=eval(input("enter farrenheit teperture: "))
   cel=(far-32)/1.8
   print(f"celsius equivalent: {cel:.2f}")
else:
   print("invalid input")

'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  
            --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?
              --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  
            ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?
              --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ? 
             ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ? 
             --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ? 
             --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''

x=int(input("enter 'x' +ve or -ve value: "))
y=int(input("enter 'y' +ve or -ve value: "))
if x>0 and y>0:
   print(f"{x,y} 1st quadrant")
elif x<0 and y>0:
   print(f"{x,y} 2nd quadrant")
elif x<0 and y<0:
   print(f"{x,y} 3rd quadrant")
elif x>0 and y<0:
   print(f"{x,y} 4th quadrant")
elif x==0 and y!=0:
   print(f"{x,y} values on y-axis")
elif x!=0 and y==0:
   print(f"{x,y} values on x-axis")
else:
   print("values points on origin")



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

Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0
'''


a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
c=int(input("enter 3rd num: "))
max_val=a
min_val=a
if b>max_val:
   max_val=b
if c>max_val:
   max_val=c

if b<min_val:
   min_val=b
if c<min_val:
   min_val=c

mid=(a+b+c)-(max_val+min_val)
print("largest: ",max_val)
print("samllest: ",min_val)
print("mid: ",mid)

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
a=int(input("enter 1st length: "))
b=int(input("enter 2nd length: "))
c=int(input("enter 3rd length: "))
if a+b>c and b+c>a and a+c>b:
   if a==b==c:
      equ_tri=(math.sqrt(3)/4)*(a**2)
      print(f"area of equilateral triangle is: {equ_tri:.2f}")
   elif a==b or b==c or c==a:
      iso_tri=a+b+c
      print(f"perimeter of isosceles triangle is: {iso_tri}")
   else:
      s=(a+b+c)/2
      s_area=math.sqrt(s*(s-a)*(s-b)*(s-c))
      s_peri=a+b+c
      print(f"area of scalene triangle is: {s_area:.2f}")
      print(f"perimeter of scalene triangle is: {s_peri}")
else:
   print("enter valid lengths")

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
import cmath
a=int(input("enter 1st value: "))
b=int(input("enter 2nd value: "))
c=int(input("enter 3rd value: "))

disc=(b**2) - (4*a*c)
if disc>0:
   print("real and distinct")
   root1=(-b+math.sqrt(disc))/(2*a)
   root2=(-b-math.sqrt(disc))/(2*a)
   print(f"root1 is:{root1}")
   print(f"root2 is:{root2}")
   

elif disc==0:
   print("real and same")
   root=-b/(2*a)
   print(f"root is: {root}")
else:
   print("complex or imaginary roots")
   real=-b/(2*a)
   imag=math.sqrt(-disc)/(2*a)
   root1=(-b+cmath.sqrt(disc))/(2*a)
   root2=(-b-cmath.sqrt(disc))/(2*a)
   print(f"real part: {real}")
   print(f"imaginary part: {imag:.2f}")
   print(f"root1 is:{root1}")
   print(f"root2 is:{root2}")



'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math
r=int(input("enter R value: "))
x=int(input("enter x value: "))
y=int(input("enter y value: "))
dist=math.sqrt((x**2)+(y**2))
if dist>r:
   print("outside the circle")
elif dist<r:
   print("inside the circle")
else:
   print("On the circle ")

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
	case  _:   #unnonamous must be last case in match fun
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')  #Error because there is 2 unnonamous 

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')    # Hyd Bye because when ever match found it print and  leave the rest of the cases


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
print('Bye')   #Book Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->    #Hyd <nl> Sec <nl> Cyb <nl> Bye
2) What  are  the  outputs  if  input  is  15  ?  --->   One <nl> Two <nl> Three <nl> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->  India <nl> China <nl> Usa <nl> Bye
4) What  are  the  outputs  if  input  is  0  ?  --->  #Hyd <nl> Sec <nl> Cyb <nl> Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->  One <nl> Two <nl> Three <nl> Bye
6) What  are  the  outputs  if  input  is  7  ?  --->  #Hyd <nl> Sec <nl> Cyb <nl> Bye
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
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop
'''   

n=int(input("enter n number: "))
print("fibbinoci serie")
a=0
b=1
print(a)
print(b)
while a+b<=n:
     c=a+b
     a=b
     b=c
     print(c)


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
match units // 100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 3:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case 4:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
print(f'Bill  amount  is :  {cost:.2f}') 

                        
               

#  Find  outputs
while  True:
	print('Hello')
print('Bye') #Hello prints never stops

#  Find  outputs
while  False:
	print('Hello')
print('Bye') #Bye

# Find  outputs  (Home  work)
'''How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()'''
lst=[10,20,15,18]
for i in lst:
     print(i)

'''How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()'''
for ch in 'Hyd':
   print(ch)

'''How  to  print  each  element  of   range(5)  with  for  loop'''
for i in range(5):
   print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)  #10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)  #(10,20) (30,40) (50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)  #10 30 50
     
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x ,  y  in   a:
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
     

# Identify  error  (Home  work)
for  x  in   123:
        print(x) #Error because 123 is int we must use ref there 

# Find  outputs  (Home  work)
for  x   in   ():
        print(x)# Empty tuple
for  x   in  []:
        print(x) # Empty list
for  x   in   {}:
        print(x)  # Empty dict
for  x   in   set():
        print(x)  # Empty set
for  x   in   '':    
        print(x)   #Empty string
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)  # range obj atleast  contain a single arg 
for  x  in   (25):
	print(x)    # int obj is not be iterable
      

      #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')         #1,1 1,2 1,3 1,4 Hello ............3,4 Hello Bye


# How  to  print  each  element  and  the  corresponding  index
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
   print(f'Index: {i}, Element: {a[i]}')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
print('For each loop')
for element in a:
   print(f'Element: {element}')

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
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for i in range(len(a)):
   c.append(a[i] + b[i])
print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')

#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2, 5):
   print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
for 

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)   #[11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1 #[   10, 20, 15, 18] because x is not a reference to b
print('b :  ' ,  b)



'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> #Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> #x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> #y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->#origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> #Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> #Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> #y - axis
8) What  is  the  output  when  input  is  ()  ?  ---> #Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->  #Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->    #Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> #Not  a  point
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