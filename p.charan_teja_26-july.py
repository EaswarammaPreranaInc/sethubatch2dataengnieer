1.
# Simple Interest Formula: (P
R) / 100 simple interest = (principal time rate) / 100
# Compound Interest Formula: P (1 + R / 100)^T - P
# Note: (1 + R/100) is the growth factor per period compound interest = principal * ((1+rate / 100) ** time)
principal
print (f"For Principal (principal), Time = {time} years, Rate= {rate}%:") print (f"Simple Interest = {simple_interest:.2f}") # Format to 2 decimal places print (f"Compound Interest = {compound_interest:.2f}") # Format to 2 decimal places
except ValueError:
print("Invalid input: Please enter valid numbers for principal, time, and rate.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to swap values of two objects using a third object. print("\n--- Swap Two Objects (using a third object) ---")
def swap with third object():
try:
# Get two inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc.
# NOTE: eval() carries security risks if used with untrusted input.
input x str = input("Enter the value for x: ")
input v str = input("Enter the value for y: ")
x = eval(input_x_str)
y = eval(input_y_str)
print (f"Before swap: x = {x}, y = {y}")
# Perform the swap using a third temporary variable
temp = x
x = y
y = temp
print(f"After swap: x = {x}, y = {y}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., "RAMA").")
except Exception as e:
print (f"An unexpected error occurred: {e}")
# --- Call the functions to run the programs
# call the function to run the largest of three program with user input
find largest of three()
# call the function to run the two input comparison program with user input compare two inputs()
# Call the function to run the number sign determination program with user input determine sign()
# call the function to run the even/odd check program with user input check_even_odd()
# Call the function to run the rectangle properties calculation program with user input calculate rectangle properties()
# call the function to run the sphere volume calculation program with user input calculate sphere.volume()
# Call the function to run the interest calculation program with user input calculate interest()
# Call the function to run the swap with third object program with user input swap with third object





2.
Program to determine the largest of three inputs without using the max() function. This program uses a nested ternary operator for finding the largest valus.
print("--- Determine the Largest of Three Inputs ---
Function to get input and determine the largest using a nested ternary operator def find largest of three):
try:
Gat three inputs from the user
Using eval() for flexibility as inputs can be numbers, strings, lists, etc. NOTE: eval() carries security risks if used with untrusted input. For this homework, it's used to match the varied input type. Input_st-input("Enter the first input for largest of three: ") Input2_xt-input("Enter the second input for largest of three:") Input_xt-input("Enter the third input for largest of three:")
vallaval{input_str)
vala – eval(input)
Determine the largest using a nested tarnary operator
Lager
If vall is greater than va12:
Then compare all with val. If all val, vall in largert, ale val is largest. Elas (val2 is greater than or equal to vall):
Then compare val with val. If val2 val, val2 in largest, ale val is largest. Largest vall i vall>val2 als va12
Largest largest if largest vald miss val
Alternatively, a single nested ternary (more compact but harder to read for complex logic): largest vall if all wall and vall>val
als (val2 17 val2> vall and val2> val is val)
A simpler single line for three distinct values:
largest
vall if wall wall and wall wall i
(val2 i val2 > vald eine val2)
printf The Inputs are: (val), (2), (
print The largest valus is: far)")
capt SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, tact, [1,2])) accept Na
print Invalid input: (). If entering strings, enclose then in quotes (... "RAM")")
cpt TypeGro
print("Comparison Error: ). Ensure inputs are comparable types (.g., all numbers, all strings, or all list).") at cptions:
printf unpected error occurred: {}")
• Program to print "", "", or based on the comparison of two inputs.
This program uses a ternary operator.
print("\n---Compere Two Inputs ---)
def compare two)
try:
Input_st-input("Enter the first input for comparison: Input2_xt-input("Enter the second input for comparison:
vall - eval(input_str) 12-valinput2_t)
Use a ternary operator to determine the comparison result rault="" if all > vall also ('' i valle val2 )
print("Comparing {vall) and (va12); (result)"}
accept Syntaar:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, tact, [1,2])) captar
print Invalid input: (). If entering strings, enclose then in quotes (... "RAM")")
coat Tyror:
print("Comparison Error: ). Ensure inputs are comparable types (.g., all numbers, all strings, or all list).") capt caption :
printf unpected error occurred: {}")
Program to determine the sign of a number [+1, -1, or 2).
This program uses a nested ternary operator.
print("\n--- Determine Number Sign")
der determine s
try:
nxt-input("Enter a number to determine its sign: ")
num-float(nu str) Convert to flost to handle decimals and integers
• Use a nested ternary operator to determine the sign
Logte:
If num > 2, result is 1
(n-2):
Ifnun, it is -1
fLns {num -- 2}, rarult is d
sign-1 if nun
alss (-1 if nun als 2)
printf The sign of (num) : sign)")
capt Valuar
print("Invalid input: Please enter a valid number.")
scot Rocaption
:
print An unexpected error occurred: {}")
Call the functions to run the program***
Call the function to run the largest of three program with user input





3.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")
vall eval(input1_str) val2 eval(input2_str) val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If val1 is greater than val2:
# Then compare vall with val3. If val1 > val3, val1 is largest, else val3 is largest. # Else (val2 is greater than or equal to val1):
#
Then compare val2 with val3. If val2> va13, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest
largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic): # largest = val1 if val1 > val2 and val1 > val3\
#
else (val2 if val2 > val1 and val2> val3 else val3)
# A simpler single line for three distinct values:
# largest = vall if val1 > val2 and val1 > val3 else \ (val2 if val2 > val3 else val3)
print (f"The inputs are: {val1}, {val2}, {val3}") print("The largest value is: (largest)")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
print("Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print("An unexpected error occurred: {e}")
Dronram to print 'NUME or haced on the comnaricon of twn innute





4.
# Program to determine the sign of a number (+1, -1, or e). # This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")
def determine sign():
try:
num str = input("Enter a number to determine its sign: ")
num = float(num str) # Convert to float to handle decimals and integers
# Use a nested ternary operator to determine the sign
# Logic:
#
If num > 0, result is 1
# Else (num <= 0):
# If num < 0, result is -1
#
Else (num == 0), result is e
sign = 1 if num > else (-1 if num < > else 0)
print (f"The sign of {num} is: {sign}")
except ValueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd # An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not 8).
result = "Even" if num % 2 == 0 else "odd"
print (f"The number {num} is: {result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---")
def calculate rectangle properties():
try:
length str = input("Enter the length of the rectangle: ") breadth str = input("Enter the breadth of the rectangle: ")
length = float(length, str)
breadth = float(breadth str)
if length <e or breadth < 0:
print("Length and breadth cannot be negative.")
return
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"For a rectangle with length (length} and breadth {breadth}:") print (f"Area = {area}")
print("Perimeter = {perimeter}")
except ValueError:
print("Invalid input: Please enter valid numbers for length and breadth.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine the volume of a sphere.
import math #Tmnart math module for ni and nour





5.
import math # Import math module for pi and power print("\n--- Calculate Sphere Volume ---")
def calculate sphere volume():
try:
radius str = input("Enter the radius of the sphere: ") radius= float(radius, str)
if radius < 0:
print("Radius cannot be negative.") return
# Volume of sphere formula: (4/3) * pi * г^3 volume = (4/3)* math.pi* (radius ** 3)
print (f"For a sphere with radius (radius}:")
print (f"Volume = {volume}")
except ValueError:
print("Invalid input: Please enter a valid number for the radius.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine simple interest and compound interest. print("\n--- Calculate Simple and Compound Interest ---")
def calculate interest():
try:
principal str = input("Enter the principal amount (P): ")
time str = input("Enter the time in years (T): ")
rate str = input("Enter the annual rate of interest (R, as a percentage): ")
principal = float (principal str)
time = float(time str)
rate = float(rate_str)
if principale or time <e or rate < 0:
print("Principal, time, and rate cannot be negative.")
return
# Simple Interest Formula: (P * T * R) / 100
simple interest = (principal time * rate) / 100
# Compound Interest Formula: P (1 + R / 100)^T - P
# Note: (1 + R/100) is the growth factor per period
compound interest = principal * ((1+rate / 100) ** time) - principal
print (f"For Principal = {principal}, Time = {time} years, Rate = {rate}%:") print("Simple Interest = (simple_interest: .2f}") # Format to 2 decimal places print (f"Compound Interest = (compound_interest:.2f}") # Format to 2 decimal places
except ValueError:
print("Invalid input: Please enter valid numbers for principal, time, and rate.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# --- call the functions to run the programs
# Call the function to run the largest of three program with user input
find largest of three()
# Call the function to run the two input comparison program with user input compare two inputs()
# Call the function to run the number sign determination program with user input determine sign()
# Call the function to run the even/odd check program with user input
check even odd()
# call the function to run the rectangle properties calculation program with user input calculate rectangle properties()




6.
# Program to determine the sign of a number (+1, -1, or e). # This program uses a nested ternary operator. print("\n--- Determine Number Sign ---")
def determine sign():
try:
num str = input("Enter a number to determine its sign: ")
num = float(num str) # Convert to float to handle decimals and integers
# Use a nested ternary operator to determine the sign
# Logic:
#
# Else (num <= 0):
If num > 0, result is 1
If nume, result is -1
#
#
Else (num == 0), result is e
sign = 1 if num > e else (-1 if num < e else e)
print (f"The sign of {num} is: {sign}")
except ValueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd. # This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even_odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd # An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not e).
result = "Even" if num % 2 == 0 else "Odd"
print (f"The number {num} is: {result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---")
def calculate rectangle properties():
try:
length str = input("Enter the length of the rectangle: ") breadth _str = input("Enter the breadth of the rectangle: ")
length = float(length_str) breadth = float(breadth_str)
if length <e or breadth < 0:
print("Length and breadth cannot be negative.")
return
area = length * breadth
perimeter = 2
(length
breadth)
print (f"For a rectangle with length (length} and breadth {breadth}:") print (f"Area = {area}")
print("Perimeter = {perimeter}")
except ValueError:
print("Invalid input: Please enter valid numbers for length and breadth.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine the volume of a sphere. import math # Import math module for pi and power






7.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: ") input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")
vall
eval(input1_str)
val2 = eval(input2_str)
val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If val1 is greater than val2:
#
Then compare vall with val3. If val1 val3, val1 is largest, else val3 is largest. # Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> val3, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest
largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic # largest = vali if val1 > val2 and val1 val3 \
#
else (val2 if val2 > val1 and val2> val3 else val3)
# A simpler single line for three distinct values:
# largest = vali if val1 > val2 and val1 > val3 else \ (val2 if val2 > val3 else val3)
#
print("The inputs are: {val1}, {val2}, {val3}")
print (f"The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text' except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").") except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all s except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs. # This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')






8.
3
<, or
based on the comparison of two inputs.
# Program to print # This program uses a ternary operator. print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ") vall
eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if vall > val2 else ('<' if val1 < val2 else '=')
print(f"Comparing (val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., "RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine the sign of a number (+1, -1, or e).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")
def determine sign():
try:
num str = input("Enter a number to determine its sign: ")
num = float(num str) # Convert to float to handle decimals and integers
# Use a nested ternary operator to determine the sign
# Logic:
# If num > 0, result is 1
# Else (num <= 0):
# If nume, result is -1
#
Else (num == 0), result is e
sign = 1 if num>e else (-1 if num < > else 0)
print (f"The sign of (num) is: {sign}")
except valueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd
# An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not e).
result = "Even" if num % 2 == 0 else "Odd"
print (f"The number {num} is: (result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---")
dof calculate rectangle nnnnortion/\.






9.
# Program to swap values of any two objects in a single statement # without using a third object.
# Initialize two objects with different types and values
x = 25
y = 'Hyd'
print (f"Before swap: x = {x}, y = {y}")
# Swap the values using Python's tuple unpacking (simultaneous assignment) # This swaps the references that x and y point to.
x, y = y, x
print (f"After swap: x = {x}, y = {y}")
# Another example with different types a = [10, 20]
b = {'city': 'Sec'}
print(f"\nBefore swap: a = {a}, y = {b}") a, b = b, a
print (f"After swap: a = {a}, y = {b}")
# Example with numerical values
num1 = 100
num2 = 200
print("\nBefore swap: num1 = {num1}, num2 = {num2}") num1, num2 = num2, num1
print (f"After swap: num1 = {num1}, num2 = {num2}")





10.
except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---") def calculate rectangle properties():
try:
length str = input("Enter the length of the rectangle: ") breadth str = input("Enter the breadth of the rectangle: ")
length
float(length_str)
breadth float (breadth, str)
if length <e or breadth < 0:
print("Length and breadth cannot be negative.")
return
area length breadth
perimeter = 2 * (length + breadth)
print (f"For a rectangle with length (length} and breadth {breadth}:") print(f"Area = {area}")
print("Perimeter = {perimeter}")
except ValueError:
print("Invalid input: Please enter valid numbers for length and breadth.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine the volume of a sphere.
import math # Import math module for pi and power
print("\n--- Calculate Sphere Volume ---")
def calculate sphere volume():
try:
radius str = input("Enter the radius of the sphere: ") radius= float(radius__str)
if radius < 8:
print("Radius cannot be negative.")
return
# Volume of sphere formula: (4/3) * pi * r^3 volume = (4/3)* math.pi (radius ** 3)
print (f"For a sphere with radius (radius}:")
print (f"Volume = {volume}")
except ValueError:
print("Invalid input: Please enter a valid number for the radius.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# --- call the functions to run the programs
# Call the function to run the largest of three program with user input find largest of three()
# Call the function to run the two input comparison program with user input compare two inputs()
# Call the function to run the number sign determination program with user input determine sign()
# Call the function to run the even/odd check program with user input
check even odd()
# call the function to run the rectangle properties calculation program with user input calculate rectangle properties()
# Call the function to run the sphere volume calculation program with user input calculate sphere.volume()






11.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: ") input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")
val1 = eval(input1_str) val2 eval(input2_str)
val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If vall is greater than val2:
# Then compare vall with val3. If vall› val3, val1 is largest, else val3 is largest.
# Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> va13, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest = largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic):
# largest = vali if valı > val2 and vali valз \
#
else (val2 if val2> val1 and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vall if val1 > val2 and val1 > val3 else \ (val2 if val2 > val3 else val3)
print("The inputs are: {val1}, {val2}, {val3}")
print (f"The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
print (f"Comparing {val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")






12.
# Program to print '>',
or '=' based on the comparison of two inputs.
# This program uses a ternary operator. print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
print (f"Comparing (val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine the sign of a number (+1, -1, or e).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")
def determine sign():
try:
num str = input("Enter a number to determine its sign: ")
num = float(num str) # Convert to float to handle decimals and integers
# Use a nested ternary operator to determine the sign
# Logic:
# If num > 0, result is 1
#Else (num <= 0):
#
#
If nume, result is -1
Else (num == 0), result is e
sign = 1 if num > e else (-1 if num < @ else 0)
print (f"The sign of {num} is: {sign}")
except ValueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = =int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd
# An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not e).
result = "Even" if num % 2 == 0 else "odd"
print (f"The number {num} is: {result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---")







13.
Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: ") input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")"
val1 = eval(input1_str) val2 eval(input2_str) val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If val1 is greater than val2:
# Then compare vall with val3. If val1 > val3, val1 is largest, else val3 is largest. # Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> val3, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest
largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic): # largest = val1 if val1 > val2 and val1 > val3 \
#
else (val2 if val2 > val1 and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vali if val1 > val2 and val1 > valз else \
#
(val2 if val2 > val3 else val3)
print("The inputs are: (val1}, {val2}, {val3}") print("The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str) val2 eval(input2 str)





14.
X = 25
print (F'{x}')
# Output: 25
# Explanation: A single pair of curly braces {} evaluates the expression x and inserts its value.
print(F'{{x}}')
# Output: {x}
# Explanation: Double curly braces {{ and }} are "escaped" and result in a single literal and respectively in the output. The `x inside is treated as a literal character because it's not within an unescaped pair of braces.
print(F'{{{x}}}')
# Output: {25}
# Explanation: This f-string has {{ (escaped to {), then {x} (evaluates x to 25), then }} (escaped to }). Effectively, it's '{' + str(x) + '}'`.
print('{{{{x}}}}')
# Output: {{x}}
# Explanation: {{{{ becomes {{ (two escaped pairs). x is literal. }}}} becomes }} (two escaped pairs).
print(F'{{{{{x}}}}}')
# Output: {{25}}
# Explanation: This breaks down to "{{ (escaped to ''), then "{{ (escaped to {), then {x} (evaluates to 25), then }} (escaped to }), then "}}" (escaped to }). Effectively, `'{{' + str(x) + '}}'`.
print(F'{{{{{{x}}}}}}')
# Output: {{{x}}}
# Explanation: Three escaped {{ pairs lead to {{{. Literal x. Three escaped }} pairs lead to "}}}".
print (F'{{{{{{{x}}}}}}}')
# Output: {{{25}}}
# Explanation: Three escaped ( pairs lead to {{{. Then '(x) evaluates to 25. Then three escaped }} pairs lead to }}}`.
print(F'{{{{{{{{x}}}}}}}}')
# Output: {{{{x}}}}
# Explanation: Four escaped {{ pairs lead to {{{{. Literal x. Four escaped }} pairs lead to }}}}.






15.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")
vall
eval(input1_str)
val2 eval(input2_str) val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If val1 is greater than val2:
# Then compare val1 with val3. If vall > val3, val1 is largest, else val3 is largest.
# Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> val3, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic):
# largest = vali if val1 > val2 and val1 > val3 \
#
else (val2 if val2> val1 and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vall if val1 > val2 and val1 > val3 else \
#
(val2 if val2 > val3 else val3)
print (f"The inputs are: {val1}, {val2}, {val3}")
print (f"The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., "RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
vall eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if vall > val2 else ('<' if val1 < val2 else '=')
print(f"Comparing {val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., "RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")






16.
X = 25
print (F'{x}')
# Output: 25
# Explanation: A single pair of curly braces {} evaluates the expression x and inserts its value.
print(F'{{x}}')
# Output: {x}
# Explanation: Double curly braces {{ and }} are "escaped" and result in a single literal and respectively in the output. The `x inside is treated as a literal character because it's not within an unescaped pair of braces.
print(F'{{{x}}}')
# Output: {25}
# Explanation: This f-string has {{ (escaped to {), then {x} (evaluates x to 25), then }} (escaped to }). Effectively, it's '{' + str(x) + '}'`.
print('{{{{x}}}}')
# Output: {{x}}
# Explanation: {{{{ becomes {{ (two escaped pairs). x is literal. }}}} becomes }} (two escaped pairs).
print(F'{{{{{x}}}}}')
# Output: {{25}}
# Explanation: This breaks down to "{{ (escaped to ''), then "{{ (escaped to {), then {x} (evaluates to 25), then }} (escaped to }), then "}}" (escaped to }). Effectively, `'{{' + str(x) + '}}'`.
print(F'{{{{{{x}}}}}}')
# Output: {{{x}}}
# Explanation: Three escaped {{ pairs lead to {{{. Literal x. Three escaped }} pairs lead to "}}}".
print (F'{{{{{{{x}}}}}}}')
# Output: {{{25}}}
# Explanation: Three escaped ( pairs lead to {{{. Then '(x) evaluates to 25. Then three escaped }} pairs lead to }}}`.
print(F'{{{{{{{{x}}}}}}}}')
# Output: {{{{x}}}}
# Explanation: Four escaped {{ pairs lead to {{{{. Literal x. Four escaped }} pairs lead to }}}}.





17.
# Program to print '>',
or '=' based on the comparison of two inputs.
# This program uses a ternary operator. print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
print (f"Comparing (val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine the sign of a number (+1, -1, or e).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")
def determine sign():
try:
num str = input("Enter a number to determine its sign: ")
num = float(num str) # Convert to float to handle decimals and integers
# Use a nested ternary operator to determine the sign
# Logic:
# If num > 0, result is 1
#Else (num <= 0):
#
#
If nume, result is -1
Else (num == 0), result is e
sign = 1 if num > e else (-1 if num < @ else 0)
print (f"The sign of {num} is: {sign}")
except ValueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = =int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd
# An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not e).
result = "Even" if num % 2 == 0 else "odd"
print (f"The number {num} is: {result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---")





18.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")
vall
eval(input1_str)
val2 eval(input2_str) val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If val1 is greater than val2:
# Then compare val1 with val3. If vall > val3, val1 is largest, else val3 is largest.
# Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> val3, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic):
# largest = vali if val1 > val2 and val1 > val3 \
#
else (val2 if val2> val1 and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vall if val1 > val2 and val1 > val3 else \
#
(val2 if val2 > val3 else val3)
print (f"The inputs are: {val1}, {val2}, {val3}")
print (f"The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., "RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
vall eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if vall > val2 else ('<' if val1 < val2 else '=')
print(f"Comparing {val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., "RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")





19.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: ") input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")
val1 = eval(input1_str) val2 eval(input2_str)
val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If vall is greater than val2:
# Then compare vall with val3. If vall› val3, val1 is largest, else val3 is largest.
# Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> va13, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest = largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic):
# largest = vali if valı > val2 and vali valз \
#
else (val2 if val2> val1 and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vall if val1 > val2 and val1 > val3 else \ (val2 if val2 > val3 else val3)
print("The inputs are: {val1}, {val2}, {val3}")
print (f"The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
print (f"Comparing {val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")







20.
Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest of three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input. # For this homework, it's used to match the varied input types. input1_str = input("Enter the first input for largest of three: ") input2_str = input("Enter the second input for largest of three: ") input3_str = input("Enter the third input for largest of three: ")"
val1 = eval(input1_str) val2 eval(input2_str) val3 = eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If val1 is greater than val2:
# Then compare vall with val3. If val1 > val3, val1 is largest, else val3 is largest. # Else (val2 is greater than or equal to val1):
# Then compare val2 with val3. If val2> val3, val2 is largest, else val3 is largest. largest val1 if val1 > val2 else val2
largest
largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic): # largest = val1 if val1 > val2 and val1 > val3 \
#
else (val2 if val2 > val1 and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vali if val1 > val2 and val1 > valз else \
#
(val2 if val2 > val3 else val3)
print("The inputs are: (val1}, {val2}, {val3}") print("The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str) val2 eval(input2 str)






21.
print(f"The sign of (num} is: {sign}")
except ValueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print("An unexpected error occurred: {e}")
# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd # An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not 8).
result = "Even" if num % 2 == 0 else "odd"
print (f"The number {num} is: {result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine area and perimeter of a rectangle. print("\n--- Calculate Rectangle Area and Perimeter ---")
def calculate rectangle properties():
try:
length_str = input("Enter the length of the rectangle: ") breadth str = input("Enter the breadth of the rectangle: ")
length = float(length_str) breadth = float(breadth_str)
if length <e or breadth < 0:
print("Length and breadth cannot be negative.")
return
area length
breadth
*
perimeter = 2 (length + breadth)
print(f"For a rectangle with length (length} and breadth {breadth}:") print("Area (area)")
print("Perimeter = {perimeter}")
except ValueError:
print("Invalid input: Please enter valid numbers for length and breadth.") except Exception as e:
print (f"An unexpected error occurred: {e}")
call the functions to run the programs
# call the function to run the largest of three program with user input find largest of three()
# call the function to run the two input comparison program with user input compare two inputs()
# Call the function to run the number sign determination program with user input determine sign()
# call the function to run the even/odd check program with user input
check even odd()
# Call the function to run the rectangle properties calculation program with user input calculate rectangle properties()





22.
largest = vali if val1 val2 and val1 > val3 else \
(val2 if val2 > val3 else val3)
print(f"The inputs are: {val1}, {val2}, {val3}")
print("The largest value is: (largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs
def compare two inputs():
try:
input1_str = input("Enter the first input for comparison: ") input2_str = input("Enter the second input for comparison: ")
val1 = eval(input1_str)
val2 = eval(input2_str)
# Use a ternary operator to determine the comparison result
result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
print (f"Comparing {val1} and {val2}: {result}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA").")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print(f"An unexpected error occurred: {e}")
# Program to determine the sign of a number (+1, -1, or e).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")
def determine sign():
try:
num str = input("Enter a number to determine its sign: ")
num = float(num_str) # Convert to float to handle decimals and integers
# Use a nested ternary operator to determine the sign
# Logic:
# If num > 0, result is 1
#Else (num <= 0):
#
If num < 0, result is -1
# Else (num == 0), result is e
sign = 1 if num > else (-1 if num < > else 0)
print (f"The sign of (num} is: (sign}")
except valueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even odd():
try:





23.
# Program to determine the largest of three inputs without using the max() function. # This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")
# Function to get input and determine the largest using a nested ternary operator def find largest_of_three():
try:
# Get three inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc.
# NOTE: eval() carries security risks if used with untrusted input.
# For this homework, it's used to match the varied input types.
=
input1_str input2_str = input3_str
=
input("Enter the first input: ")
input("Enter the second input: ")
input("Enter the third input: ")
val1 = eval(input1_str) val2 eval(input2_str)
=
=
val3 eval(input3_str)
# Determine the largest using a nested ternary operator
# Logic:
# If vall is greater than val2:
# Then compare vall with val3. If vall > val3, vall is largest, else val3 is largest. # Else (val2 is greater than or equal to vall):
# Then compare val2 with val3. If val2 > val3, val2 is largest, else val3 is largest. largest = vall if val1 > val2 else val2
largest
=
largest if largest > val3 else val3
# Alternatively, a single nested ternary (more compact but harder to read for complex logic): # largest = vall if vall > val2 and val1 > val3 \
#
else (val2 if val2 > vall and val2 > val3 else val3)
# A simpler single line for three distinct values:
# largest = vall if val1 > val2 and val1 > val3 else \
#
(val2 if val2 > val3 else va13)
print (f"The inputs are: {val1}, {val2}, {val3}")
print (f" The largest value is: {largest}")
except SyntaxError:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).") except NameError as e:
print (f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
print (f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Call the function to run the program with user input
find largest_of_three()





24.
Get input from the user for
For the cample output (18 and 7), you can uncomment the lines below and comment out the input lines.
try:
nutrinput("Enter the first number:
nun2_str - input("Enter the second number: ")
• Convert inputs to appropriate numeric types
We'll try to convert to flost first to handle decimals,
⚫ but some operations like factorial require integers.
* For factorial and GCD, we'll cast to int.
nun-flat(nur)
print("\nResults ---")
print What is the sun? ---> { result)")
Difference
difference result-un- un
print("What is the difference? --> difference_result}")
• Product
product, result - nun nu
printf What is the product? ---> product_t}")
Quotient (floating-point division)
quotient, result - n/
print What is the quotient? (quotient result:.2") Formatted to 2 decimal places
print("What is the quotient? ---> Cannot divide by zero.")
Remainder (modulo operator)
*Note: Modulo work correctly with floats, but if you expect integer remainder,
print What is the remainder?remainder rel}")
print("What is the remainder? Cannot calculate remainder with zero divizor.")
• Largest and Small
print What is the largest number? ---> Large_bar)")
print? What is the smallest number?-> {mallest number)}")
• Square root of first input
print What is the sort of 1st input? ---> {eart_result: 293) Formatted to 2 decimal places
print("What is the art of let input? Canet calculate square root of a negative number.")
Power (first input raised to the power of second input)
Using built-in pow() which handles fists
print("What is the result of power?(ul)")
GOD (Greatest Common Ever)
nath.pod requires integer arguments.
god result-math.god[num_int, num2_int)
print("What is the god of 2 numbers? --> {god, result)"}
*Factorial of first input
if un- and numinum_int: Check if it's a non-negative whole number
factorial result-math.factorial(num_int)
print What is the factorial of let input? ---> {num_int} - {factorial_result}")
print("What is the factorial of 1st input? Factorial is defined for non-negative integers only.")
print("Invalid input. Please enter valid numbers.")
printf An arrar assured: {}")





25.
import math # Import math module for pi and power
print("\n--- Calculate Sphere Volume ---")
def calculate sphere volume():
try:
radius str = input("Enter the radius of the sphere: ") radius= float(radius__str)
if radius < 0:
print("Radius cannot be negative.") return
# Volume of sphere formula: (4/3) * pi * r^3 volume = (4/3) * math.pi* (radius ** 3)
print (f"For a sphere with radius {radius}:") print("volume = {volume}")
except ValueError:
print("Invalid input: Please enter a valid number for the radius.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to determine simple interest and compound interest. print("\n- Calculate Simple and Compound Interest ---")
def calculate interest():
try:
principal str = input("Enter the principal amount (P): ")
time str = input("Enter the time in years (T): ")
rate str = input("Enter the annual rate of interest (R, as a percentage): ")
principal = float(principal str)
time = float(time str)
rate = float(rate str)
if principale or time <e or rate < 0:
print("Principal, time, and rate cannot be negative.")
return
# Simple Interest Formula: (P* T * R) / 180
simple interest = (principal time * rate) / 100
# Compound Interest Formula: P * (1 + R / 100)^T - P
# Note: (1 + R/100) is the growth factor per period
compound interest = principal ((1+rate / 100) ** time) - principal
print(f"For Principal = {principal}, Time = {time} years, Rate = {rate}%:") print("Simple Interest = {simple_interest: .2f}") # Format to 2 decimal places print (f"Compound Interest = {compound_interest:.2f}") # Format to 2 decimal places
except ValueError:
print("Invalid input: Please enter valid numbers for principal, time, and rate.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to swap values of two objects using a third object. print("\n--- Swap Two Objects (using a third object) ---")
def swap with third object():
try:
# Get two inputs from the user
# Using eval() for flexibility as inputs can be numbers, strings, lists, etc. # NOTE: eval() carries security risks if used with untrusted input.
input x_str = input("Enter the value for x: ")
input v str = input("Enter the value for y: ")
x = eval(input_x_str)
y = eval(input y str)
print(f"Before swap: x = {x}, y = {y}")
# Perform the swap using a third temporary variable






26.
# Find outputs (Home work)
X = 25
y = F'{x}'
# Explanation: `x` is an integer. In an f-string, the expression inside `{}` is evaluated,
# and its string representation (`str(x)`) is embedded. So, `y` becomes the string '25'. print(y)
# Output: 25 print(type(y))
# Output: <class 'str'>
# Explanation: The result of an f-string expression is always a string.
X = 10.8
y = F'{x}'
# Explanation: `x` is a float. `str(10.8)` results in '10.8'. So, `y` becomes the string '10.8'. print(y)
# Output: 10.8
print(type(y))
# Output: <class 'str'>
# Explanation: The result of an f-string expression is always a string.
X = [10,20,30,40]
y = F'{x}'
# Explanation: `x` is a list. `str([10, 20, 30, 40])` results in '[10, 20, 30, 40]'.
# So, y becomes the string '[10, 20, 30, 40]'.
print (y)
# Output: [10, 20, 30, 40]
print(type(y))
# Output: <class 'str'>
# Explanation: The result of an f-string expression is always a string.




27.
# Find outputs (Home work)
a, b, c = 25, 10.8, 'Hyd'
# Explanation: Variables a, b, and c are initialized with an integer, a float, and a string respectively.
print(F'{a} \t {b} \t {c}')
# Output: 25
10.8
Hyd
# Explanation: This is an f-string. Variables `a`, `b`, and `c` are evaluated and inserted into the string. # '\t' inserts a tab character, creating horizontal spacing.
print(F'a = {a} \t b = {b} \t c = {c}')
# Output: a = 25 b 10.8 c = Hyd
# Explanation: This is an f-string. Literal text "a ", "b = ",
is included along with the evaluated values of
`b`, and `c`, separated by tabs.
c='Hyd'
print(F'{a} \t {b=} \t {c=}')
# Output: a=25 b=10.8
# Explanation: The = sign inside the f-string curly braces (Python 3.8+) allows for "debug f-strings".
# It prints the expression text (`a`, `b`, `c`), an equals sign =`, and then the representation of the value.
# Strings like 'Hyd' are printed with their quotes.
print(F'{a:} \t {b:} \t {c:}')
# Output: 25
10.8 Hyd
# Explanation: Including a colon : after the variable name in an f-string, but without any specific format specifier,
# is equivalent to just `{variable_name}`. It simply embeds the string representation of the variable.
print('a = {a} \t b = {b} \t c = {c}')
# Output: a = {a} b = {b}
c = {c}
# Explanation: This is a regular string literal (it does *not* have an `F' or `f' prefix).
# Therefore, `{a}`, `{b}`, and `{c}` are treated as literal characters within the string, not as placeholders for variables. print (F'a = a \t b = b \t c = c')
# Output: a = a b = b
C = C
# Explanation: This is an f-string, but the characters 'a', 'b', 'c' within the string are not enclosed in curly braces. # Thus, they are treated as literal characters, not as variables to be evaluated.
print (F'{x} \t {y =} \t {z =}')
# Output: NameError: name 'x' is not defined
# Explanation: In the current scope, variables `x`, `y`, and `z have not been defined. Only `a`, `b`, and `c` exist.
# Attempting to use an undefined variable within an f-string (especially with the = debug specifier, which tries to evaluate it) # results in a `NameError. The program execution stops at this line.






28.
except ValueError:
print("Invalid input: Please enter a valid number.") except Exception as e:
print (f"An unexpected error occurred: {e}")
# Program to test if an input number is even or odd. # This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")
def check even_odd():
try:
num str = input("Enter an integer to check if it's even or odd: ") num = int(num str) # Convert to integer
# Use a ternary operator to determine if the number is even or odd # An even number is divisible by 2 (remainder is 0).
# An odd number is not divisible by 2 (remainder is not e).
result = "Even" if num % 2 == 0 else "Odd"
print (f"The number {num} is: {result}")
except ValueError:
print("Invalid input: Please enter a valid integer number.") except Exception as e:
#---
print("An unexpected error occurred: {e}")
Call the functions to run the programs
# Call the function to run the largest of three program with user input find largest of three()
# call the function to run the two input comparison program with user input compare two inputs()
# call the function to run the number sign determination program with user input determine sign()
# Call the function to run the even/odd check program with user input
check even odd()
# --- Test Cases for determine sign (Uncomment to run directly without manual input)
# print("\n--- Test Cases for Number sign ---")
# # Test Case 1: Negative input
#num-25
# sign = 1 if num > e else (-1 if num < e else 0)
# print(f"The sign of {num} is: {sign}") # Expected: -1
# # Test Case 2: Positive input
#num = 75
#sign = 1 if num > e else (-1 if num < e else e)
# print(f"The sign of {num} is: {sign}") # Expected: 1
# # Test Case 3: Zero input
#num = 0
# sign = 1 if num > e else (-1 if num < e else 0)
# print(f"The sign of {num} is: {sign}") # Expected:
# # Test Case 4: Positive float
#num 15.5
#sign = 1 if num > else (-1 if num <e else 0)
# print(f"The sign of {num} is: {sign}") # Expected: 1
# # Test Case 5: Negative float
#num -0.001
# sign = 1 if num > e else (-1 if num <e else 0)
# print(f"The sign of {num} is: {sign}") # Expected: -1
# --- Test Cases for check even odd (Uncomment to run directly without manual input)
# print("\n--- Test Cases for Even/Odd Check ---")





29.
Program to determine the largest of three inputs without using the max() function. * This program uses a nested tamary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---"y
*Function to get input and determine the largest using a nested ternary operator def find, Larpast, of three():
try:
Get the inputs from the
Using eval() for flexibility as inputs can be numbers, strings, lists, etc. NOTE: eval() carries security risks if used with untrusted input. *For this homework, it's used to match the varied input types. Input_xt-input("Enter the first input for largest of three: ") Input_xt-input("Enter the second input for largest of thras: ") Input_xt-input("Enter the third input for largest of three: ")
vall - eval{input_str)
val-valt)
* Determine the largest using a nastad ternary operator
Lage:
If all is greater than 12:
Then compare all with vall. If all val, vallis largest, ale val is largest. Else (val2 is greater than or equal to vall):
Then compare val2 with val. It val2 val, va12 in largest, ale val in largest. Largest vall i all val la val
Largest-largest if largest
val val
Alternatively, a single nested tamery (more compact but harder largest vall i vall val
A simple largest
size (val2 i
val2 and vall
val2> vall and val2> valaize val)
single line for three distinct values:
vall if vall val2 and vall>vall als (val2 + 12 > valle val)
complex lagle):
print The inputs are: (val), (12), {vnt}")
printf The Largest valus in: (largest)")
Except Syntrar:
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'test', [1,2])-"))
print Invalid input: (a). If entering strings, enclose then in quotes (... RAMA"))
capt Typirar as
print("Comparison Error: (). Ensure inputs are comparable types (.g., all numbers, all strings, or all lists).") opt Reception:
print("An unpacted error occurred: ()")
* Program to print "", "", or based on the comparison of two inputs.
This program uses a ternary operator.
print("--- Compare Two Input ---
def comer, two int():
try:
Input_xt-input Enter the first input for comparison:") Input_xt-input("Enter the second input for comparison: "
vall - eval{input_str)
12_)
Use a ternary operator to determine the compet
print("Comparing vall) and (val2): (ul)")
at Synt
print("Invalid input: Please ensure inputs are valid Python literals (e.g., 18, 3.5, 'test', [1,2])-")) captar a:
print("Invalid input: (a). If entering strings, enclose then in quotes (... RAMA"))
capt Tyra
print("Comparison Error: (). Ensure inputs are comparable types (.g., all numbers, all strings, or all lists).") capt Reception :
print("An unpacted error occurred: {}")
Call the functions to run the programs --
Call the function to run the largest of three program with user input
Find Largest of the()
Call the function to run the two input comparison program with user input
+--- Test Cases for compere, two, nuts (Uncomment to run directly without manual input) ---
# print("\n--- Test Cases for Two Input Comparison---")
Test Case 1: et ingut 2nd nut
vall, val2-18, 22
result - ">" if vall > vall size ('e' if valle val2 size '-') print("Comparing vall) and (v12): (rault)")⚫pected:
Test Case 2: Let Input 2nd nut
result - ">' if vall>vall size ('e if all val2 -")
# print("Comparing vall) and (v12): {ult)") Ropected:
Test Case 2: nuts are
result - ">" if vall>vall size ('e' i valle val2 size"-") # print("Comparing vall) and (v12): mult)") Ropected: -
**Test Case 4: Strings





30.
#Find outputs a, b, c = 25 print (F'{a} \t print(F'a = {a} print (F' {a} \t print(F'{a:} \t print('a print (F'a = a
=
(Home work)
و
10.8, 'Hyd' {b} \t {c}')
\t b = {b} \t c = {c}')
{b=} {b:}
{a} \t b
print (F'{x =} \t
\t b
=
{y =}
\t {c=}')
\t {c:}')
= {b} \t c
b \t c
=
\t {z =}')
=
{c}')
c')
