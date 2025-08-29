#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)           # {40, 30}
print(type(c))     # <class 'set'>
d = a & b
print(d)           # {40, 30}
print(type(d))     # <class 'set'>
print(c  is  d)    # False
print(c  ==  d)    # True

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)           # {10, 20}
print(type(c))     # <class 'set'>
d = a - b
print(d)           # {10, 20}
print(type(d))     # <class 'set'>
print(c  is  d)    # False
print(c  ==  d)    # True

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)           # {50, 20, 10, 60}
print(type(c))     # <class 'set'>
d = a ^ b
print(d)           # {50, 20, 10, 60}
print(type(d))     # <class 'set'>
print(c   is   d)  # False
print(c  ==   d)   # True

# Find outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)           # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a))     # <class 'set'>

# Remove duplicate characters of string using set (Home  work)
input_str = input("Enter  input  string : ")
result = ''.join(set(input_str))
print(result)      # ao mR (order can vary)

# Enter  input  string :  Rama Rao
# String  without  duplicates  :   ao mR  (order can vary)

# Remove duplicate elements of list using set (Home  work)
input_list = [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
result = list(set(input_list))
print(result)      # [False, 1, None, 'Sec', 10.8, 25, 'Hyd'] (order can vary)

# Enter  list  with  duplicates :  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
# List  without  duplicates :   [False, 1, None, 'Sec', 10.8, 25, 'Hyd'] (order can vary)

# Obtain common elements between two lists using sets (Home  work)
list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
common = list(set(list1) & set(list2))
print(common)      # [40, 20, 30] (order can vary)

# Enter 1st list : [10,20,30,40,50,60]
# Enter 2nd list : [30,40,70,80,20]
# Common elements between the 2 lists :   [40, 20, 30] (order can vary)

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])       # 25
print(a['Ename'])       # Rama Rao
print(a['Sal'])         # 1000.65

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)                # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(id(a))            # <id-1>
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)                # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))            # <id-1> (same as before)

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)                # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a['Gender'] = 'M'
a['Married'] = True
print(a)                # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

# Find  outputs (Home  work)
a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)                # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#  How  to  remove  key : value  pairs  of  dictionary (Home  work)
a =  {'Empno':25,'Ename':'Rama Rao','Sal':1000.65}
print(a)                # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
del a['Sal']
print(a)                # {'Empno': 25, 'Ename': 'Rama Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())         # True
print(60  in  a . keys())         # False
print(60  in  a . values())       # True
print(30  in  a . values())       # False
print(50  in  a)                  # True
print(20  in  a)                  # False
print(70  not  in  a . keys())    # False
print(40  not  in  a . values())  # False
print(25  not  in  a)             # True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = "{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}"    # as input string
print(a)                # {10: 'A', 20: 'B', 15: 'C' , 20: 'D'}
print(type(a))          # <class 'str'>
b = eval(a)
print(b)                # {10: 'A', 20: 'D', 15: 'C'}
print(type(b))          # <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)                # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b)         # False
print(a  ==  b)         # True
c = a
print(a  is   c)        # True
print(a  ==  c)         # True

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)                # {10, 14, 15, 18, 19, 20, 25}
print(type(d))          # <class 'set'>
e = {**a , **b , **c}
print(e)                # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))          # <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b)           # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
c = {**a , **b}
print(c)                # {10: 60, 30: 50}
d = a | b
print(d)                # {10: 60, 30: 50}

# Write a program to create a dictionary with emp names and salaries (Home work)
# How many Employees ? : 4
# Enter Emp Name : AAA
# Enter Salary : 100000
# Enter Emp Name : BBB
# Enter Salary : 200000
# Enter Emp Name : CCC
# Enter Salary : 150000
# Enter Emp Name : DDD
# Enter Salary : 175000
# {'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}
a={}
b=int(input("How many Employees ? : "))
for i in range(b):
        name=input("Enter Emp Name : ")
        sal=float(input("Enter Salary : "))
        a[name]=sal
print(a)

# Write a program to convert a string to dictionary (Home work)
s = input("Enter string : ")
result = {}
b=s.split(',')
for i in b:
        k,v = i.split(':')
        result[k.strip()] = v.strip()
print(result)           # {'Emp no': '25', 'Emp name': 'Rama  Rao', 'sal': '10000.0', 'gender': 'm'}

# len()  function  demo  program  (Home  work)
a  =  {'Empno':25,'Ename':'Rama Rao','Sal':1000.65}
print(len(a))           # 3
b = {}
print(len(b))           # 0

# sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))      # 90
print(sum(a . values()))    # 120
print(sum(a))               # 90
# print(sum(a . items()))    # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))      # 40
print(min(a . keys()))      # 7
print(max(a . values()))    # 50
print(min(a . values()))    # 5
print(max(a . items()))     # (40, 5)
print(min(a . items()))     # (7, 28)
print(max(a))               # 40
print(min(a))               # 7

# dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)                    # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)                    # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
# print(dict(e))            # ValueError: dictionary update sequence element #0 has length 3; 2 is required
f = [[10] , [20] , [30]]
# print(dict(f))            # ValueError: dictionary update sequence element #0 has length 1; 2 is required
# print(dict([10 , 20]))    # TypeError: 'int' object is not iterable
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))              # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h))              # {(10, 20): 30, (40, 50): 60, (70, 80): 90}
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))              # {(10, 20): 30, (40, 50): 60, (70, 80): 90}

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)                    # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)                    # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)                    # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)                    # [20, 18, 15, 10, 5]
print(a)                    # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

# Tricky  program - sort dictionary wrt keys (Home work)
s = eval(input('Enter dictionary'))
sorted_dict = {k: s[k] for k in sorted(s)}
print(sorted_dict)          # {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

# Enter  dictionary  :  {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
# {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)                    # {10: 20, 30: 40, 50: 60}
a . clear()
print(a)                    # {}
del  a
# print(a)                  # NameError: name 'a' is not defined

# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)                    # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b)             # False
print(a  ==  b)             # True

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)                    # dict_keys([10, 20, 15, 18])
print(type(b))              # <class 'dict_keys'>
for  x  in   b:
        print(x)            # 10 20 15 18

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)                    # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))              # <class 'dict_values'>
for  x   in   b:
	print(x)                # Hyd Sec Cyb Pune

# items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)                    # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))              # <class 'dict_items'>
for  x   in   b:
        print(x)            # (10, 'Hyd') (20, 'Sec') etc.
for  x , y   in  b:
        print(x , y , sep = ' ... ')  # 10 ... Hyd etc.

# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')   # 10 ... Hyd etc.
# for  x , y   in  a . keys():         # ValueError: not enough values to unpack (expected 2, got 1)
# for  x , y   in  a . values():       # ValueError: not enough values to unpack (expected 2, got 1)
# for  x , y   in  a:                  # ValueError: not enough values to unpack (expected 2, got 1)

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)      # 10
print(y)      # 20
print(z)      # 15
print()
x , y , z = a . values()
print(x)      # Rama
print(y)      # Sita
print(z)      # Rajesh
print()
x , y ,  z = a . items()
print(x)      # (10, 'Rama')
print(y)      # (20, 'Sita')
print(z)      # (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)      # 10 Rama
print(rno2 , sname2)      # 20 Sita
print(rno3 , sname3)      # 15 Rajesh

# Write a program to determine frequency of each alphabet in a string in alphabetical order (Home work)
input_str = input("enter string")
r={}
for i in set(input_str):
        r[i]=input_str.count(i)
print(r)              