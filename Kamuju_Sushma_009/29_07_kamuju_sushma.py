#Home Work-1
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''
year=int(input("Enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} is leap year' )
        else:
            print(f'{year} is  not leap year' )
    else:
            print(f'{year} is  leap year' )
else:
            print(f'{year} is  not leap year' )

#Home Work-2
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a=eval(input("Enter 1st element: "))
b=eval(input("Enter 2nd element: "))
c=eval(input("Enter 3rd element: "))
if(a>b and a>c):
      print(f'{a} is the largest')
elif b>c:
      print(f'{b} is the largest')
else:
      print(f'{c} is the largest')     

#Home Work-3
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
x=eval(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius: "))
if x==1:
      c=eval(input("Enter  celsius  temperature :  "))
      print(f'Fahrenheit  Equivalent  : {1.8*c+32}')
elif x==2:
      f=eval(input("Enter  fahrenheit  temperature : "))
      print(f'celsius  Equivalent  : {(f-32)/1.8}')
else:
      print("Invalid Input")

#Home Work-3
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

x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))
if x==0 and y==0:
	print("Origin")
elif x==0 and y!=0:
	print("y-axis")
elif x!=0 and y==0:
	print("x-axis")
elif x>0 and y>0:
	print("1st quadrant")
elif x<0 and y>0:
	print("2nd quadrant")
elif x<0 and y<0:
	print("3rd quadrant")
elif x>0 and y<0:
	print("4th quadrant")

#Home Work-4
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
a=eval(input("Enter 1st value: "))
b=eval(input("Enter 2nd value: "))
c=eval(input("Enter 3rd value: "))
l=[]
l.append(a)
l.append(b)
l.append(c)
max=l[0]
min=l[0]
mid=l[0]
for i in range(1,len(l)):
	max=max(max,l[i])
	min=min(min,l[i])
mid=l[0]+l[1]+l[2]-max-min

#Home Work
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
a=float(input("1st side: "))
b=float(input("1nd side: "))
c=float(input("3rd side: "))
if(a+b>c  and b+c >a and a+c>b):
	print("Can form triangle")
if(a==b and b==c):
	print(f'Area of equilateral Triangle {(math.sqrt(3)/4)*a*a}')
elif ((a==b and a!=c) or (a==c and a!=b) or (b==c) and b!=a):
	print(f'perimeter of isoceles triangle {a+b+c}')
else:
	print(f'perimeter: {a+b+c}')
	s=(a+b+c)/2
	area=math.sqrt(s*(s-a)*(s-b)*(s-c))
	print(f'Area: {area}')
	
#Home Work
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

# output is just Bye , because there is no case for 4, so no case will be executed

#Home Work
# Identify  Error
# i = 2
# match  i:
# 	case  1:
# 		print('One')
# 	case  _:
# 		print('None of   the  above')
# 	case  2:
# 		print('Two')
# print('Bye')
# case _ should be at the end of the match not anywhere in middle

#Home Work
# Find  outputs  (Home  work)
# m = 2
# match  m:
# 	case  1:
# 		print('One')
# 	case  _:
# 		print('Hello')
# 	case  _:
# 		print('Bye')
# print('End')
# case _ should be at the end of the match not anywhere in middle

#Home Work
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
#output: Hyd <new line> Bye

#Home Work
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
#output: Book <new line> Bye

#Home Work
'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd <nl> Sec <nl> Cyb 
2) What  are  the  outputs  if  input  is  15  ?  --->One<nl>Two<nl> Three
3) What  are  the  outputs  if  input  is  10.8  ?  --->India<nl> China <nl> Usa
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd <nl> Sec <nl> Cyb 
5) What  are  the  outputs  if  input  is  -10  ?  --->India<nl> China <nl> Usa
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd <nl> Sec <nl> Cyb 
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

#Home Work
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
		
#Error, we should use object only not reference

#Home Work
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
units = int(input('Enter units: '))

match units // 100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print(cost)

#Home Work
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
x=int(input("Enter  value  of  x  : "))
a=0
b=1
c=a+b
print("Fibonacci  Series")
print(a)
print(b)
while(c<=x):
       print(c)
       a=b
       b=c
       c=a+b

#Home Work
#  Find  outputs
while  True:
	print('Hello')
print('Bye')
#output: Hello <new line>Hello<nl>.... infinite times

#Home Work
#  Find  outputs
while  False:
	print('Hello')
print('Bye')
#Output: Bye , as while loop wont be executed

#Home Work
# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
l=[10,20,15,18]
for x in l:
       print(x)
# print()
# How  to  print  each  character  of   string  'Hyd'  with  for  loop
s='Hyd'
for x in s:
       print(x)
# print()
# How  to  print  each  element  of   range(5)  with  for  loop
for x in range(5):
       print(x)

#Home Work
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
#10 <nl> 30 <nl> 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
#20 <nl> 40 <nl> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
# (10,20) <nl> (30, 40) <nl> (50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
#10 <nl> 30 <nl> 50

#Home Work
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') 
#output: 10...20 <new line> 30...40<nl> 50...60
for  x ,  y  in   a:
	print(x , y)
#output: 10 20 <nl> 30 40 <nl> 50 60
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
#output: 10...20 <new line> 30...40<nl> 50...60

#Home Work
# Identify  error  (Home  work)
for  x  in   123:
        print(x)
#cannot itertate over non sequences

#Home Work
# Find  outputs  (Home  work)
for  x   in   ():
        print(x) #not executed, because empty tuple
for  x   in  []:
        print(x) #not executed, because empty list
for  x   in   {}:
        print(x) #not executed, because empty dictionary
for  x   in   set():
        print(x) #not executed, because empty set
for  x   in   '':
        print(x) #not executed, because empty string
for  x  in  range(10 , 10):
	print(x) #not executed, because empty range
for  x  in   range():
	print(x) #not executed, because empty range
for  x  in   (25):
	print(x) #not executed, because it is treated as non sequences not as a tuple because of missing ',' which is mandatory
	
#Home Work
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
#output
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
# Bye

#Home Work
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
# print('Indexed  based  for loop')
# How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
	print(i,a[i])
# print('For each loop')
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for x in a:
	for i in range(len(a)):
		if x==a[i]:
			print(x,i)
			
#Home Work
#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
# How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(1,len(a)+1):
	print(a[-1*i])
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

#Home Work
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
res1=[]
res2=[]
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
n=len(a)
m=len(b)
t=min(n,m)
for i in range(t):
	res1.append(a[i]+b[i])
print(res1)
# print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
a=[1,2,3,4]
b=[5,6,7]
res2=[]
n=len(a)
m=len(b)
if n>m:
    for x in b:
        res2.append(x)
    for i in range(len(res2)):
        res2[i]+=a[i]
else:
    for x in a:
        res2.append(x)
    for i in range(len(res2)):
        res2[i]+=b[i]
print(res2)

#Home Work
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
	print(a[i])
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
temp=[]
for i in range(2,4):
	temp.append(a[i])
for x in temp:
	print(x)
#Home Work
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) #[11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #[10, 20, 15, 18]