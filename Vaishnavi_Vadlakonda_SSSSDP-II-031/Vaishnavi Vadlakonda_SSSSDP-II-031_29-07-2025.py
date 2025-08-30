'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''
a = int(input("Enter year:"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(F'{a} is a leap year')
else:
    print(F'{a} is not a leap year')








'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple conditions
'''
a = eval(input("Enter 1st input:"))
b = eval(input("Enter 2nd input:"))
c = eval(input("Enter 3rd input:"))
if a > b and a > c:
    print(F'{a} is largest number')
else:
    if b > c:
        print(F'{b} is largest number')
    else:
        print(F'{c} is largest number')











'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp-32)/1.8
'''
a = int(input("Enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius:"))
if a == 1:
    celsius = float(input("Enter celsius temperature:"))
    farenheit = 1.8 * a + 32
    print("Farenheit Equivalent:", farenheit)
elif a == 2:
    farenheit = float(input("Enter farenheit temperature:"))
    celsius = (a - 32) // 1.8
    print("Celsius Equivalent:", celsius)
else:
    print("Input should be 1 or 2")











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

8) Hint:  Use  if  ..  elif
'''
x = float(input("Enter 1st input:"))
y = float(input("Enter 2nd input:"))
if x > 0 and y > 0:
    print(F'{x,y} lies in 1st quadrant')
elif x < 0 and y > 0:
    print(F'{x,y} lies in 2st quadrant')
elif x < 0 and y < 0:
    print(F'{x,y} lies in 3rd quadrant')
elif x > 0 and y < 0:
    print(F'{x,y} lies in 4th quadrant')
elif x != 0 and y == 0:
    print(F'{x,y} lies on y axis')
elif x == 0 and y != 0:
    print(F'{x,y} lies on x axis')
else:
    print(F'{x,y} lies on origin')








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

6) Hint : Do  not  use  else  in  the program
'''

a = int(input("Enter first input:"))
b = int(input("Enter second input:"))
c = int(input("Enter third input:"))
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
mid = (a + b+ c) - (max + min)
print("Largest number:",max)
print("Smallest number:",min)
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

5) Hint: Use nested if
'''

import math
a = float(input("Enter 1st input:"))
b = float(input("Enter 2nd input:"))
c = float(input("Enter 3rd input:"))
if a + b > c and  a + c > b and b + c > a:
    print("Given sides form a triangle")
    if a == b:
        if b == c:
            print("It is an Equilateral triangle")
            area = (math.sqrt(3) / 4) * a ** 2
            print(F'Area of Equilateral triangle: {area:.2f}')
            if (a == b and b != c) or (b == c and a != b) or (a == c and b != c):
                print("It is an Isosceles triangle")
                perimeter = a + b + c
                print("Perimeter:",perimeter)
                if a != b and b != c and a != c:
                    print("It is a Scalene triangle")
                    perimeter =  a + b + c
                    s = perimeter / 2
                    area = math.sqrt(s *(s - a) * (s - b) * (s - c))
                    print("Perimeter:",perimeter)
                    print(F"Area: {area:.2f}")
else:
    print("Given sides cannot form a triangl")












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
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("THis is not a quadratic equation(a != 0)")
else:
    disc = b ** 2 - 4*a*c
    print(F'Discriminant = {disc}')
    if disc > 0:
        print("Roots are real and distinct")
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Root1 =",root1)
        print("Root2 =",root2)
    elif disc == 0:
        print("Roots are real and same")
        root = -b / (2 * a)
        print("Root1 = Root2 =", root)
    else:
        print("Roots are complex and imaginary")
        realpart = -b / (2 * a)
        imagpart = math.sqrt(-disc) / (2 * a)
        print(F"Root1 = {realpart:.2f} + {imagpart:.2f}j")
        print(F"Root2 = {realpart:.2f} - {imagpart:.2f}j")













'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math
x = float(input("Enter 1st input:"))
y = float(input("Enter 2nd input:"))
r = float(input("Enter radius of circle:"))
distance = math.sqrt(x * 2 + y * 2)
if distance < r:
    print("The point lies inside the circle")
elif distance > r:
    print("The point lies outside the circle")
else:
    print("The point lies on the circle")










# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three') # prints nothing because there is no case 4
print('Bye')  #prints Bye










# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:    #  Error because case_ should be after all cases but not middle and it does not check cases after this
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
		print('Hello') # Error bacause case_ should not be there in middle of cases
	case  _:
		print('Bye')
print('End')









#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # prints Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # prints Bye









# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') # prints Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') # prints Bye









'''
1) What  are  the  outputs  if  input  is  -6 ? ---> # prints Hyd<nextline>Sec<nextline>Cyb<nextline>
2) What  are  the  outputs  if  input  is  15  ?  ---> # prints One<nextline>Two<nextline>Three<nextline>
3) What  are  the  outputs  if  input  is  10.8  ?  ---> # prints India<nextline>China<nextline>Usa<nextline>
4) What  are  the  outputs  if  input  is  0  ?  ---> # prints Hyd<nextline>Sec<nextline>Cyb<nextline>
5) What  are  the  outputs  if  input  is  -10  ?  ---> # prints One<nextline>Two<nextline>Three<nextline>
6) What  are  the  outputs  if  input  is  7  ?  ---> # prints Hyd<nextline>Sec<nextline>Cyb<nextline>
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd') 
		print('Sec')
		print('Cyb')  # prints Hyd<nextline>Sec<nextline>Cyb<nextline> if input is 7 or -6 or 0
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three') # prints One<nextline>Two<nextline>Three<nextline> if input is -10 or 15
	case  _:
		print('India')
		print('China')
		print('Usa') # prints India<nextline>China<nextline>Usa<nextline> if two cases didnt match
	case  _:
# End  of  match
print('Bye') # Error should be indented with case












'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->
2) What  is  the  output  when  input  is  (10 , 0) ?  --->
3) What  is  the  output  when  input  is  (0 , -20) ?  --->
4) What  is  the  output  when  input  is  (0 , 0) ?  --->
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->
8) What  is  the  output  when  input  is  ()  ?  --->
9) What  is  the  output  when  input  is  {10 , 20} ?  --->
10) What  is  the  output  when  input  is  (25,) ?  --->
11) What  is  the  output  when  input  is  {10 : 20} ?  --->
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case (0 , 0):
		print('Origin')
	case (0 , y):
		print('y - axis')
	case  (x , 0):
		print('x - axis')
	case (x , y):
		print('Quadrant')
	case _:
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
    case 0:  # if input is from 0–99
        cost = units * 3.00
    case 1:  # if input is from 100–199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:  # if input is from 200–399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:  # if input is from 400–699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:  # if input is  from 700 and above
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

3) Hint:  Use while loop
'''
n=int(input("Enter the Integer Number:"))
f1 = 0
f2 = 1
f3 = 0
print("Fibonacci  Series")
while(f3 <= n):
    print(f3)
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    








#  Find  outputs
while  True:
	print('Hello') # prints Hello Infinitely
print('Bye')








#  Find  outputs
while  False:
	print('Hello') 
print('Bye') # prints Bye









# Find  outputs  (Home  work)
for x in [10, 20, 15, 18]:# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop 
    print(x) # prints each element in list
for x in 'Hyd':#How  to  print  each  character  of   string  'Hyd'  with  for  loop  
    print(x) # prints each character in string
for x in range(5):# How  to  print  each  element  of   range(5)  with  for  loop  
    print(x) # prints from 0 to 4 









# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # prints keys in  dictionary i.e., 10<nextline>30<nextline>50
print() # prints nothing and moves to next line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #prints values of dictionary i.e., 20<nextline>40<nextline>60
print() # prints nothing and moves to next line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # prints items in dictionary i.e., (10,20)<nextline>(30,40)<nextline>(50,60)
print() # prints nothing and moves to next line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # prints 10<nextline>30<nextline>50










 # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for x , y  in a.items(): 
	print(x, y, sep = "...") # prints 10...20<nextline>30...40<nextline>50...60
for x , y in a: # Error because by default it takes dict_keys object and it only has one variable
	print(x , y)    # Error because the brace is not closed
for x , y in {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')  # Error because it cannot give key value pairs it can only give keys










# Identify  error  (Home  work)
for  x  in   123:
        print(x)   # Error because int object cannot be traversed









 # Find  outputs  (Home  work)
for  x   in   (): 
        print(x) # No output
for  x   in  []:
        print(x) # No output
for  x   in   {}:
        print(x) # No output
for  x   in   set():
        print(x) # No output
for x in  '':
        print(x) # No output
for x in range(10 , 10):
	print(x) # No output because range is from 10 to 10
for x in range():# Error because atleast 1 argument is mandatory
	print(x) 
for x in (25):
	print(x)   # Error because cannot be traversed through int object









 #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')
''' Outputs
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
'''









# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)): # print('Indexed  based  for loop') 
    print(a[i])
for in range(len(a)): # How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop  
    print(a[i],i)
for x in a:#print('For each loop')   
    print(x)
a = [25 , 10.8 , 'Hyd' , True] #without using 2nd variable means we have to use index based for loop or enumerate function
i = 0
for x in a:
    print(x, i)
    i = i + 1      
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable) 
a = [25 , 10.8 , 'Hyd' , True] #without using 2nd variable means we have to use index based for loop or enumerate function
i = 0
for x in a:
    print(x, i)
    i = i + 1      
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable) 









# How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop  
for i in range(-1,-(len(a)+1),-1):
    print(a[i])   
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
a = [25 , 10.8 , 'Hyd' , True]   #i have used reversed method  for  reversing   
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
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []     
for i in range(len(a)):# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
    c.append(a[i] + b[i])
print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
#index based loop 
for i in range(len(min(a,b))):    
      c.append((l1[i]+l2[i]))
print(c)
#for each loop     #used  new  function zip()
for x, y in zip(a, b):
    c.append(x + y)
print(c)











#index based loop 
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
for i in range(2,5):   
      print(a[i])
#for each loop   # Use enumerate function 
for idx, val in enumerate(a):
    if 2 <= idx < 5:
        print(val)









#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # prints a : [11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:     
	x += 1
print('b :  ' ,  b) #prints b : [10 , 20 , 15 , 18]
