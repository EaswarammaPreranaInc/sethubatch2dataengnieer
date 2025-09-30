#Leap Year

try:
    year = int(input('Enter a year:  '))
    if(year%4==0 and year%100!=0 or year%400==0):
        print('Leap Year')
    else:
        print('Not a Leap Year')
except ValueError:
    print('Please enter only integer value')
except:
    print('Please try again')



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple conditions
'''

try:
    num1 = float(input('Enter numbmer1:  '))
    num2 = float(input('Enter number 2:  '))
    num3 = float(input('Enter number 3:  '))
    max = 0
    if num1 > num2 and num1 > num3:
        max = num1
    elif num2 > num3:
        max = num2
    else:
        max = num3
    print(f'Largest of three is {max}')
except ValueError:
    print('Please enter either integer or float number')
except:
    print('Please try again')




'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

# Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
# Enter  celsius  temperature :  30
# Fahrenheit  Equivalent : 86.0

try:
    option = float(input('Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius:  '))
    if(option==1):
        cel = float(input('Enter celsius temperature: '))
        fah = 1.8 * cel + 32
        print(f'Fahrenheit Equivalent: {fah}')
    else:
        fah = float(input('Enter fahrenheit temperature:  '))
        cel = (fah - 32) / 1.8
        print(f'Celsius Equivalent: {cel}')
except ValueError:
    print('Please enter only float or integer')
except:
    print('Please try again')



try:
    x = float(input('Enter the x:  '))
    y = float(input('Enter the y:  '))
    q = 0
    if x > 0 and y > 0:
        q = 1
    elif x < 0 and y > 0:
        q = 2
    elif x < 0 and y < 0:
        q = 3
    else:
        q = 4
    print(f'Quadrant:  {q}')
except ValueError:
    print('Please enter only integer or float')
except:
    print('Please try again')    



try:
    num1 = float(input('Enter number1:  '))
    num2 = float(input('Enter number2:  '))
    num3 = float(input('Enter number3:  '))
    max = num1
    if(num2 > max):
        max = num2
    if(num3 > max):
        max = num3
    min = num1
    if(num2 < min):
        min = num2
    if(num3 < min):
        min = num3
    mid = num1 + num2 + num3 - max - min
    print(f'Largest: {max} \nSmallest: {min} \nMiddle: {mid}')
except ValueError:
    print('Please enter only integer or float number')
except:
    print('Please try again')



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
try:
    s1 = float(input('Enter length of side1:  '))
    s2 = float(input('Enter length of side2:  '))
    s3 = float(input('Enter length of side3:  '))
    if(s1 > s2 + s3 and s2 > s1 + s3 and s3 > s1 + s2):
        #if equilateral print its area
        if(s1 == s2 == s3):
            print(f'Area of Triangle is: {(math.sqrt(3) / 4) * pow(s1, 2)}')
        #if isosceles, any two sides equal print its perimeter
        elif(s1 == s2 or s2 == s3 or s3 == s1):
            print(f'Perimeter of Triangle is: {s1 + s2 + s3}')
        #if scalene, print both area and perimeter
        else:
            #for scalene, use semiperimeter(s) and heron's formula: sqrt(s * (s-a) * (s-b) * (s-c))
            s = (s1 + s2 + s3) / 2
            area = math.sqrt( s * (s-s1) * (s-s2) * (s-s3) )
            print(f'Area of triangle: {area} \nPerimeter of Triangle is: {s1+s2+s3}')
    else:
        print('Not a Triangle')
except ValueError:
    print('Please enter only integer or float numbers')
except:
    print('Please try again')


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
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j
'''

import math
try:
     a = float(input('Please enter \'a\' of quadratic equation ax^2+bx+c: '))
     b = float(input('Please enter \'b\' of quadratic equation ax^2+bx+c: '))
     c = float(input('Please enter \'c\' of quadratic equation ax^2+bx+c: '))
     d = pow(b,2) - 4*a*c
     root1 = 0
     root2 = 0
     if(d > 0):
        print('Real and Distinct roots')
        root1 = (-b + math.sqrt(d)) / 2 * a
        root2 = (-b - math.sqrt(d)) / 2 * a
     elif(d==0):
        print('Real and Equal roots')
        root1 = root2 = -b / 2 * a
     else:
        print('Complex and Imaginary roots')
        real = -b/2*a
        imag = math.sqrt(-d)/2*a
        root1 = real + imag
        root2 = real - imag
     print(f'Root1: {root1} \nRoot2: {root2}')
except ValueError:
    print('Please enter only integer or float number')
except:
    print('Please try again')



'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On the circle
'''

import math
try:
    radius = float(input('Enter radius of the circle: '))
    x, y = [float(x) for x in input('Please enter x and y with space separated: ').split()]
    #center is origin and distance from orgin is below formula
    distance = math.sqrt(x**2 + y**2)
    if(distance==radius):
        print('On the Circle')
    elif(distance > radius):
        print('Out of the Circle')
    else:
        print('Inside the Circle')
except ValueError:
    print('Please enter only integer or float number')






#Match
# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')            #Bye, because no case matched


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	# case  _:
	# 	print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

# case _ must be the last case and not in middle


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	# case  _:
	# 	print('Hello')
	case  _:
		print('Bye')
print('End')

#There can be only one case _

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')  #Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')  
print('Bye')         #Bye

#after the 1st case match, control goes out of the match suite


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
print('Bye')                         #Bye



'''
1) What  are  the  outputs  if  input  is  -6 ? --->      Hyd<space>Sec<space>Cyb<newline>Bye<newline>
2) What  are  the  outputs  if  input  is  15  ?  --->    One<space>Two<space>Three<newline>Bye<newline>
3) What  are  the  outputs  if  input  is  10.8  ?  --->  India<space>China<space>Usa<newline>Bye<newline>
4) What  are  the  outputs  if  input  is  0  ?  --->     Hyd<space>Sec<space>Cyb<newline>Bye<newline>
5) What  are  the  outputs  if  input  is  -10  ?  --->   One<space>Two<space>Three<newline>Bye<newline>
6) What  are  the  outputs  if  input  is  7  ?  --->     Hyd<space>Sec<space>Cyb<newline>Bye<newline>
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->         Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->            x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->           y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->             Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->      Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->          Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->          y - axis
8) What  is  the  output  when  input  is  ()  ?  --->                 Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->           Not a point
10) What  is  the  output  when  input  is  (25,) ?  --->              Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->          Not a point
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
		print('Not a point')
          

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

try:
    units = int(input('Enter  units :   ')) 
    bill = 0
    match units // 100:
        case 0: 
            bill = units * 3.0
        case 1:
            bill = 100*3.0 + (units-100)*3.5
        case 2 | 3:
            bill = 100*3.0 + 100*3.5 + (units-100)*4.0
        case 4 | 5 | 6:
            bill = 100*3.0 + 100*3.5 + 200*4.0 + (units-400)*4.5
        case _:
            bill = 100*3.0 + 100*3.5 + 200*4.0 + 300*4.5 + (units-700)*5.0
    print(f'The bill amount is {bill}')
except ValueError:
    print('Please enter only integer value')



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

try:
    num = int(input('Enter a number:  '))
    a = 0
    b = 1
    print(0, 1, sep='\n')
    while(a+b < num):
        c = a+b
        print(c)
        a=b
        b=c
except ValueError:
    print('Please enter only integer number')


#  Find  outputs
while  True:
	print('Hello')  #keeps printing Hello<newline>Hello<newline>........
print('Bye')        #this line is never reached


#  Find  outputs
while  False:
	print('Hello')
print('Bye')         #Bye




#For Each
# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in [10, 20, 15, 18]:
    print(x, end=" ")
print()
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
for x in 'Hyd':
    print(x, end=" ")
print()
#How  to  print  each  element  of   range(5) with for loop
for x in range(5):
    print(x, end=" ")


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                                           #10<newline>30<newline>50<newline>
print()                                         
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)                                           #20<newline>40<newline>60<newline>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)                                           #(10,20) <newline> (30,40) <newline> (50,60) <newline>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)                                           #10 <newline> 30 <newline> 50 <newline>
     

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')                    #10<space>20...30<space>40...50<space>60...
# for  x ,  y  in   a:                            #error because by default a.keys() 
# 	print(x , y)                                
# for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:    #error iterating on dictonary means iterating on keys 
# 	print(x , y , sep = '...')                       



# Identify  error  (Home  work)
for  x  in   123:   #we can't iterate on non-sequences
   print(x)



# Find  outputs  (Home  work)
for  x   in   ():           #empty tuple, 0 iterations
        print(x)
for  x   in  []:            #empty list, 0 iterations
        print(x)
for  x   in   {}:           #empty dict, 0 iterations
        print(x)
for  x   in   set():        #empty set, 0 iterations
        print(x)
for  x   in   '':           #empty str, 0 iterations
        print(x)
for  x  in  range(10 , 10): #empty range, 0 iterations
	print(x)
# for  x  in   range():       #error: range cannot be empty
# 	print(x)
# for  x  in  (25):           #error: cannot iterate on non-sequences
# 	print(x)



#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')
# 1<space>1<newline>1<space>2<newline>1<space>3<newline>1<space>4<newline>Hello<newline>
# 2<space>1<newline>2<space>2<newline>2<space>3<newline>2<space>4<newline>Hello<newline>
# 3<space>1<newline>3<space>2<newline>3<space>3<newline>3<space>4<newline>Hello<newline>



# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
    print(i, a[i])
print('For each loop')
for x in a:
    print(x)



#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
print('Indexed for loop')
for i in range(1, len(a)+1):
    print(a[-i])

# How  to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable and slice)
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
min = min(len(a), len(b))
for i in range(min):
    c.append(a[i]+b[i])
print('3rd  list : ' , c)

c=[]
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use 2nd variable)
for x, y in zip(a, b):
    c.append(x+y)
print('3rd  list : ' , c)


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
print('Indexed for loop')
for i in range(2, 5):
    print(a[i])
print('For each loop')
i = -1
#How to print elements from indexes 2 to 4 of list 'a' with for each loop  without using 2nd  variable and slice
for x in a:
    i+=1
    if( 2 <= i <= 4):
        print(x)



#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):  
	a[i] +=  1                #increments each value of sequence
print('a :  ' , a)            #a: [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1                    #does not increment the values of sequence, just x is incremented
print('b : ' , b)             #b: [10, 20, 15, 18]
