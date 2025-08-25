# intersection() method demo program
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b)
print(c)              # {40, 30}
print(type(c))        # <class 'set'>
d = a & b
print(d)              # {40, 30}
print(type(d))        # <class 'set'>
print(c is d)         # False
print(c == d)         # True

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

# Find outputs
a = {x * x for x in range(10)}
print(a)              # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a))        # <class 'set'>

q) Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o
Ans) a = input('enter the list = ')
b = set(a)
c = "".join(b)
print(c)

q)Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
Ans) a = eval(input('enter the list = '))
b = set(a)
c = list(b)
print(c)

q) Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]
2) Both  input  and  output  are  lists
Ans) a = eval(input('enter the list1 = '))
b = eval(input('enter the list2 = '))
c = list(set(a)&set(b))
print(F'common of a and b = {c}' )

# How to access dictionary values
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])     # 25
print(a['Ename'])     # Rama Rao
print(a['Sal'])       # 1000.65

# Modify values in dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
#some address
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)              # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
#new address

# Append key:value pairs to dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a['Gender'] = 'M'
a['Married'] = True
print(a)     # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}


# Append values to empty dictionary
a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)              # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

# Remove key:value pairs from dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a.pop('Sal')
print(a)              # {'Empno': 25, 'Ename': 'Rama Rao'}

# in and not in operators
a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())     # True
print(60 in a.keys())     # False
print(60 in a.values())   # True
print(30 in a.values())   # False
print(50 in a)            # True
print(20 in a)            # False
print(70 not in a.keys()) # False
print(40 not in a.values()) # False
print(25 not in a)        # True

# What are the outputs if input is {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)       # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a)
print(b)       # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)              # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b)         # False  (different objects in memory)
print(a == b)         # True   (contents are same)
c = a
print(a is c)         # True   (same reference)
print(a == c)         # True   (contents are same)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)       # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e)       # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class 'dict'>

a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # Error: dict objects cannot be added using +
c = {**a , **b}
print(c)        # {10: 60, 30: 50}  (values from b overwrite a)
d = a | b
print(d)        # {10: 60, 30: 50}  (| merges dictionaries, b overwrites a)

q) Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
Ans) a = {}
n = int(input("Enter the no. of Employees  : "))
for i in range(n):
    name = input("Enter Emp Name : ")
    sal = float(input("Enter Salary : "))
    a[name] = sal
print(a)

q) Write  a  program  to  convert  a  string  to  dictionary
Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}
Hint :  Use  split()  method  twice
Ans) s = "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
a = {}
pairs = s.split(" , ")
for p in pairs:
    key, val = p.split(" = ")
    a[key] = val
print(a)

# len() function
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))     # 3
b = {}
print(len(b))     # 0
# sum() function
a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))    # 90
print(sum(a.values()))  # 120
print(sum(a))           # 90
#print(sum(a.items()))   # TypeError (cannot sum tuples)

# max() and min() functions
a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))    # 40
print(min(a.keys()))    # 7
print(max(a.values()))  # 50
print(min(a.values()))  # 5
print(max(a.items()))   # (40, 5)
print(min(a.items()))   # (7, 28)
print(max(a))           # 40
print(min(a))           # 7

#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)   # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)   # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e))   # Error: dictionary update sequence element has length 3; 2 is required
f = [[10] , [20] , [30]]
print(dict(f))   # Error: dictionary update sequence element has length 1; 2 is required
print(dict([10 , 20]))# Error: cannot convert int to dict because argument is not a nested sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))   # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h))   # {[10, 20]: 30, [40, 50]: 60, [70, 80]: 90}
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))   # {(10, 20): 30, (40, 50): 60, (70, 80): 90}

# sorted() function
a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
print(sorted(a.keys()))   # [5, 10, 15, 18, 20]
print(sorted(a.values())) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
print(sorted(a.items()))  # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
print(sorted(a, reverse=True)) # [20, 18, 15, 10, 5]
print(a)
q) Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}
Ans) a = eval(input("Enter the dictionary = "))
b = dict(sorted(a.items()))
print(b)

# clear() method
a = {10: 20, 30: 40, 50: 60}
a.clear()
print(a)  # {}

# copy() method
a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
b = a.copy()
print(b)         # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a is b)    # False
print(a == b)    # True

# keys() method
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a.keys()
print(b)           # dict_keys([10, 20, 15, 18])
print(type(b))     # <class 'dict_keys'>
for x in b:
   print(x)       # 10 # 20 # 15  # 18

# values() method
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a.values()
print(b)           # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))     # <class 'dict_values'>
for x in b:
    print(x)       # Hyd # Sec  # Cyb # Pune

#items()method
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a.items()
print(b)            # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))      # <class 'dict_items'>
for x in b:
    print(x)        # (10, 'Hyd') # (20, 'Sec') # (15, 'Cyb') # (18, 'Pune')

for x, y in b:
    print(x, y, sep=' ... ')  # 10 ... Hyd # 20 ... Sec # 15 ... Cyb # 18 ... Pune

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for x , y in a.items():
    print(x , y , sep = ' ... ') # 10 ... Hyd # 20 ... Sec # 15 ... Cyb # 18 ... Pune
for x , y in a.keys():
    print(x , y , sep = ' ... ') # Error: keys() returns only keys, cannot unpack into two variables
for x , y in a.values():
    print(x , y , sep = ' ... ') # Error: values() returns only values, cannot unpack into two variables
for x , y in a:
    print(x , y , sep = ' ... ') # Error: iterating a dictionary gives only keys, cannot unpack into two variables

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)  # 10
print(y)  # 20
print(z)  # 15
print()
x , y , z = a . values()
print(x)  # Rama
print(y)  # Sita
print(z)  # Rajesh
print()
x , y ,  z = a . items()
print(x)  # (10, 'Rama')
print(y)  # (20, 'Sita')
print(z)  # (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)  # 10 Rama
print(rno2 , sname2)  # 20 Sita
print(rno3 , sname3)  # 15 Rajesh

q) Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)
Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order
Ans) s = input("Enter the string: ")
s = s.upper()
lst = sorted(s)
a = {}
for ch in lst:
    if ch.isalpha():
        a[ch] = a.get(ch, 0) + 1
print(a)
