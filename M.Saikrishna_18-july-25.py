

#Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)  # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) #25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) # Prints Type of object 'a' is <class 'List'>
print(id(a))   # Prints Address of object 'a'
print(len(a))  # Prints No.Number of Elements in the list:8
a[2] = 'Sec'   # Modifying the list at index a[2]='sec'
print(a)       # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])# ['Sec', True, (3+4j)]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)	       # []
a . append(25)     # append(adding) the value into the list at the end 25
a . append(10.8)   # append(adding) the value into the list at the end 10.8
a . append('Hyd')  # append(adding) the value into the list at the end 'Hyd'
a . append(True)   # append(adding) the value into the list at the end True
print(a)           # [25,10.8,'Hyd',1]
a . remove('Hyd')  # remove the first occurrence of 'Hyd'  from the list
print(a)           # [25,10.8,True]
a . remove('25')   # remove the first occurrence of 25  from the list
print(a)           # [10.8, True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) 	# [25 , 10.8 , 'Hyd']
print(id(a))    # id can be anything like 1475634
print(a * 3)    # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)    # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)    # [25 , 10.8 , 'Hyd']
print(a * 0)    # []
print(a * -1)   # []
print(a * 4.0)  # can't multiply sequence
a = a * 3
print(a) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) # id can be anything like 19057828
a = [25]
print(a * a) # can not multiply sequence

# list()  function  demo  program
a = list('Hyd') 
print(a) # ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a))  # 3
b = (10 , 20 , 15 , 18)
print(list(b))        # [10, 20, 15, 18]
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(25))       # int is iterable
'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->   No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting'''

# Find  outputs
a = [ ]
print(type(a)) # <class 'list'>
print(a)       # []
print(len(a))  # 0
b = list()
print(b)       #[]
print(len(b))  #0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 ,      3 + 4j , 'Hyd' ,     True ,   None ,   10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) #[3 + 4j , 'Hyd' ,     True ,   None ,   10.8]
print(list[ : : ]) # [25 , 10.8 ,      3 + 4j , 'Hyd' ,     True ,   None ,   10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # ['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25]
print(list[ : : 2])  # [25,3+4j,True,10.8]
print(list[1 : : 2]) # [10.8,'Hyd',None,'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # [10.8, True, (3+4j), 25]
print(list[1 : 4])     # [10.8,3+4j,'Hyd']
print(list[-4 : -1])   # [True ,   None ,   10.8]
print(list[3 : -3])    # ['Hyd' , True]
print(list[2 : -5])    # [3+4j]
print(list[-1:-5])     # []

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] 
print('x : ' , x)    # x:'Hyd'
print('y : ' , y)    # y:True
for  x  in  list[2:7]:
	print(x)     # 3+4j
                       #'Hyd'
                      # True
                       #None
                       #10.8

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10, 20, 30, 40, 50] 123548
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10, 60, 70, 50] 
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10, 60, 100, 200, 300] 

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # list index is out if the range
print(a[1:]) # []

# Find  outputs  (Home  work)
a = (25) # without comma in the () it is not considered as a tuple as it is an integer
b = 25,  # for single element in tuple their is not compulsory for () but should contain 25,
c = 25   # without comma it is not considered as a tuple as it is an integer
d = (25,)# tuple for single element (25,)
print(type(a)) # <class int>
print(type(b)) # <class tuple>
print(type(c)) # <class int>
print(type(d)) # <class tuple>
print(a * 4) # 100
print(b * 4) # (25,25,25,25)
print(c * 4) # 100
print(d * 4) # (25,25,25,25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') 
print(a) #('H','y','d')
print(type(a)) #<class 'tuple'>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10,20,15,18)
print(tuple(range(5))) # (0,1,2,3,4)


'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple'''


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
print(a)     # (10,20,30)
print(id(a)) # id can be anything like 14035468435
a = a * 2
print(a)     # (10,20,30,40,50,60)
print(id(a)) # id can be anything like 14035468435

#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {'Hyd',25,True,10.8,None,3+4j} (the set is unordered so while printing the elements of a they are unordered)
print(type(a))  # <class set>
print(len(a))   # 6 (duplicates are not allowed in the set)
print(a[2])     # Sets are unordered, so you can’t access items with an index.
print(a[1 : 4]) # Slicing is not supported on sets
a[2] = 'Sec' # sets are mutable,but not by index
print(a * 2) # sets do not support multiplication
print(a * a) # sets do not support multiplication

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {'Hyd','',1,False} (no duplicates are required in set)
print(len(a)) # 4
print(type(a)) # <class 'tuple'>

#  set()  function demo  program
a = set('Rama rAo') 
print(a) #{'a', 'o', 'r', ' ', 'm', 'A', 'R'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) #{10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # {10,13,16,19}
print(set(25))
print(set([25 , 10.8 , [] , 'Hyd']))


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set'''


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) #[]
print(b) #()
print(c) #{}
print(d) #set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) # {None, True, 'Hyd', 10.8, 25}
print(len(a)) # 5
a . remove(25)
print(a) # {None, True, 'Hyd', 10.8}
a . append(100) 
a . add(set())
a . add(())
a . add([])
print(a) # 'set' object has no attribute 'append'
a . add({}) # 'set' object has no attribute 'append'

# How  to  print  set  in  two  differnet ways  (Home  work)
a ={25 , True , 'Hyd' , 10.8} 
print('set  with  print  function') # print(a) {25 , 10.8 , 'Hyd' , 1} 
print(a)#How  to  print  set) # print(a)
print('Iterate  thru  set  with  for  loop') #for item in a:
#     						print(item)
# How  to  iterate  thru  set  with  for  loop  # True
#                                                10.8
#                                                25
#                                                Hyd
