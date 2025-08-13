



: '''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else

######
year = int(input('Enter any year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is a Leap Year')
else:
    print(year, 'is NOT a Leap Year')
#####
| Year | Result        | Reason                       |
| ---- | ------------- | ---------------------------- |
| 2016 | Leap Year     | Divisible by 4, not by 100   |
| 1900 | Not Leap Year | Divisible by 100, not by 400 |
| 2000 | Leap Year     | Divisible by 400             |
| 2023 | Not Leap Year | Not divisible by 4           |
| 2024 | Leap Year     | Divisible by 4, not by 100   |


//////////////////////////////////////////////////////////////////////


'''
: '''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions

##### Program to find the largest of three numbers using if and else

# Input three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare using multiple if-else conditions
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)


///////////////////////////////////////////////////////////////////////////

: '''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

##########Temperature conversion program

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

# Convert Celsius to Fahrenheit
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print("Temperature in Fahrenheit:", fahrenheit)

# Convert Fahrenheit to Celsius
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice. Please enter 1 or 2.")


//////////////////////////////////////////////////////////////////////////////

'''
: Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0
: Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78
: Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input


######## Temperature conversion program with matching output format

choice = input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : ")

if choice == '1':
    celsius = float(input("Enter  celsius  temperature : "))
    fahrenheit = 1.8 * celsius + 32
    print("Fahrenheit  Equivalent  : ", round(fahrenheit, 2))

elif choice == '2':
    fahrenheit = float(input("Enter  fahrenheit  temperature : "))
    celsius = (fahrenheit - 32) / 1.8
    print("celsius   equivalent : ", round(celsius, 2))

else:
    print("Invalid input")


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


: '''
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


######## Program to check the location of a point (x, y)

# Input coordinates
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

# Check conditions using if..elif
if x > 0 and y > 0:
    print("The point lies in the 1st quadrant")
elif x < 0 and y > 0:
    print("The point lies in the 2nd quadrant")
elif x < 0 and y < 0:
    print("The point lies in the 3rd quadrant")
elif x > 0 and y < 0:
    print("The point lies in the 4th quadrant")
elif x != 0 and y == 0:
    print("The point lies on the x-axis")
elif x == 0 and y != 0:
    print("The point lies on the y-axis")
elif x == 0 and y == 0:
    print("The point is at the origin")
else:
    print("Invalid input")

////////////////////////////////////////////////////////////////////////////////////////////////////////////

'''
: '''
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
: Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0


######### Program to find largest, smallest, and middle of three numbers

# Take inputs
a = float(input("Enter  first  input   :  "))
b = float(input("Enter  second   input   :  "))
c = float(input("Enter  third  input   :  "))

# Initialize max and min to 'a'
max = a
min = a

# Determine max
if b > max:
    max = b
if c > max:
    max = c

# Determine min
if b < min:
    min = b
if c < min:
    min = c

# Calculate middle value
mid = a + b + c - (max + min)

# Display results
print("Largest number :", max)
print("Smallest number :", min)
print("Middle number :", mid)

////////////////////////////////////////////////////////////////////////////////////////////////////

: '''
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

########import math

# Input the three sides
a = float(input("Enter first side : "))
b = float(input("Enter second side : "))
c = float(input("Enter third side : "))

# Check triangle validity using triangle inequality rule
if a + b > c and a + c > b and b + c > a:
    print("It is a triangle.")

    # Check for equilateral triangle
    if a == b and b == c:
        print("It is an Equilateral Triangle")
        area = (math.sqrt(3) / 4) * a * a
        print("Area of Equilateral Triangle:", round(area, 2))

    # Check for isosceles triangle
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle")
        perimeter = a + b + c
        print("Perimeter of Isosceles Triangle:", round(perimeter, 2))

    # If not equilateral or isosceles, it must be scalene
    else:
        print("It is a Scalene Triangle")
        perimeter = a + b + c
        s = perimeter / 2  # semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Perimeter of Scalene Triangle:", round(perimeter, 2))
        print("Area of Scalene Triangle:", round(area, 2))

else:
    print("The given sides do not form a triangle.")



####Enter first side : 5
Enter second side : 5
Enter third side : 5
It is a triangle.
It is an Equilateral Triangle
Area of Equilateral Triangle: 10.83


####Enter first side : 6
Enter second side : 6
Enter third side : 8
It is a triangle.
It is an Isosceles Triangle
Perimeter of Isosceles Triangle: 20.0


####Enter first side : 5
Enter second side : 6
Enter third side : 7
It is a triangle.
It is a Scalene Triangle
Perimeter of Scalene Triangle: 18.0
Area of Scalene Triangle: 14.7


######Enter first side : 2
Enter second side : 3
Enter third side : 6
The given sides do not form a triangle.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


: '''
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


###########import math

# Input coefficients
a = float(input("Enter coefficient a (a ≠ 0): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Ensure a ≠ 0
if a == 0:
    print("Invalid input: 'a' must not be zero.")
else:
    # Calculate discriminant
    disc = b ** 2 - 4 * a * c
    print("Discriminant =", round(disc, 2))

    # Case 1: Real and Distinct Roots
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Roots are real and distinct.")
        print("Root1 =", round(root1, 2))
        print("Root2 =", round(root2, 2))

    # Case 2: Real and Same Roots
    elif disc == 0:
        root = -b / (2 * a)
        print("Roots are real and same.")
        print("Root =", round(root, 2))

    # Case 3: Complex Roots
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-disc) / (2 * a)
        print("Roots are complex (imaginary).")
        print("Root1 =", round(real_part, 2), "+", round(imag_part, 2), "j")
        print("Root2 =", round(real_part, 2), "-", round(imag_part, 2), "j")

####Enter coefficient a (a ≠ 0): 1
Enter coefficient b: -5
Enter coefficient c: 6
Discriminant = 1.0
Roots are real and distinct.
Root1 = 3.0
Root2 = 2.0


#######Enter coefficient a (a ≠ 0): 1
Enter coefficient b: 4
Enter coefficient c: 4
Discriminant = 0.0
Roots are real and same.
Root = -2.0


#####Enter coefficient a (a ≠ 0): 1
Enter coefficient b: 2
Enter coefficient c: 5
Discriminant = -16.0
Roots are complex (imaginary).
Root1 = -1.0 + 2.0 j
Root2 = -1.0 - 2.0 j

///////////////////////////////////////////////////////////////////////////////////////////////////////////////



: '''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle

#########import math

# Input point and radius
x = float(input("Enter x-coordinate of point: "))
y = float(input("Enter y-coordinate of point: "))
r = float(input("Enter radius of the circle: "))

# Calculate distance from origin to point (x, y)
distance = math.sqrt(x ** 2 + y ** 2)
print("Distance from origin to point:", round(distance, 2))

# Compare distance with radius
if distance > r:
    print("The point lies outside the circle.")
elif distance < r:
    print("The point lies inside the circle.")
elif distance == r:
    print("The point lies on the circle.")


####Enter x-coordinate of point: 3
Enter y-coordinate of point: 4
Enter radius of the circle: 5
Distance from origin to point: 5.0
The point lies on the circle.


#####Enter x-coordinate of point: 2
Enter y-coordinate of point: 2
Enter radius of the circle: 3
Distance from origin to point: 2.83
The point lies inside the circle.


#####Enter x-coordinate of point: 5
Enter y-coordinate of point: 5
Enter radius of the circle: 6
Distance from origin to point: 7.07
The point lies outside the circle.

///////////////////////////////////////////////////
: # Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')

##### output: Bye  due to no case is match outside statement is executed

/////////////////////////////////////////////////////////////////////////////

: # Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

#### syntax error: wildcard'_ 'must be the last case in match statement

///////////////////////////////////////////////////////////

: # Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')


###### error '_' this case use only once at the last
///////////////////////////////////////////////////////////////////
: #  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')

#### output: Hyd
             Bye  reapted case 1 only first case is executed
///////////////////////////////////////////////////////////////////
: # Find  outputs  (Home  work)
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

###### output: Book
               Bye

//////////////////////////////////////////////////////////////////

: '''
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


#######x = eval(input('Enter any  number :  '))

match x:
    case 7 | -6 | 0:
        print('Hyd')
        print('Sec')
        print('Cyb')
    case -10 | 15:
        print('One')
        print('Two')
        print('Three')
    case _:
        print('India')
        print('China')
        print('Usa')

print('Bye')



##########
| Input  | Output                 |
| ------ | ---------------------- |
| -6   | Hyd, Sec, Cyb, Bye     |
| 15   | One, Two, Three, Bye   |
| 10.8 | India, China, Usa, Bye |
| 0    | Hyd, Sec, Cyb, Bye     |
| -10  | One, Two, Three, Bye   |
| 7    | Hyd, Sec, Cyb, Bye     |


/////////////////////////////////////////////////////////////////////////////////////////////


: '''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->  x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->   origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> 3 points not in a tuple pattran
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> list is not a tuple
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> list is not a tuple
8) What  is  the  output  when  input  is  ()  ?  --->        empty tuple does not points
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> set is not a tuple
10) What  is  the  output  when  input  is  (25,) ?  --->  1 element tuple does not match 2- element pattern 
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> dictonary is not a tuple
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

#####################
| #  | Input          | Output      |
| -- | -------------- | ----------- |
| 1  | (-10, -20)   | Quadrant    |
| 2  | (10, 0)      | x - axis    |
| 3  | (0, -20)     | y - axis    |
| 4  | (0, 0)       | Origin      |
| 5  | (10, 20, 30) | Not a point |
| 6  | [10, 20]     | Not a point |
| 7  | [0, -25]     | Not a point |
| 8  | ()           | Not a point |
| 9  | {10, 20}     | Not a point |
| 10 | (25,)        | Not a point |
| 11 | {10: 20}     | Not a point |

///////////////////////////////////////////////////////////////////////////////////////////

: '''
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


##################
units = int(input("Enter units: "))

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

print("Bill Amount = Rs.", round(cost, 2))

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


: '''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop
'''
[: Enter  value  of  x  :  10
Fibonacci  Series
0
1
1
2
3
5
8

############
# Program to print Fibonacci series up to a given number x

x = int(input("Enter value of x : "))
print("Fibonacci Series")

# First two terms
a = 0
b = 1

# Print the first term if within range
if a <= x:
    print(a)

# Print the second term if within range
if b <= x:
    print(b)

# Generate next terms
while True:
    c = a + b  # ith term = (i-1)th + (i-2)th
    if c > x:
        break
    print(c)
    a = b
    b = c

///////////////////////////////////////////////////////////////////////
: #  Find  outputs
while  True:
	print('Hello')
print('Bye')

### output:Hello
           Hello
           Hello
           ...
Infinite loop. It keeps printing "Hello" forever and never reaches print('Bye').
////////////////////////////////////////////////////////////////////////////////////////////////


: #  Find  outputs
while  False:
	print('Hello')
print('Bye')

###### output:Bye
The condition is False, so the loop never executes, and only "Bye" is printed.

////////////////////////////////////////////////////////////////////////////////////////////////////
: # Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()  ######for x in [10, 20, 15, 18]:
                     print(x)
         output:10
                20
                15
                18


How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()########for ch in 'Hyd':
                   print(ch)
          output:H
                 y
                 d


How  to  print  each  element  of   range(5)  with  for  loop

########for x in range(5):
         print(x)
        output:0
               1
               2
               3
               4
////////////////////////////////////////////////////////////////////

: # Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)

output:10
       30
       50


print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
output:20
       40
       60

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
output:
(10, 20)
(30, 40)
(50, 60)

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)

output
10
30
50
Iterating over a dictionary directly gives keys.

//////////////////////////////////////////////////////////////////////
: # Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

output:
10...20
30...40
50...60


for  x ,  y  in   a:
	print(x , y
output: error ValueError: too many values to unpack (expected 2)

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')

output: error
///////////////////////////////////////////////////////////////////////////

: # Identify  error  (Home  work)
for  x  in   123:
        print(x)
output: error
TypeError: 'int' object is not iterable
////////////////////////////////////////////////////////////////////////////////////

 # Find  outputs  (Home  work)
for  x   in   ():
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)

Output: (All print nothing; no error)
All are empty iterables, so loops do not run


for  x  in  range(10 , 10):
	print(x)
output:Also prints nothing. range(10, 10) is empty.

for  x  in   range():
	print(x)
output: error
TypeError: range expected at least 1 argument, got 0


for  x  in   (25):
	print(x)
output:error
TypeError: 'int' object is not iterable
/////////////////////////////////////////////////////////////
: #  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

#######
# Nested Loop demo program
for i in range(1, 4):           # Outer loop: i = 1, 2, 3
    for j in range(1, 5):       # Inner loop: j = 1, 2, 3, 4
        print(i, j)             # Prints i and j combinations
    print('Hello')              # Runs after inner loop completes each time
print('Bye')                    # Runs once after both loops are done

###### output
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

///////////////////////////////////////////////////////////////////////////////////

: # How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

#######
a = [25, 10.8, 'Hyd', True]

print('Indexed based for loop')
for i in range(len(a)):
    print('Index:', i, 'Element:', a[i])

print('For each loop')
for i, value in enumerate(a):
    print('Index:', i, 'Element:', value)

////////////////////////////////////////////////////////////////////////////////////


: #  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
##########
a = [25, 10.8, 'Hyd', True]

print('Indexed for loop')
for i in range(len(a) - 1, -1, -1):
    print(a[i])

print('For each loop (no second variable, no slicing)')
reversed_list = reversed(a)
for item in reversed_list:
    print(item)

///////////////////////////////////////////////////////////////////////////////////////

: '''
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
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

#########
a = eval(input('Enter 1st list: '))     # e.g., [10, 20, 15, 18]
b = eval(input('Enter 2nd list: '))     # e.g., [30, 40, 35, 12, 100]
c = []

# Indexed-based for loop
min_len = min(len(a), len(b))
for i in range(min_len):
    c.append(a[i] + b[i])
print('3rd list:', c)

# For-each loop (zips only up to shortest length)
c = []
for x, y in zip(a, b):
    c.append(x + y)
print('3rd list (for-each):', c)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

: #  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

########
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']

print('Indexed for loop')
for i in range(2, 5):
    print(a[i])

print('For each loop (without slice or second variable)')
i = 0
for val in a:
    if 2 <= i <= 4:
        print(val)
    i += 1

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

: #  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

##############
a = [10, 20, 15, 18]
for i in range(len(a)):
    a[i] += 1
print('a:', a)  # Output: [11, 21, 16, 19]

b = [10, 20, 15, 18]
for x in b:
    x += 1       # This does NOT change the original list
print('b:', b)  # Output: [10, 20, 15, 18]
//////////////////////////////////////////////////////////////////////////////////////////////////
