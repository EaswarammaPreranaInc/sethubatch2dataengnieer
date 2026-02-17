#TARUN BANALA         13-09-2025
#  How  to  iterate  generator  with  for  loop
import  time  # Import time module for sleep functionality
def   f1():  # Define generator function f1
	print('One')  # Print 'One' when generator starts
	yield  25  # Yield value 25
	print('Two')  # Print 'Two' after first yield
	yield  10.8  # Yield value 10.8
	print('Three')  # Print 'Three' after second yield
	yield  'Hyd'  # Yield string 'Hyd'
	print('Four')  # Print 'Four' after third yield
# End  of  generator
g = f1()  # Create generator object
for   x   in   g:  # Iterate through generator using for loop
	print(x)  # Print yielded value
	time . sleep(1)  # Pause execution for 1 second
	print('Hello')  # Print 'Hello' after each yield
# End  of  for  loop
print('End')  # Print 'End' after loop completion
print(g)  # Print generator object reference
print(next(g))  # Try to get next value from exhausted generator 
g = f1()  # Create new generator object
print(next(g))  # Get first value from new generator
# Most  tricky  program

# Find  outputs(Home  work)
import  time  # Import time module
def   f1():  # Define simpler generator function
	yield  25  # Yield value 25
	yield  10.8  # Yield value 10.8
	yield  'Hyd'  # Yield string 'Hyd'
# End  of  generator
g = f1()  # Create generator object
print(next(g))  # Get and print first value (25)
for  x  in   g:  # Iterate through remaining values in generator
	print(x)  # Print remaining values (10.8, 'Hyd')
print()  # Print empty line
for  x  in   f1():  # Create new generator and iterate through all values
	print(x)  # Print all values (25, 10.8, 'Hyd')
print()  # Print empty line
gen = f1()  # Create generator object
print(next(gen))  # Get and print first value (25)
for  x  in   f1():  # Create new generator and iterate through all values
	print(x)  # Print all values from new generator (25, 10.8, 'Hyd')
print(next(gen))  # Get next value from original generator (10.8)

#Find  outputs (Home  work)
import  time  # Import time module
g = (x * x   for    x    in    range(5))  # Create generator expression for squares
for  y  in   g:  # Iterate through generator
	print(y)  # Print square value (0, 1, 4, 9, 16)
	time . sleep(2)  # Pause for 2 seconds
	print('Hello')  # Print 'Hello' after each value
for  y  in   g:  # Try to iterate through exhausted generator
	print(y)  # Nothing will be printed 
  
# Find  outputs (Home  work)
import  time  # Import time module
for  y  in   (x * x   for    x    in    range(5)):  # Create and iterate through generator expression
	print(y)  # Print square value (0, 1, 4, 9, 16)
	time . sleep(2)  # Pause for 2 seconds
for  y  in   (x * x   for    x    in    range(5)):  # Create new generator and iterate
	print(y)  # Print square value (0, 1, 4, 9, 16) again
	time . sleep(2)  # Pause for 2 seconds
  
# Find  outputs(Home  work)
import  time  # Import time module
g1 = (x * x   for  x  in  range(5))  # Create generator expression
g2 = g1  # Create reference to same generator object
for  y  in  g1:  # Iterate through generator
	print(y)  # Print square values (0, 1, 4, 9, 16)
	time . sleep(2)  # Pause for 2 seconds
for  y  in  g2:  # Try to iterate through same exhausted generator
	print(y)  # Nothing will be printed
print(g1  is  g2)  # Check if both variables reference same object 

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]  # Create list comprehension
print(l)  # Print list [0, 1, 4, 9, 16]
print(type(l))  # Print type <class 'list'>

s = {x * x   for   x   in   range(5)}  # Create set comprehension
print(s)  # Print set {0, 1, 4, 9, 16}
print(type(s))  # Print type <class 'set'>

d = {x : x * x    for   x   in   range(5)}  # Create dictionary comprehension
print(d)  # Print dict {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d))  # Print type <class 'dict'>

g = (x * x   for   x   in   range(5))  # Create generator expression
print(g)  # Print generator object reference
print(type(g))  # Print type <class 'generator'>

#  Find  outputs (Home  work)
def  f1():  # Define regular function
	return  10  # Return value 10 (function exits here)
	return  20  # Unreachable code
	return  30  # Unreachable code
def  f2():  # Define generator function
	yield  10  # Yield value 10
	yield  20  # Yield value 20
	yield  30  # Yield value 30
# End  of  the  function
print(f1())  # Call function and print return value (10)
print(f1())  # Call function again and print return value (10)
print(f1())  # Call function again and print return value (10)
print()  # Print empty line
g = f2()  # Create generator object
print(next(g))  # Get and print first yield value (10)
print(next(g))  # Get and print second yield value (20)
print(next(g))  # Get and print third yield value (30)
print(next(g))  # Try to get next value from exhausted generator (StopIteration error)
#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit  # Import timeit for performance measurement
print(timeit('[x * x   for  x  in  range(500) ]'))  # Time list comprehension execution
print(timeit('( x * x   for  x  in  range(500) )'))  # Time generator expression creation
# Prove  that  there  is  no  memory  error  for  generator
import  sys  # Import sys module for memory size checking
list = [x * x   for   x   in    range(10000)]  # Create large list
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))  # Create huge generator expression
print(sys . getsizeof(list))  # Print memory size of list (large)
print(sys . getsizeof(gen))  # Print memory size of generator (small, constant)
