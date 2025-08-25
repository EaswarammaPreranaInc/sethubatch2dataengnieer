a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b)
print(c)         # {40, 30}
print(type(c))   # <class 'set'>

d = a & b
print(d)         # {40, 30}
print(type(d))   # <class 'set'>

print(c is d)    # False (different objects)
print(c == d)    # True  (same contents)




a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.difference(b)
print(c)         # {10, 20}
print(type(c))   # <class 'set'>

d = a - b
print(d)         # {10, 20}
print(type(d))   # <class 'set'>

print(c is d)    # False
print(c == d)    # True





a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b)
print(c)         # {10, 20, 50, 60}
print(type(c))   # <class 'set'>

d = a ^ b
print(d)         # {10, 20, 50, 60}
print(type(d))   # <class 'set'>

print(c is d)    # False
print(c == d)    # True




a = {x * x for x in range(10)}
print(a)         # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a))   # <class 'set'>




s = "Rama Rao"
res = "".join(set(s))
print(res)  # order is not preserved → e.g. "ao mR"




lst = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
res = list(set(lst))
print(res)  
# Example: [False, 1, None, 'Sec', 10.8, 25, 'Hyd']




l1 = [10, 20, 30, 40, 50, 60]
l2 = [30, 40, 70, 80, 20]
common = list(set(l1) & set(l2))
print(common)    # [40, 20, 30]




a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])   # 25
print(a['Ename'])   # Rama Rao
print(a['Sal'])     # 1000.65





a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)   # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}




a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)
# {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}




a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
del a['Sal']
print(a)   # {'Empno': 25, 'Ename': 'Rama Rao'}





a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())     # True
print(60 in a.keys())     # False
print(60 in a.values())   # True
print(30 in a.values())   # False
print(50 in a)            # True (default checks keys)
print(20 in a)            # False
print(70 not in a.keys()) # False
print(40 not in a.values()) # False
print(25 not in a)        # True




# Input: {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
# In Python, duplicate keys are not allowed → last one overrides
a = {10: 'A', 20: 'D', 15: 'C'}
print(a)   # {10: 'A', 20: 'D', 15: 'C'}






a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}     # shallow copy
print(b)      # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b) # False
print(a == b) # True

c = a         # reference
print(a is c) # True
print(a == c) # True






a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}

d = {*a, *b, *c}
print(d)         # {10, 14, 15, 18, 19, 20, 25}  (just keys → set)
print(type(d))   # <class 'set'>

e = {**a, **b, **c}
print(e)         # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))   # <class 'dict'>





a = {10: 20, 30: 40}
b = {30: 50, 10: 60}

print(a + b)   # Error

c = {**a, **b}
print(c)       # {10: 60, 30: 50}

d = a | b      # (Python 3.9+ only)
print(d)       # {10: 60, 30: 50}





a = {}
n = int(input("How many Employees ? : "))

for i in range(n):
    name = input("Enter Emp Name : ")
    sal = float(input("Enter Salary : "))
    a[name] = sal   # append to dictionary

print(a)






s = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
pairs = s.split(" , ")   # split by comma

a = {}
for p in pairs:
    k, v = p.split(" = ", 1)  # split only on first '='
    a[k] = v

print(a)





a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))   # 3 → three key:value pairs

b = {}
print(len(b))   # 0 → empty dictionary





a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))     # 10+30+50 = 90
print(sum(a.values()))   # 20+40+60 = 120
print(sum(a))            # same as sum(a.keys()) = 90
print(sum(a.items()))    # Error







a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))    # 40
print(min(a.keys()))    # 7
print(max(a.values()))  # 50
print(min(a.values()))  # 5
print(max(a.items()))   # (40, 5)  (compares first by key)
print(min(a.items()))   # (7, 28)
print(max(a))           # 40  (keys only)
print(min(a))           # 7








a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
print(dict(a))   # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'} → last value kept

c = (['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray'])
print(dict(c))   # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}

e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(dict(e))   # Error

f = [[10], [20], [30]]
print(dict(f))   # Error

print(dict([10, 20]))  # Error

g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))   # {10: [20, 30], 40: [50, 60], 70: [80, 90]}

h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))   # {(10, 20): 30, (40, 50): 60, (70, 80): 90}

i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))   # {(10, 20): 30, (40, 50): 60, (70, 80): 90}







a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

b = sorted(a.keys())
print(b)   # [5, 10, 15, 18, 20]

c = sorted(a.values())
print(c)   # ['Blue', 'Green', 'Red', 'White', 'Yellow']

d = sorted(a.items())
print(d)   # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]

f = sorted(a, reverse=True)
print(f)   # [20, 18, 15, 10, 5]

print(a)   # original dict unchanged





a = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}
sorted_a = dict(sorted(a.items()))
print(sorted_a)






a = {10: 20, 30: 40, 50: 60}
print(a)     # {10: 20, 30: 40, 50: 60}
a.clear()
print(a)     # {}
del a
print(a)     # Error





s = input("Enter mixed case string : ")
s = s.upper()
a = {}

for ch in sorted(s):
    if ch.isalpha():
        a[ch] = a.get(ch, 0) + 1

print(a)













