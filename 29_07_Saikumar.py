# Write  a  program  to  test  year  is  leap  year  or  not

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")


# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp-32)/1.8
'''

choice = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  "))
if choice == 1:
    c = float(input("Enter  celsius  temperature :  "))
    f = 1.8 * c + 32
    print("Fahrenheit  Equivalent  : ", round(f, 2))
elif choice == 2:
    f = float(input("Enter  fahrenheit  temperature : "))
    c = (f - 32) / 1.8
    print("Celsius  Equivalent : ", round(c, 2))
else:
    print("Invalid input")


# Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant , 4th  quadrant , x - axis , y - axis   or  origin

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("Point lies in 1st Quadrant")
elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")
elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")
elif x > 0 and y < 0:
    print("Point lies in 4th Quadrant")
elif x != 0 and y == 0:
    print("Point lies on x-axis")
elif x == 0 and y != 0:
    print("Point lies on y-axis")
elif x == 0 and y == 0:
    print("Point is at the Origin")


# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = float(input("Enter  first  input   :  "))
b = float(input("Enter  second   input   :  "))
c = float(input("Enter  third  input   :  "))
max = a
if b > max:
    max = b
if c > max:
    max = c
min = a
if b < min:
    min = b
if c < min:
    min = c
mid = (a + b + c) - (max + min)
print("Largest number    : ", max)
print("Smallest number   : ", min)
print("Middle number     : ", mid)


# Write a program to determine three sides form a triangle or not, then compute area or perimeter based on triangle type.

import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check for triangle validity
if a + b > c and a + c > b and b + c > a:
    print("The sides form a valid triangle.")

    # Equilateral triangle: all sides equal
    if a == b and b == c:
        area = (math.sqrt(3) / 4) * a * a
        print("Triangle type: Equilateral")
        print("Area of Equilateral Triangle: ", round(area, 2))

    # Isosceles triangle: any two sides equal
    elif a == b or b == c or a == c:
        perimeter = a + b + c
        print("Triangle type: Isosceles")
        print("Perimeter of Isosceles Triangle: ", round(perimeter, 2))

    # Scalene triangle: all sides different
    else:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print("Triangle type: Scalene")
        print("Area of Scalene Triangle: ", round(area, 2))
        print("Perimeter of Scalene Triangle: ", round(perimeter, 2))

else:
    print("The sides do NOT form a triangle.")


# Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

import math

a = float(input("Enter coefficient a (a ≠ 0): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Invalid input. 'a' should not be zero.")
else:
    disc = b ** 2 - 4 * a * c
    print("Discriminant:", disc)

    if disc > 0:
        print("Roots are Real and Distinct")
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Root 1:", round(root1, 2))
        print("Root 2:", round(root2, 2))

    elif disc == 0:
        print("Roots are Real and Same")
        root = -b / (2 * a)
        print("Root:", round(root, 2))

    else:
        print("Roots are Complex or Imaginary")
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-disc) / (2 * a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        print("Root 1:", root1)
        print("Root 2:", root2)


# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle. Center  is  origin  and  radius  is  'r'

import math

x = float(input("Enter x coordinate of the point: "))
y = float(input("Enter y coordinate of the point: "))
r = float(input("Enter radius of the circle: "))
distance = math.sqrt(x ** 2 + y ** 2)
print("Distance from origin to point:", round(distance, 2))
if distance < r:
    print("The point lies Inside the circle")
elif distance > r:
    print("The point lies Outside the circle")
elif distance == r:
    print("The point lies On the circle")


'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)			        Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	        Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
'''

units = int(input('Enter units: '))
match units // 100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = (100 * 3.00) + (units - 100) * 3.50
    case 2 | 3:
        cost = (100 * 3.00) + (100 * 3.50) + (units - 200) * 4.00
    case 4 | 5 | 6:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (units - 400) * 4.50
    case _:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (units - 700) * 5.00
print("Bill Amount: Rs.", round(cost, 2))


# Write  a  program  to  print  fibonacci  series  upto   x

x = int(input("Enter value of x: "))
a = 0
b = 1
c = a + b
while c <= x:
    print(c)
    a = b
    b = c
    c = a + b


'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]
'''

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []

print('Using index-based for loop')
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print('3rd list :', c)

print('Using for-each loop (without second variable)')
c = []
i = 0
for x in a:
    c.append(x + b[i])
    i += 1
print('3rd list :', c)


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

# The value of m is 4 No case matches (1, 2, or 3), and there is no case. So, nothing is printed from inside the match, only "Bye" outside is printed.

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

# case _ is a default case that matches anything. Once Python sees case _, it stops checking further. So writing any case after case _ is not allowed. That’s why case 2 after case _ causes an error.

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

# Two case _ statements. But _ is a special pattern used only once to mean "match anything". Having it twice is a syntax error.

# Find  outputs  (Home  work)

m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')

# m is 1, so case 1 matches. Only the first matching case runs: print('Hyd'). The other case 1 lines are ignored. Then, "Bye" is printed outside the match block.


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

# The value of ch is 'B', so it matches case 'B'. It prints "Book". The other cases are skipped. Then "Bye" is printed outside the match block.


# output's :

x = eval(input('Enter any  number :  '))
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

'''
What are the outputs if input is -6 ? --->
Hyd
Sec
Cyb
Bye

What are the outputs if input is 15 ? --->
One
Two
Three
Bye

What are the outputs if input is 10.8 ? --->
India
China
Usa
Bye

What are the outputs if input is 0 ? --->
Hyd
Sec
Cyb
Bye

What are the outputs if input is -10 ? --->
One
Two
Three
Bye

What are the outputs if input is 7 ? --->
Hyd
Sec
Cyb
Bye
'''


#output's :

tpl = eval(input('Enter any point in the form of (x, y): '))
match tpl:
    case (0, 0):
        print('Origin')
    case (0, y):
        print('y - axis')
    case (x, 0):
        print('x - axis')
    case (x, y):
        print('Quadrant')
    case _:
        print('Not a point')

'''
What is the output when input is (-10 , -20) ? --->
Quadrant

What is the output when input is (10 , 0) ? --->
x - axis

What is the output when input is (0 , -20) ? --->
y - axis

What is the output when input is (0 , 0) ? --->
Origin

What is the output when input is (10 , 20 , 30) ? --->
Not a point (3 elements — doesn’t match any (x, y) pattern)

What is the output when input is [10 , 20] ? --->
Not a point (list — not a tuple)

What is the output when input is [0 , -25] ? --->
Not a point (list — not a tuple)

What is the output when input is () ? --->
Not a point (empty tuple — doesn't match any case)

What is the output when input is {10 , 20} ? --->
Not a point (set — doesn't match tuple)

What is the output when input is (25,) ? --->
Not a point (only one element — not a 2-element tuple)

What is the output when input is {10 : 20} ? --->
Not a point (dictionary — doesn't match any pattern)
'''


# Find  outputs

while  True:
	print('Hello')
print('Bye')

# while True means the loop will run forever (infinite loop). So, "Hello" will keep printing endlessly. "Bye" is never reached — the program never exits the loop.


# Find  outputs

while  False:
	print('Hello')
print('Bye')

# while False means the loop will not run at all. So "Hello" is never printed. Only "Bye" is printed.


# Find  outputs  (Home  work)

# Print each element of list [10, 20, 15, 18]
print("List Elements:")
l = [10, 20, 15, 18]
for x in l:
    print(x)

# Print each character of string 'Hyd'
print("\nCharacters in String:")
s = 'Hyd'
for ch in s:
    print(ch)

# Print each element of range(5)
print("\nRange Elements:")
for i in range(5):
    print(i)


# Find  outputs  (Home  work)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 :60}:
	print(x)

'''
output:
Keys:
10
30
50

Values:
20
40
60

Items:
(10, 20)
(30, 40)
(50, 60)

Keys (Direct Iteration):
10
30
50
'''


# Find outputs  (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x ,  y  in   a:
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y,sep='...')

'''
output:
10...20
30...40
50...60
Error:
a is a dictionary, and iterating directly over it gives only the keys. x, y in a tries to unpack a single key into two variables.
Same as above — dictionary iteration gives only keys, not key-value pairs. Can't unpack.
'''

# Identify  error  (Home  work)

for  x  in   123:
   print(x)

# Error: 123 is an integer, which is not iterable. for needs a sequence like list, tuple, string, etc.


# Find  outputs  (Home  work)

for x in ():       # Empty tuple
    print(x)
for x in []:       # Empty list
    print(x)
for x in {}:       # Empty dictionary (no keys)
    print(x)
for x in set():    # Empty set
    print(x)
for x in '':       # Empty string
    print(x)
for x in range(10, 10):  # Range with no numbers
    print(x)
for x in range():
    print(x)        # Error range needs at least one argument
for x in (25):
    print(x)        # Error (25) is just an integer, not a tuple
for x in (25,):       # Tuple with one element
    print(x)


# Nested loop demonstration

for i in range(1, 4):          # Outer loop: i = 1 to 3
    for j in range(1, 5):      # Inner loop: j = 1 to 4
        print(i, j)            # Print i and j values
    print('Hello')             # Print after inner loop finishes
print('Bye')                   # Print after both loops complete


# How  to  print  each  element  and  the  corresponding  index

a = [25, 10.8, 'Hyd', True]

# Index-based for loop
print('Index based for loop')
for i in range(len(a)):             # Looping over index values
    print(i, a[i])                  # Print index and corresponding element

# For-each loop with index using enumerate()
print('For each loop')
for i, val in enumerate(a):         # enumerate gives index and value
    print(i, val)

# For-each loop (only element; no second variable used)
print('For each loop without index')  
i = 0
for val in a:                       # Loop over values
    print(i, val)                   # Manually track index
    i += 1

'''
output:

Index based for loop
0 25
1 10.8
2 Hyd
3 True
For each loop
0 25
1 10.8
2 Hyd
3 True
For each loop without index
0 25
1 10.8
2 Hyd
3 True
'''


# How  to  print  list  elements  in  reverse  order   without  slice

a = [25, 10.8, 'Hyd', True]

# Using index-based for loop to print in reverse
print('Indexed for loop')
for i in range(len(a) - 1, -1, -1):   # Start from last index to 0
    print(a[i])

# Using for-each loop with manual index (no second variable, no slicing)
print('For each loop without 2nd variable and without slice')
i = len(a)                           # Start from length of list
for _ in a:                          # Just loop same number of times
    i -= 1
    print(a[i])                      # Print in reverse using decreasing index
'''
output:

Indexed for loop
True
Hyd
10.8
25
For each loop without 2nd variable and without slice
True
Hyd
10.8
25
'''


# How  to  print  list  elements  from  indexes  2  to  4  without  slice

a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']

print('Indexed for loop')
for i in range(2, 5):
    print(a[i])

print('For each loop without 2nd variable and without slice')
i = 0
for x in a:
    if 2 <= i <= 4:
        print(x)
    i += 1

#Tricky  program
#Find  outputs  (Home  work)

a = [10, 20, 15, 18]
for i in range(len(a)):
    a[i] += 1                 # Increases each element of list 'a' by 1
print('a :  ', a)             # Output will be: [11, 21, 16, 19]
b = [10, 20, 15, 18]
for x in b:
    x += 1                    # Only modifies the local copy, not the list
print('b :  ', b)             # Output remains unchanged: [10, 20, 15, 18]

a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]
