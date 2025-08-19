#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)          # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)          # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))      # <class 'list'>
print(id(a))        # address of the object
print(len(a))       # 8
a[2] = 'Sec'        # a[2] is changed from 'Hyd' to 'Sec'
print(a)             # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])        # ['Sec', True, (3+4j)]


# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)                 # []
a . append(25)             # 25 append to list a
a . append(10.8)           # 10.8 append to list a
a . append('Hyd')         # 'Hyd' append to list a
a . append(True)              # True append to list a
print(a)                  # [25, 10.8, 'Hyd', True]
a . remove('Hyd')          # 'Hyd' is removed from list a
print(a)                    # [25, 10.8, True]
a . remove('25')           #Error because 25 is not in the list
print(a)                       # [25, 10.8, True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)         # [25, 10.8, 'Hyd']
print(id(a))      # address of the object 
print(a * 3)      # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)       # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)         # [25, 10.8, 'Hyd']
print(a * 0)        # []
print(a * -1)         # []
print(a * 4.0)        #error because list can't be multiplied by float number
a = a * 3             
print(a)              # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd'] because a is updated to a*3
print(id(a))           # address of the new object a
a = [25]               # a is updated to [25] 
print(a * a)           #Error because list-object can't be multiplied by list-object 



# list()  function  demo  program
a = list('Hyd')
print(a)           # ['H', 'y', 'd']   
print(type(a))      # <class 'list'>
print(len(a))      # 3
b = (10 , 20 , 15 , 18 )
print(list(b))             # [10, 20, 15, 18]
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(25))                   # Error because list() can't take integer as argument


# Find  outputs
a = [ ]
print(type(a))         # <class 'list'>
print(a)                  # []
print(len(a))              # 0
b = list()     
print(b)                      # []
print(len(b))                # 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 ,     3 + 4j ,   'Hyd' ,   True ,   None ,   10.8 ,  'Hyd']
#       -8     -7        -6        -5         -4      -3       -2        -1
print(list[2 : 7])       # [3+4j, 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : ])                   #[25 , 10.8, 3 + 4j, 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])                #['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])                # [25, 3+4j, True, 10.8]
print(list[1 : : 2])               # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])                  #[10.8, True , 3+4j, 25]
print(list[1 : 4])                   # [10.8, 3+4j, 'Hyd']
print(list[-4 : -1])                  # [True, None, 10.8]
print(list[3 : -3])                  #['Hyd', True]
print(list[2 : -5])                 # [3+4j]
print(list[-1:-5])               # []




#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]                 # x = 'Hyd', y = True
print('x : ' , x)                  # x :  Hyd
print('y : ' , y)                # y :  True
for  x  in  list[2:7]:                    
	print(x)                      ''' 3+4j
                                             Hyd   
                                                   True
                                                None
                                             10.8
																'''
 

 #  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))                 # [10, 20, 30, 40, 50] ,address of the list object
a[1 : 4] = [60 , 70]             
print(a , id(a))              # [10, 60, 70, 50] , same address as before     
a[2: 4] = [100 , 200 ,  300]     
print(a , id(a))             # doubt



#  Find  outputs  (Home  work)
a =  [25]
print(a[1])            # Error list index out of range
print(a[1:])       # []


# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))                  # <class 'int'>
print(type(b))                # <class 'tuple'>
print(type(c))                # <class 'int'>
print(type(d))                # <class 'tuple'>                   
print(a * 4)                   # 100
print(b * 4)                 # (25, 25, 25, 25)
print(c * 4)                    # 100
print(d * 4)               # (25, 25, 25, 25)


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)                     # ('H', 'y', 'd')
print(type(a))               # <class 'tuple'>
print(len(a))               # 3
b = [10 , 20 , 15 , 18] 
print(tuple(b))                   # (10, 20, 15, 18) 
print(tuple(range(5)))              # (0, 1, 2, 3, 4)
print(tuple(25))                 # Error because tuple() can't take int as paramater


# Find  outputs (Home  work)
a = ()
print(type(a))                  # <class 'tuple'>
print(a)                      # ()
print(len(a))                  # 0
b = tuple() 
print(b)                         # ()
print(len(b))                       # 0



# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)                 # (10, 20, 30)
print(id(a))             # address of the tuple object
a = a * 2                
print(a)                   # (10, 20, 30, 10, 20, 30) because a is updated to a*2
print(id(a))              # address of the new tuple (a*2) object


#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)                            #  (order may change) {10.8, 25, 'Hyd', True, (3+4j), None}
print(type(a))                     # <class 'set'>
print(len(a))                     # 6 because set does not support duplicate values
print(a[2])                       #Error because set object doesn't support indexing
print(a[1 : 4])                  #Error because set object doesn't support slicing
a[2] = 'Sec'                   #Error because set object does't support itm assignment
print(a * 2)                   #Error because set object does't support multiplication
print(a * a)                   #Error, set with set can't be multiplied



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)                #  (order may change)  {1, 0.0, 'Hyd', False, True, ''}
print(len(a))            # 5 because set does not support duplicate values
print(type(a))       # <class 'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a)                #order may change,  
print(len(a))            # 8 because set does not support duplicate values
print(set([10 , 20 , 15 , 20]))           # {10, 15, 20}   order may change
 print(set((25 , 10.8 , 'Hyd' , 10.8)))    # {10.8, 25, 'Hyd'} order may change
 print(set(range(10 , 20 , 3)))            # {10, 13, 16, 19} order may change
 print(set(25))                            # Error because set() can not take int as parameter
print(set([25 , 10.8 , [] , 'Hyd']))      # Error because set() can not take list as parameter


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))             # <class 'list'>
print(type(b))              # <class 'tuple'>
print(type(c))            # <class 'dict'>
print(type(d))       # <class 'set'>
print(a)              # []
print(b)             # ()
print(c)           # {}
print(d)         # set()



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
print(a)                  # {None, 1, 10.8, 25, 'Hyd', True} (order may change) 
print(len(a))            # 6 because set does not support duplicate values
a . remove(25)                   
print(a)                      # {None, 10.8, 1 ,True,'Hyd'} (order may change) 
a . append(100)           #error because set object does not support append method
a . add(set())          # Error because set() cannot be added to a set 
a . add(())                
a . add([])             
print(a)                     
a . add({})             

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')      #print(a) # {10.8, 25, 'Hyd', True} (order may )
print(How  to  print  set)                
print('Iterate  thru  set  with  for  loop')
'''
for i in a:
	print(i) # 10.8
	         # 25
            # Hyd
            # True
            (order may change)'''
How  to  iterate  thru  set  with  for  loop