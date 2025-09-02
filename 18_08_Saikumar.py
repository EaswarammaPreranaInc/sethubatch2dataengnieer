# len() function demo program

a = [25, 10.8, 'Hyd', True]
print(len(a))     # list 'a' has 4 elements
b = []
print(len(b))     # list 'b' is empty
c = [[10, 20], 30, 40]
print(len(c))     # list 'c' has 3 elements


# sum() function demo program

a = [25, 10.8, True]
print(sum(a))      # 25 + 10.8 + 1(True) = 36.8
b = [3 + 4j, 5 + 6j]
print(sum(b))      # (3+4j) + (5+6j) = (8+10j)
c = [25, 10.8, True, 3 + 4j, False]
print(sum(c))      # 25 + 10.8 + 1(True) + (3+4j) + 0(False) = (39.8+4j)
d = [10, 20, 15, 18]
print(sum(d))      # 10 + 20 + 15 + 18 = 63
e = [25, 10.8, 'Hyd', True]
print(sum(e))      # Error: sum() does not work with strings


#  Find  outputs

a = [[10 , 20 , 15 , 18]]
print(sum(a))
print("How  to  determine  sum  of  inner  list  elements")
print(sum(a[0])) 
print("How  to  determine  sum  of  inner  list  elements  in another way")
total = 0
for x in a[0]:
    total += x
print(total) 


# max() and min() functions demo program

a = [10, 20, 15, 18, 30, 5, 12]
print(max(a))   # 30 (largest number)
print(min(a))   # 5  (smallest number)
b = ['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Vamsi', 'Manohar']
print(max(b))   # 'Vamsi' (max based on alphabetical order)
print(min(b))   # 'Amar'  (min based on alphabetical order)
c = [25, 10.8, 3 + 4j, True]
print(max(c))   # Error: complex numbers cannot be compared with int/float
d = [25, '35']
print(max(d))   # Error: int and str cannot be compared
print(max([]))  # Error: empty sequence has no maximum
print(min([]))  # Error: empty sequence has no minimum


# list() function demo program

a = (10, 20, 15, 18)      # a is a tuple
b = list(a)               # converting tuple 'a' into a list
print(b)                  # [10, 20, 15, 18]
print(type(b))            # <class 'list'>
print(a is b)             # False, 'a' and 'b' are different objects
print(a == b)             # True, references are equal


# Find outputs (Home work)

a = range(4, 10, 2)      # range(start=4, stop=10, step=2)
b = list(a)              # convert range to list
print(b)                 # [4, 6, 8]
print(type(b))           # <class 'list'>
a = list('Vamsi')        # string → list of characters
print(a)                 # ['V', 'a', 'm', 's', 'i']
a = list()               # empty list
print(a)                 # []
print(list(25))          # ERROR → int is not iterable
print(list(10.8))        # ERROR → float is not iterable
print(list(True))        # ERROR → bool is not iterable
print(list(None))        # ERROR → NoneType is not iterable


# Find outputs (Home work)

a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))   # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))   # [(30, 40, 50), (10, 20), (60, 70, 80, 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))   # Output: [[10, 20], (30, 40), {50, 60}]


# sorted() function demo program

a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)  
print(b)        # [5, 10, 12, 15, 20] 
print(type(b))  # <class 'list'>  
c = sorted(a , reverse = True)  
print(c)        # [20, 15, 12, 10, 5] 
print(a)        # [10, 20, 15, 5, 12]  


# Find  outputs  (Home  work)

a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
b = sorted(a)
print(b)        # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']  
c = sorted(a , reverse = True)
print(c)        # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']  
print(a)        # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']  


# all()  function demo  program  (Home  work)

a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))    # True 
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))    # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))    # False 
d = [10 , 0 , 20]
print(all(d))    # False 
e = []
print(all(e))    # True 


# any() function demo program (Home work)

a  = [12 > 18 , 5 < 20 , 35 == 30]        # [False, True, False]
print(any(a))                             # True, at least one True (5 < 20)
b = [12 > 18 , 25 < 20 , 35 == 30]        # [False, False, False]
print(any(b))                             # False, all are False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]  # contains 25 (truthy)
print(any(c))                             # True, 25 makes it True
d = [0 , 0.0 , '' , 0 + 0j , False]       # all are falsy values
print(any(d))                             # False, no truthy element
e = []                                    # empty list
print(any(e))                             # False


# del operator demo program (Home work)

a = [10 , 20 , 15 , 18]
print(a)        # [10, 20, 15, 18]
del a[2]        # deletes element at index 2 (15)
print(a)        # [10, 20, 18]
del a[2]        # deletes element at index 2 (18)
print(a)        # [10, 20]
del a           # deletes the whole list object
print(a)        # Error because 'a' not exists


# append() method demo program (Home work)

list = [10, 20, 15, 18]
print(list)             # [10, 20, 15, 18]
list.append(19)         # adds 19 at the end of the list
print(list)             # [10, 20, 15, 18, 19]


# Find outputs (Home work)

list = []
print(list)                  # []  (empty list)
list.append(25)              # adds 25 to list
list.append(10.8)            # adds 10.8 to list
list.append('Hyd')           # adds string "Hyd"
list.append(True)            # adds boolean True
print(list)                  # [25, 10.8, 'Hyd', True]


# Find outputs (Home work)

list = []                                # start with empty list
for x in range(0, 50, 10):               # values will be 0, 10, 20, 30, 40
    list.append(x)                       # each value is added to the list
print(list)                              # [0, 10, 20, 30, 40]


# Find outputs (Home work)

a = [10, 20, 30]        # list with 3 elements
a.append('Hyd')         # append string 'Hyd' to the list
print(a)                # [10, 20, 30, 'Hyd']
print(len(a))           # 4  (list now has 4 elements)
# How to print 4th element of list 'a':
print(a[3])             # Hyd
# How to print characters 'H', 'y', 'd' from 'Hyd':
print(a[3][0])          # H
print(a[3][1])          # y
print(a[3][2])          # d


# remove() method demo program (Home work)

try:
    list = [10, 20, 15, 18, 15, 12, 15, 19]   # initial list
    list.remove(15)                           # removes the first occurrence of 15
    print(list)                               # [10, 20, 18, 15, 12, 15, 19]
    list.remove(25)                           # tries to remove 25, but it's not in the list
except:
    print('25 is not in the list')            # handled by exception


''' 
Write a program to delete 'all' occurences of 'x' from the list 
Let 1st input be [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14] and 2nd input be 15 
What is the output ? ---> [10 , 20 , 18 , 19 , 17 , 20 , 14] 
'''

a = eval(input("Enter List : "))
x = eval(input("Enter element to be deleted : "))
while x in a:
    a.remove(x)
print(a)


# clear() method demo program (Home work)

list = [10 , 20 , 15 , 18]   # Create a list with 4 elements
print(list)                  # Print original list [10, 20, 15, 18]
list.clear()                 # Removes all elements from the list
print(list)                  # Prints an empty list []


# reverse() method demo program (Home work)

a = [10 , 20 , 15 , 18]   
print(a)                  # [10, 20, 15, 18]
a.reverse()               # Reverses the list in place
print(a)                  # [18, 15, 20, 10]


# sort() method demo program (Home work)

list = [10 , 20 , 15 , 18 , 5] 
print(list)                      # [10, 20, 15, 18, 5]
list.sort()                      # Sorts in ascending order
print(list)                      # [5, 10, 15, 18, 20]
list.sort(reverse=True)          # Sorts in descending order
print(list)                      # [20, 18, 15, 10, 5]


# Find outputs (Home work)

a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)               # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a.sort()               # Sorts alphabetically (A → Z)
print(a)               # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a.sort(reverse=True)   # Sorts in reverse alphabetical order (Z → A)
print(a)               # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']


# Identify error (Home work)

a = [25 , 10.8 , 'Hyd' , True]
a.sort()   #  ERROR due to different elements


# count() method demo program (Home work)

a = [10, 20, 15, 18, 15, 12, 14, 15, 19]
print(a.count(15))   # 3  (because 15 appears 3 times)
print(a.count(25))   # 0  (25 is not in the list)
print(len(a))        # 9  (total number of elements in the list)


# Program to remove all duplicate elements of the list (Not even a single occurrence)

a = [10, 20, 15, 10, 14, 10, 18, 20, 19]
b = []   
for x in a:
    if a.count(x) == 1:  
        b.append(x)
print("Original List:", a)
print("List without duplicates:", b)


# Program to check if all list elements are identical

a = eval(input("Enter any list : "))
if a.count(a[0]) == len(a):
    print("All the list elements are identical")
else:
    print("List elements are not identical")


# index() method demo program (Home Work)

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
    i = a.index(15)                             # i = 2
    while True:
        print(i)                                # 2 , 5 , 8
        i = a.index(15 , i + 1)                 # next occurrence of 15
except:
    print(f"15 is found {a.count(15)} times")   # 15 is found 3 times