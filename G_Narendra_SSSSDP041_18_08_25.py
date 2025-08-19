# len() function demo program
a = [25, 10.8, 'Hyd', True]
print(len(a))     # 4
b = []
print(len(b))     # 0
c = [[10, 20], 30, 40]
print(len(c))     # 3   (inner list counts as 1 element)
len(list) # returns number of elements in the list


# sum() function demo program
a = [25, 10.8, True]
print(sum(a))     # 36.8   (25 + 10.8 + 1)
b = [3 + 4j, 5 + 6j]
print(sum(b))     # (8+10j)
c = [25, 10.8, True, 3 + 4j, False]
print(sum(c))     # (39.8+4j)
d = [10, 20, 15, 18]
print(sum(d))     # 63
e = [25, 10.8, 'Hyd', True]
print(sum(e))   # TypeError (cannot add str with numbers)
sum(list)# returns sum of numeric elements


# Find outputs
a = [[10, 20, 15, 18]]
# print(sum(a))   # TypeError: unsupported operand
# To get sum of inner list:
print(sum(a[0]))  # 63
print(sum(a))  # 63 (same another way)


# max() and min() functions demo program
a = [10, 20, 15, 18, 30, 5, 12]
print(max(a))     # 30
print(min(a))     # 5
b = ['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Vamsi', 'Manohar']
print(max(b))     # Vamsi   (lexicographic comparison)
print(min(b))     # Amar
c = [25, 10.8, 3 + 4j, True]
print(max(c))   # TypeError (cannot compare complex)
d = [25, '35']
print(max(d))   # TypeError (int and str cannot be compared)
print(max([]))  # ValueError (empty list not allowed)
print(min([]))  # ValueError (empty list not allowed)


# list() function demo program
a = (10, 20, 15, 18)
b = list(a)
print(b)          # [10, 20, 15, 18]
print(type(b))    # <class 'list'>
print(a is b)     # False
print(a == b)     # True


# Find outputs
a = range(4, 10, 2)
b = list(a)
print(b)          # [4, 6, 8]
print(type(b))    # <class 'list'>
a = list('Vamsi')
print(a)          # ['V', 'a', 'm', 's', 'i']
a = list()
print(a)          # []
print(list(25)) # TypeError
print(list(10.8)) # TypeError
print(list(True)) # TypeError
print(list(None)) # TypeError


a = ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(list(a))    # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = {(10, 20), (30, 40, 50), (60, 70, 80, 90)}
print(list(b))    # order could vary because set is unordered
c = ([10, 20], (30, 40), {50, 60})
print(list(c))    # [[10, 20], (30, 40), {50, 60}]


# sorted() function
a = [10, 20, 15, 5, 12]
b = sorted(a)
print(b)          # [5, 10, 12, 15, 20]
print(type(b))    # <class 'list'>
c = sorted(a, reverse=True)
print(c)          # [20, 15, 12, 10, 5]
print(a)          # [10, 20, 15, 5, 12] (unchanged)


# Find outputs
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
b = sorted(a)
print(b)          # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a, reverse=True)
print(c)          # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)          # original list not changed


# all() function demo program
a = [12 > 10, 5 < 20, 30 == 30]
print(all(a))     # True
b = [9 >= 6, 12 <= 9, 6 == 6]
print(all(b))     # False (because 12 <= 9 is False)
c = [25, 10.8, '', True, 3+4j, 'Hyd']
print(all(c))     # False ('' is False)
d = [10, 0, 20]
print(all(d))     # False (0 is False)
e = []
print(all(e))     # True  (empty list → True)


# any() function demo program
a = [12 > 18, 5 < 20, 35 == 30]
print(any(a))     # True (5 < 20 is True)
b = [12 > 18, 25 < 20, 35 == 30]
print(any(b))     # False (all False)
c = [0, 0.0, '', 25, 0+0j, False]
print(any(c))     # True (25 is True)
d = [0, 0.0, '', 0+0j, False]
print(any(d))     # False
e = []
print(any(e))     # False


# del operator demo program
a = [10, 20, 15, 18]
print(a)          # [10, 20, 15, 18]
del a[2]
print(a)          # [10, 20, 18]
del a  # IndexError after previous deletion
del a     # deletes list itself
print(a)  # NameError: a is not defined


# append() demo
list = [10, 20, 15, 18]
print(list)       # [10, 20, 15, 18]
list.append(19)
print(list)       # [10, 20, 15, 18, 19]


list = []
print(list)       # []
list.append(25)
list.append(10.8)
list.append('Hyd')
list.append(True)
print(list)       # [25, 10.8, 'Hyd', True]


list = []
for x in range(0, 50, 10):
    list.append(x)
print(list)       # [0, 10, 20, 30, 40]


a = [10, 20, 30]
a.append('Hyd')
print(a)          # [10, 20, 30, 'Hyd']
print(len(a))     # 4
# How to print 4th element of 'a'
print(a[3])       # Hyd
print(a)    # H
print(a)    # y
print(a)    # d


# remove() method demo program
try:
    list = [10, 20, 15, 18, 15, 12, 15, 19]
    list.remove(15)
    print(list)   # [10, 20, 18, 15, 12, 15, 19] (first 15 removed)
    list.remove(25)
except:
    print('25 is not in the list') # 25 is not in the list


# delete all occurrences
a = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
x = 15
result = [i for i in a if i != x]
print(result)     # [10, 20, 18, 19, 17, 20, 14]


# clear() method demo
list = [10, 20, 15, 18]
print(list)       # [10, 20, 15, 18]
list.clear()
print(list)       # []


# reverse() method demo
a = [10, 20, 15, 18]
print(a)          # [10, 20, 15, 18]
a.reverse()
print(a)          # [18, 15, 20, 10]


# sort() method demo
list = [10, 20, 15, 18, 5]
print(list)       # [10, 20, 15, 18, 5]
list.sort()
print(list)       # [5, 10, 15, 18, 20]
list.sort(reverse=True)
print(list)       # [20, 18, 15, 10, 5]


a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
print(a)          # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a.sort()
print(a)          # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a.sort(reverse=True)
print(a)          # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
a = [25, 10.8, 'Hyd', True]
a.sort()        # TypeError (different datatypes can't be compared)


# count() method
a = [10, 20, 15, 18, 15, 12, 14, 15, 19]
print(a.count(15))   # 3
print(a.count(25))   # 0
print(len(a))        # 9


# tricky remove duplicates completely
a = [10, 20, 15, 10, 14, 10, 18, 20, 19]
result = []
for i in a:
    if a.count(i) == 1:
        result.append(i)
print(result)     # [15, 14, 18, 19]


# check identical elements
a = [25, 25, 25, 25]
if a.count(a[0]) == len(a):
    print("All the elements are identical")  # All the elements are identical
else:
    print("All the elements are not identical")
print(len(a))      # 4
print(a.count(a))  # 4

a = [10, 10, 20, 10]
if a.count(a) == len(a):
    print("All the elements are identical")
else:
    print("All the elements are not identical")  # All the elements are not identical
print(len(a))      # 4
print(a.count(a))  # 3


# index() method demo
a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
#     0    1    2   3    4    5    6    7    8    9    10
try:
    i = a.index(15)
    while True:
        print(i)   # 2, 5, 8
        i = a.index(15, i + 1)
except:
    print(f'15 is found {a.count(15)} times ') 
    # 15 is found 3 times
