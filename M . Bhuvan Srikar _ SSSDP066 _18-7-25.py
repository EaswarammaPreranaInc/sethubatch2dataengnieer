# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # How  to  print  set)
print('Iterate  thru  set  with  for  loop')
# How  to  iterate  thru  set  with  for  loop
for x in a:
	print(x)

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # empty list []
a . append(25) # adds 25 to the list
a . append(10.8) # adds 10.8 to the list
a . append('Hyd') # adds Hyd to the List
a . append(True) # adds True to the list
print(a) # [25 , 10.8 , Hyd , True]
a . remove('Hyd') # Removes Hyd from the list
print(a) # [25 , 10.8 , True]
a . remove('25') # error as there is no '25'
print(a) # [25 , 10.8 , True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) # address of the list object
print(a * 3) # [25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd']
print(a * 2) # [25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd']
print(a * 1) # [25 , 10.8 , 'Hyd']
print(a * 0) # [] empty list
print(a * -1) # [] empty list
print(a * 4.0) # error as for repetition 2nd argument must be int
a = a * 3
print(a) # [25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd']
print(id(a)) # address of the new list object
a = [25]  

# list()  function  demo  program
a = list('Hyd')
print(a) # ['Hyd']
print(type(a)) # <class 'list'>
print(len(a)) # 1
b = (10 , 20 , 15 , 18)
print(list(b)) # [10 , 20 , 15 , 18]
print(list(range(5))) # [0 , 1 , 2 , 3 , 4]
print(list(25)) # error becoz argument should be sequence only

# Find  outputs
a = [ ]
print(type(a)) # <class 'list'>
print(a) # [] empty list
print(len(a)) # 0
b = list() 
print(b) # []
print(len(b)) # 0

# Slice  demo  program (Home  work)
#        0      1     2         3     4       5    6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7     -6      -5      -4     -3     -2      -1
print(list[2 : 7]) # list[2 : 7 : 1] --> list from indexes 2 to 6 in steps of 1 ---> [3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])# list[0 : 8 : 1] --> list from indexes 0 to 7 in steps of 1 --->  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # list[-1 : -9 : -1] --> list from indexes -1 to -7 in steps of -1 --> ['Hyd' , 10.8 , None , True , 'Hyd' , 3+4j , 10.8 , 25]
print(list[ : : 2]) # list[0 : 8 : 2]--> list from indexes 0 to 7 in steps of 2 --> [25 , 3 + 4j , True , 10.8]
print(list[1 : : 2]) # list[1 : 8 : 2] --> list from indexes 1 to 7 in steps of 2 --> [10.8 , 'Hyd' , None , 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # list[-2 : -9 : -2] --->  List  from  indexes   -2  to  -8  in  steps  of   -2 i.e. [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # list[1 : 4 : 1] --> --->  List  from  indexes 1 to 3  in  steps of 1 i.e. [25 , 10.8 , 3+4j]
print(list[-4 : -1]) # list[-4 : -1 : 1] --> --->  List  from  indexes   -4  to  -2  in  steps  of   -1 i.e. [True , None , 10.8]
print(list[3 : -3]) # list[3 : -3 : 1] --> List from indexes 3 to -4 in strps of 1 i.e. ['Hyd' , True]
print(list[2 : -5]) # list[2 : -5 : 1] ---> List from indexes 2 to -6 in steps of 1 i.e. [3 + 4j]
print(list[-1:-5]) # []

#  Find  outputs  (Home  work)
#        0       1    2      3       4     5      6       7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # x : Hyd
print('y : ' , y) # y : True
for  x  in  list[2:7]: 
	print(x) # 3+4j <next line> Hyd <next line> True <next line> None <next line> 10.8


#  Find  outputs  (Home  work)
#     0     1   2    3    4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10 , 20 , 30 , 40 , 50] <space> address of the list
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10 , 60 , 70 , 50] <space> address of the list
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # error 

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # error becoz index is invalid
print(a[1:]) # []

# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'tuple'>
print(a * 4) # 100
print(b * 4) # (25 , 25 , 25 , 25)
print(c * 4) # 100
print(d * 4) # (25 , 25 , 25 , 25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) #  (Hyd,)
print(type(a)) # <class 'tuple'>
print(len(a)) # 1
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10 , 20 , 15 , 18)
print(tuple(range(5))) # (0 , 1 , 2 , 3 , 4)
print(tuple(25)) # error becoz argument is non - sequence

# Find  outputs (Home  work)
a = ()
print(type(a)) # <class 'tuple'>
print(a) # ()
print(len(a)) # 0
b = tuple()
print(b) # ()
print(len(b)) # 0

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # <class 'tuple'>
a = a * 2
print(a) # (10 , 20 , 30 , 10 , 20 , 30)
print(id(a)) # address of the new tuple

#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , True , 3 + 4j , None , 'Hyd'} can be any order
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # error becoz set does not have indexes
print(a[1 : 4]) # error as set does not have slicing
a[2] = 'Sec' # error as set cannot be modified
print(a * 2) # error as set cannot be repeated
print(a * a) # error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , ''} can be any order
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'r' , 'R' , 'a' , 'A' , 'm' , 'o' , ''} can be any order
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10 , 20 , 15} can be any order
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25 , 10.8 , 'Hyd'} can be any order
print(set(range(10 , 20 , 3))) # {10 , 13 , 16 , 19} can be any order
print(set(25)) # error becoz argument is sequence
print(set([25 , 10.8 , [] , 'Hyd'])) # error becoz set cannot hold mutable elements

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'set'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) # adds 25 any where in the set
a . add(10.8) # adds 10.87 anywhere in the set
a . add('Hyd') # adds Hyd anywhere in the set
a . add(True) # adds True anywhere in the set 
a . add(None) # adds None anywhere in the sett
a . add('Hyd') # Hyd is already added so it is ignored
a . add(1) # True is already added so it is ignored
print(a) # {25 , 10.8 , 'Hyd' , True , None}  can be any order
print(len(a)) # 5 
a . remove(25) # removes 25 from the set
print(a) # {10.8 , 'Hyd' , True , None} can be any order 
a . append(100) # error as there is no append method in the set
a . add(set()) # error as set cannot hold mutable elements
a . add(()) # adds empty tuple anywhere in the set
a . add([]) # error as set cannot hold mutable elements
print(a) # {10.8 , 'Hyd' , True , None , ()} can be any order
a . add({}) # error as set cannot hold mutable elements 

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # How  to  print  set)
print('Iterate  thru  set  with  for  loop')
# How  to  iterate  thru  set  with  for  loop
for x in a:
	print(x)
print(a * a) # error becoz of list multiplication
