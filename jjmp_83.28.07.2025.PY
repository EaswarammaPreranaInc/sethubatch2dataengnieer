# Define two complex numbers
c1 = 3 + 4j
c2 = 5 + 6j

# Addition
add_result = c1 + c2

# Subtraction
sub_result = c1 - c2

# Multiplication
mul_result = c1 * c2

# Division
div_result = c1 / c2

# Display results
print("First complex number:", c1)
print("Second complex number:", c2)
print("Sum:", add_result)
print("Difference:", sub_result)
print("Product:", mul_result)
print("Division:", div_result)

################################################

# Error Code# Error Code
if  9 > 5
    print('Hello')
print('Bye')

# Error Message:
SyntaxError: expected ':'

# Reason:
The 'if' statement is missing a colon (:) at the end of the condition.
In Python, all 'if', 'else', 'elif', 'for', and 'while' statements must end with a colon.
else:
    print('else suite')
print('Outside')

#############################################

# Error Code
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# Error Message:
IndentationError: expected an indented block

# Reason:
In Python, the code inside 'if' and 'else' blocks must be indented.
Also, the condition (10, 20, 15) is a non-empty tuple, which is always treated as True.

####################################################

# Error Code
if  ():
        print('Hyd')
    else:
            print('Sec')
print('Bye')

# Error Message:
IndentationError: unexpected indent

# Reason:
In Python, the 'else:' block must align with the corresponding 'if' block.
Also, the condition '()' is an empty tuple, which is considered False in a boolean context.

###############################################

# Error Code
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

# Error Message:
SyntaxError: invalid syntax

# Reason:
1. In Python, curly braces `{}’are not used to define code blocks. 
   Python uses **indentation** instead of `{}’.
2. The condition `{}’ is an empty dictionary, which is treated as **False**.
3. Using `{}’as a block results in a syntax error.

######################################################

# Error Code
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

# Error Message:
SyntaxError: expected an indented block or invalid syntax (on 'else:' and 'if' lines)

# Reason:
1. Python does not allow 'if' immediately after 'else' without proper indentation or using `elif’.

2. The correct chaining is either using `elif’ or nesting with proper indentation.

3. Empty tuple (), empty list [], and empty dict {} all evaluate to False.

# Error Message:
SyntaxError: invalid syntax

# Reason:
The 'else:' statement must be part of an if-else or loop structure.
It cannot be used alone, as in the code above.

###########################################

# Error Code
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

# Error Message:
SyntaxError: expected an indented block or invalid syntax (on 'else:' and 'if' lines)

# Reason:
1. Python does not allow 'if' immediately after 'else' without proper indentation or using `elif’.

2. The correct chaining is either using `elif’ or nesting with proper indentation.

3. Empty tuple (), empty list [], and empty dict {} all evaluate to False.

#####################################################

# Program to determine whether a number is even or odd using if statement

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
if number % 2 != 0:
    print("The number is odd")

    ############################################

    # Code
if():
    print('Hyd')
    print('Sec')
    print('Cyb')
else:
    print('One')
    print('Two')
    print('Three')
print('Bye')

# Analysis
The condition `if():`uses empty parentheses `()’.

In Python, `()`represents an empty tuple, which is treated as **False** in a boolean context.

# So, the 'else' block will be executed.

# Output
One
Two
Three
Bye

######################################

# Code
if():
    print('Hyd')
    print('Sec')
    print('Cyb')
else:
    print('One')
    print('Two')
    print('Three')
print('Bye')

# Analysis:
  The condition `if():`uses empty parentheses.
   In Python, an empty tuple `()`is considered **False**.
   So, the `if`block is skipped, and the `else`block is executed.

# Output:
One
Two
Three
Bye

###################################################

# Code
if{10 : 20 , 30 : 40}:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')

# Error:
SyntaxError: expected '(' after 'if'

# Reason:
  Python syntax requires parentheses `()`after `if`not curly braces `{}’.
  Curly braces `{}`define a dictionary in Python.
  The correct way is: if {10: 20, 30: 40}: → but wrapped inside parentheses.

# Corrected Code:
if {10: 20, 30: 40}:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')

# Explanation:
`{10: 20, 30: 40}`is a non-empty dictionary  it evaluates to **True**.
  So the `if`block will be executed.

# Output:
Hyd
Sec
Cyb
Bye

################################################

# Program to print month name for given month number using if and elif

month = int(input("Enter month number (1 to 12): "))

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
    print("Invalid month number")
    
    ##################################################


    # Program to print digit in words using if and else (without using elif)

digit = int(input("Enter a digit (0 to 9): "))

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

