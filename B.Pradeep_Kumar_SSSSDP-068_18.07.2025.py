1)#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)  #   [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)  #  25 10.8  Hyd  True  3+4j  None  Hyd  25
print(type(a)) #  Class List
print(id(a))  # Address Of ‘list’
print(len(a))  #  8
a[2] = 'Sec'
print(a)  #  25 10.8  Sec  True  3+4j  None  Hyd  25
print(a[2 : 5])  #  Sec  True  3+4j  


2# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # Empty String
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)  #  [25,10.8,’Hyd’,True]
a . remove('Hyd')
print(a)   #  [25,10.8 ,True]
a . remove('25')
print(a) # [10.8 ,True]



3)#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)  #   [25 , 10.8 , 'Hyd']
print(id(a))  # Address of list
print(a * 3)  #   [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2)  #  [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1)  # [25 , 10.8 , 'Hyd'}
print(a * 0)  # empty list
print(a * -1)  # Empty list
print(a * 4.0)  #  Error list is not multiply by float 
a = a * 3
print(a)  #       [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a))   #  address of list
a = [25]
print(a * a)   #  625


4) # list()  function  demo  program
a = list('Hyd')
print(a)   #  list('Hyd')
print(type(a))   # class ‘tuple’
print(len(a))   #   
b = (10 , 20 , 15 , 18)
print(list(b))  #  [10 , 20 , 15 , 18]
print(list(range(5)))  #  0 1 2 3 4
print(list(25))  #Error

5# Find  outputs
a = [ ]
print(type(a))  # class ‘list’
print(a)  # [empty]
print(len(a)) # 0
b = list()
print(b) #  [empty]
print(len(b)) # 0
6) # Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#     +    -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])  #  [3 + 4j , 'Hyd' , True , None]
print(list[ : : ])  #  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])  # List from -1 to -8 in steps of -1   [‘Hyd’ ,10.8 , None , True , ‘Hyd’ , 3+4j , 10.8 , 25 ]
print(list[ : : 2])  #  List from 0 to 8 in steps of 2 [  25 , 3+4j , True , 10.8]
print(list[1 : : 2])  # list from 1 to 8 in steps of 2  [10.8 , ‘Hyd’ , None , ‘Hyd’]
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])  #  list of -2 to -8 in steps of -2   [10.8 , True , 3+4j , 25]
print(list[1 : 4])  #  list[1:4:1]   [10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])  #  list[-4:-1:1]   [True , None , 10.8]
print(list[3 : -3])  #  list[3:-3:1]  ['Hyd' , True , None]
print(list[2 : -5])  #  list[2:-5:1]    [3 + 4j]
print(list[-1:-5])  #  list[-1:-5:1]    # empty set

7) #  Find  outputs  (Home  work)
#          0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)  #  x: Hyd
print('y : ' , y)  #y: True
for  x  in  list[2:7]:
	print(x)     #  3+4j  <Nextline> 'Hyd'  <Nextline> True  <Nextline>None <Nextline>10.8

8)#  Find  outputs  (Home  work)
#       0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))   #   [10 , 20 , 30 , 40 , 50] , Address of list object
a[1 : 4] = [60 , 70]  # Error
print(a , id(a))  #  10 , 20 , 30 , 40 , 50] , Address of list object
a[2: 4] = [100 , 200 ,  300]  
print(a , id(a))   #  [ 10 , 20 , 100 , 200 , 300] , Address of list object

9) #  Find  outputs  (Home  work)
a =  [25]
print(a[1])  #Error There is no a[2] value
print(a[1:])  ##Error There is only have a[0] 


10) # Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))  #  class ‘int’
print(type(b))  #  class ‘tuple’
print(type(c))  #  class int
print(type(d))  #  class tuple
print(a * 4)   #  100
print(b * 4)  #  (25,25,25,25)
print(c * 4)  #  100
print(d * 4)  #  (25,25,25,25)

11) # tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)   #  (‘H’,’y’,’d’)
print(type(a))  #  class ‘tuple’
print(len(a))   #   3
b = [10 , 20 , 15 , 18]
print(tuple(b))   #   (10 , 20 , 15 , 18)
print(tuple(range(5)))  #  (0,1,2,3,4)
print(tuple(25))   #   25


12) # Find  outputs (Home  work)
a = ()
print(type(a))   #   class ‘tuple’
print(a)   # ()
print(len(a))   # 0
b = tuple()
print(b)   #   ()
print(len(b))   #   0


13) # Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)    #  (10 , 20 , 30)
print(id(a))  #  address of tuple object
a = a * 2
print(a)   #   (10, 20, 30, 10, 20, 30)
print(id(a))   #   Address of Tuple Object


14) #  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}	
print(a)    #   {25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a))  #  Class “set’
print(len(a))    #   6
print(a[2])   #  Error due to Set not allowed indexes  becoz of values sequence may changable
print(a[1 : 4])    #  Error due to Set not allowed indexes  becoz of values sequence may changable
a[2] = 'Sec'   #  Error Due to Set not accepted the Modification
print(a * 2)   #   Error
print(a * a)   #  Error


15) # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,0}
print(a)  #   {1 , 'Hyd' , False , True , 0.0 , '' }
print(len(a))   #  5
print(type(a))   #   Class ‘Set’


16) #  set()  function demo  program
a = set('Rama rAo')
print(a)    #   {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a))    #    7
print(set([10 , 20 , 15 , 20]))   # {10, 15, 20}
print(set((25 , 10.8 , 'Hyd' , 10.8)))    #    # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))    # {10, 13, 16, 19}
print(set(25))   #Error
print(set([25 , 10.8 , [] , 'Hyd']))   #  Error




