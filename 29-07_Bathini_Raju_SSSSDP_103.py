#BATHINI RAJU
 
 
 
 
 '''

Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''


# Program to check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is Not a Leap Year')






 '''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a >= b and a >= c:
    print(f"The largest number is {a}")
elif b >= a and b >= c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")








 '''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''


 Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0
 Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78
 Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input


# Temperature conversion program

c= int(input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius: "))

if c == 1:
    celsius = float(input("Enter Celsius temperature: "))
    fahrenheit = 1.8 * celsius + 32
    print("Fahrenheit Equivalent:", fahrenheit)

elif c == 2:
    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Celsius Equivalent:",celsius)

else:
    print("Invalid input")


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



# Program to test where a point lies on orgin

x = eval(input("Enter x-coordinate: "))
y = eval(input("Enter y-coordinate: "))

if x == 0 and y == 0:
    print("The point lies at the Origin.")
elif x > 0 and y > 0:
    print("The point lies in the 1st Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the 4th Quadrant.")
elif x != 0 and y == 0:
    print("The point lies on the X-axis.")
elif x == 0 and y != 0:
    print("The point lies on the Y-axis.")







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


#  program to find largest, smallest, and middle of three numbers

a = eval(input("Enter first input: "))
b = eval(input("Enter second input: "))
c = eval(input("Enter third input: "))

max = a
min = a

if b > max:
    max = b
if c > max:
    max = c

if b < min:
    min = b
if c < min:
    min = c

mid = a + b + c - max - min

print("Largest number:", max)
print("Smallest number:", min)
print("Middle number:", mid)








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


a = eval(input("Enter first side: "))
b = eval(input("Enter second side: "))
c = eval(input("Enter third side: "))

if a + b > c and b + c > a and c + a > b:
    print("The sides form a triangle")

    if a == b and b == c:
        print("It is an Equilateral Triangle")
        area = (math.sqrt(3) / 4) * a * a
        print("Area =", area)

    elif a == b or b == c or c == a:
        print("It is an Isosceles Triangle")
        perimeter = a + b + c
        print("Perimeter =", perimeter)

    else:
        print("It is a Scalene Triangle")
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print("Area =", area)
        print("Perimeter =", perimeter)
else:
    print("The sides do notform a triangle")





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

a = float(input("Enter value of a (a != 0): "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    disc = b**2 - 4*a*c
    print("Discriminant =", disc)
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Roots are real and distinct")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif disc == 0:
        root = -b / (2 * a)
        print("Roots are real and same")
        print("Root =", root)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-disc) / (2 * a)
        print("Roots are complex (imaginary)")
        print("Root 1 =", complex(real, imag))
        print("Root 2 =", complex(real, -imag))





 '''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''


import math

r = float(input("Enter radius of the circle: "))
x = float(input("Enter x-coordinate of the point: "))
y = float(input("Enter y-coordinate of the point: "))

distance = math.sqrt(x**2 + y**2)

if distance < r:
    print("The point lies inside the circle.")
elif distance > r:
    print("The point lies outside the circle.")
else:
    print("The point lies on the circle.")





# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  #Bye


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:             #SyntaxError
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
		print('Hello') #SyntaxError
	case  _:
		print('Bye')
print('End')



#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') #Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') #Bye


 
 # Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')#Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') #Bye



 '''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd Sec Cyb Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One Two Three Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India China Usa Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd Sec Cyb Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One Two Three Bye
6) What  are  the  outputs  if  input  is  7  ?  --->  Hyd Sec Cyb Bye
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
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Not a point
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> Not a point
8) What  is  the  output  when  input  is  ()  ?  ---> Not a point 
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Not a point

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




units = int(input("Enter units: "))
cost = 0

match units // 100:
    case 0:  # 0–99
        cost = units * 3.00
    case 1:  # 100–199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:  # 200–399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:  # 400–699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:  # 700 and above
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print("Bill amount = Rs.", cost)



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

 n=int(input("Enter the Integer Number "))

f1=0
f2=1
f3=0
print("Fibonacci  Series")
while(f3<=n):
    f1=f2
    f2=f3
    f3=f1+f2
    print(f3)








#  Find  outputs
while  True:
	print('Hello') # Infinity Hello printed
print('Bye')



 #  Find  outputs
while  False:
	print('Hello') 
print('Bye') #Bye





# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop # for x in list: print(x)
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop  # for x in 'Hyd: print(x)
print()
How  to  print  each  element  of   range(5)  with  for  loop  ## for i in range(5): print(i)



 # Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) #10 30 50
print() #nextLine
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10,20) (30,40) (50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) #10 30 50


 # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items(): 
	print(x , y , sep = '...') #10...20 30...40 50...60
for  x ,  y  in   a:
	print(x , y    #Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')  #Error


 # Identify  error  (Home  work)
for  x  in   123:
        print(x)   #Error


 # Find  outputs  (Home  work)
for  x   in   (): 
        print(x) #No Output
for  x   in  []:
        print(x)#No Output
for  x   in   {}:
        print(x) #No Output
for  x   in   set():
        print(x) #No Output
for  x   in   '':
        print(x) #No Output
for  x  in  range(10 , 10):
	print(x) #No Output
for  x  in   range():# Atleast 1 argument is allowed
	print(x) 
for  x  in   (25):
	print(x)   #Eror




 #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
''' Outputs of above loop
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
Bye '''






 # How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop') # for in range(len(a)): print(a[i])
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop  #  for in range(len(a)): print(a[i],i)
print('For each loop')   # for x in a: print(x)
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable) 

'''a = [25 , 10.8 , 'Hyd' , True] #without using 2nd variable    means   we have to use   indexbased for loop  or enumerate function
 
i=0
for x in a:
    print(x,i)
    i=i+1      ''' 
 
 
 #  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')


How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop  
 '''
for i in range(-1,-(len(a)+1),-1):
    print(a[i]) '''
    
    
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
'''a = [25 , 10.8 , 'Hyd' , True]   #i have used reversed method  for  reversing   
for x in reversed(a):
    print(x)          '''



'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''

l1=list(map(int,input("Enter 1st list Values").split(",")))
l2=list(map(int,input("Enter 2nd list Values").split(",")))

res=[]
for i in range(len(min(l1,l2))):
    
      res.append((l1[i]+l2[i]))
print(res)
   




a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []     
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)


 #index based loop 
for i in range(len(min(a,b))):
    
      c.append((l1[i]+l2[i]))
print(c)


#for each loop     #used  new  function zip()

for x, y in zip(a, b):
    c.append(x + y)

print(c)



   




#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice


 #index based loop 
for i in range(2,5):
    
      print(a[i])


#for each loop   # Use enumerate function 


'''for idx, val in enumerate(a):
    if 2 <= idx < 5:
        print(val)'''




 #  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a : [11 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
for  x  in   b:     
	x += 1
print('b :  ' ,  b) ## b : [10 , 20 , 15 , 18]