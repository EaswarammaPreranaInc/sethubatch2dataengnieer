# Program to add, subtract, multiply and divide two complex numbers

x = complex(input("Enter first complex number : "))
y = complex(input("Enter second complex number: "))
sum_result = x + y
diff_result = x - y
prod_result = x * y
div_result = x / y
print(f"Sum         :  {sum_result}")
print(f"Difference  :  {diff_result}")
print(f"Product     :  {prod_result}")
print(f"Division    :  {div_result}")


# Identify  error

else:
	print('else  suite')
print('Outside')

# Error: else without if, 'else' must always come after an 'if' block. It can't be used alone.


# Identify  error

if  9 > 5
	print('Hello')
print('Bye')

# Error: Missing colon (:) after the if condition, All 'if' statements must end with a colon to define the block.


# Identify  error

if  9 > 12:
	print('Hyd')
else
	print('Sec')

# Error: Missing colon (:) after 'else', The 'else' must end with a colon to indicate the start of its block.


# Identify  error

if  (10,20,15):
print('Hyd')
else:
print('Sec')

# Error: Indentation is missing, All code inside if/else must be indented properly. Also, the condition is a tuple which is always truthy (not empty), so 'if' will run.


# Identify  error

if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# Error: Improper indentation of 'else' must align with its corresponding 'if'. All blocks must follow indentation rules in Python.


# Identify  error

if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')

# Error: Curly braces {} used for block is not allowed, uses indentation (not {}) to define blocks. 


# Identify  error

if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# Error: 'else if' must be written as 'elif'. In Python, use 'elif' instead of 'else: if' to avoid syntax errors.


# Find outputs  (Home  work)

if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')


# Error: () is an empty tuple, which is treated as False. So, 'else' block executes.
'''
Output:
    One
    Two
    Three
    Bye
'''


# Find  outputs  (Home  work)

if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

# Error: Non-empty dictionary is treated as True. So, 'if' block executes.
'''
Output:
 Hyd
 Sec
 Cyb
 Bye
'''

# Find outputs  (Home  work)

if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# Error: {} is an empty dictionary, which is treated as False.
'''
So, 'if' block is skipped.
Output:
 Bye
'''


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

month= int(input("Enter month number (1 - 12): "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Input should be between 1 and 12")


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

digit = int(input("Enter a digit (0 - 9): "))
if digit == 0:
    print("Zero")
else:
    if digit == 1:
        print("One")
    else:
        if digit == 2:
            print("Two")
        else:
            if digit == 3:
                print("Three")
            else:
                if digit == 4:
                    print("Four")
                else:
                    if digit == 5:
                        print("Five")
                    else:
                        if digit == 6:
                            print("Six")
                        else:
                            if digit == 7:
                                print("Seven")
                            else:
                                if digit == 8:
                                    print("Eight")
                                else:
                                    if digit == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")