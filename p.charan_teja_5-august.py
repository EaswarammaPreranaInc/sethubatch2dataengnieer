1.
# Find outputs (Home work) a = (10, 20, 15, 18)
print(a) print(a[0]) del a[2]
del a
print(a) print (a[0])
output:
(10, 20, 15, 18)
10
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
del a[2]
TypeError: 'tuple' object doesn't support item deletion




2.
# Find outputs (Home work) for i in range(1, 8): print(i)
if i % 3 == 0:
else:
exit()
print('Sec')
print('Hello')
# End of the loop
print('Outside loop')
output:
1
Sec Hello
2
Sec Hello
3



3.
# Find outputs (Home work)
a = 0
if a == 0:
print('Hyd')
else:
print('Sec')
if b := 0:
print('Hyd')
else:
print('Sec :
, b)
if c = 0:
print('Hyd')
else:
print('Sec')
output:
Here are the outputs for the Python code you provided:
Hyd
Sec : 0
Traceback (most recent call last):
File "<stdin>", line 10
if c = 0:
SyntaxError: invalid syntax



4.
# Find outputs
(Home work)
for i in range(1, 8):
print(i)
if i == 8:
else:
break
print('Sec')
else:
print('Hello')
print('else suite')
# End of the loop
print('Outside loop')
output:
1
Sec Hello
2
Sec
Hello
3
Sec Hello
4
Sec Hello
5
Sec Hello
6
Sec Hello
7
Sec
Hello
else suite
Outside loop


5.
# Find outputs
(Home work)
for i in range(1, 8): print(i)
if i % 3 == 0:
else:
print('Hello')
# End of loop
print('Outside loop')
output:
1
Sec
Hello
2
Sec Hello
3
m 4
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop
continue
print('Sec')



6.
# Find outputs (Home work) [10, 20, 15, 18]
a = [10
print(a)
del a[2]
print(a)
del a print(a) print (a[0]) output:
[10, 20, 15, 18]
[10, 20, 18]
Traceback (most recent call last):
File "<stdin>", line 6, in <module> print(a)
NameError: name 'a' is not defined



7.
# Find outputs (Home work) for i in range(1, 8): print(i)
if i % 3 == 0:
else:
break
print('Sec')
print('Hello')
# End of the loop
print('Outside loop')
output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop



8.
# Find outputs (Home work)
for i
in range(1, 8): print(i)
if i % 3 == 0:
pass
print('Hyd')
else:
print('Sec')
print('Hello')
# End of the loop
print('Outside loop')
output:
1
Sec Hello
2
Sec
Hello
3
Hyd Hello
4
Sec
Hello
5
Sec Hello
6
Hyd Hello
7
Sec
Hello
Outside loop




9.
# Walrus operator (:=) demo program
print(a := 25)
# Assigns 25 to 'a' AND prints 25. Output: 25
# print(a = 25)
# ERROR: SyntaxError. '=' is a statement, not an expression. Cannot be in print().
# The following lines are unreachable due to the SyntaxError above.
# print(a)
# print(a = 6 + 7)
# print(a)
# print((a = 6) + 7)
# print(a)
# print((a = 6) + 7) # This would also be a SyntaxError.




10.
Can multiple objects be deleted with same del operator ? 25, 10.8, 'Hyd'
a, b, C =
print(a b c)
و
del a, b, c
print(a)
print(b)
print(c)
output:
25 10.8 Hyd
Traceback (most recent call last):
File "<stdin>", line 4, in <module> print(a)
NameError: name 'a' is not defined





11.
# Find outputs
(Home work)
for i in range(1, 8):
print(i)
if i % 3 == 0:
else:
continue
else:
print('Sec')
print('Hello')
print('else suite')
# End of the loop
print('Outside loop')
output:
1
Sec Hello
2
Sec Hello
3
4
Sec Hello
5
Sec Hello
6
7
Sec
Hello
else suite Outside loop



12.
# del operator demo program
a = 25
print(a)
del a
print(a)
# This line assigns the integer value 25 to the variable 'a'. # This line prints the current value of 'a'. # Output: 25
# This line uses the 'del' operator to delete the variable 'a'.
# After this line executes, the name 'a' is no longer bound to any object
# in the current scope. It's like 'a' never existed from this point on.
# This line attempts to print the value of 'a' again.
# However, 'a' has been deleted, so Python will raise a NameError
# because it cannot find a variable named 'a'.
# Output: NameError: name 'a' is not defined




13.
#
Program to Determine Average of Inputs (Terminated by Ctrl+Z)
---
total sum = 0.0 # Initialize sum to a float to handle decimal inputs count = 0 # Initialize count of numbers entered
print("Enter numbers one by one. Press Ctrl+Z (then Enter) to finish and calculate the average.")
while True:
try:
# Get input from the user
user_input = input("Enter a number: ")
# Convert the input to a number and add to sum
# Using float() to handle decimal numbers as well as integers
number float (user_input)
total_sum += number
count += 1
except EOFError:
# This error is raised when Ctrl+Z (Windows) or Ctrl+D (Unix/Linux/macOS) is pressed print("\nEnd of input detected.")
break # Exit the loop
except ValueError:
# This error is raised if the user enters non-numeric input print("Invalid input. Please enter a valid number.")
# Do not increment count or add to sum for invalid input
# Calculate and print the average after the loop terminates if count > 0:
else:
average total_sum / count
print(f"Total numbers entered: {count}")
print (f"Sum of numbers: {total_sum: .2f}")
print (f"Average of the numbers: {average:.2f}")
print("No numbers were entered to calculate an average.")





14.
# Find outputs (Home work) a = b = c = 25
print(a, b, c)
del
a
print(b, c) print(a) del b print(c) print(b) del c print(c) output:
25 25 25
25 25
Traceback (most recent call last):
File "<stdin>", line 5, in <module> print(a)
NameError: name 'a' is not defined



15.
#--- Program to Search for an Element in a List
# Get the list from the user
try:
my_list = eval(input("Enter the list (e.g., [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]): ")) if not isinstance(my_list, list):
raise ValueError("Input is not a list.")
except (ValueError, NameError, SyntaxError):
print("Invalid list input. Please enter a list in the correct format.")
exit() # Exit if list input is invalid
# Get the element to search for
try:
search_element = eval(input("Enter the element to search for: ")) except (ValueError, NameError, SyntaxError):
print("Invalid search element input.")
exit() # Exit if search element input is invalid
found_count = 0 # Counter to track how many times the element is found
# Iterate through the list using an indexed-based for loop
# This allows us to get both the element and its index
for index in range(len(my_list)):
# Check if the current list element matches the search element if my_list[index] == search_element:
print (f" {search_element} is found at index {index}") found_count += 1 # Increment the counter if found
# After the loop, check the found_count to determine final output if found_count > 0:
print (f"{search_element} is found {found_count} times") else:
print (f" {search_element} is not found")




16.
Program to Search for an Element in a List
# Get the list from the user
try:
my_list = eval(input("Enter the list (e.g., [10, 20, 15, 12, 18]); ")) if not isinstance(my list, list):
raise ValueError("Input is not a list.")
except (ValueError, NameError, SyntaxError):
print("Invalid list input. Please enter a list in the correct format.") exit() # Exit if list input is invalid
# Get the element to search for
try:
search_element
eval(input("Enter the element to search for: "))
except (ValueError, NameError, SyntaxError):
print("Invalid search element input.")
exit() # Exit if search element input is invalid
found = False # Flag to track if the element is found
# Iterate through the list using an indexed-based for loop
# This allows us to get both the element and its index
for index in range(len(my_list)):
# Check if the current list element matches the search element
if my list [index]
==
search_element:
print(f"Found at index (index)")
found = True # Set flag to True
break # Stop searching as element is found (no duplicates assumed)
# The 'else' block of a for loop executes only if the loop completes without a 'break' else:
# If 'found' is still False after the loop, it means the element was not found
if not found: # This check is redundant due to how for-else works, but for clarity print("Not found")



17.
# Find outputs (Home work) for i in range(1, 8):
print(i)
if i % 3 == 0:
else:
break
print('Sec')
else:
#End
output:
1
print('Hello')
print('else suite')
of the loop
print('Outside loop')
Sec Hello
2
Sec
Hello
3
Outside loop




18.
# Identify Error (Home work)
if ():
print('Hyd') continue print('Sec')
#The continue statement can only be used inside a for or while loop.




19.
# Identify Error (Home work)
if(10, 20, 30):
print('Hyd') break
print('Sec')
#The break statement can only be used inside a for or while loop.
