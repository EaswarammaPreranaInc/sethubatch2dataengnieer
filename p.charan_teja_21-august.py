Integers and Floats
Python

# Integers
a = 25
print(id(a)) # Prints memory address for integer 25

a = 35
print(id(a)) # Prints a new, different memory address for integer 35

# Floats
a = 25.7
print(id(a)) # Prints memory address for float 25.7

a = 35.6
print(id(a)) # Prints a new, different memory address for float 35.6
Integers and floats are immutable. When you change the value of an integer or float variable, you are actually making the variable point to a new object in a different memory location.







Strings, Tuples, and Ranges
Python

# Strings
a = "Hyd"
print(id(a)) # Prints memory address for string "Hyd"

# This will cause a TypeError because strings are immutable.
try:
    a[1] = 'e'
except TypeError as e:
    print(f"Output: TypeError: {e}")

# Reassigning the variable 'a' to a new string
a = "Sec"
print(id(a)) # Prints a new, different memory address for "Sec"

# Tuples
b = (10, 20, 15, 18)
print(id(b)) # Prints memory address for the tuple

# This will cause a TypeError because tuples are immutable.
try:
    b[2] = 19
except TypeError as e:
    print(f"Output: TypeError: {e}")

# Reassigning the variable 'b' to a new tuple
b = (30, 40, 35, 32)
print(id(b)) # Prints a new, different memory address for the new tuple

# Ranges
c = range(5)
print(id(c)) # Prints memory address for the range object

# This will cause a TypeError because range objects are immutable.
try:
    c[3] = 10
except TypeError as e:
    print(f"Output: TypeError: {e}")

# Reassigning the variable 'c' to a new range object
c = range(5)
print(id(c)) # Prints a new, different memory address for the new range object
Strings, tuples, and range objects are also immutable. Attempting to change an element within them will result in a TypeError. Reassigning the variable simply makes it point to a new object.







Booleans and NoneType
Python

# Booleans
b = True
print(id(b)) # Prints the fixed memory address for True

b = False
print(id(b)) # Prints the fixed memory address for False

# NoneType
c = None
print(id(c)) # Prints the fixed memory address for None

# Reassigning to the same singleton
c = None
print(id(c)) # Prints the same fixed memory address
True, False, and None are singleton objects. This means there is only one instance of each in memory throughout the program's execution. Reassigning a variable to one of these values will always make it point to the same, fixed memory address.







Standard Variable and Loop Usage
Python

# Basic variable assignment and type checking
a = 25
print(a)
print(type(a))

# Tuple unpacking and variable reassignment
a, _, c = 10, 20, 30
print(a)
print(_) # The underscore variable holds the value 20
print(c)

# Using the underscore variable in a for loop
for _ in range(5):
    print(_, 'Hello')








Mutability of Lists and Dictionaries
Mutable data types can be changed after they are created without changing their memory address. Lists and dictionaries are mutable.

Python

# Lists are mutable
l1 = [1, 2, 3, 4]
print(id(l1))

l1[2] = 5
print(l1)
print(id(l1)) # The ID remains the same

l1.append(6)
print(l1)
print(id(l1)) # The ID remains the same

# Dictionaries are mutable
d1 = {'A': 1, 'B': 2, 'C': 3}
print(id(d1))

d1['C'] = 4
print(d1)
print(id(d1)) # The ID remains the same

d1['D'] = 5
print(d1)
print(id(d1)) # The ID remains the same

# Mutable objects inside an immutable object can still be changed.
t1 = (1, 2, [3, 4])
print(t1)
print(id(t1))

t1[2][0] = 5
print(t1)
print(id(t1)) # The ID of the tuple remains the same, but the list inside it has been modified.







Common Dictionary Methods
Python

d1 = {10 : 'Hyd', 20 : 'Sec', 15 : 'Amar', 18 : 'Sita'}

# Get a view of all keys
keys = d1.keys()
print(keys)
print(type(keys))

# Get a view of all values
values = d1.values()
print(values)
print(type(values))

# Get a view of all key-value pairs
items = d1.items()
print(items)
print(type(items))

# Convert views to lists
print(list(d1.keys()))
print(list(d1.values()))
print(list(d1.items()))
dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.

dict.values(): Returns a view object that displays a list of all the values in the dictionary.

dict.items(): Returns a view object that displays a list of all the key-value pairs as tuples.







Looping Through a Dictionary
Python

d1 = {10: 'Hyd', 20: 'Sec', 15: 'Amar', 18: 'Sita'}

# Loop through keys only
for x in d1.keys():
    print(x)

# Loop through values only
for x in d1.values():
    print(x)

# Loop through both keys and values
for x, y in d1.items():
    print(x, '--->', y)

# Loop directly over the dictionary (this iterates through keys by default)
for x in d1:
    print(x)

# Access values by looping over keys
for x in d1:
    print(d1[x])






Operator Precedence and Floor Division
Python

# Floor division (//)
print(9 // 2)
# Output: 4
# Explanation: Floor division returns the integer part of the quotient, rounding down to the nearest whole number.

print(9.0 // 2)
# Output: 4.0
# Explanation: If at least one operand is a float, the result of floor division is a float.

print(9 // 2.0)
# Output: 4.0

print(9.0 // 2.0)
# Output: 4.0

print(10.5 // 2)
# Output: 5.0
# Explanation: The floor of 5.25 is 5.0.

print(10 // 3)
# Output: 3
# Explanation: The floor of 3.33 is 3.

print(10.0 // 3)
# Output: 3.0

print(8.5 // 3)
# Output: 2.0
# Explanation: The floor of 2.83 is 2.0.

print(18 // 4)
# Output: 4
# Explanation: The floor of 4.5 is 4.

# Floor division with negative numbers
print(-18 // 4)
# Output: -5
# Explanation: For negative numbers, floor division rounds down towards negative infinity. The floor of -4.5 is -5.

# Operator Precedence
print(-(18 // 4))
# Output: -4
# Explanation: Parentheses have higher precedence. `18 // 4` is evaluated first to 4, then the negation is applied.







Arithmetic and String Operations

Multiplication (*)
Python

# Standard integer and float multiplication
print(25 * 3)
# Output: 75

print(10.8 * 25.6)
# Output: 276.48

# Multiplication with booleans
print(True * False)
# Output: 0
# Explanation: In arithmetic operations, `True` is treated as 1 and `False` as 0.

# Multiplication with complex numbers
print((3 + 4j) * (5 + 6j))
# Output: (-9+38j)

# Operator precedence
print(3 + 4j * 5 + 6j)
# Output: (3+26j)
# Explanation: Multiplication has a higher precedence than addition.

# Sequence repetition
print("25" * 3)
# Output: 252525
# Explanation: Multiplies a string by an integer, resulting in string repetition.

print(3 * "25")
# Output: 252525
# Explanation: The order of operands doesn't matter for string repetition with an integer multiplier.

print("Hyd" * 4)
# Output: HydHydHydHyd

print([10, 20, 15] * 2)
# Output: [10, 20, 15, 10, 20, 15]
# Explanation: List repetition.

print((25, 10.8, 'Hyd', True) * 3)
# Output: (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
# Explanation: Tuple repetition.

# Error: Unsupported operand type
try:
    print([10, 20, 15] * 3.0)
except TypeError as e:
    print(f"Output: TypeError: {e}")
# Explanation: Sequence repetition requires an integer multiplier.







Addition (+)
Python

# Integer and float addition
print(10 + 20)
# Output: 30

print(10.8 + 20.6)
# Output: 31.4

# Complex number addition
print(3 + 4j + 5 + 6j)
# Output: (8+10j)

# Addition with booleans
print(True + False)
# Output: 1

# String concatenation
print("Hyd" + "abad")
# Output: Hydabad

print("Sankar" + "Daya" + "Sarma")
# Output: SankarDayaSarma

# String concatenation with numbers
print("10" + "20")
# Output: 1020

# List concatenation
print([10, 20, 30] + [1, 2, 3])
# Output: [10, 20, 30, 1, 2, 3]

# Tuple concatenation
print((25, 10.8, 'Hyd') + (3 + 4j, True, None))
# Output: (25, 10.8, 'Hyd', (3+4j), True, None)

# Error: Unsupported operand type
try:
    print({10, 20} + {30, 40})
except TypeError as e:
    print(f"Output: TypeError: {e}")
# Explanation: Sets do not support the `+` operator for concatenation.







Object Identity and The is Operator

Python

# Integers - interning
a = 25
b = 25
print(a is b)
# Output: True
# Explanation: For small integers (typically -5 to 256), Python "interns" them, meaning they refer to the same object.

# Strings - interning
c = 'Hyd'
d = 'Hyd'
print(c is d)
# Output: True
# Explanation: Python often interns short string literals.

# Booleans - singletons
e = False
f = False
print(e is f)
# Output: True
# Explanation: `True` and `False` are singleton objects, so they always refer to the same instance.

# Lists - not interned
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
print(a is b)
# Output: False
# Explanation: Lists are mutable. Even with identical content, separate literal assignments create two distinct objects.

# Dictionaries - not interned
c = {10: 20, 30: 40}
d = {10: 20, 30: 40}
print(c is d)
# Output: False
# Explanation: Dictionaries are mutable and not interned.

# Tuples - interning (with immutable elements)
e = (10, 20, 15, 18)
f = (10, 20, 15, 18)
print(e is f)
# Output: True
# Explanation: Python may "intern" tuples that contain only immutable elements.

# Sets - not interned
g = {10, 20, 15, 18}
h = {10, 20, 15, 18}
print(g is h)
# Output: False
# Explanation: Sets are mutable and not interned.

# Range objects - not interned
g = range(10)
h = range(10)
print(g is h)
# Output: False
# Explanation: The `range()` constructor creates a new object each time it's called.






Exponentiation and Operator Precedence
This section focuses on the ** (exponentiation) operator and the order of operations in Python.

Python

# Exponentiation (**)
print(3 ** 4)
# Output: 81
# Explanation: This performs 3 raised to the power of 4 (3 * 3 * 3 * 3).

print(10 ** -2)
# Output: 0.01
# Explanation: This performs exponentiation with a negative exponent, which is 1 / (10 ** 2).

# Right-to-left associativity
print(4 ** 3 ** 2)
# Output: 262144
# Explanation: The `**` operator has right-to-left associativity. This means `3 ** 2` is evaluated first (9), then `4 ** 9` is calculated.

# Order of Operations (PEMDAS/BODMAS)
print(3 + 4 * 5 - 32 / 2 ** 3)
# Output: 19.0
# Explanation: The expression is evaluated in this order:
# 1. Exponentiation: `2 ** 3` becomes `8`.
# 2. Multiplication/Division (from left to right):
#    - `4 * 5` becomes `20`.
#    - `32 / 8` becomes `4.0` (because division always returns a float in Python 3).
# 3. Addition/Subtraction (from left to right):
#    - `3 + 20` becomes `23`.
#    - `23 - 4.0` becomes `19.0`.
Modulus and Division Errors
This section explores the % (modulus) operator and the ZeroDivisionError.

Python

# Modulus (%) operator
print(9 % 5)
# Output: 4
# Explanation: For integers, the modulus operator returns the remainder of the division. 9 divided by 5 is 1 with a remainder of 4.

print(9.0 % 5)
# Output: 4.0
# Explanation: If at least one operand is a float, the result is a float.

print(10.5 % 2)
# Output: 0.5
# Explanation: 10.5 divided by 2 is 5 with a remainder of 0.5.

print(8.9 % 3)
# Output: 2.9
# Explanation: 8.9 divided by 3 is 2 with a remainder of 2.9.

# Division by zero
try:
    print(7 / 0)
except ZeroDivisionError as e:
    print(f"Output: ZeroDivisionError: {e}")
# Explanation: Division by zero is mathematically undefined. In Python, it raises a `ZeroDivisionError`, which stops the program's execution unless handled.
Relational Operators
This section demonstrates how to use comparison (relational) operators (>, <, ==, !=, etc.) with different data types.

Python

# Standard comparisons
print(3 > 5)
# Output: False

print(9 >= 9)
# Output: True

print(10 <= 12)
# Output: True

print(6 <= 6)
# Output: True

print(7 != 8)
# Output: True

print(6 == 8)
# Output: False

# Boolean comparison
print(True > False)
# Output: True
# Explanation: `True` is treated as 1 and `False` as 0 in numerical comparisons.

# Comparing numerical values with different types
print(10.0 == 10)
# Output: True
# Explanation: Python compares the "value" of the numerical types, which are the same.

# String comparisons (lexicographical)
print('Rama' > 'Rajesh')
# Output: True
# Explanation: Comparison is lexicographical (based on character Unicode values). 'R' == 'R', but 'm' > 'j', so 'Rama' > 'Rajesh'.

print('Rama' < 'Sita')
# Output: True
# Explanation: 'R' < 'S'.

print('Hyd' == 'Hyd')
# Output: True

print('Rama' <= 'Ramana')
# Output: True
# Explanation: When one string is a prefix of another, the shorter string is considered less than or equal to the longer string.

print('Hyd' != 'Sec')
# Output: True

print('HYD' < 'hyd')
# Output: True
# Explanation: String comparison is case-sensitive. The Unicode value for 'H' is less than 'h'.

# Complex number comparisons
print(3 + 4j == 3 + 4j)
# Output: True

print(3 + 4j == 5 + 6j)
# Output: False

print(3 + 4j <= 5 + 6j)
# Output: TypeError: '>=' not supported between instances of 'complex' and 'complex'
# Explanation: Complex numbers cannot be ordered. This raises a `TypeError` when using comparison operators like `>`, `<`, `>=`, or `<=`.
Set and Dictionary Initialization
This section shows a unique and potentially confusing way to initialize a set and how duplicate keys are handled in dictionaries.

Python

# Set initialization using function calls
a = {
    print('Hyd'),
    print('Sec'),
    print('Cyb')
}
# Output during execution:
# Hyd
# Sec
# Cyb

print(type(a))
# Output: <class 'set'>

print(a)
# Output: {None}
# Explanation: The `print()` function returns the `None` object. The set is populated with the return values of the `print()` calls. Sets only store unique elements, so only one `None` object is stored.

print(len(a))
# Output: 1
# Explanation: The set contains only one unique element: `None`.











Exponentiation and Operator Precedence
This section focuses on the ** (exponentiation) operator and the order of operations in Python.

Python

# Exponentiation (**)
print(3 ** 4)
# Output: 81
# Explanation: This performs 3 raised to the power of 4 (3 * 3 * 3 * 3).

print(10 ** -2)
# Output: 0.01
# Explanation: This performs exponentiation with a negative exponent, which is 1 / (10 ** 2).

# Right-to-left associativity
print(4 ** 3 ** 2)
# Output: 262144
# Explanation: The `**` operator has right-to-left associativity. This means `3 ** 2` is evaluated first (9), then `4 ** 9` is calculated.

# Order of Operations (PEMDAS/BODMAS)
print(3 + 4 * 5 - 32 / 2 ** 3)
# Output: 19.0
# Explanation: The expression is evaluated in this order:
# 1. Exponentiation: `2 ** 3` becomes `8`.
# 2. Multiplication/Division (from left to right):
#    - `4 * 5` becomes `20`.
#    - `32 / 8` becomes `4.0` (because division always returns a float in Python 3).
# 3. Addition/Subtraction (from left to right):
#    - `3 + 20` becomes `23`.
#    - `23 - 4.0` becomes `19.0`.
Modulus and Division Errors
This section explores the % (modulus) operator and the ZeroDivisionError.

Python

# Modulus (%) operator
print(9 % 5)
# Output: 4
# Explanation: For integers, the modulus operator returns the remainder of the division. 9 divided by 5 is 1 with a remainder of 4.

print(9.0 % 5)
# Output: 4.0
# Explanation: If at least one operand is a float, the result is a float.

print(10.5 % 2)
# Output: 0.5
# Explanation: 10.5 divided by 2 is 5 with a remainder of 0.5.

print(8.9 % 3)
# Output: 2.9
# Explanation: 8.9 divided by 3 is 2 with a remainder of 2.9.

# Division by zero
try:
    print(7 / 0)
except ZeroDivisionError as e:
    print(f"Output: ZeroDivisionError: {e}")
# Explanation: Division by zero is mathematically undefined. In Python, it raises a `ZeroDivisionError`, which stops the program's execution unless handled.
Relational Operators
This section demonstrates how to use comparison (relational) operators (>, <, ==, !=, etc.) with different data types.

Python

# Standard comparisons
print(3 > 5)
# Output: False

print(9 >= 9)
# Output: True

print(10 <= 12)
# Output: True

print(6 <= 6)
# Output: True

print(7 != 8)
# Output: True

print(6 == 8)
# Output: False

# Boolean comparison
print(True > False)
# Output: True
# Explanation: `True` is treated as 1 and `False` as 0 in numerical comparisons.

# Comparing numerical values with different types
print(10.0 == 10)
# Output: True
# Explanation: Python compares the "value" of the numerical types, which are the same.

# String comparisons (lexicographical)
print('Rama' > 'Rajesh')
# Output: True
# Explanation: Comparison is lexicographical (based on character Unicode values). 'R' == 'R', but 'm' > 'j', so 'Rama' > 'Rajesh'.

print('Rama' < 'Sita')
# Output: True
# Explanation: 'R' < 'S'.

print('Hyd' == 'Hyd')
# Output: True

print('Rama' <= 'Ramana')
# Output: True
# Explanation: When one string is a prefix of another, the shorter string is considered less than or equal to the longer string.

print('Hyd' != 'Sec')
# Output: True

print('HYD' < 'hyd')
# Output: True
# Explanation: String comparison is case-sensitive. The Unicode value for 'H' is less than 'h'.

# Complex number comparisons
print(3 + 4j == 3 + 4j)
# Output: True

print(3 + 4j == 5 + 6j)
# Output: False

print(3 + 4j <= 5 + 6j)
# Output: TypeError: '>=' not supported between instances of 'complex' and 'complex'
# Explanation: Complex numbers cannot be ordered. This raises a `TypeError` when using comparison operators like `>`, `<`, `>=`, or `<=`.
Set and Dictionary Initialization
This section shows a unique and potentially confusing way to initialize a set and how duplicate keys are handled in dictionaries.

Python

# Set initialization using function calls
a = {
    print('Hyd'),
    print('Sec'),
    print('Cyb')
}
# Output during execution:
# Hyd
# Sec
# Cyb

print(type(a))
# Output: <class 'set'>

print(a)
# Output: {None}
# Explanation: The `print()` function returns the `None` object. The set is populated with the return values of the `print()` calls. Sets only store unique elements, so only one `None` object is stored.

print(len(a))
# Output: 1
# Explanation: The set contains only one unique element: `None`.










Exponentiation and Operator Precedence

Python

# Exponentiation (**)
print(3 ** 4)
# Output: 81
# Explanation: This performs 3 raised to the power of 4 (3 * 3 * 3 * 3).

print(10 ** -2)
# Output: 0.01
# Explanation: This performs exponentiation with a negative exponent, which is 1 / (10 ** 2).

# Right-to-left associativity
print(4 ** 3 ** 2)
# Output: 262144
# Explanation: The `**` operator has right-to-left associativity. This means `3 ** 2` is evaluated first (9), then `4 ** 9` is calculated.

# Order of Operations (PEMDAS/BODMAS)
print(3 + 4 * 5 - 32 / 2 ** 3)
# Output: 19.0
# Explanation: The expression is evaluated in this order:
# 1. Exponentiation: `2 ** 3` becomes `8`.
# 2. Multiplication/Division (from left to right):
#    - `4 * 5` becomes `20`.
#    - `32 / 8` becomes `4.0` (because division always returns a float in Python 3).
# 3. Addition/Subtraction (from left to right):
#    - `3 + 20` becomes `23`.
#    - `23 - 4.0` becomes `19.0`.






Modulus and Division Errors

Python

# Modulus (%) operator
print(9 % 5)
# Output: 4
# Explanation: For integers, the modulus operator returns the remainder of the division. 9 divided by 5 is 1 with a remainder of 4.

print(9.0 % 5)
# Output: 4.0
# Explanation: If at least one operand is a float, the result is a float.

print(10.5 % 2)
# Output: 0.5
# Explanation: 10.5 divided by 2 is 5 with a remainder of 0.5.

print(8.9 % 3)
# Output: 2.9
# Explanation: 8.9 divided by 3 is 2 with a remainder of 2.9.

# Division by zero
try:
    print(7 / 0)
except ZeroDivisionError as e:
    print(f"Output: ZeroDivisionError: {e}")
# Explanation: Division by zero is mathematically undefined. In Python, it raises a `ZeroDivisionError`, which stops the program's execution unless handled.







Relational Operators

Python

# Standard comparisons
print(3 > 5)
# Output: False

print(9 >= 9)
# Output: True

print(10 <= 12)
# Output: True

print(6 <= 6)
# Output: True

print(7 != 8)
# Output: True

print(6 == 8)
# Output: False

# Boolean comparison
print(True > False)
# Output: True
# Explanation: `True` is treated as 1 and `False` as 0 in numerical comparisons.

# Comparing numerical values with different types
print(10.0 == 10)
# Output: True
# Explanation: Python compares the "value" of the numerical types, which are the same.

# String comparisons (lexicographical)
print('Rama' > 'Rajesh')
# Output: True
# Explanation: Comparison is lexicographical (based on character Unicode values). 'R' == 'R', but 'm' > 'j', so 'Rama' > 'Rajesh'.

print('Rama' < 'Sita')
# Output: True
# Explanation: 'R' < 'S'.

print('Hyd' == 'Hyd')
# Output: True

print('Rama' <= 'Ramana')
# Output: True
# Explanation: When one string is a prefix of another, the shorter string is considered less than or equal to the longer string.

print('Hyd' != 'Sec')
# Output: True

print('HYD' < 'hyd')
# Output: True
# Explanation: String comparison is case-sensitive. The Unicode value for 'H' is less than 'h'.

# Complex number comparisons
print(3 + 4j == 3 + 4j)
# Output: True

print(3 + 4j == 5 + 6j)
# Output: False

print(3 + 4j <= 5 + 6j)
# Output: TypeError: '>=' not supported between instances of 'complex' and 'complex'
# Explanation: Complex numbers cannot be ordered. This raises a `TypeError` when using comparison operators like `>`, `<`, `>=`, or `<=`.








Set and Dictionary Initialization

Python

# Set initialization using function calls
a = {
    print('Hyd'),
    print('Sec'),
    print('Cyb')
}
# Output during execution:
# Hyd
# Sec
# Cyb

print(type(a))
# Output: <class 'set'>

print(a)
# Output: {None}
# Explanation: The `print()` function returns the `None` object. The set is populated with the return values of the `print()` calls. Sets only store unique elements, so only one `None` object is stored.

print(len(a))
# Output: 1
# Explanation: The set contains only one unique element: `None`.






1.
text
# / operator demo program

print(9.0 / 2)
# Output: 4.5
# Explanation: Division of a float by an integer results in a float.

print(9 / 2.0)
# Output: 4.5
# Explanation: Division of an integer by a float results in a float.

print(9.0 / 2.0)
# Output: 4.5
# Explanation: Division of a float by a float results in a float.

print(9 / 2)
# Output: 4.5
# Explanation: In Python 3 (and later), the `/` operator performs "true division," meaning it always returns a float, even if both operands are integers and the result is a whole number.

print(10.5 / 2)
# Output: 5.25
# Explanation: Division of a float by an integer results in a float.

print(10 / 3)
# Output: 3.3333333333333335
# Explanation: True division of integers results in a float, even if there's a remainder.

print(10 / 2)
# Output: 5.0
# Explanation: True division of integers results in a float, even if the result is a whole number.





2.
text
# Chaining relational operators demo program

print(10 < 20 < 30)
# Output: True
# Explanation: Chained comparisons are evaluated as a series of ANDed comparisons. This is equivalent to (10 < 20) and (20 < 30). Both are True, so the result is True.

print(10 >= 20 < 30)
# Output: False
# Explanation: This is equivalent to (10 >= 20) and (20 < 30).
# (10 >= 20) is False.
# (20 < 30) is True.
# False and True results in False.

print(10 < 20 > 30)
# Output: False
# Explanation: This is equivalent to (10 < 20) and (20 > 30).
# (10 < 20) is True.
# (20 > 30) is False.
# True and False results in False.

print(1 < 2 < 3 < 4)
# Output: True
# Explanation: This is equivalent to (1 < 2) and (2 < 3) and (3 < 4). All are True, so the result is True.

print(1 < 2 < 3 > 1)
# Output: False
# Explanation: This is equivalent to (1 < 2) and (2 < 3) and (3 > 1).
# (1 < 2) is True.
# (2 < 3) is True.
# (3 > 1) is True.
# True and True and True results in True.

print(4 > 3 >= 3 > 2)
# Output: True
# Explanation: This is equivalent to (4 > 3) and (3 >= 3) and (3 > 2).
# (4 > 3) is True.
# (3 >= 3) is True.
# (3 > 2) is True.
# True and True and True results in True.








3.
text
a = b = c = 25
# Explanation: This is a chained assignment. It assigns the value 25 to `c`, then assigns `c`'s reference to `b`, and finally assigns `b`'s reference to `a`. Because 25 is a small integer, Python typically "interns" it, meaning there's only one object for that value in memory. Therefore, `a`, `b`, and `c` will all refer to the *exact same* integer object.

print(id(a))
# Output: [A unique memory address for integer 25, e.g., 14073753974592]
# Explanation: Prints the memory address of the integer object 25 that `a` refers to.

print(id(b))
# Output: [The exact same memory address as id(a), e.g., 14073753974592]
# Explanation: Since `b` refers to the same object as `a`, its ID will be identical.

print(id(c))
# Output: [The exact same memory address as id(a) and id(b), e.g., 14073753974592]
# Explanation: Since `c` refers to the same object as `a` and `b`, its ID will also be identical.

print(a , b , c)
# Output: 25 25 25
# Explanation: Prints the values of `a`, `b`, and `c`, which are all 25.








4.
text
# Find outputs (Home work)
a = 20
# Explanation: Variable `a` is initialized with the value 20.

a %= 3 + 2 * 4
# Explanation: This is a compound assignment operator.
# The expression `a %= 3 + 2 * 4` is equivalent to `a = a % (3 + 2 * 4)`.
# Step 1: Evaluate the right-hand side expression `3 + 2 * 4` first, following operator precedence (multiplication before addition).
# `2 * 4` evaluates to `8`.
# The expression becomes `3 + 8`.
# Step 2: Evaluate the addition.
# `3 + 8` evaluates to `11`.
# Step 3: Now, the assignment effectively becomes `a = a % 11`.
# Since `a` was initially 20, this becomes `a = 20 % 11`.
# Step 4: Perform the modulo operation (remainder of 20 divided by 11).
# `20 // 11` is `1`.
# `20 - (1 * 11)` is `20 - 11` which is `9`.
# So, `a` is assigned the value 9.

print(a)
# Output: 9
# Explanation: The final value of `a` after the operation is 9.






5.
text
# / operator demo program

print(9.0 / 2)
# Output: 4.5
# Explanation: Division of a float by an integer results in a float.

print(9 / 2.0)
# Output: 4.5
# Explanation: Division of an integer by a float results in a float.

print(9.0 / 2.0)
# Output: 4.5
# Explanation: Division of a float by a float results in a float.

print(9 / 2)
# Output: 4.5
# Explanation: In Python 3 (and later), the `/` operator performs "true division," meaning it always returns a float, even if both operands are integers and the result is a whole number.

print(10.5 / 2)
# Output: 5.25
# Explanation: Division of a float by an integer results in a float.

print(10 / 3)
# Output: 3.3333333333333335
# Explanation: True division of integers results in a float, even if there's a remainder.

print(10 / 2)
# Output: 5.0
# Explanation: True division of integers results in a float, even if the result is a whole number.






6.
text
# Chaining relational operators demo program

print(10 < 20 < 30)
# Output: True
# Explanation: Chained comparisons are evaluated as a series of ANDed comparisons. This is equivalent to (10 < 20) and (20 < 30). Both are True, so the result is True.

print(10 >= 20 < 30)
# Output: False
# Explanation: This is equivalent to (10 >= 20) and (20 < 30).
# (10 >= 20) is False.
# (20 < 30) is True.
# False and True results in False.

print(10 < 20 > 30)
# Output: False
# Explanation: This is equivalent to (10 < 20) and (20 > 30).
# (10 < 20) is True.
# (20 > 30) is False.
# True and False results in False.

print(1 < 2 < 3 < 4)
# Output: True
# Explanation: This is equivalent to (1 < 2) and (2 < 3) and (3 < 4). All are True, so the result is True.

print(1 < 2 < 3 > 1)
# Output: False
# Explanation: This is equivalent to (1 < 2) and (2 < 3) and (3 > 1).
# (1 < 2) is True.
# (2 < 3) is True.
# (3 > 1) is True.
# True and True and True results in True.

print(4 > 3 >= 3 > 2)
# Output: True
# Explanation: This is equivalent to (4 > 3) and (3 >= 3) and (3 > 2).
# (4 > 3) is True.
# (3 >= 3) is True.
# (3 > 2) is True.
# True and True and True results in True.







7.
text
a = b = c = 25
# Explanation: This is a chained assignment. It assigns the value 25 to `c`, then assigns `c`'s reference to `b`, and finally assigns `b`'s reference to `a`. Because 25 is a small integer, Python typically "interns" it, meaning there's only one object for that value in memory. Therefore, `a`, `b`, and `c` will all refer to the *exact same* integer object.

print(id(a))
# Output: [A unique memory address for integer 25, e.g., 14073753974592]
# Explanation: Prints the memory address of the integer object 25 that `a` refers to.

print(id(b))
# Output: [The exact same memory address as id(a), e.g., 14073753974592]
# Explanation: Since `b` refers to the same object as `a`, its ID will be identical.

print(id(c))
# Output: [The exact same memory address as id(a) and id(b), e.g., 14073753974592]
# Explanation: Since `c` refers to the same object as `a` and `b`, its ID will also be identical.

print(a , b , c)
# Output: 25 25 25
# Explanation: Prints the values of `a`, `b`, and `c`, which are all 25.








8.
text
# Find outputs (Home work)
a = 20
# Explanation: Variable `a` is initialized with the value 20.

a %= 3 + 2 * 4
# Explanation: This is a compound assignment operator.
# The expression `a %= 3 + 2 * 4` is equivalent to `a = a % (3 + 2 * 4)`.
# Step 1: Evaluate the right-hand side expression `3 + 2 * 4` first, following operator precedence (multiplication before addition).
# `2 * 4` evaluates to `8`.
# The expression becomes `3 + 8`.
# Step 2: Evaluate the addition.
# `3 + 8` evaluates to `11`.
# Step 3: Now, the assignment effectively becomes `a = a % 11`.
# Since `a` was initially 20, this becomes `a = 20 % 11`.
# Step 4: Perform the modulo operation (remainder of 20 divided by 11).
# `20 // 11` is `1`.
# `20 - (1 * 11)` is `20 - 11` which is `9`.
# So, `a` is assigned the value 9.

print(a)
# Output: 9
# Explanation: The final value of `a` after the operation is 9.







9.
text
# not operator demo program

print(not True)
# Output: False
# Explanation: The `not` operator returns the boolean opposite of its operand's truthiness. `True` is truthy, so `not True` is `False`.

print(not False)
# Output: True
# Explanation: `False` is falsy, so `not False` is `True`.

print(not 25)
# Output: False
# Explanation: Any non-zero number (like 25) is considered truthy in Python. So, `not 25` is `False`.

print(not 0)
# Output: True
# Explanation: `0` (zero) is considered falsy in Python. So, `not 0` is `True`.

print(not "Hyd")
# Output: False
# Explanation: A non-empty string (like `'Hyd'`) is considered truthy in Python. So, `not 'Hyd'` is `False`.

print(not '')
# Output: True
# Explanation: An empty string (like `''`) is considered falsy in Python. So, `not ''` is `True`.

print(not -10)
# Output: False
# Explanation: Any non-zero number (like -10) is considered truthy in Python. So, `not -10` is `False`.

print(not not 'Hyd')
# Output: True
# Explanation: This is evaluated from right to left (or simply applying `not` twice).
# 1. `not 'Hyd'`: `'Hyd'` is truthy, so `not 'Hyd'` evaluates to `False`.
# 2. `not False`: `False` is falsy, so `not False` evaluates to `True`.







10.
text
# Find outputs (Home work)
a, b, c = 3, 4, 5
# Explanation: Variables are initialized:
# a = 3
# b = 4
# c = 5

a *= b + c
# Explanation: This is a compound assignment operator.
# The expression `a *= b + c` is equivalent to `a = a * (b + c)`.

# Step 1: Evaluate the expression `b + c` first due to operator precedence (addition before multiplication in the effective expanded form).
# b + c = 4 + 5 = 9

# Step 2: Now, the assignment becomes `a = a * 9`.
# Since `a` was initially 3, this becomes `a = 3 * 9`.

# Step 3: Perform the multiplication.
# a = 27

print(a)
# Output: 27
# Explanation: The final value of `a` after the operation is 27.








11.
text
# or operator demo program

print(True or False)
# Output: True
# Explanation: `True` is a truthy value. In an `or` operation, if the left operand is truthy, it is returned immediately (short-circuiting).

print(False or True)
# Output: True
# Explanation: `False` is falsy value. The `or` operation proceeds to evaluate the right operand. `True` is truthy, so `True` is returned.

print(True or True)
# Output: True
# Explanation: `True` is truthy. The left operand (`True`) is returned immediately.

print(False or False)
# Output: False
# Explanation: `False` is falsy. The `or` operation proceeds to the right operand. `False` is falsy, so `False` is returned.

print(10 or 20)
# Output: 10
# Explanation: `10` is a non-zero integer, which is a truthy value. In an `or` operation, if the left operand is truthy, it is returned.

print(0 or 20)
# Output: 20
# Explanation: `0` is a falsy value. The `or` operation proceeds to the right operand. `20` is truthy, so `20` is returned.

print(-25 or 0)
# Output: -25
# Explanation: `-25` is a non-zero integer, which is a truthy value. The left operand (`-25`) is returned.

print('' or 35)
# Output: 35
# Explanation: An empty string (`''`) is a falsy value. The `or` operation proceeds to the right operand. `35` is truthy, so `35` is returned.

print(6j or 'Hyd')
# Output: 6j
# Explanation: A non-zero complex number (`6j`) is a truthy value. The left operand (`6j`) is returned.

print(0.0 or 3 + 4j)
# Output: (3+4j)
# Explanation: `0.0` is a falsy value. The `or` operation proceeds to the right operand. `3 + 4j` (a non-zero complex number) is truthy, so `(3+4j)` is returned.

print('Hyd' or 10.8)
# Output: Hyd
# Explanation: A non-empty string (`'Hyd'`) is a truthy value. The left operand (`'Hyd'`) is returned.








12.
text
# Find outputs (Home work)

a = [10, 20, 30]
b = (10, 20, 30)
# Explanation: `a` is a list containing the elements 10, 20, and 30.
# `b` is a tuple containing the same elements 10, 20, and 30.
# Lists are mutable (can be changed), while tuples are immutable (cannot be changed after creation). They are distinct data types.

print(a is b)
# Output: False
# Explanation: The `is` operator checks for object identity (i.e., if two variables refer to the exact same object in memory).
# Since `a` is a list object and `b` is a tuple object, they are fundamentally different types of objects, even if their contents are similar. They reside at different memory locations.

print(a == b)
# Output: True
# Explanation: The `==` operator checks for value equality. Python can compare different sequence types (like lists and tuples) by checking if they have the same length and if all their corresponding elements are equal. In this case, both `a` and `b` have the same elements in the same order, so they are considered equal in value.




13.
text
# Find outputs (Home work)

a = 25
b = 25.0
# Explanation: `a` refers to an integer object with the value 25.
# `b` refers to a float object with the value 25.0.
# Although they represent the same numerical quantity, they are distinct objects of different data types.

print(a is b)
# Output: False
# Explanation: The `is` operator checks for object identity (i.e., if two variables refer to the exact same object in memory).
# Since `a` is an `int` and `b` is a `float`, they are different types of objects stored at different memory locations. Therefore, they are not the same object.

print(a is not b)
# Output: True
# Explanation: The `is not` operator checks if two variables do *not* refer to the same object.
# As explained above, `a` and `b` are distinct objects, so this expression evaluates to True.

print(a == b)
# Output: True
# Explanation: The `==` operator checks for value equality. Python can correctly compare the numerical value of an integer and a float.
# Since the numerical value of 25 is equal to the numerical value of 25.0, this returns True.





14.
text
# Find outputs (Home work)

x = [1, 2, 3, 4]
y = [1, 2, 4, 3]
print(x == y)
# Output: False
# Explanation: Lists are ordered sequences. For two lists to be equal using `==`, they must have the same length AND all their elements must be equal in the same order. In this case, the elements at index 2 (3 vs 4) and index 3 (4 vs 3) are different.

a = (4, 1, 3, 2)
b = (4, 2, 3, 1)
print(a == b)
# Output: False
# Explanation: Tuples are also ordered sequences, and their equality comparison works like lists. The elements must be equal in the same order. Here, elements at index 1 (1 vs 2) and index 3 (2 vs 1) are different.

p = {1, 2, 3, 4}
q = {4, 1, 3, 2}
print(p == q)
# Output: True
# Explanation: Sets are unordered collections of unique elements. For two sets to be equal using `==`, they must contain *exactly the same elements*, regardless of their order. Both `p` and `q` contain the same set of elements: 1, 2, 3, and 4.

m = range(5)
n = range(5)
print(m == n)
# Output: True
# Explanation: `range` objects are considered equal if they represent the exact same sequence of numbers (i.e., same start, stop, and step values). Both `m` and `n` represent the sequence 0, 1, 2, 3, 4, so they are considered equal.
