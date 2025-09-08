c = a . intersection(b) # {30, 40}                                                                                                                                                                                                                                                  c = a . intersection(b) # {30, 40}
print(type(c)) # <class 'set'>
d = a & b # {30, 40}
print(type(d)) # <class 'set'>
print(c is d) # False
print(c == d) # True



c = a . difference(b) # {10, 20}
print(type(c)) # <class 'set'>
d = a - b # {10, 20}
print(type(d)) # <class 'set'>
print(c is d) # False
print(c == d) # True

c = a . symmetric_difference(b) # {10, 20, 50, 60}
print(type(c)) # <class 'set'>
d = a ^ b # {10, 20, 50, 60}
print(type(d)) # <class 'set'>
print(c is d) # False
print(c == d) # True

a = {x * x for x in range(10)} # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) # <class 'set'>

s = input('Enter a string : ')
s = ''.join(dict.fromkeys(s))
print(s)

input_list = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
output_list = list(set(input_list))
print(output_list)

list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 20]
common_elements = list(set(list1) & set(list2))
print(common_elements)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])  # prints 25
print(a['Ename'])  # prints Rama Rao
print(a['Sal'])    # prints 1000.65

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)  # prints {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(id(a))
# Modifying values
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)  # prints {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)

# Appending key-value pairs
a.update({'Gender': 'M', 'Married': True})
print(a)

a = {}
a.update({10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'})
print(a)

a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())  # True
print(60 in a.keys())  # False
print(60 in a.values())  # True
print(30 in a.values())  # False
print(50 in a)  # True
print(20 in a)  # False
print(70 not in a.keys())  # False
print(40 not in a.values())  # False
print(25 not in a)  # True

Enter dictionary : {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
{10: 'A', 20: 'B', 15: 'C', 20: 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}
print(b)  # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b)  # False
print(a == b)  # True
c = a
print(a is c)  # True
print(a == c)  # True
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)  # {10, 20, 15, 18, 14, 25, 19}
print(type(d))  # <class 'set'>
e = {**a, **b, **c}
print(e)  # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))  # <class 'dict'>
a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
# print(a + b)  # This will raise a TypeError
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

c = {**a, **b}
print(c)  # {10: 60, 30: 50}

d = a | b
print(d)  # {10: 60, 30: 50}
 
a = {}
n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    a[name] = salary

print("Employee Salaries:")
print(a)

s = input("Enter a string in the format 'key = value, key = value': ")
d = {}
pairs = s.split(',')
for pair in pairs:
    key, value = pair.split('=')
    key = key.strip()
    value = value.strip()
    try:
        d[key] = float(value)
    except ValueError:
        d[key] = value

print("Dictionary:")
print(d)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))  # Output: 3

b = {}
print(len(b))  # Output: 0

a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))  # Output: 90 (10 + 30 + 50)
print(sum(a.values()))  # Output: 120 (20 + 40 + 60)
print(sum(a))  # Output: 90 (10 + 30 + 50)
# print(sum(a.items()))  # This will raise a TypeError

a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))  # Output: 40
print(min(a.keys()))  # Output: 7
print(max(a.values()))  # Output: 50
print(min(a.values()))  # Output: 5
print(max(a.items()))  # Output: (40, 5)
print(min(a.items()))  # Output: (7, 28)
print(max(a))  # Output: 40
print(min(a))  # Output: 7
 
 = dict(a)
print(b)  # Output: {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}

c = (['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray'])
d = dict(c)
print(d)  # Output: {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}

e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(dict(e))  # This will raise a ValueError

f = [[10], [20], [30]]
# print(dict(f))  # This will raise a ValueError

# print(dict([10, 20]))  # This will raise a ValueError

g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))  # Output: {10: [20, 30], 40: [50, 60], 70: [80, 90]}

h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))  # Output: {(10, 20): 30, (40, 50): 60, (70, 80): 90}

i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))  # Output: {(10, 20): 30, (40, 50): 60, (70, 80): 90}

a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b)  # Output: [5, 10, 15, 18, 20]

c = sorted(a.values())
print(c)  # Output: ['Blue', 'Green', 'Red', 'White', 'Yellow']

d = sorted(a.items())
print(d)  # Output: [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]

f = sorted(a, reverse=True)
print(f)  # Output: [20, 18, 15, 10, 5]

print(a)  # Output: {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

a = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}
b = dict(sorted(a.items()))
print(b)  # Output: {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

a = {10: 20, 30: 40, 50: 60}
print(a)  # Output: {10: 20, 30: 40, 50: 60}
a.clear()
print(a)  # Output: {}

del a
# print(a)  # This will raise a NameError

a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
b = a.copy()
print(b)  # Output: {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a is b)  # Output: False
print(a == b)  # Output: True

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.keys()
print(b)  # Output: dict_keys([10, 20, 15, 18])
print(type(b))  # Output: <class 'dict_keys'>
for x in b:
    print(x)
# Output:
# 10
# 20
# 15
# 18

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.values()
print(b)  # Output: dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))  # Output: <class 'dict_values'>
for x in b:
    print(x)
# Output:
# Hyd
# Sec
# Cyb
# Pune

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.items()
print(b)  # Output: dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))  # Output: <class 'dict_items'>
for x in b:
    print(x)
# Output:
# (10, 'Hyd')
# (20, 'Sec')
# (15, 'Cyb')
# (18, 'Pune')

for x, y in b:
    print(x, y, sep=' ... ')
# Output:
# 10 ... Hyd
# 20 ... Sec
# 15 ... Cyb
# 18 ... Pune

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
for x, y in a.items():
    print(x, y, sep=' ... ')
# Output:
# 10 ... Hyd
# 20 ... Sec
# 15 ... Cyb
# 18 ... Pune

for x, y in a.keys():
    # This will raise a ValueError because a.keys() only returns keys, not key-value pairs
    # print(x, y, sep=' ... ')
    # Instead, you can use:
    for x in a.keys():
        print(x)
    # Output:
    # 10
    # 20
    # 15
    # 18

for x, y in a.values():
    # This will raise a ValueError because a.values() only returns values, not key-value pairs
    # print(x, y, sep=' ... ')
    # Instead, you can use:
    for x in a.values():
  print(x)
    # Output:
    # Hyd
    # Sec
    # Cyb
    # Pune

for x, y in a:
    # This will raise a ValueError because iterating over a dictionary only returns keys, not key-value pairs
    # print(x, y, sep=' ... ')
    # Instead, you can use:
    for x in a:
        print(x, a[x], sep=' ... ')
    # Output:
    # 10 ... Hyd
    # 20 ... Sec
    # 15 ... Cyb
    # 18 ... Pune



a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
x, y, z = a.keys()
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 15
print()

x, y, z = a.values()
print(x)  # Output: Rama
print(y)  # Output: Sita
print(z)  # Output: Rajesh
print()

# This will raise a ValueError because a.items() returns a list of tuples, not individual values
# x, y, z = a.items()
# Instead, you can use:
x, y, z = a.items()
print(list(a.items())[0])  # Output: (10, 'Rama')
print(list(a.items())[1])  # Output: (20, 'Sita')
print(list(a.items())[2])  # Output: (15, 'Rajesh')
print()

(rno1, sname1), (rno2, sname2), (rno3, sname3) = a.items()
print(rno1, sname1)  # Output: 10 Rama
print(rno2, sname2)  # Output: 20 Sita
print(rno3, sname3)  # Output: 15 Rajesh

def alphabet_frequency(s):
    s = s.upper()
    a = {}
    for char in sorted(s):
        if char.isalpha():
            a[char] = a.get(char, 0) + 1
    return dict(sorted(a.items()))

s = "RamA raO"
print(alphabet_frequency(s))  # Output: {'A': 3, 'M': 1, 'O': 1, 'R': 2}
