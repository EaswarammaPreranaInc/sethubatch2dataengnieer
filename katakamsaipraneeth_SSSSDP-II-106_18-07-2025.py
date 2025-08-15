#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25] # ref 'a' is pointed to list object 
print(a) # prints list [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)# prints elements of list object ---> 25  10.8  Hyd  True  3+4j  None  Hyd  25
print(type(a)) # <class 'list'>
print(id(a))# prints address of list object 'a'
print(len(a)) # 8
a[2] = 'Sec' # it updates element at index 2 of list object
print(a) # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # prints new object when sliced --->[ 'Sec' , True , 3 + 4j ]


# append()  and  remove()  methods  (Home  work)
a = [ ] # [ ] is said to be list operator 
print(a) # prints empty list [ ]
a . append(25) # inserts 25 into list object 'a' --->[25,]
a . append(10.8) # inserts 10.8 into list object --->[25, 10.8 ]
a . append('Hyd') # inserts Hyd into list object
a . append(True) # inserts True into list object
print(a) # prints---> [25, 10.8, 'Hyd', True]
a . remove('Hyd') ----> it deletes Hyd at first occurrence in list object
print(a) # [25, 10.8, True]

a . remove('25') # deletes 25 from list object 'a'
print(a) # [10.8, True]


#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd'] # ref 'a' is assigned list class object 
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) # prints address of list object
print(a * 3) # list object is repeated 3 times and makes new list ---> [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) # repeates list 2 times ---> [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) # repeates list 1 time ---> [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 0) # empty list [ ]
print(a * -1) # empty list [ ]
print(a * 4.0) # cannot be multipied with float arg---> error
a = a * 3 # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) # return address of object 'a'
a = [25] # ref 'a' is pointed to list obj with element 25
print(a * a) # [25, 25]


# list()  function  demo  program
a = list('Hyd') # ref 'a' is pointed to list object with str element
print(a) # ['Hyd',]
print(type(a)) # <class  'list'>
print(len(a)) # 1
b = (10 , 20 , 15 , 18) # ref 'b' is pointed to tuple object 
print(list(b)) # here tuple is converted to list --> Type Casting  # [10 , 20 , 15 , 18]
print(list(range(5))) # prints--> [0 ,1, 2, 3, 4]
print(list(25))# error


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->   No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''


# Find  outputs
a = [ ] # empty list object
print(type(a)) # <class  'list'>
print(a) # [ ]
print(len(a)) # 0
b = list() # ref 'b' is pointed to list object
print(b) # [ ] 
print(len(b)) # 0


# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # list[2:7:1]---> [3 + 4j , 'Hyd' , True , None , 10.8]  new list
print(list[ : : ]) #  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # reverse of list ---> ['Hyd', 10.8, None, True, 'Hyd', 3+4j, 10.8, 25]
print(list[ : : 2]) # with step 2 it prints--->[25 , 3 + 4j , True , 10.8 ] 
print(list[1 : : 2]) # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # list[-2: -len-1:-2] ---> [10.8, True, 3+4j, 25]
print(list[1 : 4]) # # [25, 10.8, 3+4j, 'Hyd']
print(list[-4 : -1])# [ True, None , 10.8]
print(list[3 : -3]) # empty list 
print(list[2 : -5]) # [ ] 
print(list[-1:-5]) # [ ]


#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd'] # list object is created
x ,  y = list[3 : 5] # x=' Hyd' , y = True
print('x : ' , x) # x : 'Hyd'
print('y : ' , y) #y :  True
for  x  in  list[2:7]:
	print(x) # prints all elements one by one
# 3+4j 
#'Hyd'
# True
# None 
# 10.8

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10 , 20 , 30 , 40 , 50] and  address of obj 'a'
a[1 : 4] = [60 , 70] # from index 1,2,3 elements are replaced with 60, 70--> [10, 60, 70, 50]
print(a , id(a))#  [10, 60, 70, 50] address of a
a[2: 4] = [100 , 200 ,  300] # from index 2-4 the elements are replaced 
print(a , id(a)) # [10, 60, 100, 200, 300] with same address

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # empty [ ]
print(a[1:]) # [ ]


# Find  outputs  (Home  work)
a = (25) # ref 'a' is pointed to int class obj ,where () is optional for tuple
b = 25, # its tuple object
c = 25 # its int object
d = (25,) # its tuple object where ( ) is optional
print(type(a)) # <class  'int'>
print(type(b)) # <class  'tuple'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'tuple'>
print(a * 4) # 100
print(b * 4) # error
print(c * 4) # 100
print(d * 4)# error


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') # a is tuple object
print(a) # ( 'H','y',d')
print(type(a)) # <class  'tuple'>
print(len(a)) # 3
b = [10 , 20 , 15 , 18] # list object with elements
print(tuple(b)) # (10 , 20 , 15 , 18) --> list converts into tuple
print(tuple(range(5)))# (0,1,2,3,4)
print(tuple(25)) # error



'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''

# Find  outputs (Home  work)
a = () # empty tuple object 
print(type(a)) # <class  'tuple'>
print(a) # ( ) 
print(len(a)) # 0
b = tuple() # ref is pointed to tuple object
print(b) # ( )
print(len(b)) # 0

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # address of object
a = a * 2 # error
print(a) #(10 , 20 , 30)
print(id(a)) # same address

#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'} # ref 'a' is pointed to set object 
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a)) # <class  'set'>
print(len(a)) # 6
print(a[2]) # error because set has no index
print(a[1 : 4]) # error --no index --no slicing
a[2] = 'Sec' #error
print(a * 2) # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(a * a) # error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {False, '', 1, 'Hyd'}
print(len(a)) # 4
print(type(a)) # <class  'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a) #{'r', 'a', ' ', 'R', 'A', 'm', 'o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}
print(set(25)) # error
print(set([25 , 10.8 , [] , 'Hyd'])) # {25 , 10.8 , [] , 'Hyd'}


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set
'''

# Find  outputs  (Home  work)
a =   [ ] # ----> list object
b =   ( ) # ----> tuple object
c =   {} # ----> set object
d =   set() # ----> set object
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'set'>
print(type(d)) # <class 'set'>
print(a) # [ ]
print(b) # ( )
print(c) # { }
print(d) # { }

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() # set object 
a . add(25) # inserts 25 into tuple object 
a . add(10.8) # same inserts 10.8
a . add('Hyd') # inserts 'Hyd'
a . add(True) # inserts True
a . add(None) # inserts None
a . add('Hyd') # inserts 'Hyd'
a . add(1) # inserts 1
print(a) # { 25, 10.8, 'Hyd', True, None, 1}
print(len(a)) # 6
a . remove(25) # removes element 25 from tuple object
print(a)# { 10.8, 'Hyd', True, None, 1}
a . append(100) # tuple has no append method like list so -- error
a . add(set()) # error
a . add(()) # added into obj as element
a . add([]) # error because list is mutable
print(a) #  { 10.8, 'Hyd', True, None, 1, ( )}
a . add({}) # error because set is mutable

# How  to  print  set  in  two  differnet ways  (Home  work) 
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # print(set(a))
print(How  to  print  set) # print(a)
print('Iterate  thru  set  with  for  loop') 
How  to  iterate  thru  set  with  for  loop
---->
a = {25 , True , 'Hyd' , 10.8}
for i in a:
     print( i )
# prints--
25
True
'Hyd'
10.8 
# set may prints output in diff format according to input given