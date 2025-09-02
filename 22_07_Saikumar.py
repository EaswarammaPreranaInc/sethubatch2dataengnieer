# Find outputs

print({10, 20} | {30, 20})                              # Prints the {10, 20, 30}  
print({10: 'Hyd', 20: 'Sec'} | {30: 'Cyb', 20: 'Vja'})  # Prints the {10: 'Hyd', 20: 'Vja', 30: 'Cyb'} print(range(4) | range(5))                              # Error  'range' objects don't support '|' operator
print([10, 20] | [30, 20])                              # Error  lists don't support '|' operator


# Assignment operators demo program (Home work)

a = 25                  # a is assigned the value 25
print(a)                # prints 25
b = a                   # b is assigned the value of a (i.e., 25)
print(b)                # prints 25
print(a is b)           # True, both refer to the same integer object 25 
x = 4                   # x is assigned the value 4
y = 5                   # y is assigned the value 5
z = x + y * 6           # z = 4 + (5 * 6) = 34 
print(z)                # prints 34
25 = a                  # Error reference can't assign to a number
a + b = x + y           # Error left-hand side of assignment is an expression


# Find outputs (Home work)

a = b = c = 25           # All three variables point to the same integer object 25
print(id(a))             # Prints the address of the integer object 25
print(id(b))             # Same as id(a), since b refers to the same object
print(id(c))             # Same as id(a) and id(b), since c also refers to 25
print(a, b, c)           # Prints the 25 25 25


# Multiple Assignment (Home work)

x, y, z = 25, 10.8, 'Hyd'   # Assigns 25 to x, 10.8 to y, and 'Hyd' to z 
print(x)                    # Prints 25
print(y)                    # Prints 10.8
print(z)                    # Prints 'Hyd'


# Find outputs (Home work)

a, b, c = 3, 4, 5          # a = 3, b = 4, c = 5
a *= b + c                 # a = 3 * (4 + 5) = 3 * 9 = 27
print(a)                   # Prints 27


# Find outputs (Home work)

a = 20                  
a %= 3 + 2 * 4          # a %= 3 + 8 => a %= 11 => a = 20 % 11 = 9
print(a)                # Prints 9


# Find outputs (Home work)

a = 3           
a **= 4          # a = a ** 4 => a = 3 ** 4 = 81
print(a)         # Prints 81


# Identity operators demo program

a = 25                  # a is assigned the value 25
b = 25                  # b is also assigned 25, Python reuses immutable objects integers
print(a is b)           # True, a and b refer to the same address
print(a is not b)       # False, a and b are not different objects
print(a == b)           # True, values of a and b are equal


# Find outputs (Home work)

a = 25                  # 'a' is assigned an integer value
b = 25.0                # 'b' is assigned a float value
print(a is b)           # False, int and float are different objects
print(a is not b)       # True, 'a' and 'b' are not the same object
print(a == b)           # True, values are equal (25 == 25.0)


# Find outputs (Home work)

a = 'Hyd'
b = 'Hyd'
print(a is b)            # True, Both refer to the same string object due to string interning
print(a is not b)        # False, Same object, so 'is not' returns False
print(a == b)            # True, Values are equal
print()                  # Prints a blank line for separation
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x is y)            # False, Different list objects
print(x is not y)        # True, Not the same object
print(x == y)            # True, Contents of both lists are equal
print()                  # Prints a blank line for separation
m = (1, 2, 3, 4)
n = (1, 2, 3, 4)
print(m is n)            # True, Tuples with same values are often the same object 
print(m is not n)        # False, Same object, so 'is not' is False
print(m == n)            # True, Values are equal
print(x == m)            # False, List and tuple types are different, so not equal


# Membership operators demo program (Home work)

list = [10, 20, 15, 12, 18]
print(15 in list)           # True, 15 is present in the list
print(19 in list)           # False, 19 is not in the list
print(14 not in list)       # True, 14 is not in the list
print(15 not in list)       # False, 15 is in the list
s = 'Hyd is green city'
print('is' in s)            # True, Substring 'is' is in the string
print('was' in s)           # False, Substring 'was' is not in the string
print('g' in s)             # True, Character 'g' exists in the string
print('z' in s)             # False, Character 'z' does not exist in the string
print(' ' in s)             # True, There are space characters in the string
print('gre' in s)           # True, Substring 'gre' is present in 'green'
print('yd i' in s)          # True, Substring 'yd i' is found in 'Hyd is...'
print('' in s)              # True, Empty string is considered to be in any string
print('' not in s)          # False, Empty string is always considered to be in the string


# Find outputs (Home work)

x = [1, 2, 3, 4]       # List x with ordered elements
y = [1, 2, 4, 3]       # List y with the same elements in different order
print(x == y)          # False, Lists are ordered
a = (4, 1, 3, 2)       # Tuple a with a specific order
b = (4, 2, 3, 1)       # Tuple b with the same elements in different order
print(a == b)          # False tuples are ordered so not equal
p = {1, 2, 3, 4}       # Set p with 4 elements
q = {4, 1, 3, 2}       # Set q with same elements but different address
print(p == q)          # True, Sets are unordered
m = range(5)           # Range m from 0 to 4
n = range(5)           # Range n also from 0 to 4 but different address
print(m == n)          # True, Both ranges represent the same sequence


# Find outputs (Home work)

a = [10, 20, 30]    # a is a list
b = (10, 20, 30)    # b is a tuple
print(a is b)       # False     
print(a == b)       # False     