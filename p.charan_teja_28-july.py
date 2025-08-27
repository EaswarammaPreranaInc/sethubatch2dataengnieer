1.
# Define the two complex numbers
# A complex number is represented as (real part, imaginary_part)
complex1_real = 3
complex1_imaginary = 4
complex2_real = 5
complex2_imaginary = 6
print (f"First complex number: ((complex1_real} + {complex1_imaginary}j)")
print (f"Second complex number: ({complex2_real} + {complex2_imaginary}j)\n")
#
Addition
sum_real = complex1_real + complex2_real
sum imaginary = complex1_imaginary + complex2_imaginary
print (f"Sum: ({complex1_real} + {complex1_imaginary}j) + ((complex2_real} + {complex2_imaginary}j) = {sum_real} + {sum_imaginary}j")
Subtraction ---
diff_real = complex1_real complex2_real
diff imaginary complex1_imaginary complex2_imaginary
print (f"Difference: ({complexi real} + {complex1_imaginary}j) ({complex2_real} + {complex2_imaginary}j) = {diff_real} + {diff_imaginary}j") #Multiplication ---
# Formula: (a + bj) (c + dj) = (acbd) + (ad + bc)j
prod_real = (complex1_real* complex2_real) - (complex1_imaginary * complex2_imaginary)
prod_imaginary = (complex1_real complex2_imaginary) + (complex1_imaginary complex2_real)
print("Product: ({complexi_real} + {complex1_imaginary}j) * ({complex2_real} + {complex2_imaginary}j) = {prod_real} + {prod_imaginary}j")
# --- Division
# Formula: (a + bj) / (c + dj) = [(ac + bd) + (bc - ad)j] / (c^2 + d^2)
denominator = (complex2_real**2)+(complex2_imaginary**2)
if denominator == 0:
else:
print("Error: Division by zero is not allowed.")
div_real = ((complex1_real * complex2_real) + (complex1_imaginary complex2_imaginary)) / denominator
div_imaginary = ((complex1_imaginary complex2_real) - (complex1_real complex2_imaginary)) / denominator
print (f"Division: ({complex1_real} + {complex1_imaginary}j) / ({complex2_real} + {complex2_imaginary}j) = {div_real:.4f} + {div_imaginary:.4f}j") # Formatted to 4 decimal places





2.
if (10,20,15): print('Hyd')
else: print('Sec') correct version:
if (10,20,15):
else:
# The tuple is non-empty → truthy so the condition passes
# Not indented under the `if statement
# Missing colon? No colon is present, but indentation context is wrong # Not indented under the `else block
# Tuple is non-empty (truthy) print('Hyd') # Properly indented under `if`
print('Sec') print('Done')
# Colon is required after `else` # Properly indented under `else
# This runs after the if-else block





3.
if (10: 20, 30: 40}:
print('Hyd') print('Sec')
print('Cyb')
# No else branch here
print('Bye')
#{10:20,30:40} is a non-empty dict→ Truthy
# Runs
# Runs afterwards regardless of condition
Hyd
Sec
Cyb
Bye





4.
if():
else:
#
SyntaxError: missing a condition inside ()`-Python expects a valid expression or none print('One') # Intended to run when `if` is True, but code fails before reaching here print('Two')
print('Three')
print('Hyd')
# Valid else block, but never reached due to earlier syntax error
print('Sec')
print('Cyb') print('Bye')
correct version:
# This will run if code parsed successfully, but parsing fails earlier
# Example using an empty tuple condition: `()` is falsey
if ():
print('One') print('Two') print('Three')
# Not executed (since ()` is False)
else:
# Executes because `()` is False
print('Hyd') print('Sec') print('Cyb')
print('Bye')
# Executes after conditional logic






5.
while True:
user_input = input("Enter month number (1-12): ") try:
month_num = int(user_input)
except ValueError: # Handles non-integer input print("Input should be an integer") continue
else:
break # Exit loop if conversion succeeded
# Now check month range using if, elif if month_num == 1:
print("January")
elif month_num == 2: print("February")
elif month_num == 3:
print("March")
elif month_num == 4:
print("April")
elif month_num
== 5:
print("May")
elif month_num == 6:
print("June")
elif month_num == 7:
print("July")
elif month_num
== 8:
print("August")
elif month_num == 9: print("September")
elif month_num == 10: print("October")
elif month_num == 11:
print("November")
elif month_num == 12:
else:
print("December")
print("Input should be between 1 and 12")





6.
if ():
print('Hyd') print('Sec')
# {} is an empty dict evaluates as False in boolean context contentReference[oaicite: 1]{index=1} # This block is skipped because the condition is False
print('Cyb')
print('Bye')
# Runs unconditionally after the if
output:
Bye




7.
if 9 > 12: print('Hyd')
else
print('Sec')
correct version: if 9 > 12:
print('Hyd')
else:
print('Sec')
print('Bye')
# This has a colon and is syntactically valid
# Missing colon leads to SyntaxError: invalid syntax
# Keeps the necessary colon
# | Added colon here
# This will always run afterward





8.
# The following line is missing a colon `:` at the end
if 9 > 5 # | SyntaxError: invalid syntax - Python expects a colon here print('Hello') # This line won't execute because the above line is invalid
print('Bye')
# This line is fine but never runs due to the prior syntax error





9.
if ():
else:
# The condition is an empty tuple evaluates to False print('Hyd') # This must be indented under the `if` block # Else has proper colon
print('Sec') # This must be indented under the `else` block
print('Bye')
correct version:
if ():
# This is at top level and prints last
# Condition is an empty tuple (False)
# Indented under `if` – runs if tuple truthy (it isn't)
print('Hyd')
else:
print('Sec')
# Indented under `else`
print('Bye')
executes since `if` is False
# Outside both blocks - always executes last





10.
if {}:
{
print('One')
print('Two')
print('Three')
}
else:
{
print('Four')
print('Five')
print('six')
}
# Curly braces {} are not control flow in Python # Invalid block attempt
print('Bye')
correct version:
if True:
print('One')
print('Two')
print('Three')
# Example condition - could be any boolean
else:
print('Four')
print('Five')
print('six')
print('Bye')






11.
num = int(input("Enter a number: ")) # Read input and convert to integer
if num % 2 == 0:
else:
print (f" {num} is Even")
print(f" {num} is Odd")
# `% 2` returns for even numbers
# This block runs if the condition is True
# This runs when the condition is False




12.
# `if` must appear before `else: on the same indentation level # without it, Python triggers a `SyntaxError: invalid syntax`
else:
print('else suite') print('Outside')
# SyntaxError: `else has no matching `if`
# Python doesn't know what to execute when (no preceding condition) # This is valid only if the earlier block parsed successfully





13.
# Prompt the user for input
num_str = input("Enter a digit (0-9): ")
# Validate it's a single character and a digit if len(num_str) != 1 or not num_str.isdigit(): print("Invalid")
else:
n = int(num_str)
if n == 0:
else:
print("Zero")
if n == 1:
else:
print("One")
if n == 2:
else:
print("Two")
if n == 3:
else:
print("Three")
if n == 4:
print("Four")
else:
if n == 5:
else:
print("Five")
if n == 6:
else:
print("Six")
if n == 7:
else:
print("Seven")
if n == 8:
else:
print("Eight")
if n == 9:
else:
print("Nine")
print("Invalid")





14.
if ():
else:
print('One') print('Two') print('Three')
if []:
print('Four')
# Valid: empty tuple → False
# SyntaxError: `else: must be followed by an indented block, not another 'if' with no indentation
print('Five')
print('Six')
else:
if {}:
# Same problem repeated
print('Seven')
print('Eight')
print('Nine')
else:
print('Hyd')
print('Sec')
print('Cyb')
print('Bye')
correct version:
if ():
print('One') print('Two') print('Three')
# () → False
elif []:
# [] → False
print('Four')
print('Five')
print('Six')
elif {}:
# {}
→ False
print('Seven')
print('Eight')
print('Nine')
else:
print('Hyd')
print('Sec') print('Cyb') print('Bye')
# Always executes at the end
