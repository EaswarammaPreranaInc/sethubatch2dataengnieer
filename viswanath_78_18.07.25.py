a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Hyd', 25]
print(a)  # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)  # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))  # <class 'list'>
print(id(a))  # (varies) – memory address of the list
print(len(a))  # 8
a[2] = 'Sec'
print(a)  # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])  # ['Sec', True, (3+4j)]

a = [ ]
print(a)  # []
a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)
print(a)  # [25, 10.8, 'Hyd', True]
a.remove('Hyd')
print(a)  # [25, 10.8, True]
a.remove('25')  # Error: '25' (a string) not found in list
print(a)  # [25, 10.8, True]

a = [25, 10.8, 'Hyd']
print(a)  # [25, 10.8, 'Hyd']
print(id(a))  # (some memory address)
print(a * 3)  # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)  # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)  # [25, 10.8, 'Hyd']
print(a * 0)  # []
print(a * -1)  # []
print(a * 4.0)  # Error: can't multiply sequence by non-int of type 'float'
a = a * 3
print(a)  # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))  # New memory address 
a = [25]
print(a * a)  # Error: can't multiply sequence by non-int of type 'list'

a = list('Hyd')
print(a)  # ['H', 'y', 'd']
print(type(a))  # <class 'list'>
print(len(a))  # 3
b = (10, 20, 15, 18)
print(list(b))  # [10, 20, 15, 18]
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(25))  # Error: 'int' object is not iterable


a = [ ]
print(type(a))  # <class 'list'>
print(a)  # [ ]
print(len(a))  # 0
b = list()
print(b)  # [ ]
print(len(b))  # 0

#        0       1         2          3         4         5         6         7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#        -8     -7       -6         -5       -4        -3        -2        -1
print(list[2 : 7])        # list[2:7:1], [3+4j, 'Hyd', True, None, 10.8]
print(list[::])           # list[0:8:1], [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])            # list[0:8], [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd']
print(list[::-1])         # list[-1:-9:-1], ['Hyd', 10.8, None, True, 'Hyd', 3+4j, 10.8, 25]
print(list[::2])          # list[0:8:2], [25, 3+4j, True, 10.8]
print(list[1::2])         # list[1:8:2], [10.8, 'Hyd', None, 'Hyd']
print(list[::-2])         # list[-1:-9:-2], ['Hyd', None, 'Hyd', 10.8]
print(list[-2::-2])       # list[-2:-9:-2], [10.8, True, 3+4j, 25]
print(list[1:4])          # list[1:4:1], [10.8, 3+4j, 'Hyd']
print(list[-4:-1])        # list[-4:-1:1], [True, None, 10.8]
print(list[3:-3])         # list[3:-3:1] ['Hyd', True]
print(list[2:-5])         # [3+4j]
print(list[-1:-5])        # list[-1:-5:1], [ ]  empty string

#         0       1       2         3         4         5         6         7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x, y = list[3:5]
print('x : ', x)  # x :  Hyd
print('y : ', y)  # y :  True
for x in list[2:7]:
print(x)
# (3+4j)
# Hyd
# True
# None
# 10.8

#     0     1     2    3     4
a = [10, 20, 30, 40, 50]
print(a, id(a))  # [10, 20, 30, 40, 50] <original_id>
a[1:4] = [60, 70] # 20,40 gets replaced with 60,70
print(a, id(a))  #  [10, 60, 70, 50] <same_id>
a[2:4] = [100, 200, 300] # 20,40 gets replaced with 60,70
print(a, id(a))  # [10, 60, 100, 200, 300] <same_id>

a = [25]
print(a[1])        # Error: Index 1 is out of range 
print(a[1:])        # []  empty list 


a = (25)       #just an integer 
b = 25,        # Trailing comma makes it a tuple
c = 25         # Just an integer
d = (25,)      # Tuple with one element 
print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'int'>
print(type(d))  # <class 'tuple'>
print(a * 4)    # 100      # 25 * 4 = 100 (int multiplication)
print(b * 4)    # (25, 25, 25, 25)  # tuple repetition
print(c * 4)    # 100      # 25 * 4 = 100 (int multiplication)
print(d * 4)    # (25, 25, 25, 25)  # tuple repetition

a = tuple('Hyd')
print(a)             # ('H', 'y', 'd')
print(type(a))       # <class 'tuple'>
print(len(a))        # 3
b = [10, 20, 15, 18]
print(tuple(b))      # (10, 20, 15, 18)
print(tuple(range(5)))  # (0, 1, 2, 3, 4)
print(tuple(25))     # Error: int object is not iterable

a = ()
print(type(a))       # <class 'tuple'>
print(a)             # ()
print(len(a))        # 0
b = tuple()
print(b)             # ()
print(len(b))        # 0

a = (10, 20, 30)
print(a)             # (10, 20, 30)
print(id(a))         # id1 (some memory address)
a = a * 2
print(a)             # (10, 20, 30, 10, 20, 30)
print(id(a))         # id2 (different from id1)

a = {25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'}
print(a)               # {None, 3+4j, 10.8, True, 25, 'Hyd'}
print(type(a))         # <class 'set'>
print(len(a))          # 6 (duplicates removed)
print(a[2])            # Error: 'set' object is not subscriptable
print(a[1:4])          # Error: 'set' object is not subscriptable
a[2] = 'Sec'           # Error: 'set' object does not support item assignment
print(a * 2)           # Error: unsupported operand type 
print(a * a)           # Error: unsupported operand type

a = {1, 'Hyd', False, True, 0.0, '', 1.0, 0}
print(a)            # {'Hyd'}  --> All others are treated as duplicates
print(len(a))       # 1
print(type(a))      # <class 'set'>

a = set('Rama rAo')
print(a)                      # {'a', 'A', 'o', 'R', ' ', 'r', 'm'} -> Unique characters only
print(len(a))                 # 7
print(set([10 , 20 , 15 , 20]))                # {10, 20, 15}     # duplicates removed
print(set((25 , 10.8 , 'Hyd' , 10.8)))         # {25, 10.8, 'Hyd'} # 10.8 duplicate removed
print(set(range(10 , 20 , 3)))                 # {10, 13, 16, 19} # range converted to set
print(set(25))                                # Error: 'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))          # Error: unhashable type: 'list'

a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))     # <class 'list'>
print(type(b))     # <class 'tuple'>
print(type(c))     # <class 'dict'>
print(type(d))     # <class 'set'>
print(a)           # []
print(b)           # ()
print(c)           # {}
print(d)           # set()

a = set()
a.add(25)         # OK
a.add(10.8)       # OK
a.add('Hyd')      # OK
a.add(True)       # OK, but True == 1, so both True and 1 are same
a.add(None)       # OK
a.add('Hyd')      # Duplicate → ignored
a.add(1)          # Duplicate of True → ignored
print(a)          # {None, 10.8, 'Hyd', 25, True}
print(len(a))     # 5
a.remove(25)      # OK
print(a)          # {None, 10.8, 'Hyd', True}
a.append(100)     # Error: 'set' object has no attribute 'append'
a.add(set())      # Error: unhashable type: 'set'
a.add(())         #  OK — tuple is hashable
a.add([])         # Error: unhashable type: 'list'
a.add({})         # Error: unhashable type: 'dict'

a = {25 , True , 'Hyd' , 10.8}
print('set with print function') # set with print function
print(a)  # {'Hyd', 10.8, 25}  → order may vary
print('Iterate thru set with for loop') # Iterate thru set with for loop
for i in a: print(i)
# Hyd      ← order may vary
# 10.8
# 25
