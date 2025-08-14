# Find outputs
print({10 , 20} | {30 , 20})  # {10, 20, 30}
print({10: 'Hyd', 20: 'Sec'} | {30: 'Cyb', 20: 'Vja'})
# {10: 'Hyd', 20: 'Vja', 30: 'Cyb'} 
print(range(4) | range(5))  # TypeError
print([10, 20] | [30, 20])  # TypeError


# Assignment operators demo program (Homework)
a = 25
print(a)  # 25
b = a
print(b)  # 25
print(a is b)  # True
x = 4
y = 5
z = x + y * 6
print(z)  # 4 + 30 = 34

25 = a  
#SyntaxError: cannot assign to literal
a + b = x + y  
#SyntaxError: cannot assign to expression


# Find outputs
a = b = c = 25
print(id(a))  # id of object 25
print(id(b))  # same as a
print(id(c))  # same as a
print(a, b, c)  # 25 25 25


# Multiple Assignment
x, y, z = 25, 10.8, 'Hyd'
print(x)  # 25
print(y)  # 10.8
print(z)  # 'Hyd'

# Find outputs
a, b, c = 3, 4, 5
a *= b + c
a = 3 * (4 + 5) = 3 * 9 = 27
print(a)  # 27


# Find outputs
a = 20
a %= 3 + 2 * 4
a %= 3 + 8 = 11 → 20 % 11 = 9
print(a)  # 9


# Find outputs
a = 3
a **= 4  # 3 ** 4 = 81
print(a)  # 81


# Identity operators demo
a = 25
b = 25
print(a is b)        # True (same object in cache)
print(a is not b)    # False
print(a == b)        # True


# Find outputs
a = 25
b = 25.0
print(a is b)        # False (int vs float → different objects)
print(a is not b)    # True
print(a == b)        # True (values are equal)


# Find outputs
a = 'Hyd'
b = 'Hyd'
print(a is b)        # True (string interning)
print(a is not b)    # False
print(a == b)        # True
print()
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x is y)        # False (different list objects)
print(x is not y)    # True
print(x == y)        # True (same values)
print()
m = (1, 2, 3, 4)
n = (1, 2, 3, 4)
print(m is n)        # True (tuples with same values may be cached)
print(m is not n)    # False
print(m == n)        # True
print(x == m)        # False (list vs tuple → different types)


# Membership operators demo
list = [10, 20, 15, 12, 18]
print(15 in list)        # True
print(19 in list)        # False
print(14 not in list)    # True
print(15 not in list)    # False

s = 'Hyd is green city'
print('is' in s)         # True
print('was' in s)        # False
print('g' in s)          # True
print('z' in s)          # False
print(' ' in s)          # True
print('gre' in s)        # True
print('yd i' in s)       # True
print('' in s)           # True (empty string is in all strings)
print('' not in s)       # False


# Find outputs
x = [1, 2, 3, 4]
y = [1, 2, 4, 3]
print(x == y)  # False (different order)
a = (4, 1, 3, 2)
b = (4, 2, 3, 1)
print(a == b)  # False (order matters)
p = {1, 2, 3, 4}
q = {4, 1, 3, 2}
print(p == q)  # True (sets are unordered)
m = range(5)
n = range(5)
print(m == n)  # True (equal range objects)


# Find outputs
a = [10, 20, 30]
b = (10, 20, 30)
print(a is b)   # False (different types, different objects)
print(a == b)   # False (list != tuple → even if elements match)


s = {20,12,4,320,320}
print(s) # {20,12,4,320}

for i in s:
    print(i)

print(s | {12,320,43,1})
