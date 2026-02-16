1.
text
# Find outputs (Home work)
a = 3
# Explanation: Variable `a` is initialized with the value 3.

a **= 4
# Explanation: This is a compound assignment operator.
# The expression `a **= 4` is equivalent to `a = a ** 4`.
#
# Step 1: Perform the exponentiation.
#   `3 ** 4` means 3 raised to the power of 4, which is 3 * 3 * 3 * 3 = 81.
#
# Step 2: Assign the result to `a`.
#   So, `a` is assigned the value 81.

print(a)
# Output: 81
# Explanation: The final value of `a` after the exponentiation and assignment is 81.





2.
text
# Membership operators demo program

list = [10, 20, 15, 12, 18]

print(15 in list)
# Output: True
# Explanation: The element `15` is present in the `list`.

print(19 in list)
# Output: False
# Explanation: The element `19` is not present in the `list`.

print(14 not in list)
# Output: True
# Explanation: The element `14` is not present in the `list`.

print(15 not in list)
# Output: False
# Explanation: The element `15` *is* present in the `list`, so `15 not in list` is False.

s = 'Hyd is green city'

print('is' in s)
# Output: True
# Explanation: The substring `'is'` is found within the string `s`.

print('was' in s)
# Output: False
# Explanation: The substring `'was'` is not found within the string `s`.

print('g' in s)
# Output: True
# Explanation: The character `'g'` is found within the string `s`.

print('z' in s)
# Output: False
# Explanation: The character `'z'` is not found within the string `s`.

print(' ' in s)
# Output: True
# Explanation: The space character `' '` is found within the string `s`.

print('gre' in s)
# Output: True
# Explanation: The substring `'gre'` is found within the string `s`.

print('yd i' in s)
# Output: True
# Explanation: The substring `'yd i'` is found within the string `s`.

print('' in s)
# Output: True
# Explanation: An empty string `''` is always considered to be a substring of any string (it can be found at any position, including before the first character and after the last).

print('' not in s)
# Output: False
# Explanation: Since an empty string `''` *is* found in `s`, `'' not in s` is False.





3.
text
# Identity operators demo program

a = 25
b = 25
# Explanation: For small integers (typically -5 to 256 in CPython, the standard Python interpreter),
# Python performs an optimization called "interning" or "caching." This means that
# when you assign the same small integer literal to different variables, those variables
# will actually refer to the *same* underlying integer object in memory.

print(a is b)
# Output: True
# Explanation: The `is` operator checks for object identity (i.e., if two variables refer to the exact same object in memory).
# Due to integer interning, `a` and `b` both point to the same object representing the integer 25, so this returns True.

print(a is not b)
# Output: False
# Explanation: The `is not` operator checks if two variables do *not* refer to the same object.
# Since `a` and `b` *do* refer to the same object, this expression evaluates to False.

print(a == b)
# Output: True
# Explanation: The `==` operator checks for value equality. Since the value of `a` (25) is
# equal to the value of `b` (25), this returns True.




4.
text
# Find outputs (Home work)
--- Strings ---
a = 'Hyd'
b = 'Hyd'
# Explanation: For short string literals, Python (CPython implementation) often "interns" them for efficiency.
# This means that if identical string literals are created, they often refer to the exact same object in memory.

print(a is b)
# Output: True
# Explanation: Due to string interning, `a` and `b` refer to the same string object in memory.

print(a is not b)
# Output: False
# Explanation: Since `a` and `b` refer to the same object, they are not "not the same object."

print(a == b)
# Output: True
# Explanation: The values of `a` and `b` are identical.

print() # Prints a blank line for separation

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
# Explanation: Lists are mutable data types. When you create two lists using separate literal syntax (`[]`),
# Python always creates two *distinct* list objects in memory, even if their contents are identical.
# Python does not intern mutable objects like lists.

print(x is y)
# Output: False
# Explanation: `x` and `y` are two separate list objects, even though they contain the same elements.

print(x is not y)
# Output: True
# Explanation: Since `x` and `y` are distinct objects, they are indeed "not the same object."

print(x == y)
# Output: True
# Explanation: The `==` operator checks for value equality. The contents (elements and their order) of `x` and `y` are identical.

print() # Prints a blank line for separation

--- Tuples ---
m = (1, 2, 3, 4)
n = (1, 2, 3, 4)
# Explanation: Tuples are immutable data types. Similar to small integers and strings,
# Python sometimes interns or caches simple, identical tuple literals (especially those 
# containing only other immutable types) for optimization.

print(m is n)
# Output: True
# Explanation: Due to optimization for immutable tuple literals, `m` and `n` often refer to the same tuple object in memory.

print(m is not n)
# Output: False
# Explanation: Since `m` and `n` refer to the same object, they are not "not the same object."

print(m == n)
# Output: True
# Explanation: The values of `m` and `n` are identical.

--- Cross-type comparison ---
print(x == m)
# Output: True
# Explanation: The `==` operator performs value comparison. For sequences like lists and tuples,
# Python checks if they have the same length and if their corresponding elements are equal.
# Even though `x` is a list and `m` is a tuple, their contents are element-wise identical.
