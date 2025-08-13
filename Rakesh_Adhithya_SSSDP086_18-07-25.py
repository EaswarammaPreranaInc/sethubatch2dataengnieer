#List Object


#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]  #'a'  is  list  due  to  []
print(a)                                                     #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)                                    #Unpacks list into elements i.e. 25<sp>10.8<sp>Hyd<sp>True<sp>(3 + 4j)<sp>None<sp>Hyd<sp>25
print(type(a))                                               #<class  'list'>
print(id(a))                                                 #Address of   list
print(len(a))                                                #8
a[2] = 'Sec'                                                 #Element at  index 2  of  list  'a'  is  modified  to  'Sec'
print(a)                                                     #[25 , 10.8 , 'Sec' , True , (3+4j) , None , 'Hyd' , 25]
print(a[2 : 5])                                            #List from indexes  2  to  4  in  steps  of  1   i.e.  ['Sec'  , True , 3 + 4j]

# append()  and  remove()  methods  (Home  work)
a = [ ]            #Empty  list
print(a)           #[]
a . append(25)     #Appends  25  to  empty  list
a . append(10.8)   #Appends  10.8  to   list
a . append('Hyd')  #Appends  'Hyd'  to   list
a . append(True)   #Appends  True   to   list
print(a)           #[25,10.8,'Hyd',True]
a . remove('Hyd')  #Removes 'Hyd' from   list   'a'
print(a)           #[25,10.8,True]
#a . remove('25')  #ValueError: list.remove(x): x not in list,  No  '25'  in  list  'a'
print(a)           #[25,10.8,True]


#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']   #Ref  'a'  points  to  list  of  3  elements
print(a)                  #[25 , 10.8 , 'Hyd']
print(id(a))              #Address of  list  with  3  elements
print(a * 3)              #Repeats list thrice i.e. [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)              #Repeats  list  twice i.e.  [25 , 10.8 ,  'Hyd'  , 25  ,  10.8  ,   'Hyd']
print(a * 1)              #Repeats  list  once  i.e.  [25 , 10.8 ,  'Hyd']
print(a * 0)              #Repeats  list   0  times  i.e.  []
print(a * -1)             #Repeats  list   -1  times  i.e.  []
#print(a * 4.0)           #TypeError: can't multiply sequence by non-int of type 'float', due to float operand 4.0
a = a * 3                 #Ref  'a'   is  modified  to   list  of   9  elements
print(a)                  #[25 , 10.8 ,  'Hyd'  , 25  ,  10.8  ,   'Hyd' ,  25 ,  10.8 ,  'Hyd']
print(id(a))              #Address of  list  with  9  elements
a = [25]                  #Ref  'a'   is  modified  to   list  of    single   element
print(a , id(a))          #[25]  <space>  Address  of  list  with  single  element
#print(a * a)             #TypeError: can't multiply sequence by non-int of type 'float', operand2 should be an integer but not list

# list()  function  demo  program
a = list('Hyd')          #Converts  string  to  list
print(a)                 #['H' , 'y' , 'd']
print(type(a))           #<class  'list'>
print(len(a))            #3
b = (10 , 20 , 15 , 18)  #Tuple  due to  ()
print(list(b))           #Converts   tuple  to  list  i.e.  [10 , 20 , 15 , 18]
print(list(range(5)))    #Converts   range   object to  list  i.e.  [0 , 1 , 2 ,3 , 4]
#print(list(25))         #TypeError: 'int' object is not iterable, becoz  25  is  not a  sequence


# Find  outputs
a = [ ]        #Empty  list
print(type(a)) #<class  'list'>
print(a)       #[]
print(len(a))  #0
b = list()     #Returns  an  empty  list
print(b)       #[]
print(len(b))  #0

# Slice  demo  program (Home  work)
#        0      1         2          3         4         5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5        -4       -3        -2      -1
print(list[2 : 7])     # list[2 : 7 :1] ---> List from indexes 2 to 6 in steps of 1 i.e. [3+4j,'Hyd' , True,None,10.8]
print(list[ : : ])     # list[0 : 8 :1] ---> List from indexes 0 to 7 in steps of 1 i.e. [25, 10.8, (3+4j),'Hyd', True, None, 10.8, 'Hyd']
print(list[:])         # list[0 : 8 :1] ---> List from indexes 0 to 7 in steps of 1 i.e. [25 , 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1])   # [-1:-9:-1] ---> List from indexes -1 to -8 in steps of -1 i.e. ['Hyd , 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])    # list[0 : 8 :2] ---> List from indexes 0 to 7 in steps of 2 i.e. [25, (3+4j), True, 10.8]
print(list[1 : : 2])   # list[1 : 8 :2] ---> List from indexes 1 to 7 in steps of 2 i.e. [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])   # [-1:-9:-2] ---> List from indexes -1 to -8 in steps of -2 i.e ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # [-2:-9:-2] ---> List from indexes -2 to -8 in steps of -2 i.e [10.8, True, (3+4j), 25]
print(list[1 : 4])     # [1:4:1] ---> List from indexes 1 to 3 in steps of 1 i.e [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])   # [-4:-9:-1] ---> List from indexes -4 to -8 in steps of -1 i.e [True, 'Hyd', (3+4j), 10.8, 25]
print(list[3 : -3])    # list[3 : -3 :1] ---> List from indexes 3 to -4 in steps of 1 i.e. ['Hyd' , True]
print(list[2 : -5])    # list[2 : -5 :1] ---> List from indexes 2 to -6 in steps of 1 i.e [3 + 4j]
print(list[-1:-5])     # list[-1 : -5 :1] ---> List from indexes -1 to -6 in steps of 1 i.e []

#  Find  outputs  (Home  work)
#        0      1         2        3          4       5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]     #  x , y = ['Hyd' , True]
print('x : ' , x)        #  x :  Hyd
print('y : ' , y)        #   y : True
for  x  in  list[2:7]:   #  for   x  in  [3+4j , 'Hyd' , True , None ,  10.8]
	print(x)             #(3+4j)<next line>Hyd<nl>True<nl>None<nl>10.8<nextline>
	

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))              #[10 , 20 , 30 , 40 , 50]   <space>  Address of list
a[1 : 4] = [60 , 70]          #Modifies  elements  of  list  from  indexes  1  to  3  to  60 , 70
print(a , id(a))              #[10 , 60 , 70 ,  50]   <space>  Same  address
a[2: 4] = [100 , 200 ,  300]  #Modifies  elements  of same list  from  indexes   2  to  3  to  100 , 200 , 300
print(a , id(a))              #[10,60,100,200,300]  <space> Same  address

#  Find  outputs  (Home  work)
a =  [25]
#print(a[1])  #IndexError: list index out of range
print(a[1:])  # List  without  first  element  i.e. []

#  How  to  print  list  in  different  ways  (Home  work)
a = [25 , 10.8 , 'Hyd' , True]
print('List  with   print   function')
print(a)                                                #How  to  print  list  --->  [25 , 10.8 , 'Hyd' , True]
print('Iterate  thru  list  without  using  indexes')
for   x   in    a:                                      #'x'  is  each  element  of  list  'a'
	print(x)                                            #25<nextline>10.8<nl>Hyd<nl>True<nextline>
print('Iterate  thru  list   using  indexes')
for  i  in  range(len(a)):
		print(a[i])                                     #prints a[i] where 'i' varies from 0 to len - 1
print('Iterate  thru  list  in  reverse  order')
for   i  in  range(1 , len(a) + 1):
		print(a[-i])                                    #prints a[-i] where  'i'  varies  from  1   to  len
print('Reverse  List  with  slice  :   '  ,   a[::-1])  #a[-1 : -5 : -1]  ---> List from indexes -1 to -4  in steps of -1 i.e. 
																									#[True , 'Hyd' , 10.8 , 25]





#Set Object
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)          #{25 , 10.8 , 'Hyd' , True , 3+4j , None}  in  any  order
print(type(a))    #<class 'set'>
print(len(a))     #6
#print(a[2])      #TypeError: 'set' object is not subscriptable, set  is  not  indexed
#print(a[1 : 4])  #TypeError: 'set' object is not subscriptable, set   can  not  be  sliced
#a[2] = 'Sec'     #TypeError: 'set' object does not support item assignment, there is no index for set
#print(a * 2)     #TypeError: unsupported operand type(s) for *: 'set' and 'int', set can't repeated duplicate elements
#print(a * a)     #TypeError: unsupported operand type(s) for *: 'set' and 'set'

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)           #{1 , 'Hyd' , False ,  ''}  in  any  order
print(len(a))      #4
print(type(a))     #<class 'set'>

#  set()  function demo  program
a = set('Rama rAo')                     #Converts  string  to  set
print(a)                                #{'R' , 'a' , 'm' , ' ' , 'r' , 'A' , 'o'}  in   any  order
print(len(a))                           #7
print(set([10 , 20 , 15 , 20]))         #Converts list  to  set  i.e. {20,10,15}  in  any  order
print(set((25 , 10.8 , 'Hyd' , 10.8)))  #Converts   tuple to  set  i.e.  {25,10.8,'Hyd'} in  any order
print(set(range(10 , 20 , 3)))          #Converts  range  object  to  set  i.e.  {10,13,16,19} in any  order
#print(set(25))                         #TypeError: 'int' object is not iterable
#print(set([25 , 10.8 , [] , 'Hyd']))  #TypeError: unhashable type: 'list', set cannot have a mutable sequences


# Find  outputs  (Home  work)
a =   [ ]       #Empty list
b =   ( )       #Empty  tuple
c =   { }       #Empty  dictionary
d =   set()     #Empty  set
print(type(a))  #<class 'list'>
print(type(b))  #<class 'tuple'>
print(type(c))  #<class 'dict'>
print(type(d))  #<class 'set'>
print(a)        #[]
print(b)        #()
print(c)        #{ }
print(d)        #set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()          #Empty  set
a . add(25)        #Inserts   25 into  empty  set
a . add(10.8)      #Inserts  10.8  any  where in  the  set
a . add('Hyd')     #Inserts  'Hyd'   any  where in  the  set
a . add(True)      #Inserts  True   any  where in  the  set
a . add(None)      #Inserts  None  any  where in  the  set
a . add('Hyd')     #Ignored :  set  already  contains  'Hyd'
a . add(1)         #Ignored :  set  already  contains   True
print(a)           #{25,10,8,'Hyd',True,None} in  any  order
print(len(a))      #5
a . remove(25)     #Removes 25 from  set
print(a)           #{10,8,'Hyd',True,None}  (Order  is  same as  line  11)
#a . append(100)   #AttributeError: 'set' object has no attribute 'append', No append() method in set
#a . add(set())    #TypeError: unhashable type: 'set', set can't have mutable
a . add(())        #Inserts  ()   any  where   in  set  'a'
#a . add([])       #TypeError: unhashable type: 'list'
print(a)           #{10.8 , 'Hyd' , True , None , ()}  in  any  order
#a . add({})       #TypeError: unhashable type: 'dict'

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)                                             #{'Hyd', 25, 10.8, True} in any order
print('Iterate  elements  of  set  with  for  loop')
for  x  in  a:
	print(x)                                         #   Hyd<next line> 25<nl>  10.8  <nl>  True <nl>


#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)           #(25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a)          #Unpacks tuple into elements i.e. 25 <sp> 10.8  <sp> Hyd  <sp> True <sp>  3+4j  <sp>  None  <sp>   Hyd <sp> 25
print(type(a))     #<class  'Tuple'>
print(len(a))      #8
print(a[2 : 5])    #Tuple  from  indexes  2 to 4  in steps  of  1  i.e ('Hyd',True,3+4j)
print(*a[2 : 5])   #Unpacks  tuple  from  indexes from 2 to 4  in  steps  of  1  i.e  Hyd  <sp>  True  <space>  3+4j
#a[2] = 'Sec'      #TypeError: 'tuple' object does not support item assignment,  it  is  immutable
#a . append('Sec') #AttributeError: 'tuple' object has no attribute 'append',  No  append()  method  in  tuple
#a . remove('Hyd') #AttributeError: 'tuple' object has no attribute 'remove',  No  remove()  method  in  tuple
b =  10 , 20 , 30  #Valid  :   ()  are  optional
print(b)           #(10,20,30)
print(b * 2)       #Repeats  tuple  twice  i.e.  (10, 20, 30, 10, 20, 30)
c = 40 , 50 , 60,  #Valid  and  last  comma  is  optional
print(c)           #(40,50,60)
print(type(c))     #<class 'tuple'>

# Find  outputs  (Home  work)
a = (25)       #Integer :  comma is  missing
b = 25,        #Tuple  due  to  comma
c = 25         #Integer :  comma is  missing
d = (25,)      #Tuple  due  to  comma
print(type(a)) #<class  'int'>
print(type(b)) #<class  'tuple'>
print(type(c)) #<class 'int'>
print(type(d)) #<class 'tuple'>
print(a * 4)   #25 * 4 = 100
print(b * 4)   #Repeats  tuple  4  times  i.e.  (25,25,25,25)
print(c * 4)   #25 * 4 = 100
print(d * 4)   #Repeats  tuple  4  times  i.e.  (25,25,25,25)

# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')         #Converts  string  to  tuple
print(a)                 #('H' , 'y' , 'd')
print(type(a))           #<class 'tuple'>
print(len(a))            #3
b = [10 , 20 , 15 , 18]  #List  due  to  []
print(tuple(b))          #Converts  list  to  tuple i.e.  (10,20,15,18)
print(tuple(range(5)))   #Converts  range  object  to  tuple i.e. (0,1,2,3,4)
#print(tuple(25))        #TypeError: 'int' object is not iterable, 25  is  not  a  sequence


# Find  outputs (Home  work)
a = ()          #Empty   tuple
print(type(a))  #<class 'tuple'>
print(a)        #()
print(len(a))   #0
b = tuple()     #Returns  an  empty  tuple
print(b)        #()
print(len(b))   #0

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)  #Ref  'a'  points   to  tuple  of  3  elements
print(a)            #(10,20,30)
print(id(a))        #Address of  tuple with  3  elements  (may  be  1000)
a = a * 2           #a = (10, 20, 30, 10, 20, 30)  --->Ref 'a' is modified to another tuple of 6 elements
print(a)            #(10 , 20 , 30 , 10 , 20 , 30)
print(id(a))        #Address of  tuple with  6  elements  (may  be  2000)
