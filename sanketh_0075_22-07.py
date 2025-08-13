#22/07: Homework 7
a = {
    print('Hyd'),   # Hyd
    print('Sec'),   # Sec
    print('Cyb')    # Cyb
}
print(type(a))      # <class 'set'>  # { ... } creates a set
print(a)            # {None}         # print() returns None, so set has None
print(len(a))       # 1              # Only one element (None) in set

_ = 25
print(_)            # 25             # Value of _
print(type(_))      # <class 'int'>  # _ is an int
a, _, c = 10, 20, 30
print(a)            # 10             # a = 10
print(_)            # 20             # _ now updated to 20
print(c)            # 30             # c = 30
for _ in range(5):
    print(_, 'Hello')  # 0 Hello ... 4 Hello # _ used as loop variable
a = 25
print(id(a))        # 140733838292472 (example) # Unique id for 25
a = 35
print(id(a))        # 140733838292792 (example) # New id as int is immutable
a = 25.7
print(id(a))        # 2328924434768 (example) # Unique id
print(a)            # 25.7           # Value of a
a = 35.6
print(id(a))        # 2328924435056 (example) # New id for new float
print(a)            # 35.6           # Updated value
b = True
print(id(b))        # 140733838287688 (example) # id for True
b = False
print(id(b))        # 140733838287704 (example) # id for False
c = None
print(id(c))        # 140733838285600 (example) # id for None
c = None
print(id(c))        # 140733838285600 (same)   # id unchanged
a = 'Hyd'
print(id(a))        # 2328924408432 (example)  # id of string
a[1] = 'e'          #  Error: 'str' object does not support item assignment
a = 'Sec'
print(id(a))        # Won't execute if error above
b = (10, 20, 15, 18)
print(id(b))        # 2328924408144 (example) # id of tuple
b[2] = 19           #  Error: 'tuple' object does not support item assignment
b = (30, 40, 35, 32)
print(id(b))        # Won't execute if error above
c = range(5)
print(id(c))        # 2328924408576 (example) # id of range
c[3] = 10           #  Error: 'range' object does not support item assignment
c = range(5)
print(id(c))        # Won't execute if error above
a = 25
b = 25
print(a is b)       # True            # Same int object (interned)
c = 'Hyd'
d = 'Hyd'
print(c is d)       # True            # Same string object (interned)
e = False
f = False
print(e is f)       # True            # Same bool object
g = range(10)
h = range(10)
print(g is h)       # False           # Different range objects
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
print(a is b)       # False           # Different list objects
c = {10: 20, 30: 40}
d = {10: 20, 30: 40}
print(c is d)       # False           # Different dict objects
e = (10, 20, 15, 18)
f = (10, 20, 15, 18)
print(e is f)       # True            # Same tuple object (immutable)
g = {10, 20, 15, 18}
h = {10, 20, 15, 18}
print(g is h)       # False           # Different set objects
print(10 + 20)                        # 30              # Integer addition
print(10.8 + 20.6)                    # 31.4            # Float addition
print(3 + 4j + 5 + 6j)                # (8+10j)         # Complex addition
print(True + False)                   # 1               # True=1, False=0
print('Hyder' + 'abad')               # Hyderabad       # String concatenation
print('Sankar' + 'Dayal' + 'Sarma')   # SankarDayalSarma# String concatenation
print('10' + '20')                    # 1020            # String concatenation
print([10, 20, 30] + [1, 2, 3])       # [10, 20, 30, 1, 2, 3] # List concatenation
print((25, 10.8, 'Hyd') + (3+4j, True, None)) # (25, 10.8, 'Hyd', (3+4j), True, None) # Tuple concatenation
print({10, 20} + {30, 40})            #  Error         # '+' not supported for sets
print({10: 'Hyd'} + {20: 'Sec'})      #  Error         # '+' not supported for dicts
print(range(4) + range(5))            #  Error         # '+' not supported for range
print(10 + '20')                      #  Error         # Cannot add int and str
print([10, 20, 30] + 5)               #  Error         # Cannot add list and int
print([10, 20, 30] + (40, 50, 60))    #  Error         # Cannot add list and tuple
# Assignment operators demo program (Home work)
a = 25               # 25
print(a)             # 25
b = a                # 25
print(b)             # 25
print(a is b)        # True
x = 4                # 4
y = 5                # 5
z = x + y * 6        # 4 + 5*6 = 4 + 30 = 34
print(z)             # 34
# 25 = a             # SyntaxError: cannot assign to literal
# a + b = x + y      # SyntaxError: cannot assign to expression

# Find outputs (Home work)
a = b = c = 25
print(id(a))         # Same id for all since all refer to same int object
print(id(b))         # Same as id(a)
print(id(c))         # Same as id(a)
print(a, b, c)       # 25 25 25

# Multiple Assignment (Home work)
x, y, z = 25, 10.8, 'Hyd'
print(x)             # 25
print(y)             # 10.8
print(z)             # Hyd

# Find outputs (Home work)
a, b, c = 3, 4, 5
a *= b + c           # a = a * (b + c) = 3 * (4 + 5) = 3 * 9 = 27
print(a)             # 27

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4       # a %= (3 + 8) => a %= 11 => a = 20 % 11 = 9
print(a)             # 9

# Find outputs (Home work)
a = 3
a **= 4              # a = a ** 4 = 3 ** 4 = 81
print(a)             # 81

# Identity operators demo program
a = 25
b = 25
print(a is b)        # True
print(a is not b)    # False
print(a == b)        # True

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)        # False (different types: int and float)
print(a is not b)    # True
print(a == b)        # True (values are equal)

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a is b)        # True (string interning)
print(a is not b)    # False
print(a == b)        # True
print()
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x is y)        # False (different objects)
print(x is not y)    # True
print(x == y)        # True (values are equal)
print()
m = (1, 2, 3, 4)
n = (1, 2, 3, 4)
print(m is n)        # True (tuple interning)
print(m is not n)    # False
print(m == n)        # True
print(x == m)        # False (list != tuple)

# Membership operators demo program (Home work)
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

# Find outputs (Home work)
x = [1, 2, 3, 4]
y = [1, 2, 4, 3]
print(x == y)            # False (order matters in lists)
a = (4, 1, 3, 2)
b = (4, 2, 3, 1)
print(a == b)            # False (order matters in tuples)
p = {1, 2, 3, 4}
q = {4, 1, 3, 2}
print(p == q)            # True (order doesn't matter in sets)
m = range(5)
n = range(5)
print(m == n)            # True (same ranges)

# Find outputs (Home work)
a = [10, 20, 30]
b = (10, 20, 30)
print(a is b)            # False (list and tuple are different objects)
print(a == b)            # False (list != tuple)
