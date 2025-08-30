#  len()  function demo   program  (Home  work)
a = [25, 10.8, 'Hyd', True]
print(len(a))     # 4

b = []
print(len(b))     # 0

c = [[10, 20], 30, 40]
print(len(c))     # 3   


'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''
# sum()  function  demo  program  (Home  work)
a = [25, 10.8, True]
print(sum(a))          # 36.8   (25 + 10.8 + 1)

b = [3+4j, 5+6j]
print(sum(b))          # (8+10j)

c = [25, 10.8, True, 3+4j, False]
print(sum(c))          # (39.8+4j)

d = [10, 20, 15, 18]
print(sum(d))          # 63

#e = [25, 10.8, 'Hyd', True]
#print(sum(e))          # ERROR 



'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''
#  Find  outputs
#a = [[10 , 20 , 15 , 18]]
#print(sum(a))
#print(How  to  determine  sum  of  inner  list  elements)
#print(How  to  determine  sum  of  inner  list  elements  in  another  way)


# max()  and  min()  functions  demo  program  (Home  work)
a = [10, 20, 15, 18, 30, 5, 12]
print(max(a))    # 30
print(min(a))    # 5

b = ['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Vamsi', 'Manohar']
print(max(b))    # Vamsi  
print(min(b))    # Amar    

#c = [25, 10.8, 3+4j, True]
#print(max(c))    #  ERROR (complex numbers can’t be compared with real numbers)

#d = [25, '35']
#print(max(d))    # ERROR (int and str can’t be compared)

#print(max([]))   #  ERROR (empty list)
#print(min([]))   #  ERROR (empty list)

'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

# list()  function  demo  program
a = (10, 20, 15, 18)
b = list(a)
print(b)          # [10, 20, 15, 18]
print(type(b))    # <class 'list'>
print(a is b)     # False (different objects)
print(a == b)     # True  (values same)


#  Find  outputs (Home  work)
a = range(4, 10, 2)
b = list(a)
print(b)          # [4, 6, 8]
print(type(b))    # <class 'list'>

a = list('Vamsi')
print(a)          # ['V', 'a', 'm', 's', 'i']

a = list()
print(a)          # []

#print(list(25))       #  ERROR 
#print(list(10.8))     #  ERROR 
#print(list(True))     #  ERROR 
#print(list(None))     #  ERROR 



'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  ---> Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''
# Find  outputs (Home  work)
a = [10, 20, 15, 5, 12]
b = sorted(a)
print(b)           # [5, 10, 12, 15, 20]
print(type(b))     # <class 'list'>
c = sorted(a, reverse=True)
print(c)           # [20, 15, 12, 10, 5]
print(a)           # original list unchanged


# sorted()  function   demo  program
a = [10, 20, 15, 5, 12]
b = sorted(a)
print(b)           # [5, 10, 12, 15, 20]
print(type(b))     # <class 'list'>
c = sorted(a, reverse=True)
print(c)           # [20, 15, 12, 10, 5]
print(a)           # original list unchanged



# Find  outputs  (Home  work)
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
b = sorted(a)
print(b)           # Alphabetical
c = sorted(a, reverse=True)
print(c)           # Reverse alphabetical
print(a)           # Original list unchanged


# all()  function demo  program  (Home  work)
a = [12 > 10, 5 < 20, 30 == 30]   # [True, True, True]
print(all(a))    # True

b = [9 >= 6, 12 <= 9, 6 == 6]     # [True, False, True]
print(all(b))    # False

c = [25, 10.8, '', True, 3+4j, 'Hyd']
print(all(c))    # False (because '' is falsy)

d = [10, 0, 20]
print(all(d))    # False (0 is falsy)

e = []
print(all(e))    # True  (all() of empty list is True by definition)



# any() function demo program (Home work)
a = [12 > 18, 5 < 20, 35 == 30]
print(any(a))   # True (because 5 < 20 is True)
b = [12 > 18, 25 < 20, 35 == 30]
print(any(b))   # False (all are False)
c = [0, 0.0, '', 25, 0 + 0j, False]
print(any(c))   # True (25 is truthy)
d = [0, 0.0, '', 0 + 0j, False]
print(any(d))   # False (all falsy)
e = []
print(any(e))   # False (empty list → False)

# del operator demo program (Home work)
a = [10, 20, 15, 18]
print(a)
del a[2]
print(a)
del a[2]        # after deletion, new index
print(a)
del a           # deletes whole list
# print(a)      # ERROR: a is not defined


# append() method demo program (Home work)
list1 = [10, 20, 15, 18]
print(list1)
list1.append(19)
print(list1)

# Find outputs (Home work)
list2 = []
print(list2)
list2.append(25)
list2.append(10.8)
list2.append('Hyd')
list2.append(True)
print(list2)    # [25, 10.8, 'Hyd', True]

# Find outputs (Home work)
list3 = []
for x in range(0, 50, 10):
    list3.append(x)
print(list3)    # [0, 10, 20, 30, 40]

# Find outputs (Home work)
a = [10, 20, 30]
a.append('Hyd')
print(a)        # [10, 20, 30, 'Hyd']
print(len(a))   # 4
print(a[3])     # 4th element → 'Hyd'
print(a[3][0])  # 'H'
print(a[3][1])  # 'y'
print(a[3][2])  # 'd'

# remove() method demo program (Home work)
try:
    list4 = [10, 20, 15, 18, 15, 12, 15, 19]
    list4.remove(15)   # removes first 15
    print(list4)
    list4.remove(25)   # element not found
except:
    print('25 is not in the list')


# Program to remove all occurrences of an element
lst = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
ele = 15
res = [x for x in lst if x != ele]
print("List without 15's :", res)  # [10, 20, 18, 19, 17, 20, 14]


# clear() method demo program (Home work)
list5 = [10, 20, 15, 18]
print(list5)
list5.clear()
print(list5)   # []

'''
clear() method
------------------
1) Removes all the elements → empty list
2) remove() and pop() → remove only one element
'''

# reverse() method demo program (Home work)
a = [10, 20, 15, 18]
print(a)
a.reverse()
print(a)   # [18, 15, 20, 10]

'''
reverse() method
---------------------
1) Reverses all elements of list
2) Changes happen in same list (mutable)
'''

# sort() method demo program (Home work)
list6 = [10, 20, 15, 18, 5]
print(list6)
list6.sort()
print(list6)   # [5, 10, 15, 18, 20]
list6.sort(reverse=True)
print(list6)   # [20, 18, 15, 10, 5]

# Find outputs (Home work)
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
print(a)
a.sort()
print(a)    # Alphabetical order
a.sort(reverse=True)
print(a)    # Reverse alphabetical

# Identify error (Home work)
a = [25, 10.8, 'Hyd', True]
# a.sort()   # ERROR: Cannot compare int, float, str, bool


# count() method demo program (Home work)
a = [10, 20, 15, 18, 15, 12, 14, 15, 19]
print(a.count(15))   # 3
print(a.count(25))   # 0
print(len(a))        # 9

'''
count(x) → returns number of times 'x' occurs in the list
'''


# TRICKY PROGRAM:
# Remove all elements that appear more than once (keep only unique elements)
lst = [10, 20, 15, 10, 14, 10, 18, 20, 19]
res = []
for x in lst:
    if lst.count(x) == 1:
        res.append(x)
print(res)   # [15, 14, 18, 19]

'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? --->  3

3) Hint: Use  len()  and  count()
'''
a = [25, 25, 25, 25]
if len(a) == a.count(a[0]):
    print("All the elements are identical") 
else:
    print("All the elements are not identical") 
     
