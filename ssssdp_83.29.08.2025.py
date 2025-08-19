# Program to test whether a year is a leap year or not

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

############################################

# Program to determine the largest of three numbers using if and else

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

###########################################################

# Program to convert Celsius to Fahrenheit and vice-versa

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print("Temperature in Fahrenheit:", fahrenheit)
else:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Temperature in Celsius:", celsius)

#################################################################

# Program to convert Celsius to Fahrenheit and vice-versa

choice = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))

if choice == 1:
    celsius = float(input("Enter  celsius  temperature : "))
    fahrenheit = 1.8 * celsius + 32
    print("Fahrenheit  Equivalent  :", fahrenheit)
else:
    fahrenheit = float(input("Enter  fahrenheit  temperature : "))
    celsius = (fahrenheit - 32) / 1.8
    print("Celsius  Equivalent  :", celsius)

###########################################################################
# Program to convert Celsius to Fahrenheit and vice-versa

choice = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))

if choice == 1:
    celsius = float(input("Enter  celsius  temperature : "))
    fahrenheit = 1.8 * celsius + 32
    print("Fahrenheit  Equivalent  :", round(fahrenheit, 2))
else:
    fahrenheit = float(input("Enter  fahrenheit  temperature : "))
    celsius = (fahrenheit - 32) / 1.8
    print("celsius   equivalent :", round(celsius, 2))

########################################################################

# Program to convert Celsius to Fahrenheit and vice-versa with input validation

choice = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))

if choice == 1:
    celsius = float(input("Enter  celsius  temperature : "))
    fahrenheit = 1.8 * celsius + 32
    print("Fahrenheit  Equivalent  :", round(fahrenheit, 2))
elif choice == 2:
    fahrenheit = float(input("Enter  fahrenheit  temperature : "))
    celsius = (fahrenheit - 32) / 1.8
    print("celsius   equivalent :", round(celsius, 2))
else:
    print("Invalid input")

###############################################################

# Program to test where a point (x, y) lies

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x == 0 and y == 0:
    print("Point lies at the origin")
elif x == 0:
    print("Point lies on the y-axis")
elif y == 0:
    print("Point lies on the x-axis")
elif x > 0 and y > 0:
    print("Point lies in the 1st quadrant")
elif x < 0 and y > 0:
    print("Point lies in the 2nd quadrant")
elif x < 0 and y < 0:
    print("Point lies in the 3rd quadrant")
else:
    print("

Here is the Python program to **determine the largest (max), smallest (min), and middle (mid)** of three numbers using only `if` statements (no `else`), exactly as per your instructions:

```python
# Program to find largest, smallest, and middle of three numbers

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

# Step 1: Assume a is the max
max = a
if b > max:
    max = b
if c > max:
    max = c

# Step 2: Assume a is the min
min = a
if b < min:
    min = b
if c < min:
    min = c

# Step 3: Middle = total - (max + min)
mid = a + b + c - (max + min)

print("max =", max)
print("min =", min)
print("mid =", mid)

##################################################

# Program to find largest, smallest, and middle of three numbers

a = float(input("Enter  first  input   :  "))
b = float(input("Enter  second   input   :  "))
c = float(input("Enter  third  input   :  "))

# Find largest
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

# Find smallest
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

# Find middle
middle = a + b + c - (largest + smallest)

print("Largest number :", round(largest, 1))
print("Smallest number :", round(smallest, 1))
print("Middle number :", round(middle, 1))

##################################################

# Program to check if three sides form a triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and c + a > b:
    print("It is a triangle")
else:
    print("It is not a triangle")
  
  #################################################
# Program to find roots of a quadratic equation a*x^2 + b*x + c = 0

import math

a = float(input("Enter value of a (a ≠ 0): "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Real and distinct roots :", round(root1, 2), "and", round(root2, 2))
elif d == 0:
    root = -b / (2 * a)
    print("Real and equal roots :", round(root, 2), "and", round(root, 2))
else:
    real = -b / (2 * a)
    imag = math.sqrt(-d) / (2 * a)
    print("Complex roots :", f"{round(real, 2)} + {round(imag, 2)}i", "and", f"{round(real, 2)} - {round(imag, 2)}i")

##############################################################################################

# Program to check if a point lies inside, on, or outside a circle

x = float(input("Enter x-coordinate of point: "))
y = float(input("Enter y-coordinate of point: "))
r = float(input("Enter radius of the circle: "))

# Calculate distance squared from origin
distance_squared = x**2 + y**2
radius_squared = r**2

if distance_squared < radius_squared:
    print("Point lies inside the circle")
elif distance_squared == radius_squared:
    print("Point lies on the circle")
else:
    print("Point lies outside the circle")

###################################################################
m = 4
match m:
	case 1:
		print('One')
	case 2:
		print('Two')
	case 3:
		print('Three')
print('Bye')

################################################

i = 2
match i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

################################################i = 2
match i:
	case 1:
		print('One')
	case 2:
		print('Two')
	case _:
		print('None of   the  above')
print('Bye')

###########################################

m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')

########################################

m = 2
match m:
	case 1:
		print('One')
	case _:
		print('Hello')
print('End')

########################################

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

#############################################

x = eval(input('Enter any  number :  '))
match  x:
	case  7 | -6 | 0:
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
print('Bye')

#######################################

tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case (0, 0):
		print('Origin')
	case (0, y):
		print('y - axis')
	case (x, 0):
		print('x - axis')
	case (x, y):
		print('Quadrant')
	case _:
		print('Not  a  point')

#############################################

units = int(input('Enter  units :   '))
cost = 0

match units // 100:
	case 0:  # 0–99 units
		cost = units * 3.00
	case 1:  # 100–199 units
		cost = 100 * 3.00 + (units - 100) * 3.50
	case 2 | 3:  # 200–399 units
		cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
	case 4 | 5 | 6:  # 400–699 units
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
	case _:  # 700+ units
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print("Bill amount :", cost)

################################################

# Program to print Fibonacci series up to x

x = int(input("Enter a number: "))

a = 0
b = 1

print(a, end=" , ")
if x > 0:
    print(b, end=" , ")

c = a + b
while c <= x:
    print(c, end=" , ")
    a = b
    b = c
    c = a + b

################################################

while True:
    print('Hello')
print('Bye')

#################################

while False:
    print('Hello')
print('Bye')

######################################

# Print each element of list [10, 20, 15, 18]
for i in [10, 20, 15, 18]:
    print(i)

# Print each character of string 'Hyd'
for ch in 'Hyd':
    print(ch)

# Print each element of range(5)
for i in range(5):
    print(i)

####################################

a = {10: 20, 30: 40, 50: 60}

# 1st loop – correct
for x, y in a.items():
    print(x, y, sep='...')

# 2nd loop – ERROR: trying to unpack key only (not a tuple)
# This will raise: ValueError: too many values to unpack (expected 2)
# for x, y in a:
#     print(x, y)

# 3rd loop – ERROR: directly iterating over dict gives only keys, not key-value pairs
# This will raise: ValueError: too many values to unpack (expected 2)
# for x, y in {10:  20, 30: 40, 50: 60}:
#     print(x, y, sep='...')

###################################################

# 1) Empty tuple
for x in ():
    print(x)
# Output: nothing (loop doesn't run)

# 2) Empty list
for x in []:
    print(x)
# Output: nothing

# 3) Empty dictionary
for x in {}:
    print(x)
# Output: nothing

# 4) Empty set
for x in set():
    print(x)
# Output: nothing

# 5) Empty string
for x in '':
    print(x)
# Output: nothing

# 6) range(10, 10) empty range
for x in range(10, 10):
    print(x)
# Output: nothing

################################################

for i in range(1, 4):          # i = 1, 2, 3
    for j in range(1, 5):      # j = 1, 2, 3, 4
        print(i, j)            # print i and j
    print('Hello')             # after inner loop
print('Bye')                   # after outer loop

############################################

a = [25, 10.8, 'Hyd', True]

print('Indexed  based  for loop')
# Index-based for loop using range and indexing
for i in range(len(a)):
    print(i, a[i])

print('For each loop')
# For-each loop using enumerate (gives index + element) but using only 1 variable
for i in enumerate(a):
    print(i[0], i[1])

########################################

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

# Index-based for loop
for i in range(len(a)):
    c.append(a[i] + b[i])
print('3rd  list :', c)

# Reset c for next method
c = []

# For-each loop using zip (without second variable)
for pair in zip(a, b):
    c.append(pair[0] + pair[1])
print('3rd  list :', c)

#######################################

a :   [11, 21, 16, 19]
b :   [10, 20

```python
a = [10, 20, 15, 18]
for i in range(len(a)):
    a[i] += 1
print('a :  ', a)   # Output: [11, 21, 16, 19]

b = [10, 20, 15, 18]
for x in b:
    x += 1          # x is a copy; original list not modified
print('b :  ', b)   # Output: [10, 20, 15, 18]




