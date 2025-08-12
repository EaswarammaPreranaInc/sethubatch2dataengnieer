print({10 , 20}  |  {30 , 20})                   # {10, 20, 30}
 print({10 : 'Hyd' , 20 : 'Sec'} | {30 : 'Cyb', 20 : 'Vja'})   # {10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
 print(range(4) | range(5))                       # Error: unsupported operand type(s) for |: 'range' and 'range'
 print([10 , 20] | [30 , 20])                       # Error: unsupported operand type(s) for |: 'list' and 'list'

a = 25
print(a)                   # 25
b = a
print(b)                   # 25
print(a is b)            # True, a, b points to same object
x = 4
y = 5
z = x + y * 6
print(z)                  # 34, 30+4
25 = a               # Error: can't assign to literal
a + b = x + y    # Error: can't assign to operator expression

a = b = c = 25
print(id(a))    # 140732940368824 (example ID)
print(id(b))    # same as id(a)
print(id(c))    # same as id(a)
print(a, b, c)  # 25 25 25

x, y, z = 25, 10.8, 'Hyd'
print(x)        # 25
print(y)        # 10.8
print(z)        # Hyd

a, b, c = 3, 4, 5
a *= b + c
print(a)        # 27, 3*9

a = 20
a %= 3 + 2 * 4
print(a)        # 9, 20 divide by 11 remainder is 9

a = 3
a **= 4
print(a)        # 81, 3^4

a = 25
b = 25
print(a is b)          # True, a,b points to same object
print(a is not b)      # False       , print(a == b)          # True, values of a,b are same
a = 25        # int
b = 25.0      # float
print(a is b)           # False, a, b point different objects
print(a is not b)     # True
print(a == b)         # True, values of a,b are same

a = 'Hyd'
b = 'Hyd'
print(a is b)         # True, a,b points same string
print(a is not b)     # False
print(a == b)         # True, char of both string match
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x is y)           # False, x,y point different lists
print(x is not y)     # True
print(x == y)         # True, values of both list match
m = (1, 2, 3, 4)
n = (1, 2, 3, 4)
print(m is n)         # True, m,n point same tuple
print(m is not n)     # False
print(m == n)         # True, values of both tuple match
print(x == m)         # False, x is a list and m is a tuple

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
print('' in s)           # True
print('' not in s)       # False

x = [1, 2, 3, 4]
y = [1, 2, 4, 3]
print(x == y)       # False, list order differs
a = (4, 1, 3, 2)
b = (4, 2, 3, 1)
print(a == b)       # False, tuple order differs
p = {1, 2, 3, 4}
q = {4, 1, 3, 2}
print(p == q)       # True, sets match
m = range(5)
n = range(5)
print(m == n)       # True, same range

a = [10, 20, 30]     # list
b = (10, 20, 30)     # tuple
print(a is b)        # False Even though values look same, list ≠ tuple
