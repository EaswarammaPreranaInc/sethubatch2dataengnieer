1.
1) What are the outputs of input is - **
< and list ->
Hyd Sec Cyb
By
2) "what are the outputs of input is 15 p**
<- and list -->
One
Three Byk
3) "what are the outputs of input is 10.8 ***
<- and list -->
China usa Byk
4)**What are the outputs of snout is p**
<- and list -->
Hyd
Sec
Cyb
By
3) what are the outputs if input is -10 **
<- and list -->
One
Three Byk
6)hat are the outputs of input is 72**
<- and list -->
Hyd
Sec
Byk





2.
import math
#---
Program to Determine if a Point is Inside, Outside, or on a circle
print("--- Point in circle checker (Center at origin) ---")
# Get the x, y coordinates of the point and the radius of the circle from the user try:
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))
radius = float(input("Enter the radius of the circle: "))
except ValueError:
else:
print("Invalid input. Please enter numeric values for coordinates and radius.")
# Ensure radius is non-negative
if radius < 0:
print("Error: Radius cannot be negative.")
else:
# Calculate the distance between the origin (0,0) and the point (x, y) # Formula: distance = sqrt(x^2 + y^2)
distance
math.sqrt(x**2+ y**2)
print("\nPoint: ({x}, {y})")
print(f"Radius of the circle: {radius}")
print(f"Distance from origin to point: (distance:.2f}")
# Determine if the point is inside, outside, or on the circle if distance > radius:
print("The point lies OUTSIDE the circle.")
elif distance < radius:
print("The point lies INSIDE the circle.") else: # distance == radius
print("The point lies on the circle.")





3.
# Nested Loop demo program for i in range(1, 4):
for i in range(1, 5):
print('Hello')
print(i, j) #
print('Bye')
output:
text
Elements of the list:
10
20
15
18
Characters of the string:
HYA
y
d
Elements of range(5):
Ө
1
2
3
4
Nested Loop Demo
1 1
12
13
14
Hello
2 1
22
23
2 4
Hello
31
32
33
34
Hello
Bye





4.
#---
Program to Determine Point Location on a Coordinate Plane
# Get the x and y coordinates from the user
try:
x = float(input("Enter the x-coordinate of the point: ")) y = float(input("Enter the y-coordinate of the point: ")) except ValueError:
else:
print("Invalid input. Please enter numeric values for coordinates.")
# Determine the location of the point using if-elif-else structure
if x == 0 and y == 0:
print (f"The point ({x}, elif x == 0: # This means x print (f"The point ({x}, elif y == 0: # This means y print (f"The point ({x},
elif x and y > 0:
{y}) is at the origin.")
is 0, and y is not 0 (covered by the first condition) {y}) lies on the Y-axis.")
is 0, and x is not 0 (covered by the first condition) {y}) lies on the x-axis.")
print (f"The point ({x}, {y}) lies in the 1st Quadrant.") elif x and y > 0:
print (f"The point ({x}, {y}) lies in the 2nd Quadrant.") elif x and y < 0:
print (f"The point ({x}, {y}) lies in the 3rd Quadrant.")
elif x and y < 0:
print (f"The point ({x}, {y}) lies in the 4th Quadrant.")
# This else is technically not needed if all cases are covered, but for completeness
# and to catch any unexpected float precision issues, it can be left.
# However, given the rules, all points should fall into one of the above categories.
# If using integer inputs, this else would never be reached.
else:
print (f"The point ({x}, {y}) is at an undefined location (should not happen with valid inputs).")






5.
# Find outputs (Home work)
m = 4
match m:
case 1:
print('One')
case 2:
print('Two')
case 3:
print('Three')
print('Bye')
output:
Bye




6.
# How to print each element of list [10, 20, 15, 18] with for loop my list [10, 20, 15, 18]
print("Elements of the list:")
for item in my list:
print(item)
print() # Prints an empty line for separation
# How to print each character of string 'Hyd' with for loop my string 'Hvd'
print("Characters of the string: ")
for char in my string:
print(char)
print() # Prints an empty line for separation
# How to print each element of range (5) with for loop print("Elements of range(5):")
for num in range(5):
print(num)
print() # Prints an empty line for separation
#Nested Loop demo program
print("--- Nested Loop Demo ---")
for i in range(1, 4):
for i in range(1, 5): print(i, j)
print('Hello')
print('Bye')
print() # Prints an empty line for separation
# --- Printing Elements with Index ---
a = [25, 10.8, 'Hyd', True]
print('Indexed based for loop')
#How to print each element and the corresponding index with index based for loop
# This method uses range(len(list)) to get indices, then accesses elements by index. for index in range(len(a)):
print(f"Index: {index}, Element: {a[index]}")
print('For each loop (using enumerate)')
#How to print each element and the corresponding index with for ... each loop
# The 'enumerate' function is the most Pythonic way to get both the index and the element
# directly in a 'for each' style loop. It yields pairs (index, element).
for index, element in enumerate(a):
print("Index: {index}, Element: {element}")
print('For each loop (without 2nd variable for element, if strictly interpreted)')
# How to print each element and the corresponding index with for... each loop (Do not use 2nd variable)
# If "do not use 2nd variable" means not explicitly unpacking the element in the loop header,
# while still aiming for a 'for each' feel with index, it essentially reverts to an index-based approach.
# You iterate over indices and then access the element using that index.
# This is functionally similar to the "Indexed based for loop" above.
for index in range(len(a)):
# Here, 'index' is the only variable directly bound in the loop header. # we access the element 'a[index]' inside the loop body. print(f"Index: {index}, Element: {a[index]}")






7.
# Find outputs (Home work)
for x
in
():
print(x)
for x
in []:
print(x)
for x
in {}:
print(x)
for x
in set():
print(x)
for x
in
print(x)
for x in range(10, 10):
print(x)
for x in
range():
print(x)
print(x)
for x in (25):
output:
Here are the outputs for the 'for loops you provided:
# Output for: for x in ():
# (No output)
# Output for: for x in []:
# (No output)
# Output for: for x in {}: # (No output)
# Output for : for x in set(): # (No output)
#
Output for: for x in **:
# (No output)
# Output for: for x in range(10, 10): # (No output)
# Output for: for x in range():
# Traceback (most recent call last):
#
File "<stdin>", line X, in <module>
# TypeError: range expected at least 1 argument, got e
# Output for: for x in (25):
# Traceback (most recent call last):
#
File "<stdin>", line X, in <module> # TypeError: 'int' object is not iterable





8.
Program to Determine the Largest of Three Numbers
# Get three numbers as input from the user
try:
num1 = float(input("Enter the first number: ")) float(input("Enter the second number: ")) num3 = float(input("Enter the third number: "))
except ValueError:
else:
print("Invalid input. Please enter valid numbers.")
# Determine the largest number using if-else statements with multiple conditions
# Assume num1 is the largest initially
largest num1
# Compare num2 with the current largest if num2 > largest:
largest = num2
# Compare num3 with the current largest if num3 > largest:
largest = num3
print (f"\nThe numbers entered are: {num1}, {num2}, {num3}") print (f"The largest number is: {largest}")
# Alternative approach using nested if-else (as per "multiple conditions" hint) print("\n--- Alternative Method (using nested if-else) ---")
if num1 >= num2 and num1 >= num3:
print (f" The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
print (f"The largest number is: {num2}") else:
print (f"The largest number is: {num3}")





9.
Program to Determine Largest, Smallest, and Middle of Three Numbers ---
# Get three numbers as input from the user
try:
a = float(input("Enter first input : ")) b = float(input("Enter second input : ")) c = float(input("Enter third input: ")) except ValueError:
else:
print("Invalid input. Please enter numeric values.")
# Determine the largest number
max_num = a
if b max_num:
max numb
if c> max_num:
max _num = C
# Determine the smallest number
min_num = a
if bmin_num:
min_num = b
if c<min_num:
min_num = c
# Determine the middle number
# The sum of all three numbers minus the largest and smallest will give the middle number mid_num = (a + b + c) - (max_num + min_num)
# Print the results
print (f"Largest number : {max_num:.1f}") print (f"Smallest number : {min_num:.1f}") print(f"Middle number : {mid_num:.1f}")




10.
# Find outputs (Home work)
m = 2
match m:
case 1:
print('One')
case
print('Hello')
case
print('Bye')
print('End')
output:
Hello
End




11.
#
Electricity Bill Calculator
try:
units = int(input("Enter units : '))
if units < 0:
else:
print("Units cannot be negative. Please enter a non-negative number.")
bill amount = 0.0
# The match statement uses integer division (units // 100) to categorize units into slabs. # This effectively creates ranges for the match cases.
match units // 100:
case 0: # Covers units from 0 to 99
# All units fall into the first slab bill amount = units * 3.00
case 1: # Covers units from 100 to 199
# First 100 units at Rs. 3.00, remaining at Rs. 3.50 bill amount (100 3.00) + ((units - 100) * 3.50) case 2 | 3: # Covers units from 200 to 399
# First 100 units (8-99) at 3.00
# Next 100 units (100-199) at 3.50
# Remaining units (from 200 onwards) at 4.00 bill amount (100
3.00) + \
4.00)
(100 3.50) + ((units - 200)
case 4 | 5 | 6: # Covers units from 400 to 699
# First 100 units (0-99) at 3.00
# Next 100 units (100-199) at 3.50
# Next 200 units (200-399) at 4.00
# Remaining units (from 400 onwards) at 4.50 bill amount (100
3.00) + \
(100
3.50) +
(200
4.00) +
((units - 400) * 4.50)
case_: # This wildcard case handles units 700 and above (units // 100 >= 7) # First 100 units (0-99) at 3.00
# Next 100 units (100-199) at 3.50
# Next 200 units (200-399) at 4.00
# Next 300 units (400-699) at 4.50
# Remaining units (from 700 onwards) at 5.00
bill amount
(100
3.00) + \
(100
3.50) + \
(200 4.00) + \
((units - 700)
5.00)
(300 4.50) +
print(f"Bill amount (bill_amount:.2f}")
except ValueError:
print("Invalid input. Please enter a whole number for units.") except Exception as e:
print("An unexpected error occurred: {e}")





12.
• How to print each element of list [18, 22, 15, 18] with for loop
mylist [18, 20, 15, 18
print("Elements of the list:")
for iten in my
print()
How to print each character of string 'Hid" with for loop
print("Characters of the string:")
for char in my string:
print()
How to print each element of range(5) with for loop
print("ents of range(5):")
for nun in range(5):
print(num)
Nested Loop dana prag
print("---Nested Loop Demo) for i in range, 4):
farin range(1, 5) print(1, 1)
print("Hello")
print("")
Printing Elements with Index ---
- [25, 10.8, "Hyd", Trus]
print("Indeed based for loop")
How to print each element and the corresponding index with index based for loop for inde in range()):
print("Indec: Index), Element: [index]}")
print("For each loop (using enumerata)"}
How to print each element and the corresponding index with for
for index, alement in enumerate():
print Indec: Index), Element: fal}")
print("For each loop (without 2nd variable for alement, if strictly interpreted)")
How to print each element and the corresponding index with for each loop (Do not use 2nd variable) for inde in range());
print("Indec: Index), Element: [index]")
---Printing List Elements in Reverse Order
print("Indeed for loop (reverse order)")
How to print each element of list in reverse order with indeed based for loop
for inde in range(len(s)
print([index])
1,-1,-1)
print("For each loop (reverse order, without 2nd variable and slice)")
How to print each element of List in reverse order with for each loop (Do not use 2nd variable and allow) for index in range(len(s) 1, -1, -1)
print([index])
--- Add two lists and store results in 3rd list --
print
try:
Adding Two Lists)
- eval(input("Enter 1st list :")) b-eval(input("Enter 2nd at :")}
•Ensure inputs are list
if not instances, List) or not instance, list):
als:
print("Error: Please enter valid list formats (e.g., [12, 181-7)
[nitialize the third list
How to add lists 'a' and 'band store results in list 'e' with indeed based for loop
Weiterate up to the length of the shorter list to avoid Indecor.
minn minn),
for i in rang
))
print("ard list : ", c)
⚫ Reset for the next method demonstration
How to add lists 'a' and 'b' and store results in list 'c' with for each loop (Do not use 2nd variable)
• To avoid a second variable ("alent) while still performing alament-wise addition,
we still rely on indices. The for each concept here is adapted to iterate through indica
This is functionally similar to the indeed-based loop when element-wise operations are needed. for i in range(nin Jen): Iterate over indic
c.nd[[][])
Access elements using indices and append zu
print("ard list (for each loop method), c)
scat (Syntax,N):
print("Invalid list input. Make sure to use correct list syntax (... [1, 2, 3).") :
scot Reception
print An unexpected error occurred: {}")




13.
# Find outputs while False:
print('Hello')
print('Bye')
output:
Bye




14.
# How to print each element of list [10, 20, 15, 18] with for loop my list [10, 20, 15, 18]
print("Elements of the list: ")
for item in my list:
print(item)
print() # Prints an empty line for separation
# How to print each character of string 'Hyd' with for loop my string 'Hyd'
print("Characters of the string: ")
for char in my string:
print(char)
print() # Prints an empty line for separation
# How to print each element of range(5) with for loop print("Elements of range(5):")
for num in range(5):
print(num)
print() # Prints an empty line for separation
# Nested Loop demo program
print("--- Nested Loop Demo ---")
for i in range(1, 4):
for i in range(1, 5): print(i, j)
print('Hello')
print('Bye')
print() # Prints an empty line for separation
#--- Printing Elements with Index ---
== [25, 10.8, 'Hyd', True]
print('Indexed based for loop')
# How to print each element and the corresponding index with index based for loop
# This method uses range(len(list)) to get indices, then accesses elements by index. for index in range(len(a)):
print(f"Index: {index}, Element: {a[index]}")
print('For each loop (using enumerate)')
# How to print each element and the corresponding index with for... each loop
# The 'enumerate' function is the most Pythonic way to get both the index and the element
# directly in a 'for each' style loop. It yields pairs (index, element).
for index, element in enumerate(a):
print("Index: {index}, Element: {element}")
print('For each loop (without 2nd variable for element, if strictly interpreted)')
# How to print each element and the corresponding index with for... each loop (Do not use 2nd variable)
# If "do not use 2nd variable" means not explicitly unpacking the element in the loop header,
# while still aiming for a 'for each' feel with index, it essentially reverts to an index-based approach.
# You iterate over indices and then access the element using that index.
# This is functionally similar to the "Indexed based for loop" above.
for index in range(len(a)):
# Here, 'index' is the only variable directly bound in the loop header.
# We access the element a[index]' inside the loop body. print(f"Index: {index}, Element: (a[index]}")
print() # Prints an empty line for separation
#--- Printing List Elements in Reverse Order ---
print('Indexed for loop (reverse order)')
# How to print each element of list in reverse order with indexed based for loop
We use range(start, stop, step) to iterate from the last index down to 0.
# len(a) 1 is the last index. -1 is the stop (exclusive). -1 is the step (decrement).
for index in range(len(a) 1, -1, -1):
print(a[index])
print('For each loop (reverse order, without 2nd variable and slice)')
# How to print each element of list in reverse order with for each loop (Do not use 2nd variable and slice)
#To satisfy "for each loop" conceptually without a second variable (like 'element')
# and without using list slicing, we again iterate over indices in reverse and
# access the element using that index. This adheres to the constraints.
for index in range(len(a) 1, -1, -1):
print(a[index])




15.
# Find outputs (Home work)
for x in (10: 20, 30: 40, 50 60 keys():
print()
print(x)
for x in (10: 20, 30: 40, 50: 60}. values():
print()
print(x)
for x in (10 print(x)
28,
20 30
48, 50:
40 50 60}. items():
print()
for x in 10 20 30 40, 50: 60}:
outputs:
print(x)
Here are the outputs for the Python code you provided:
10
30
50
298
20
40
60
(10, 20) (30, 40) (50, 60)
10
30
50





16.
try:
Fibonacci Series Generator ---
x = int(input('Enter value of x : '))
if x < 0:
print("Please enter a non-negative integer for x.") elif x == 0:
print("Fibonacci Series")
# No output for x-e as series starts with 0 and 1 else:
print("Fibonacci Series")
# Initialize the first two terms of the Fibonacci series a, b = 0, 1
count = 0
# Print terms until the current term exceeds x
while a <= x:
print(a)
# Calculate the next term
next term = a + b
# Update a and b for the next iteration
a = b
b = next term
count += 1
except ValueError:
print("Invalid input. Please enter a whole number for x.") except Exception as e:
print (f"An unexpected error occurred: {e}")




17.
import math
#---
Program to Determine Triangle Properties print("--- Triangle Properties Calculator ---")
# Get the three side lengths from the user try:
side a = float(input("Enter the length of side A: ")) side b = float(input("Enter the length of side B: ")) side c = float(input("Enter the length of side c: ")) except ValueError:
print("Invalid input. Please enter numeric values for side lengths.")
else:
# Check if the sides can form a valid triangle
# Qualification: Sum of every two sides must be greater than the third side if (side a side b> side c) and \
(side a side c> side b) and
(side b + side c> side a):
print("\nThe given sides can form a triangle.")
# Determine triangle type and calculate properties using nested if-elif-else if side a == side b and side b == side_c:
else:
# Equilateral Triangle: All three sides are same
print("It is an Equilateral Triangle.")
# Area of equilateral triangle: sqrt(3) / 4* a^2
area (math.sqrt(3) / 4) * (side a ** 2)
perimeter = side a side b + side c# Perimeter is 3 * side a
print (f"Area: {area:.2f}")
print("Perimeter: {perimeter:.2f}")
elif side a == side b or side b == side c or side a == side c:
# Isosceles Triangle: Any two sides are same
print("It is an Isosceles Triangle.")
# Perimeter of isosceles triangle: a + b + c perimeter = side a side b + side c
print("Perimeter: {perimeter:.2f}")
# Note: Area calculation for isosceles is more complex and not requested for this type.
else:
# Scalene Triangle: All three sides are different
print("It is a Scalene Triangle.")
# Perimeter of scalene triangle: a + b + c
perimeter side a side b + side c
print (f"Perimeter: {perimeter:.2f}")
# Area of scalene triangle (Heron's formula): sqrt(s* (s - a) * (sb) * (s - c)) #'s' is the semi-perimeter: (a + b + c) / 2
S = perimeter / 2
# Check if the value under the square root is non-negative to avoid math domain error if s* (s side a) (s side b) * (s side_c) >= 0:
else:
area math.sqrt(s (s - side a) * (s side b) (s side_c)) print("Area: {area:.2f}")
print("Cannot calculate area (invalid side lengths for real triangle geometry).")
print("\nThe given sides cannot form a triangle.")




18.
# Find outputs (Home work)
ch = 'B' match
ch:
case
'A':
print('Apple')
case 'B':
print('Book')
case 'C':
print('Cafe')
case
print('Bye')
output:
Book
Bye
print('None of the above')



19.
Temperature Converter Program
def celsius_to_fahrenheit (celsius):
"""Converts temperature from Celsius to Fahrenheit.' return (celsius 1.8) + 32
def fahrenheit_to_celsius (fahrenheit):
"""Converts temperature from Fahrenheit to Celsius.""' return (fahrenheit - 32) / 1.8
print("--
---
Temperature Conversion ---")
print("1. Convert Celsius to Fahrenheit") print("2. Convert Fahrenheit to Celsius")
try:
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
temp_celsius = float(input("Enter temperature in Celsius: ")) converted_temp = celsius_to_fahrenheit (temp_celsius)
print (f" {temp_celsius}°C is equal to {converted_temp:.2f}°F") elif choice == '2':
temp_fahrenheit = float(input("Enter temperature in Fahrenheit: ")) converted_temp = fahrenheit_to_celsius (temp_fahrenheit)
else:
print (f" {temp_fahrenheit}°F is equal to {converted_temp:.2f}°C")
print("Invalid choice. Please enter 1 or 2.")
except ValueError:
print("Invalid temperature input. Please enter a numeric value.") except Exception as e:
print (f"An unexpected error occurred: {e}")



20.
Here are the outputs for each of the given inputs:
1) **what is the output when input is (-10-20) 2**
<-- and 1st -->
Quadrant
2) **What is the output when input is (100) 2** <-- and list -->
3) **What is the output when inputs (-20) 2** <-- and list -->
4) **what is the output when input is (0) 2**
<-- and 1st -->
Origin
*) **what is the output when input is (10, 20, 30) 2**
<-- and list -->
Not a point
6) **what is the output when input is [10, 20] ***
<-- and list -->
Not a point
7) **what is the output when input is [23] ***
<-- and 1st -->
Not a point
8) **What is the output when input is () 2**
<-- and list -->
Not a point
9) **what is the output when input is (1820) ***
<-- and list -->
Not a point
10) **What is the output when input is (25) 2**
<-- and list -->
Not a point
11) **what is the output when input is (1820) ***
<-- and list -->
Not a point





21.
# Identify Error
i = 2
match
i:
case 1:
case _:
case
2:
print('Bye')
print('One')
print('None of the above')
print('Two')
Error: case: must be the last case in a match statement.
Explanation: The wildcard case: matches any value. If placed before specific cases (like case 2:), those specific cases become unreachable. Python will issue a Syntaxwarning/Error for unreachable code.




22.
# Identify error (Home work)
for x in 123:
print(x)|
TypeError: 'int' object is not iterable.




23.
# Find outputs while True:
print('Hello')
print('Bye')
output:
Hello
Hello
Hello
(This will print "Hello" indefinitely)|




24.
#--- Temperature Converter Program
def celsius_to_fahrenheit (celsius):
"""Converts temperature from Celsius to Fahrenheit.""" return (celsius * 1.8) + 32
def fahrenheit_to_celsius (fahrenheit):
"""Converts temperature from Fahrenheit to Celsius."""
return (fahrenheit - 32) / 1.8
# The previous print statements for menu are no longer needed as per user's desired prompt
try:
# Updated prompt for choice
choice = input("Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : ")
if choice == '1':
# Updated prompt for Celsius input
temp_celsius = float(input("Enter celsius temperature : "))
converted_temp = celsius_to_fahrenheit (temp_celsius)
# Updated output format for Fahrenheit
# Using f-string with conditional formatting for .1f if it's a whole number, else .2f if converted_temp == int(converted_temp):
else:
print (f"Fahrenheit Equivalent: {converted_temp:.1f}")
print (f"Fahrenheit Equivalent: {converted_temp:.2f}")
elif choice == '2':
else:
# Updated prompt for Fahrenheit input
temp_fahrenheit = float(input("Enter fahrenheit temperature : ")) converted_temp = fahrenheit_to_celsius (temp_fahrenheit)
# Updated output format for Celsius
print (f"celsius equivalent: {converted_temp:.2f}")
# Updated invalid choice message print("Invalid input")
except ValueError:
print("Invalid temperature input. Please enter a numeric value.") except Exception as e:
print(f"An unexpected error occurred: {e}")




25.
# Find outputs (Home work)
m = 1 match
m:
case 1:
print('Hyd')
case 1:
print('Sec')
case 1:
print('Cyb')
print('Bye')
output:
Hyd
Bye




26.
# Find outputs (Home work)
a = {10: 20, 30: 40, 50: 60}
for x, y in
a. items():
print(x, y, sep =
for x, y in a:
print(x, y
for x, y in (10: 20, 30: 40, 50: 60}: print(x, y, sep = '.
output:
10...20
30...40
50...60
File "<stdin>", line 6
print(x, y
SyntaxError: unexpected EOF while parsing




27.
import math
#---
Program to Determine Roots of a Quadratic Equation
print("--- Quadratic Equation Roots calculator (ax^2 + bx + c = 0) ---")
# Get coefficients a, b, and c from the user
try:
a = float(input("Enter coefficient 'a': ")) b = float(input("Enter coefficient 'b': ")) c = float(input("Enter coefficient 'c': "))
except ValueError:
else:
print("Invalid input. Please enter numeric values for coefficients.")
# Check if 'a' is zero, as it's not a quadratic equation if a = e if a == 0:
else:
print("Error: Coefficient 'a' cannot be zero for a quadratic equation.")
# Calculate the discriminant
discriminant = (b**2) - (4 * a * c)
print("\nFor the equation {a}x^2 + {b}x+ {c} = 0:")
if discriminant > 0:
# Real and distinct roots
print("The roots are Real and Distinct.")
root1 = (-b+ math.sqrt(discriminant)) / (2* a)
root2 = (-b
math.sqrt(discriminant)) / (2* a)
print (f"Root 1: [root1:.2f}")
print("Root 2: (root2:.2f}")
elif discriminant == 0:
else:
# Real and same roots
print("The roots are Real and Same.")
root-b (2 a)
print("Root: {root:.2f}")
# Complex (or Imaginary) roots
print("The roots are complex (Imaginary).")
real part = -b (2 a)
imag part = math.sqrt(abs (discriminant)) / (2 a) # Use abs() for sqrt of negative print("Root 1: (real_part:.2f} + {imag part:.2f}j")
print("Root 2: (real_part:.2f} {imag part:.2f}j")
-



28.
# How to print each element of list [10, 20, 15, 18] with for loop my list [10, 20, 15, 18]
print("Elements of the list:")
for item in my list: print(item)
print() # Prints an empty line for separation
# How to print each character of string 'Hyd' with for loop my string 'Hyd'
print("Characters of the string:")
for char in my string: print(char)
print() # Prints an empty line for separation
# How to print each element of range (5) with for loop print("Elements of range(5):")
for num in range(5):
print(num)



29.
#
Leap Year Checker (User Input)
# Get year input from the user
try:
year = int(input("Enter a year to check if it's a leap year: ")) except ValueError:
else:
print("Invalid input. Please enter a whole number for the year.")
# Apply the leap year rule:
# A year is a leap year if it is divisible by 4 but not by 100, # OR if it is divisible by 400.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 print (f" {year} is a leap year.")
else:
print (f" {year} is not a leap year.")|
==
0):
