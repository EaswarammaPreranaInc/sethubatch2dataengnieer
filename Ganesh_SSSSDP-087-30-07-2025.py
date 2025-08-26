      # outputs
     '''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs
      

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else

'''
    # outputs
        #
       year=int(input('enter a year: '))
       if year % 2 ==0 and year %100 !=0 and year % 400==0:
		print('leap year',year)
       else:
		print('not a leap year')


Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
      # outputs
       a= int(input('enter 1st num: '))
       b= int(input('enter 2nd num: '))
       c= int(input('enter 3rd num: '))
       
       if a>b and a>c:
		print('a is larger')
	else:
		if b>c and b>a:
			print('b is largest',b)
		else:
			print('c is largest',c)

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
    #  Fahrenheit=(1.8×Celsius)+32
	
  

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
	#
		num= int(input('enter a num 1 or 2: '))
                if num==2:
	  		Ftemp=int(input('enter a farenheit temp: ))
	  		celsius=(Ftemp-32)/1.8
	 		print('after celsius: ',celsius)
		elif num==1:
			Ctemp=int(input('enter a celsius temp: '))
			farenhit=1.8*Ctemp+32
			print('farenhit: ',farenhit)
		else:
			print('invalid input')
        
'''


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

    #
	x= int(input('enter x value: '))
	y= int(input('enter y value: '))
	if x>0 and y>0:
		print('1st quadrant')
	elif x< 0 and y > 0:
		print('2nd quadrant')
	elif x< and y< 0
		print('3rd quadrant')
	elif x> 0 and y< 0:
		print('4th quadrant')
	elif x!= 0 and y==0:
		print('x- axis')
	elif x==0 and y!=0:
		print('y axis')
	else:
		print('Origin')


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
   #
	a=int(input('enter 1st value: '))
	b=int(input('enter 2nd value: '))
	c=int(input('enter 3rd value: '))
	l=max(a,b,c)
	s=min(a,b,c)
	m= (a+b+c)-(l+s)
	print('largest: ',l)
	print('smallest: ',s)
	print('middle: ',m)

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
     #
	a= float(input('enter value: '))
	b= float(input('enter value: '))
 	c= float(input('enter value: '))
	if(a+b>c) and (a+c>b) and (b+c>a):
		if a==b and b==c:
			print('it is equlatrail triangle')
			area= (math.sqrt(3)/4) * a * a
			print('area: ',area)
		else:
			if a==b or b==c or c==a:
				print('it is a isolation triangle')
				perimeter=a + b + c
				print('perimeter: ')
			else:
				print('all the side are different')
				perimeter= a+b+c
				s= perimeter/2
				area of ST= sqrt(s * (s-a) * (s-b) * (s-c))
				print('area: ',area)
		else:
			print('Sum  of  every  two  sides  should  be  >  3rd  side')


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

     #
        a= int(input('enter value: '))
	b= int(input('enter value: '))
	c= int(input('enter value: '))
	disc= b**2- 4ac
	if disc> 0:
		print('real and distinct')
		root1= (-b + sqrt(disc)) / 2a
		root2= (-b- sqrt(disc)) / 2a
		print('root1: ',root1)
		print('root2: ',root2)
	else:
		if disc== 0:
			print('roots are real and same')
			root= -b/2a
		else:
			print('complex or imaginary roots)
			realPart= -b/2a
			imgPart= sqrt(-disc)/2a
			root1= complex(realPart)
			root2= complex(imgPart)
			print(root1)
			print(root2)
	
     '''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

    #
	x= eval(input('enter value: '))
        y= eval(input('enter value: '))
	r= eval(input('enter value: '))
	distance= sqrt(x**2+y**2)
	if distance > r:
		print('outside the circle')
	elif distance < r:
		print('inside the circle')
	else
		print('on the circle')


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

     #  the error is case_


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

  #  error is case_


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

   #  
     Hyd
     Sec
     Cyb
     Bye

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

       #
         Book
         Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->
2) What  are  the  outputs  if  input  is  15  ?  --->
3) What  are  the  outputs  if  input  is  10.8  ?  --->
4) What  are  the  outputs  if  input  is  0  ?  --->
5) What  are  the  outputs  if  input  is  -10  ?  --->
6) What  are  the  outputs  if  input  is  7  ?  --->
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

    1.  #
        Hyd
	Sec
	Cyb
    2. #
        One
	Two
	Three
    3.
	India
	China
	Usa

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

     # output
         Quadrant
	 x-axis
	 y-axis
	 Quadrant
	 error
	 Quadrant
	 y-axis
	 Not a point
	 Quadrant
	 Not a point
	 Not a point

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
	case  1:
		cost = 100 *3.00 (unit-100)*3.50
        case  2 | 3:
		cost=100*3.00+100*3.50+(unit-200)+4.00
	case  4 | 5 | 6:
		cost=100*3.00+100*3.50+200*4.00(unit-400)+4.50  
	case_:
		cost=100*3.00+100*3.50+200*4.00+300*4.50(unit-700)+5.00
print(f'bill amount rs: {cost:.2f}')


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
	
	#output
        x=int(input('enter a value upto 10: ')
	a= 0
	b= 1
	while(a<=x):
		print(a,end=',')
		a,b=b,a+b

#  Find  outputs
while  True:
	print('Hello')
print('Bye')

     #output
	Hello
	Hello...

#  Find  outputs
while  False:
	print('Hello')
print('Bye')

    # 
      Bye

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop

   #
     for x in list:
	print(x)

print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop

   # 
     String='Hyd'
     for x in String:
	print(x)
print()
How  to  print  each  element  of   range(5)  with  for  loop

     # 
	for x in range(5):
	      print(x)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)  
# 10 30 50

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)

# 20 40 60

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
# (10 ,20)
  (30, 40)
  (50, 60)

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
   # 10
     30
     50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

  #  10....20
     30....40
     50....60

for  x ,  y  in   a:
	print(x , y)
      # error

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
     #  error

# Identify  error  (Home  work)
for  x  in   123:
        print(x)
    # error


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)   #  empty tuple
for  x   in  []:
        print(x)      #  empty list
for  x   in   {}:
        print(x)       #  empty set
for  x   in   set():
        print(x)       #  empty tuple
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):      #  empty spaces
	print(x)
for  x  in   range():      # error
	print(x)
for  x  in   (25):
	print(x)      # error


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)  #
	print('Hello')
print('Bye')

 # outputs
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

 How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

  #
   a = [25 , 10.8 , 'Hyd' , True]
   for i in range(len(a)):
	print(a[i],'indexs: ',i)
   
   for item in enumerate(a):
	print('indexs: ',item[0],'element: ',item[1])

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

   #outputs
    a= [11, 21, 16, 19]
   
    b= [10, 20, 15, 18]


       # outputs
    for i in range(1,7+1):
         print(' '*(7-i)+'*'*(2*i-1))