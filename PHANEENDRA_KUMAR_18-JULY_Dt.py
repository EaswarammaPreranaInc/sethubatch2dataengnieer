#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]  
print(a)        # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]  
print(*a)       # elements of a , 25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25
print(type(a))  # class<List>
print(id(a))    # Address of the object 
print(len(a))   # No of elements , 8
a[2] = 'Sec'    # 'Hyd' is modified to 'Sec'
print(a)        # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) # 'Sec' True (3+4j) 

# append()  and  remove()  methods  (Home  work)
a = [ ]              
print(a)             # [] ,Empty list
a . append(25)       # [25] 
a . append(10.8)     # [25 10.8]
a . append('Hyd')    # [25 10.8 'Hyd']
a . append(True)     # [25 10.8 'Hyd' True]
print(a)             # [25 10.8 'Hyd' True]
a . remove('Hyd')    # [25 10.8 True]
print(a)
a . remove('25')     # Error due to single Quotes
print(a)

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)         # [25 , 10.8 , 'Hyd']
print(id(a))     # Address of the object
print(a * 3)     # [25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd'25 , 10.8 , 'Hyd']
print(a * 2)     # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)     # [25 , 10.8 , 'Hyd']
print(a * 0)     # Empty List
print(a * -1)    # Empty List 
print(a * 4.0)   # Error can't multiply float
a = a * 3        # [25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd'25 , 10.8 , 'Hyd']
print(a)
print(id(a))     # Address of the object
a = [25]         # Now a modified to 25
print(a * a)     # Error

# list()  function  demo  program
a = list('Hyd')          # converts str 'Hyd' to List
print(a)                 # ['H','Y','D']
print(type(a))           # class <List>
print(len(a))            # len of a is 3
b = (10 , 20 , 15 , 18) 
print(list(b))           # Converts tuple b to List [10,20,15,18]
print(list(range(5)))    # [0,1,2,3,4]
print(list(25))          # Error can't convert single int into 25

# Find  outputs
a = [ ]          # Empty List
print(type(a))   # class <List>
print(a)         # [ ]
print(len(a))    # len is 0
b = list()       # Empty List
print(b)         # [ ]
print(len(b))    # len of b is 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list =    [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])     # [3 + 4j , 'Hyd' , True , None , 10.8 ]
print(list[ : : ])     # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])         #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])   # ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])    # [25, (3+4j), True, 10.8]
print(list[1 : : 2])   # [10.8,'Hyd',None,'Hyd']
print(list[ : : -2])   #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # [10.8,True,3+4j,25]
print(list[1 : 4])     # [10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])   # [True, None, 10.8]
print(list[3 : -3])    # ['Hyd',True]
print(list[2 : -5])    # [] Empty List
print(list[-1:-5])     # [] Empty List




#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]---->'hyd', True
print('x : ' , x)---->Hyd
print('y : ' , y)----->true
for  x  in  list[2:7]
	print(x)----> 3+4j,'Hyd', True,None,10.8,'Hyd'






#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))------->[10, 20, 30, 40, 50] 140567352194048
a[1 : 4] = [60 , 70]
print(a , id(a))-------------->[20, 30, 40]140567352194048
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))----->[10, 60, 100, 200, 300] 140320865712320





#  Find  outputs  (Home  work)
a =  [25]
print(a[1])----> 'int' object is not subscriptable
print(a[1:])---->[]  







# Find  outputs  (Home  work)
a = (25)---->reference b points to tuple 25
b = 25,----->reference b points to tuple 25
c = 25------>Reference c points to int 25
d = (25,)---->reference d points to tuple 25
print(type(a))-----><class'int'>
print(type(b))----><class 'tuple'>
print(type(c))---><class'int'>
print(type(d))----><class'int'>
print(a * 4)--->100
print(b * 4)---->(25, 25,25,25)
print(c * 4)---->100
print(d * 4)----->(25,25,25,25)





# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)---->a = ('H', 'y', 'd')
print(type(a))----><class 'tuple'>
print(len(a))---->3
b = [10 , 20 , 15 , 18]
print(tuple(b))--->(10, 20, 15, 18)
print(tuple(range(5)))---------->(0, 1, 2, 3, 4)
print(tuple(25))----------->TypeError: 'int' object is not iterable




# Find  outputs (Home  work)
a = ()
print(type(a))--><class 'tuple'>
print(a)---->()
print(len(a))--->0
b = tuple()
print(b)--->()
print(len(b))---->0




# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)------->(10, 20, 30)
print(id(a))-------> address of some memory
a = a * 2
print(a)---->(10, 20, 30) * 2 → (10, 20, 30, 10, 20, 30)
print(id(a))--->address of some memory



#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)---->a = {25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'}
print(type(a))----><class 'set'>
print(len(a))------>{True, 10.8, 3+4j, 'Hyd', 25, None}
print(a[2])----->TypeError: 'set' object is not subscriptable
print(a[1 : 4])----->TypeError: 'set' object is not subscriptable
a[2] = 'Sec'
print(a * 2)--->error
print(a * a)--->error 




# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)--->{0, 1, '', 'Hyd'} 
print(len(a))---->4
print(type(a))----><class 'set'>




#  set()  function demo  program
a = set('Rama rAo')
print(a)--->{'o', 'a', 'R', 'm', ' ', 'r', 'A'}
print(len(a))---->7
print(set([10 , 20 , 15 , 20]))--->{10, 20, 15}

print(set((25 , 10.8 , 'Hyd' , 10.8)))--->{25, 10.8, 'Hyd'}

print(set(range(10 , 20 , 3))--->{10, 13, 16, 19}

print(set(25))---->'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))----------->error  unhashable type: 'list'


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))-----><class 'list'>
print(type(b))-------><class 'tuple'>
print(type(c)) ------->  <class 'dict'>
print(type(d))-------><class 'set'>
print(a)----->[ ]
print(b)---->( )
print(c)---->{}
print(d)---->set()





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
print(a)---->{None, 10.8, 'Hyd', 25}
print(len(a))----->4 
a . remove(25)
print(a)--->a = {10.8, 'Hyd', None}
a . append(100)
a . add(set())
a . add(())
a . add([])
print(a)--->{100, ()}
a . add({})




# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')---->10.8
print(How  to  print  set)----->true
print('Iterate  thru  set  with  for  loop')--->hyd
How  to  iterate  thru  set  with  for  loop---->25




