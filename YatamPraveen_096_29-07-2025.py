'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''

a=int(input('Enter the year'))
if (a%4==0 and a%100!=0) or a%400==0:
      print('Leap Year')
else:
      print('Not a leap year')




'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a, b, c=int(input('Enter the 1st number : ')),int(input('Enter the 2nd number : ')),int(input('Enter the 3rd number : '))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)




Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

a=int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :'))
match a:
  case 1:
      c=int(input('Enter  celsius  temperature :'))
      f=1.8 * c + 32   
      print(f'Fahrenheit  Equivalent  : {f}')
  case 2:
      f=int(input('Enter  farenheit  temperature :'))
      c=(f - 32) / 1.8
      print(f'Celsius  Equivalent  : {c:.2f}')
  case _:
      print('Invalid input')




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

a, b= int(input('enter the 1st coordinate : ')), int(input('enter the 2nd coordinate : '))
if a>0 and b>0:
  print('1st quadrant')
elif a<0 and b>0:
  print('2nd quadrant')
elif a<0 and b<0:
  print('3rd quadrant')
elif a>0 and b<0:
  print('4th quadrant')
elif a==0 and b!=0:
  print('Lies on Y-axis')
else:
  print('Lies on X-axis')




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

a=int(input('Enter first input : '))
b=int(input('Enter seconf input : '))
c=int(input('Enter third input : '))
l=max(a,b,c) 
s=min(a,b,c)
m=(a+b+c)-(l+s)
print('Largest number : ',l)
print('Smallest number : ',s)
print('Middle number :  ',m)




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

a=int(input('Enter the length of first side : '))
b=int(input('Enter the length of second side : '))
c=int(input('Enter the length of third side : '))
if a+b>c and a+c>b and b+c>a:
  if a==b and b==c:
    print('It is an equilateral triangle')
    print('Area : ',(3*0.5) /( 4 * (a * 2)))
  elif a==b or b==c or c==a: 
    print('It is an isosceles triangle')
    print('perimeter : ',a+b+c) 
  else:
    s=(a + b + c) / 2
    ar=(s * (s - a) * (s - b) * (s - c))**0.5
    print('It is a scalene triangle')
    print('perimeter : ',a+b+c)
else: 
  print('It is not a triangle')




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


a=int(input('Enter the value of a (It must not be 0) : '))
b=int(input('Enter the value of b : '))
c=int(input('Enter the value of c : '))
d=b ** 2 - (4*a*c)
if d>0:
  print('The roots are real and distinct')
  print(f'The roots are : {(-b + d*0.5) / (2*a)} and {(-b - d*0.5) / (2*a)}')
elif d==0:
  print('The roots are real and same')
  print(f'The roots are : {-b/(2*a)} and {-b/(2*a)}')
else:    
  print('The roots are Imaginary')
  rp= -b / (2*a)
  ip= (-d)**0.5 / (2*a)
  print(f'The roots are : {rp}+{ip}j and {rp}-{ip}j')





'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

a= int(input('enter the 1st coordinate : '))
b= int(input('enter the 2nd coordinate : '))
r=int(input('Enter the radius of the circle : '))
d= (a * 2 + b * 2)**.5
if d>r:
  print('The point lies outside the circle')
elif d<r:
  print('The point lies inside the circle')
else:
  print('The point lies on the circle')




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

#prints Bye as no case is matched and the default line which prints bye is executed




# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:                         #this case in this position causes error
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')




# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:                        #this case in this position causes error
		print('Hello') 
	case  _:
		print('Bye')
print('End')




#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')            #Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')                            #Bye




# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')                #Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')                                    #Bye




'''
1) What  are  the  outputs  if  input  is  -6 ? --->     #prints Hyd, Sec and Cyd and  finally Bye
2) What  are  the  outputs  if  input  is  15  ?  --->     #prints One, Two and Three and  finally Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->     #prints India China and USA and  finally Bye
4) What  are  the  outputs  if  input  is  0  ?  --->     #prints Hyd, Sec and Cyd and  finally Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->     #prints One, Two and Three and  finally Bye
6) What  are  the  outputs  if  input  is  7  ?  --->      #prints Hyd, Sec and Cyd and  finally Bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->    #Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->       #x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->      #y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->        #Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> #Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->     #Not  a  point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->     #Not  a  point
8) What  is  the  output  when  input  is  ()  ?  --->            #Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->      #Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->         #Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->     #Not  a  point
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

a = int(input('Enter the number of units : '))
match  a // 100:
  case 0:
    cost = a*3
  case 1:
    cost = 100*3 + (a-100)*3.5     
  case 2 | 3:
    cost = 100*3 + 100*3.5 + (a-200)*4
  case 4 | 5 | 6:
    cost = 100*3 + 100*3.5 + 200*4 + (a-400)*4.5
  case _:
    cost = 100*3 + 100*3.5 + 200*4 + 300*4.5 + (a-700)*5 
print('Bill amount is : ',cost)




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

l=int(input('Enter the series limit : '))
a,b=0,1
c=a+b
print(a)
print(b)
while c<l:
  print(c)
  a,b=b,c
  c=a+b




#  Find  outputs
while  True:
	print('Hello')          3since there is no end condition, Hello goes on printing continuously
print('Bye')




#  Find  outputs
while  False:
	print('Hello')      #while loop gets ignored as the condition is false
print('Bye')                 #Bye




# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in [10 , 20 , 15 , 18]:
    print(x)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
a='Hyd'
for x in 'Hyd':
    print(x)
How  to  print  each  element  of   range(5)  with  for  loop
for x in range(5):
    print(x)




# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                              #10, 30, 50 in seperate lines
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)                              #20, 40, 60 in seperate lines
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)                              #(10, 20), (30, 40), (50, 60) in seperate lines             
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)                             #10, 30, 50 in seperate lines( because default will be keys




# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')                  #10...20, 30...40, 50...60 in seperate lines
for  x ,  y  in   a:                                   # This causes error as this line implies keys and keys can't be unpacked into two variable
	print(x , y)                            
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:     #Same error as the above
	print(x , y , sep = '...')




# Identify  error  (Home  work)
for  x  in   123:
        print(x)                     #for loop can't iterate through non sequence




# Find  outputs  (Home  work)
for  x   in   ():
        print(x)                      #prints nothing
for  x   in  []:
        print(x)                      #prints nothing
for  x   in   {}:
        print(x)                      #prints nothing
for  x   in   set():
        print(x)                      #prints nothing
for  x   in   '':
        print(x)                      #prints nothing
for  x  in  range(10 , 10):
	print(x)                      #prints nothing
for  x  in   range():
	print(x)                     #returns error as this is not an empty range
for  x  in   (25):
	print(x)                      #returns error as (25) is int not a tuple




#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)
	print('Hello')
print('Bye')

# 
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




# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop

for i in range(len(a)):
     print( a[i], i )

print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

for x in a:
     print( x, a.index(i) )




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

l=min( len(a), len(b) )
for i in range(l):
      c.append( a[i] + b[i] )
print('3rd  list : ' , c)

How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)




#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop

for i in range( 2, 5 ):
      print( a[i] )

How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

for x in a:
      if  1 <= a.index(x)  and   a.index(x)  <=4 : 
      print( x )




#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)                #a :  [11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)                #b :  [10 , 20 , 15 , 18]