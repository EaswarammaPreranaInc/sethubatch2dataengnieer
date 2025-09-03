1.
text
# Semicolon demo program

print('One');
# Output: One
# Explanation: The semicolon is an optional statement terminator in Python. It does not affect the behavior of the `print()` function itself; it simply marks the end of the statement.

print('Two');
# Output: Two
# Explanation: Same as above.

print('Three');
# Output: Three
# Explanation: Same as above.

print('Hyd') ; print('Sec'); print('Cvb')
# Output:
# Hyd
# Sec
# Cvb
# Explanation: Semicolons allow multiple statements to be written on a single line. Each `print()` function call executes independently, printing its argument followed by a default newline character.





2.
text
# ++ and -- operators demo program

a = 25
# Explanation: Variable `a` is initialized with the value 25.

print(++a)
# Output: 25
# Explanation: Python does not have pre-increment (`++`) or post-increment (`++`) operators like C++ or Java.
# In Python, `++a` is interpreted as `+(+a)`. The unary `+` operator simply returns the number itself.
# So, `+(+25)` evaluates to `+25`, which is `25`.

print(a++)
# Output: Syntax Error: invalid syntax
# Explanation: Python does not support the post-increment operator (`++`). This is a syntax error,
# and the program will stop execution at this line.







3.
text
# How to import kw list
import keyword

# How to print kwlist
print(keyword.kwlist)
# Expected Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# (Note: The exact list might vary slightly depending on your Python version, e.g., 'async' and 'await' were added in Python 3.5)

# How to print number of keywords
print(len(keyword.kwlist))
# Expected Output: 35 (for Python 3.8 and above, as of my last update)
# (The number of keywords depends on the python version. For example, it was 33 before async/await).

# How to print type of kwlist
print(type(keyword.kwlist))
# Expected Output: <class 'list'>
# Explanation: `keyword.kwlist` is a Python list containing string representations of keywords.

# Based on your last line, assuming the `keyword` module is already imported:
print(keyword.kwlist)
# Expected Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Explanation: This will print the list of keywords again, as the `keyword` module was imported previously in the session or script.







4.
text
# How to import keyword module
import keyword

# How to print kwlist
print(keyword.kwlist)
# Expected Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# (Note: The exact list might vary slightly depending on your Python version, e.g., 'async' and 'await' were added in Python 3.5)

# How to print number of keywords
print(len(keyword.kwlist))
# Expected Output: 35 (for Python 3.8 and above, as of July 2025)
# (The number of keywords depends on the python version. For example, it was 33 before async/await).

# How to print type of kwlist
print(type(keyword.kwlist))
# Expected Output: <class 'list'>
# Explanation: `keyword.kwlist` is a Python list containing string representations of keywords.

# Based on your last line, and assuming only `import keyword` was used:
print(kwlist)
# Output: NameError: name 'kwlist' is not defined
# Explanation: When you use `import keyword`, the `kwlist` object becomes an attribute of the `keyword` module. To access it, you must use `keyword.kwlist`. If you wanted to use `kwlist` directly, you would need to import it specifically like `from keyword import kwlist`. Since `kwlist` is not defined in the global namespace here, a `NameError` occurs.






5.
# abs() function demo program
from builtins import abs
# Explanation: The abs() function is a built-in function in Python, meaning it's always available
# without needing an explicit import. This 'from builtins import abs' statement is redundant but harmless.
print(abs(-35.8))
# Output: 35.8
# Explanation: abs() returns the absolute value of a number (its distance from zero), which is always non-negative.
print(abs(-27))
# Output: 27
# Explanation: The absolute value of -27 is 27.
print(abs (29.5))
# Output: 29.5
# Explanation: The absolute value of a positive number is the number itself.
print(abs (32))
# Output: 32
# Explanation: The absolute value of a positive integer is the integer itself.
import builtins
# Explanation: This imports the `builtins` module, which contains all Python's built-in functions and constants.
print(builtins.abs(-25))
# Output: 25
# Explanation: You can access built-in functions by explicitly referencing them through the 'builtins module, # though it's typically unnecessary for directly available built-ins like `abs(). The absolute value of -25 is 25.





6.
import math
print(math.floor(10.8))
+ Output: 10
# Explanation: "math.floor() returns the largest integer less than or equal to the given number. For 18.8, the largest integer less than or equal to it is 18. print(math.ceil(10.))
# Output: 11
Explanation: "math.ceil() returns the smallest integer greater than or equal to the given number. For 10.8, the smallest integer greater than or equal to it is 11. print(math.floor(25.0))
# Output: 25
+ Explanation: For a whole number, floor() returns the number itself.
print(math.ceil(25.0))
* Output: 25
Explanation: For a whole number, ceil() returns the number itself.
print(math.floor(-3.5))
Output: -4
# Explanation: "floor() rounds down towards negative infinity. The largest integer less than or equal to -3.5 is -4.
print(math.ceil(-3.5))
# Output: -3
+ Explanation: "ceil() rounds up towards positive infinity. The smallest integer greater than or equal to -3.5 is -3.
print(math.floor(-9.0))
#Output: -9
• Explanation: For a whole negative number, floor() returns the number itself.
print(math.ceil(-9.0))
* Output: -9
Explanation: For a whole negative number, `ceil()' returns the number itself.
print(math.floor(25.1))
* Output: 25
#Explanation: The largest integer less than or equal to 25.1 is 25.
print(math.ceil(25.1))
* Output: 26
• Explanation: The smallest integer greater than or equal to 25.1 is 26.
print(floor(3.5))
Output: NameError: name 'floor is not defined
+ Explanation: floor() is part of the math module and must be accessed using math.floor()". calling it directly without the 'math." prefix (or importing it specifically as 'from math import floor') results in a "NameError". The program execution stops here.







7.
# pow() function demo program
from builtins import pow
# Explanation: `pow() is a built-in function, always available. This explicit import is optional.
print (pow(10, -2))
# Output: 0.01
# Explanation: `pow(base, exp)` calculates base raised to the power of `exp`.
# 10` to the power of -2 is $10^{-2} = 1 / 10^2 = 1 / 100 = 0.01$.
print(pow(4, pow(3, 2)))
# Output: 262144
# Explanation: When `pow() is nested, the inner `pow() call is evaluated first. # 1. pow(3, 2) evaluates to $3^2 = 9$.
# 2. The expression then becomes `pow(4, 9)`.
# 3.
pow(4, 9)` evaluates to $4^9 = 262144$.
# This behavior is consistent with the right-to-left associativity of the
import builtins
operator.
# Explanation: This imports the `builtins` module, which holds all Python's built-in functions.
print(builtins. pow(2, 3))
# Output: 8
# Explanation: Accessing pow()` via the builtins module works correctly. $2^3 = 8$.
print(builtins. pow(-2, -3))
# Output: -0.125
# Explanation: -2 to the power of -3 is $(-2)^{-3} = 1 / (-2)^3 = 1 / (-8)= -0.125$.






8.
#max() and min() functions demo program
from builtins import max, min
# Explanation: `max()` and `min() are built-in functions in Python, so explicitly importing them from `builtins is not necessary, but it's a valid way to confirm their origin.
print(max(10.8, 20.6))
# Output: 20.6
# Explanation: `max()
print(min (10.8, 20.6, # Output: 5.9
# Explanation: `min()
print(max(25, 10.8))
# Output: 25
returns the largest of the given arguments. 20.6 is greater than 10.8.
5.9, 12.3))
returns the smallest of the given arguments. 5.9 is the smallest among the provided floats.
# Explanation: `max() correctly compares integers and floats. 25 is greater than 10.8.
import builtins
# Explanation: This imports the `builtins` module, which contains all Python's built-in functions.
print(builtins.max(10, 20, 30))
# Output: 30
# Explanation: Accessing `max()` via the `builtins module works correctly. 30 is the largest integer among 10, 20, and 30.
print(builtins.min(10, 20, 15, 5, 12))
# Output: 5
# Explanation: Accessing `min()` via the builtins' module works correctly. 5 is the smallest integer among 10, 20, 15, 5, and 12.










9.
import math
print(math.gcd(12, 15))
# Output: 3
# Explanation: The greatest common divisor of 12 and 15 is 3.
print(math.gcd(12, 18))
# Output: 6
# Explanation: The greatest common divisor of 12 and 18 is 6.
print(math.gcd(4, 7))
# Output: 1
# Explanation: The greatest common divisor of 4 and 7 is 1 (they are coprime).
print(math.gcd (7, 7))
# Output: 7
# Explanation: The greatest common divisor of a number with itself is the number itself.
print(math.gcd(-18, -27))
# Output: 9
# Explanation: `math.gcd()` works with the absolute values of the numbers. The GCD of 18 and 27 is 9.
print(math.gcd(-4, 6))
# Output: 2
# Explanation: The GCD of the absolute values of -4 and 6 (i.e., 4 and 6) is 2.
print(math.gcd(0, 7))
# Output: 7
# Explanation: The GCD of 0 and any non-zero integer `x` is `abs(x)`.
print(math.gcd(3, 0))
# Output: 3
# Explanation: The GCD of any non-zero integer `x and 0 is abs(x)`.
print(math.gcd(0, 0))
# Output: 0
# Explanation: By definition, math.gcd (0, 0) is 0.
print(gcd (5, 15))
# Output: NameError: name 'gcd' is not defined
# Explanation: gcd() is part of the math module and must be accessed using math.gcd()`.
# Calling it directly without the math. prefix (or importing it specifically as from math import gcd`) # results in a `NameError`. The program execution stops at this line.


