#  Find  outputs  
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # o/p: [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) # o/p: 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) # <class 'list'> 
print(id(a)) # prints the address of the list object
print(len(a)) # o/p: 8 : length of list 'a' is 8
a[2] = 'Sec' # change the element at index 2 from 'Hyd' to 'Sec'
print(a) # o/p: [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) # o/p: ['Sec', True, (3+4j)] : elements from index 2 to 4

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # o/p: []
a . append(25) # append 25 to the end of list 'a'
a . append(10.8) # append 10.8 to the end of list 'a'
a . append('Hyd') # append 'Hyd' to the end of list 'a'
a . append(True) # append True to the end of list 'a'
print(a) # o/p: [25, 10.8, 'Hyd', True]
a . remove('Hyd') # remove the first occurance 'Hyd' from the list 'a'
print(a) # o/p: [25, 10.8, True]
#a . remove('25') # valueerror: there is no string '25' in the list 'a'
print(a) # o/p: [25, 10.8, True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # o/p: [25, 10.8, 'Hyd']
print(id(a)) # prints the address of the list object
print(a * 3) # o/p: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd'] 
print(a * 2) # o/p: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # o/p: [25, 10.8, 'Hyd']
print(a * 0) # o/p: [] : empty list
print(a * -1) # o/p: [] : empty list
#print(a * 4.0) # TypeError: can't multiply sequence by non-int of type 'float'
a = a * 3 # reassign 'a' to the new list object [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a) # o/p: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) # prints the address of the new list object
a = [25] # reassign 'a' to the new list object [25]
#print(a * a) # TypeError: can't multiply sequence by non-int of type 'list'

# list()  function  demo  program
a = list('Hyd')
print(a) # ['H','y','d']
print(type(a)) # <class 'int'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10,20,15,18]
print(list(range(5))) # [0,1,2,3,4]
#print(list(25)) # typrerror: list doesn't convert non sequence integer

# Find  outputs
a = [ ]
print(type(a)) # <class 'int'>
print(a) # o/p: []
print(len(a)) # 0
b = list()
print(b) # []
print(len(b)) # 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ]) # [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2]) #  [25, (3+4j), True, 10.8]
print(list[1 : : 2]) # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # [10.8, True, (3+4j), 25]
print(list[1 : 4]) # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])  # [True, None, 10.8]
print(list[3 : -3]) # ['Hyd', True]
print(list[2 : -5]) # [(3+4j)]
print(list[-1:-5]) # empty list

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # x: Hyd
print('y : ' , y) # y: True
for  x  in  list[2:7]:
	print(x)
'''
o/p:
(3+4j)
Hyd
True
None
10.8'''

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50] 
print(a , id(a)) # [10, 20, 30, 40, 50] and address of object 'a'
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10,60,70,50] and address of obj 'a'. The address doesn't change it is same as before
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10,60,100,200,300] and address of obj 'a'

#  Find  outputs  (Home  work)
a =  [25]
#print(a[1]) # error: There os no element at index 1
print(a[1:]) # []

# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'tuple'>
print(a * 4) # 100
print(b * 4) # (25 ,25, 25, 25)
print(c * 4) # 100
print(d * 4) #(25 ,25, 25, 25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # o/p: ('H','y','d')
print(type(a)) # <class 'tuple' >
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10,20,15,18)
print(tuple(range(5))) # (0,1,2,3,4)
#print(tuple(25)) # TypeError: type(non sequence) is not valid

# Find  outputs (Home  work)
a = ()
print(type(a)) # <class 'tuple'>
print(a) # (): empty tuple
print(len(a)) # 0
b = tuple()
print(b) # (): empty tuple
print(len(b)) # 0

# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10, 20, 30)
print(id(a)) # address of tuple obj 'a'
a = a * 2
print(a) # ( 10,20,30,10,20,30)
print(id(a)) # # address of tuple obj 'a'

#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {True, 'Hyd', 25, 10.8, None, (3+4j)}: set is unordered
print(type(a)) # <class 'set'>
print(len(a)) # 6
#print(a[2]) # error: set do not support indexing or slicing
#print(a[1 : 4]) # TypeError
#a[2] = 'Sec' # error
#print(a * 2) # we cannot repeat a set
#print(a * a) # Typrerror: can not repeat a set with set

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {False, 1, 'Hyd', ''} : set is unordered
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) #{'a', ' ', 'm', 'o', 'A', 'R', 'r'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) #{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) #{16, 10, 19, 13}
#print(set(25)) # typeerror
#print(set([25 , 10.8 , [] , 'Hyd'])) # Typeerror

# Find  outputs  (Home  work)
a =   [ ] 
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c)  # {}
print(d)  # set()


# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() # creates an empty set
a . add(25) # a={25} : add element 25 to set 'a'
a . add(10.8) # a={25,20.8}
a . add('Hyd') # a={25,20.8,'Hyd'}
a . add(True) # a={25,20.8,'Hyd',True}
a . add(None) # a={25,20.8,'Hyd',True,None}
a . add('Hyd') # 'hyd' is already in the set. we cannot add same elment
a . add(1) # 1 is numerically equal to true
print(a) # {True, 'Hyd', 10.8, None, 25}
print(len(a)) # 5
a . remove(25) # removes 25 element from the set
print(a) # {True, 'Hyd', 10.8, None}
#a . append(100) # error
#a . add(set()) # error : we can not add set as an element to another set because sets are mutable
a . add(()) # add () : an empty tuple is immutable and therfore hashable . It can be added to a set.
#a . add([]) # Typeerror : list are muatble
print(a) # {True, 10.8, None, 'Hyd', ()}
#a . add({}) # Typrerror : dict are mutable

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a) # {25, 10.8, 'Hyd', True} : order is not specific
#How  to  iterate  thru  set  with  for  loop
for x in a:
	print(x)
