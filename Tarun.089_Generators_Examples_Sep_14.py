#TARUN BANALA          HOME WORK 2        14-09-2025
#Question number-1
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
#Answer:
def arithmetic_operations(a, b):  # Define generator function for arithmetic operations
    yield f"Sum: {a + b}"  # Yield sum of two numbers
    yield f"Difference: {a - b}"  # Yield difference of two numbers
    yield f"Product: {a * b}"  # Yield product of two numbers
    if b != 0:  # Check if denominator is not zero
        yield f"Division: {a / b}"  # Yield division result if valid
    else:  # If denominator is zero
        yield "Division by zero is not permitted"  # Yield error message
# Main program
a = int(input("Enter first number: "))  # Get first number from user
b = int(input("Enter second number: "))  # Get second number from user

for operation in arithmetic_operations(a, b):  # Iterate through generator results
    print(operation)  # Print each operation result
  

#Question number-2
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
#Answer:
def number_generator(start, end):  # Define generator function for number sequence
    current = start  # Initialize current number with start value
    while current <= end:  # Loop until current number reaches end value
        yield current  # Yield current number
        current += 1  # Increment current number by 1

# Main program
start_val = int(input("Enter start value: "))  # Get start value from user
end_val = int(input("Enter end value: "))  # Get end value from user

for num in number_generator(start_val, end_val):  # Iterate through number sequence
    print(num)  # Print each number


#Question-3
'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
#Answer:
def fibonacci_generator(limit):  # Define generator function for Fibonacci series
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    while a <= limit:  # Continue while current number is within limit
        yield a  # Yield current Fibonacci number
        a, b = b, a + b  # Calculate next Fibonacci numbers

# Main program
limit = int(input("Enter the last value of fibonacci series: "))  # Get limit from user

for num in fibonacci_generator(limit):  # Iterate through Fibonacci sequence
    print(num)  # Print each Fibonacci number
print("End")  # Print end message
