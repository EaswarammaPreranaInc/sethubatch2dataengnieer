# intersection() method demo program (Home work)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b)
print(c)          # {40, 30}
print(type(c))    # <class 'set'>
d = a & b
print(d)          # {40, 30}
print(type(d))    # <class 'set'>
print(c is d)     # False  
print(c == d)     # True  


# difference() method demo program (Home work)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.difference(b)
print(c)          # {10, 20}
print(type(c))    # <class 'set'>
d = a - b
print(d)          # {10, 20}
print(type(d))    # <class 'set'>
print(c is d)     # False  
print(c == d)     # True  


# symmetric_difference() method demo program (Home work)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b)
print(c)          # {10, 20, 50, 60}
print(type(c))    # <class 'set'>
d = a ^ b
print(d)          # {10, 20, 50, 60}
print(type(d))    # <class 'set'>
print(c is d)     # False  
print(c == d)     # True   


# Find outputs (Home work)

a = {x * x for x in range(10)}
print(a)        # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a))  # <class 'set'>


'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o
2) Both  input  and  output  are  strings
3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)
4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but not 'Hyd'
'''

s = input("Enter input string : ")   
char_set = set(s)
result = ''.join(char_set)
print("String without duplicates :", result)


'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
2) Both  input  and  output are lists
'''

lst = eval(input("Enter list with duplicates : "))
unique_lst = list(set(lst))
print("List without duplicates :", unique_lst)


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]
2) Both  input  and  output are lists
'''

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
common = set(list1).intersection(set(list2))
result = list(common)
print("Common elements between the 2 lists :", result)


# How to access values of dictionary (Home work)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])   # How to print value 25 in dict 'a' 
print(a['Ename'])   # How to print 'Rama Rao' in dict 'a' 
print(a['Sal'])     # How to print value 1000.65 in dict 'a' 


# How to modify values of dictionary (Home work)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)        # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(id(a))    # prints memory address of dict 'a'
a['Sal'] = 2000        # How to modify 1000.65 to 2000 
a['Ename'] = 'Sita'    # How to modify 'Rama Rao' to 'Sita' 
a['Empno'] = 35        # How to modify 25 to 35 
print(a)        # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))    # same id as before


#  How to append key : value pairs to dictionary (Home work)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)            
a['Gender'] = 'M'   # How to append 'Gender' : 'M' to dictionary 'a' 
a['Married'] = True # How to append 'Married' : True to dictionary 'a' 
print(a)            # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}


# Find outputs (Home work)
a = {}
a[10] = 'Rama'   # How to append 10 : 'Rama' to dictionary 'a' 
a[20] = 'Sita'   # How to append 20 : 'Sita' to dictionary 'a' 
a[15] = 'Rajesh' # How to append 15 : 'Rajesh' to dictionary 'a' 
a[18] = 'Kiran'  # How to append 18 : 'Kiran' to dictionary 'a' 
print(a)         # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}


#  How to remove key : value pairs of dictionary (Home work)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)  
del a['Sal'] # How to remove 'Sal' : 1000.65 from dictionary 'a' 
print(a)     # {'Empno': 25, 'Ename': 'Rama Rao'}


#  in and not in operators (Home work)

a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())      # True
print(60 in a.keys())      # False
print(60 in a.values())    # True
print(30 in a.values())    # False
print(50 in a)             # True  (checks keys)
print(20 in a)             # False (checks keys only, not values)
print(70 not in a.keys())  # False
print(40 not in a.values())# False
print(25 not in a)         # True


#  What are the outputs if input is {10: 'A', 20: 'B', 15: 'C', 20: 'D'}

a = input('Enter dictionary : ')  # Suppose input: {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
print(a)           # prints string "{10: 'A', 20: 'B', 15: 'C', 20: 'D'}"
print(type(a))     # <class 'str'>
b = eval(a)        # converts string into dictionary
print(b)           # {10: 'A', 20: 'D', 15: 'C'}  (20:'B' replaced by 20:'D')
print(type(b))     # <class 'dict'>


#  Find outputs (Home work)

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}               # shallow copy
print(b)                # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b)           # False (different objects)
print(a == b)           # True (same content)
c = a
print(a is c)           # True (same reference)
print(a == c)           # True (same content)


# Find outputs (Home work)

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)        # {10, 14, 15, 18, 19, 20, 25} (set of keys only)
print(type(d))  # <class 'set'>
e = {**a, **b, **c}
print(e)        # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))  # <class 'dict'>


#  Find outputs (Home work)

a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
# print(a + b)   # ERROR dicts cannot be added with '+'
c = {**a, **b}
print(c)        # {10: 60, 30: 50}  
d = a | b
print(d)        # {10: 60, 30: 50} 


'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
Hint:  Append  each  emp  name  and  salary  to  dictionary 'a'
'''

n = int(input("How many Employees ? : "))
a = {}
for i in range(n):
    ename = input("Enter Emp Name : ")              
    sal = float(input("Enter Salary : "))           
    a[ename] = sal                                  
print(a)


''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary
Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}
Hint :  Use  split()  method twice
'''

s = input("Enter string : ")
items = s.split(",")
d = {}
for item in items:
    key, value = item.split("=")  
    try:
        value = eval(value)
    except:
        pass 
    d[key] = value
print(d)


# len() function demo program (Home work)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))   # How many key:value pairs are present in dictionary 'a' 
b = {}
print(len(b))   # # How many key:value pairs are present in empty dictionary 'b'


# sum() function demo program (Home work)

# (a) sum() function demo program
a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))      # 90
print(sum(a.values()))    # 120
print(sum(a))             # 90
# print(sum(a.items()))   # Error


# (b) max() and min() functions demo program

a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))      # 40
print(min(a.keys()))      # 7
print(max(a.values()))    # 50
print(min(a.values()))    # 5
print(max(a.items()))     # (40, 5)
print(min(a.items()))     # (7, 28)
print(max(a))             # 40
print(min(a))             # 7


# (c) dict() function demo program

a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
b = dict(a)
print(b)                # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = (['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray'])
d = dict(c)
print(d)                # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(dict(e))          # Error each inner sequence must have exactly 2 elements
f = [[10], [20], [30]]
print(dict(f))          # Error inner sequence must have exactly 2 elements
print(dict([10, 20]))   # Error not a nested sequence
g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))          # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))          # Error keys cannot be lists
i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))          # {(10, 20): 30, (40, 50): 60, (70, 80): 90}


# (d) sorted() function demo program

a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b)   # [5, 10, 15, 18, 20]
c = sorted(a.values())
print(c)   # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a.items())
print(d)   # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f = sorted(a, reverse=True)
print(f)   # [20, 18, 15, 10, 5]
print(a)   # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}


'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}
2) Both  input  and  output  are  dictionaries
3) Hint:  Use  sorted() function
'''

a = eval(input("Enter dictionary : "))
b = dict(sorted(a.items()))
print(b)  


# clear() method demo program (Home work)

a = {10: 20, 30: 40, 50: 60}
print(a)          # {10: 20, 30: 40, 50: 60}
a.clear()
print(a)          # {}
del a
print(a)          # Error name 'a' is not defined


# copy() method demo program (Home work)

a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
b = a.copy()
print(b)          # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a is b)     # False
print(a == b)     # True


# keys() method demo program

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.keys()
print(b)          # dict_keys([10, 20, 15, 18])
print(type(b))    # <class 'dict_keys'>
for x in b:
    print(x)      # 10  20  15  18


# values() method demo program

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.values()
print(b)          # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))    # <class 'dict_values'>
for x in b:
    print(x)      # Hyd  Sec  Cyb  Pune


# items() method demo program

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.items()
print(b)          # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))    # <class 'dict_items'>
for x in b:
    print(x)      # (10, 'Hyd')  (20, 'Sec')  (15, 'Cyb')  (18, 'Pune')
for x, y in b:
    print(x, y, sep=' ... ')
    
    '''
    10 ... Hyd
    20 ... Sec
    15 ... Cyb
    18 ... Pune
    '''


# Find outputs (Home work)

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
for x, y in a.items():
    print(x, y, sep=' ... ')
    '''
     10 ... Hyd
     20 ... Sec
     15 ... Cyb
     18 ... Pune
    '''
for x, y in a.keys():     # Error each key is single value, not tuple
for x, y in a.values():   # Error each value is single string, not tuple
for x, y in a:            # Error loop gives keys only, not pairs


# Find outputs (Home work)

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
x, y, z = a.keys()
print(x)    # 10
print(y)    # 20
print(z)    # 15
print()
x, y, z = a.values()
print(x)    # Rama
print(y)    # Sita
print(z)    # Rajesh
print()
x, y, z = a.items()
print(x)    # (10, 'Rama')
print(y)    # (20, 'Sita')
print(z)    # (15, 'Rajesh')
print()
(rno1, sname1), (rno2, sname2), (rno3, sname3) = a.items()
print(rno1, sname1)   # 10 Rama
print(rno2, sname2)   # 20 Sita
print(rno3, sname3)   # 15 Rajesh


# Tricky program (Homework)
# Write a program to determine frequency of each alphabet in the string 
# in alphabetical order (ignoring the case)

s = input("Enter mixed case string : ")   # Example: RamA raO
s = s.upper()
a = {}
for ch in sorted(s):
    if ch.isalpha():               
        a[ch] = a.get(ch, 0) + 1
print(a)




