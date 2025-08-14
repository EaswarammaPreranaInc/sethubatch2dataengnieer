  #Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25
print(type(a)) # < class 'list'>
print(id(a)) # Address of object <may be 1000>
print(len(a)) # 8
a[2] = 'Sec'
print(a) # [25 , 10.8 , 'sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # 'sec' True 3+4j

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # []
a . append(25) # [25]
a . append(10.8) # [25,10.8]
a . append('Hyd') # [25,10.8,'Hyd']
a . append(True) #  [25,10.8,'Hyd',True]
print(a) # [25,10.8,'Hyd',True]
a . remove('Hyd')
print(a) # [25,10.8,True]
a . remove('25') # Error
print(a) #  [25,10.8,True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) # Address of object a i.e < may be 1000>
print(a * 3) # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2) # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1) # [25 , 10.8 , 'Hyd']
print(a * 0) # []
print(a * -1) # []
print(a * 4.0) # Error
a = a * 3 
print(a) # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a)) # Address of object a i.e < may be 2000>
a = [25]
print(a * a) # [25,25]

# list()  function  demo  program
a = list('Hyd')
print(a) # ['H','y','d']
print(type(a)) # < class 'list'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10,20,15,18]
print(list(range(5))) # [0,1,2,3,4]
print(list(25)) # Error


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->   No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''

# Find  outputs
a = [ ]
print(type(a)) # < class 'list'>
print(a) # []
print(len(a)) # 0
b = list() 
print(b) # []
print(len(b)) # 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) #  list[2 :  7 :  1]  --->  List  from  indexes  2  to  6  in  steps  of  1  i.e.  [3 + 4j , 'Hyd' , True , None , 10.8 ]
print(list[ : : ]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # ['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25]
print(list[ : : 2]) # [25,3+4j,True,10.8]
print(list[1 : : 2]) # [10.8,'Hyd','None,'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # [10.8,True,3+4j,25]
print(list[1 : 4]) # [10.8,3+4j,'Hyd']
print(list[-4 : -1]) # [True,None,10.8]
print(list[3 : -3]) # ['Hyd',True]
print(list[2 : -5]) # [3+4j]
print(list[-1:-5]) # []

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # x:True
print('y : ' , y) # y:None
for  x  in  list[2:7]:
	print(x) # 3+4j <new line> 'Hyd' <new line> True <new line> None <new line> 10.8


#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10 , 20 , 30 , 40 , 50] Address of object i.e < may be 1000>
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10,60,70,50] Address of object i.e < may be 1000>
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10,60,100,200,300] Address of object i.e < may be 1000>


#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Error
print(a[1:]) #''


# Find  outputs  (Home  work)
a = (25)
b = 25, 
c = 25
d = (25,)
print(type(a)) # < class int>
print(type(b)) # < class Tuple>
print(type(c)) # < class int>
print(type(d)) # < class Tuple>
print(a * 4) # 100
print(b * 4) # (25,25,25,25)
print(c * 4) # 100
print(d * 4) # (25,25,25,25)


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # ('H','y','d')
print(type(a)) # < class Tuple>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10,20,15,18)
print(tuple(range(5))) # (0,1,2,3,4)
print(tuple(25)) # Error



'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''

# Find  outputs (Home  work)
a = ()
print(type(a)) # < class Tuple>
print(a) # ()
print(len(a)) # 0
b = tuple() 
print(b) # ()
print(len(b)) # 0

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # Address of object< may be 1000>
a = a * 2 # (10 , 20 , 30,10 , 20 , 30)
print(a) # (10 , 20 , 30,10 , 20 , 30)
print(id(a)) # Address of object< may be 2000>


#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a)) # < class set>
print(len(a)) # 6
print(a[2]) # Error
print(a[1 : 4]) # Error
a[2] = 'Sec' # Error
print(a * 2) # Error
print(a * a) # Error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , '' }
print(len(a)) # 4
print(type(a)) # < class set >

#  set()  function demo  program
a = set('Rama rAo')
print(a) # { 'a','r','R','','A','m','o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10 , 20 , 15 , 20}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25 , 10.8 , 'Hyd' , 10.8}
print(set(range(10 , 20 , 3))) # {10,16,19,13}
print(set(25)) # Error
print(set([25 , 10.8 , [] , 'Hyd'])) # Error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set
'''


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # < class 'list'>
print(type(b)) # < class 'Tuple'>
print(type(c)) # < class 'dict'>
print(type(d)) # < class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) # {25}
a . add(10.8) # {25,10.8}
a . add('Hyd') # {25,10.8,'Hyd'}
a . add(True) # {25,10.8,'Hyd',True}
a . add(None) # {25,10.8,'Hyd',True,None}
a . add('Hyd') # Ignores 'Hyd' already exist in set a
a . add(1) #  Ignores 1 already exist in set a
print(a) # {25,10.8,'Hyd',True,None}
print(len(a)) # 5
a . remove(25) 
print(a) # {10.8,'Hyd',True,None}
a . append(100) # Error
a . add(set()) #Error
a . add(()) # {25,10.8,(),'Hyd',True,None}
a . add([]) # Error
print(a) # {25,10.8,'Hyd',True,None}
a . add({}) # Error

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # print(a)
print(How  to  print  set)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
for x in a:
  print(x)
