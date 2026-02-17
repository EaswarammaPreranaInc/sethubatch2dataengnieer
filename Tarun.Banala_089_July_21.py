#Name: *Tarun Banala*  21-07-2025

# Dictionary printing in various ways
a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

print('Dictionary with print function')
print(a)  # Prints the entire dictionary

print('Keys of dictionary')
for k in a:  # Loops through keys
    print(k)  # Prints each key

print('Values of dictionary')
for v in a.values():  # Loops through values
    print(v)  # Prints each value

print('All the tuples of dict_items object')
for item in a.items():  # Loops through (key, value) pairs
    print(item)  # Prints each (key, value) tuple

print('Elements of each tuple')
for k, v in a.items():  # Unpacks each (key, value) tuple
    print(k, v)  # Prints key and value

print('Keys and values of dictionary')
for k in a:  # Loops through keys
    print(k, a[k])  # Prints key and its corresponding value

# Find outputs (Home work)
a = {
    print('Hyd'),  # Prints 'Hyd', returns None
    print('Sec'),  # Prints 'Sec', returns None
    print('Cyb')   # Prints 'Cyb', returns None
}  # Set contains one element: None

print(type(a))  # <class 'set'>
print(a)  # {None}
print(len(a))  # 1

# Anonymous object demo program
_ = 25
print(_)  # 25
print(type(_))  # <class 'int'>
a, _, c = 10, 20, 30
print(a)  # 10
print(_)  # 20
print(c)  # 30
for _ in range(5):  # Loops 5 times
    print(_, 'Hello')  # Prints loop index and 'Hello'

# Find outputs
a = 25
print(id(a))  # Memory address of integer 25
a = 35
print(id(a))  # Different address (35 is a different object)

# Find outputs (Home work)
a = 25.7
print(id(a))  # ID of float 25.7
print(a)  # 25.7
a = 35.6
print(id(a))  # ID of float 35.6
print(a)  # 35.6
b = True
print(id(b))  # ID of True (usually 1)
b = False
print(id(b))  # ID of False (usually 0)
c = None
print(id(c))  # ID of None (singleton)
c = None
print(id(c))  # Same ID

# Find outputs (Home work)
a = 'Hyd'
print(id(a))  # ID of string 'Hyd'
# a[1] = 'e'  # Error: strings are immutable
a = 'Sec'
print(id(a))  # ID of new string 'Sec'
b = (10, 20, 15, 18)
print(id(b))  # ID of tuple
# b[2] = 19  # Error: tuples are immutable
b = (30, 40, 35, 32)
print(id(b))  # ID of new tuple
c = range(5)
print(id(c))  # ID of range object
# c[3] = 10  # Error: range is immutable
c = range(5)
print(id(c))  # Possibly same or new ID

# Find outputs (Home work)
a = 25
b = 25
print(a is b)  # True (small ints are cached)
c = 'Hyd'
d = 'Hyd'
print(c is d)  # True (string interning)
e = False
f = False
print(e is f)  # True
g = range(10)
h = range(10)
print(g is h)  # False (separate objects)

# Find outputs (Home work)
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
print(a is b)  # False (different list objects)
c = {10: 20, 30: 40}
d = {10: 20, 30: 40}
print(c is d)  # False (different dictionary objects)
e = (10, 20, 15, 18)
f = (10, 20, 15, 18)
print(e is f)  # True or False (depends on interning)
g = {10, 20, 15, 18}
h = {10, 20, 15, 18}
print(g is h)  # False (different set objects)

# Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # (8+10j)
print(True + False)  # 1 (True=1, False=0)
print('Hyder' + 'abad')  # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')  # 'SankarDayalSarma'
print('10' + '20')  # '1020'
print([10, 20, 30] + [1, 2, 3])  # [10, 20, 30, 1, 2, 3]
print((25, 10.8, 'Hyd') + (3 + 4j, True, None))  # Combined tuple
# print({10, 20} + {30, 40})  # Error: sets can't be added
# print({10: 'Hyd'} + {20: 'Sec'})  # Error: dicts can't be added
# print(range(4) + range(5))  # Error: ranges can't be added
# print(10 + '20')  # Error: int + str not allowed
# print([10, 20, 30] + 5)  # Error: list + int not allowed
# print([10, 20, 30] + (40, 50, 60))  # Error: list + tuple not allowed

# Find outputs (Home work)
print(25 * 3)  # 75
print(10.8 * 25.6)  # 276.48
print(True * False)  # 0
print((3 + 4j) * (5 + 6j))  # (-9+38j)
print(3 + 4j * 5 + 6j)  # (3+26j), 4j*5=20j + 6j = 26j
print('25' * 3)  # '252525'
print(3 * '25')  # '252525'
print('Hyd' * 4)  # 'HydHydHydHyd'
print([10, 20, 15] * 2)  # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3)  # Tuple repeated 3 times
# print([10, 20, 15] * 3.0)  # Error: can't multiply by float
# print({10, 20, 15} * 2)  # Error: sets can't be multiplied
# print({10: 20, 30: 40} * 2)  # Error: dicts can't be multiplied
# print([10] * [20])  # Error: list can't be multiplied by list

# / operator demo
print(9.0 / 2)  # 4.5
print(9 / 2.0)  # 4.5
print(9.0 / 2.0)  # 4.5
print(9 / 2)  # 4.5
print(10.5 / 2)  # 5.25
print(10 / 3)  # 3.333...
print(10 / 2)  # 5.0

# // operator demo
print(9 // 2)  # 4
print(9.0 // 2)  # 4.0
print(9 // 2.0)  # 4.0
print(9.0 // 2.0)  # 4.0
print(10.5 // 2)  # 5.0
print(10 // 3)  # 3
print(10.0 // 3)  # 3.0
print(8.5 // 3)  # 2.0
print(18 // 4)  # 4
print(-18 // 4)  # -5
print(-(18 // 4))  # -4

# % operator demo
print(9 % 5)  # 4
print(9.0 % 5)  # 4.0
print(9 % 5.0)  # 4.0
print(9.0 % 5.0)  # 4.0
print(10.5 % 2)  # 0.5
print(8.9 % 3)  # 2.9

# print(7 / 0)  # Error: division by zero
# print(7 // 0)  # Error: division by zero
# print(7 % 0)  # Error: division by zero

# ** operator demo
print(3 ** 4)  # 81
print(10 ** -2)  # 0.01
print(4 ** 3 ** 2)  # 4 ** 9 = 262144
print(3 + 4 * 5 - 32 / 2 ** 3)  # 3 + 20 - 4 = 19.0

# Relational operators
print(9 >= 5)  # True
print(9 >= 9)  # True
print(9 >= 12)  # False
print(6 <= 8)  # True
print(6 <= 6)  # True
print(6 <= 4)  # False
print(9 != 7)  # True
print(6 == 8)  # False
print(True > False)  # True
print(3 + 4j == 3 + 4j)  # True
print(3 + 4j == 5 + 6j)  # False
print(3 + 4j != 5 + 6j)  # True
print(10 == 10.0)  # True
# print(3 + 4j > 3 + 4j)  # Error: not supported for complex numbers

# String comparisons
print('Rama' > 'Rajesh')  # True
print('Rama' < 'Sita')  # True
print('Hyd' == 'Hyd')  # True
print('Rama' <= 'Ramana')  # True
print('Rama Rao' >= 'Rama')  # True
print('Hyd' != 'Sec')  # True
print('HYD' < 'hyd')  # True (capital letters < lowercase)

# Chaining relational operators
print(10 < 20 < 30)  # True
print(10 >= 20 < 30)  # False
print(10 < 20 > 30)  # False
print(1 < 2 < 3 < 4)  # True
print(1 < 2 > 3 > 1)  # False
print(4 > 3 >= 3 > 2)  # True

# or operator
print(True or False)  # True
print(False or True)  # True
print(True or True)  # True
print(False or False)  # False
print(10 or 20)  # 10 (first truthy value)
print(0 or 20)  # 20
print(-25 or 0)  # -25
print('' or 35)  # 35
print(6j or 'Hyd')  # 6j
print(0.0 or 3 + 4j)  # (3+4j)
print('Hyd' or 10.8)  # 'Hyd'

# not operator
print(not True)  # False
print(not False)  # True
print(not 25)  # False (non-zero is True → not True = False)
print(not 0)  # True
print(not 'Hyd')  # False
print(not '')  # True
print(not -10)  # False
print(not not 'Hyd')  # True

# Final logical expression
i = 10
i = not i > 14  # i > 14 is False is not False = True
print(i)  # True
print(not (6 < 4 or 9 >= 5 and 6 != 6))  # True
