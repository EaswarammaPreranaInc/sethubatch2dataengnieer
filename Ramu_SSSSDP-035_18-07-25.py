# Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # prints the list [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # prints the elements of list 25 10.8 Hyd True (3 + 4j) None Hyd 25
print(type(a)) # <class 'list'>
print(id(a)) # print the address of list
print(len(a)) # list length 8
a[2] = 'Sec'
print(a) # modified list [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # print list from range 2 to 5 in steps of 1 i.e. ['Sec' , True , 3 + 4j]


# append() and remove() methods (Home work)
a = [ ]
print(a) # print empty list []
a . append(25) # appends 25 in list a [25]
a . append(10.8) # appends 10.8 in list a [25, 10.5]
a . append('Hyd') # appends 'Hyd' in list a [25, 10.5, 'Hyd']
a . append(True) # appends True in list a [25, 10.5, 'Hyd', True]
print(a) # print list of a [25, 10.5, 'Hyd', True]
a . remove('Hyd') # removes 'Hyd' from a
print(a) #prints [25, 10.5, True]
a . remove(25) #removes 25 from list a
print(a) #prints [10.5, True]


# Find outputs (Home work)
a = [25 , 10.8 , 'Hyd']
print(a) #prints list a i.e. [25 , 10.8 , 'Hyd']
print(id(a)) # prints the address of list a
print(a * 3) # prints [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) # prints [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) # prints [25 , 10.8 , 'Hyd']
print(a * 0) # prints empty list a []
print(a * -1) # prints empty list a []
#print(a * 4.0) # error
a = a * 3
print(a) # prints [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) #prints the id of list a
a = [25]
#print(a * a) #error


# list() function demo program
a = list('Hyd')
print(a) #converts a into list i.e. ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a)) # prints length 3
b = (10 , 20 , 15 , 18)
print(list(b)) #converts tuple b into list i.e. [10, 20, 15, 18]
print(list(range(5))) #prints list i.e. [0, 1, 2, 3, 4]
#print(list(25)) # error


# Find outputs
a = [ ]
print(type(a)) #<class 'list'>
print(a) # prints empty list
print(len(a)) # length is 0
b = list()
print(b) # prints empty list
print(len(b)) #length is 0


# Slice demo program (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
# -8 -7 -6 -5 -4 -3 -2 -1
print(list[2 : 7]) # prints list [3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ]) #prints the full list as it is
print(list[:]) # list[0 : 8 : 1] ---> List from indexes 0 to 7 in steps of 1 i.e. [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #prints reverse format [10.8, None, True, 'Hyd', (3+4j)]
print(list[ : : 2]) # list [25, (3+4j), True, 10.8]
print(list[1 : : 2]) #list [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) # list[-1 : -9 : -2] ---> List from indexes -1 to -8 in steps of -2 i.e. ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # list[10.8, True, (3+4j), 25]
print(list[1 : 4]) #list[10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1]) #list [True , None , 10.8]
print(list[3 : -3]) #list ['Hyd', True]
print(list[2 : -5]) #list [3 + 4j]
print(list[-1:-5]) #list []


# Find outputs (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x , y = list[3 : 5]
print('x : ' , x) #prints x : Hyd
print('y : ' , y) #prints y : True
for x in list[2:7]:
   print(x) #prints 3+4j Hyd True None 10.8


# Find outputs (Home work)
# 0 1 2 3 4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #prints list a [10 , 20 , 30 , 40 , 50] print address of list a
a[1 : 4] = [60 , 70] 
print(a , id(a)) #prints list a [10 , 60 , 70 , 40 , 50] print address of list a
a[2: 4] = [100 , 200 , 300]
print(a , id(a)) #prints list a [10 , 60 , 100 , 200 , 300] print address of list a]


# Find outputs (Home work)
a = [25]
#print(a[1]) #error index exceed
#print(a[1:]) #error


# Find outputs (Home work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) #<class 'int'>
print(type(b)) #<class 'tuple'>
print(type(c)) #<class 'int'>
print(type(d)) #<class 'tuple'>
print(a * 4) # prints 25 * 4 i.e. 100
print(b * 4) # prints (25, 25, 25, 25)
print(c * 4) # prints 25 * 4 i.e. 100
print(d * 4) # prints (25, 25, 25, 25)
a = ()
print(type(a))
#<class 'tuple'>
print(a) # ()
print(len(a)) # 0
b = tuple()
print(b) # ()
print(len(b)) #0
print(a) # (10, 20, 30)
print(id(a)) # some unique id 140362712345344
a = a * 2
print(a) # (10, 20, 30, 10, 20, 30)
print(id(a)) # a different unique id 140362712346432
print(a) # {10.8, 'Hyd', 25, True, None, (3+4j)} (order may vary)
print(type(a)) # <class 'set'>
print(len(a)) # 6
#print(a[2]) # TypeError: 'set' object is not subscriptable
#print(a[1 : 4]) # TypeError: 'set' object is not subscriptable
#a[2] = 'Sec' # TypeError: 'set' object does not support item assignment
#print(a * 2) # TypeError: unsupported operand type(s) for *: 'set' and 'int'
#print(a * a) # TypeError: unsupported operand type(s) for *: 'set' and 'set'
print(a) # {0, 1, 'Hyd', ''}
#False is equivalent to 0 and True is equivalent to 1 in Python, and 0.0 is equivalent to 0 and 1.0 is equivalent to 1, so duplicates are removed.
print(len(a)) # 4
print(type(a)) # <class 'set'>
a = set('Rama rAo')
print(a) # {'R', 'a', 'm', 'a ', 'r', 'A', 'o'}
print(len(a)) # 7
print(set([10, 20, 15, 20])) # {10, 15,20}
print(set((25, 10.8, 'Hyd', 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10, 20, 3))) # {10, 13, 16, 19}
#print(set(25)) # TypeError: 'int' object is not iterable
#print(set([25, 10.8, [], 'Hyd'])) # TypeError: unhashable type: 'list'


# Find outputs (Home work)
a = [ ]
b = ( )
c = {}
d = set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()
a = set() # Creates an empty set
a.add(25) # 25 added
a.add(10.8) # 10.8 added
a.add('Hyd') # 'Hyd' added
a.add(True) # True added
a.add(None) # None added
a.add('Hyd') # No change (duplicate)
a.add(1) # No change (1 is same as True)
print(a) # {None, True, 10.8, 25, 'Hyd'}
print(len(a)) # 5
a.remove(25) # 25 removed
print(a) # {None, True, 10.8, 'Hyd'}
#a.append(100) # Error: 'set' object has no attribute 'append'
#a.add(set()) # Error: unhashable type: 'set'
a.add(()) # () added
#a.add([]) # Error: unhashable type: 'list'
print(a) # {None, True, 10.8, 'Hyd', ()}
#a.add({}) # Error: unhashable type: 'dict'
a = {25, True, 'Hyd', 10.8}
print('set with print function')
print(a) # Directly prints the whole set
print('Iterate through set with for loop')
for i in a:
 print(i) # Prints each element one by one using a loop
