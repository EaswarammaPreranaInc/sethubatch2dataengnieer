# difference() method demo program
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.difference(b)
print(c)              # {10, 20}
print(type(c))        # <class 'set'>
d = a - b
print(d)              # {10, 20}
print(type(d))        # <class 'set'>
print(c is d)         # False
print(c == d)         # True

'''
difference() method
-------------------
1) a.difference(b) → Returns set with elements in 'a' but not in 'b'
2) set.difference(list) → Valid
3) Alternative to a.difference(b) → a - b
4) set - list → Invalid (both operands must be sets)
'''


# symmetric_difference() method demo program
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b)
print(c)              # {10, 20, 50, 60}
print(type(c))        # <class 'set'>
d = a ^ b
print(d)              # {10, 20, 50, 60}
print(type(d))        # <class 'set'>
print(c is d)         # False
print(c == d)         # True

'''
symmetric_difference() method
-----------------------------
1) a.symmetric_difference(b) → Returns elements of 'a' and 'b' without common ones
2) set.symmetric_difference(list) → Valid
3) Alternative → a ^ b
4) set ^ list → Invalid
'''


# Find outputs
a = {x * x for x in range(10)}
print(a)              # {0, 1, 64, 36, 100, 9, 16, 49, 81, 25}
print(type(a))        # <class 'set'>


# Program: Remove duplicate characters from string
s = input("Enter input string : ")
res = "".join(dict.fromkeys(s))   # preserves order
print("String without duplicates :", res)


# Program: Remove duplicate elements from list
lst = eval(input("Enter list with duplicates : "))
res = list(dict.fromkeys(lst))
print("List without duplicates :", res)


# Program: Find common elements between 2 lists
l1 = eval(input("Enter 1st list : "))
l2 = eval(input("Enter 2nd list : "))
common = list(set(l1) & set(l2))
print("Common elements between the 2 lists :", common)


# Access values of dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])    # 25
print(a['Ename'])    # Rama Rao
print(a['Sal'])      # 1000.65


# Modify values of dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))  # same id (mutable)


# Append key:value pairs to dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)


# Append into empty dictionary
a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)


# Remove key:value pairs from dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
del a['Sal']
print(a)


# in and not in operators with dict
a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())      # True
print(60 in a.keys())      # False
print(60 in a.values())    # True
print(30 in a.values())    # False
print(50 in a)             # True
print(20 in a)             # False
print(70 not in a.keys())  # False
print(40 not in a.values())# True
print(25 not in a)         # True


# Input dictionary with duplicate keys
a = input("Enter dictionary : ")
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
# Example input: {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
# Output: {10: 'A', 20: 'D', 15: 'C'}


# Find outputs
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}
print(b)          # same as a
print(a is b)     # False
print(a == b)     # True
c = a
print(a is c)     # True
print(a == c)     # True


# Merging multiple dicts
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)          # set of keys
print(type(d))    # <class 'set'>
e = {**a, **b, **c}
print(e)          # merged dict
print(type(e))    # <class 'dict'>


# Invalid addition of dicts
a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
# print(a + b)  TypeError
c = {**a, **b}
print(c)          # {10: 60, 30: 50}
d = a | b
print(d)          # {10: 60, 30: 50}


# Create dictionary of employees
a = {}
n = int(input("How many Employees ? : "))
for i in range(n):
    name = input("Enter Emp Name : ")
    sal = float(input("Enter Salary : "))
    a[name] = sal
print(a)


# Convert string to dictionary
s = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
parts = s.split(" , ")
a = {}
for p in parts:
    k, v = p.split(" = ")
    a[k.strip()] = v.strip()
print(a)


# len() demo
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))   # 3
b = {}
print(len(b))   # 0


# sum() demo
a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))     # 90
print(sum(a.values()))   # 120
print(sum(a))            # 90 (same as keys)
# print(sum(a.items()))  TypeError


# max() and min() demo
a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))     # 40
print(min(a.keys()))     # 7
print(max(a.values()))   # 50
print(min(a.values()))   # 5
print(max(a.items()))    # (40, 5) → compares keys first
print(min(a.items()))    # (7, 28)
print(max(a))            # 40
print(min(a))            # 7


# dict() function demo
a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
b = dict(a)
print(b)   # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}

c = (['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray'])
d = dict(c)
print(d)   # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}

e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(dict(e))  # {10: 20, 40: 50, 70: 80}

f = [[10], [20], [30]]
print(dict(f))  # {10: None, 20: None, 30: None}

# print(dict([10, 20]))  invalid

g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))  # {10: [20, 30], 40: [50, 60], 70: [80, 90]}

h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))  # {(10, 20): 30, (40, 50): 60, (70, 80): 90}

i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))  # {(10, 20): 30, (40, 50): 60, (70, 80): 90}


# sorted() demo
a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b)   # [5, 10, 15, 18, 20]
c = sorted(a.values())
print(c)   # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a.items())
print(d)   # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f = sorted(a, reverse=True)
print(f)   # [20, 18, 15, 10, 5]
print(a)


# Program: Sort dictionary wrt keys
d = eval(input("Enter dictionary : "))
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)


# clear() demo
a = {10: 20, 30: 40, 50: 60}
print(a)
a.clear()
print(a)   # {}
del a
# print(a)  NameError


# copy() demo
a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
b = a.copy()
print(b)
print(a is b)   # False
print(a == b)   # True


# keys() demo
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.keys()
print(b)
print(type(b))
for x in b:
    print(x)


# values() demo
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.values()
print(b)
print(type(b))
for x in b:
    print(x)


# items() demo
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.items()
print(b)
print(type(b))
for x in b:
    print(x)
for x, y in b:
    print(x, y, sep=" ... ")


# Find outputs
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
for x, y in a.items():
    print(x, y, sep=" ... ")
# for x, y in a.keys():  Error (keys are not pairs)
# for x, y in a.values():  Error (values are not pairs)
# for x, y in a:  Error (iterates only keys)


# Find outputs
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
x, y, z = a.keys()
print(x)
print(y)
print(z)
print()
x, y, z = a.values()
print(x)
print(y)
print(z)
print()
x, y, z = a.items()
print(x)
print(y)
print(z)
print()
(rno1, sname1), (rno2, sname2), (rno3, sname3) = a.items()
print(rno1, sname1)
print(rno2, sname2)
print(rno3, sname3)


# Program: Frequency of alphabets (ignoring case, sorted)
s = input("Enter mixed case string : ")
s = s.upper()
a = {}
for ch in sorted(s):
    if ch.isalpha():
        a[ch] = a.get(ch, 0) + 1
print(a)