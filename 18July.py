1.
#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)   # [25 , 10.8 , 'Hyd' , True , (3 + 4j) , None , 'Hyd' , 25]
print(*a)   #25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))  #<class 'list'>
print(id(a))  #address of list
print(len(a))  #8
a[2] = 'Sec'
print(a)  #[25 , 10.8 , 'Sec' , True , (3 + 4j) , None , 'Hyd' , 25]
print(a[2 : 5])   #['Sec' , True , (3 + 4j)]


2.
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)   #[]
a . append(25)   
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)   #[25, 10.8 'Hyd', True]
a . remove('Hyd')
print(a)   #[25, 10.8, True]
a . remove('25')  #we get error as there is no string '25' in a
print(a)   #[25, 10.8, True]



3.
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)   #25 , 10.8 , 'Hyd'
print(id(a))   #address of list a
print(a * 3)   #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)   #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)   #[25, 10.8, 'Hyd']
print(a * 0)   #empty
print(a * -1)    #empty
print(a * 4.0)    #error as multiplier must be int only
a = a * 3   
print(a)   #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))   #address of updated list
a = [25]   
print(a * a)  #error, right operand must be an int.


4.

# list()  function  demo  program
a = list('Hyd')
print(a)   #['H', 'y', 'd']
print(type(a))   <class 'list>
print(len(a))  #3
b = (10 , 20 , 15 , 18)
print(list(b))   #[10,20,15,18]
print(list(range(5)))  #[0,1,2,3,4]
print(list(25))   #error, list cannot be done for int



5.
# Find  outputs
a = [ ]
print(type(a))   #<class 'list'>
print(a)   #empty list []
print(len(a))   #0
b = list()   
print(b)  #[]
print(len(b))    #0




6.

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])   #[3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])   #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])   #['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #[25, (3+4j), True, 10.8]  
print(list[1 : : 2])    #[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])    #[10.8,  True, (3+4j), 25 ]
print(list[1 : 4])    #[10.8, 3+4j, 'Hyd']
print(list[-4 : -1])    #[True, None, 10.8]
print(list[3 : -3])   #['Hyd', True]
print(list[2 : -5])    #[]
print(list[-1:-5])    #[]



7.

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)   #x: 'Hyd'
print('y : ' , y)   #y: True
for  x  in  list[2:7]:
	print(x)   #(3+4j)<nxt line>'Hyd'<nxt line>True<nxt line>None<nxt line>10.8



8.
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))    # [10 , 20 , 30 , 40 , 50] address of list
a[1 : 4] = [60 , 70]
print(a , id(a))   #[10,60,70,50]  same address
a[2: 4] = [100 , 200 ,  300]    
print(a , id(a))   #[10,60,100,200,300]  same address



9.

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) #[]
print(a[1:])  #error


10.
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))    #<class 'int'>
print(type(b))    #<class 'tuple'>
print(type(c))    #<class 'int'>
print(type(d))    #<class 'tuple'>
print(a * 4)    #25*4=100
print(b * 4)    #(25,25,25,25)
print(c * 4)    #25*4=100
print(d * 4)    #(25,25,25,25)


11.
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)  #('H', 'y', 'd')
print(type(a))   #<class 'tuple'>
print(len(a))  #3
b = [10 , 20 , 15 , 18]
print(tuple(b))   #(10, 20, 15, 18)
print(tuple(range(5)))  #(0,1,2,3,4)
print(tuple(25))    #error

12.

# Find  outputs (Home  work)
a = ()
print(type(a))   #<class 'tuple'>
print(a)  #()
print(len(a))   #0
b = tuple()  #
print(b)    #()
print(len(b))    #0


13.
# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)  #(10,20,30)
print(id(a))  #address of tuple a
a = a * 2   
print(a)  #(10,20,30,40,50,60)
print(id(a))   #address of new tuple with 6 elements


14.

#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)   #{15, 10.8, 'Hyd', True, 3+4j, None}
print(type(a))  #<class 'set'>
print(len(a))   #6
print(a[2])  #error, there are no indexes in set
print(a[1 : 4])     #error, slicing is not possible because they are unordered
a[2] = 'Sec' #error
print(a * 2)   #sets cannot be repeated
print(a * a)   #set*set is not possible



15.

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)   #{1, 'Hyd', False, ''} in any order
print(len(a))  #4
print(type(a))   #<class 'set'>


16.
#  set()  function demo  program
a = set('Rama rAo')
print(a)  #{'R', 'a', 'm', ' ', 'r', 'A', 'o'}  in any order
print(len(a))   #7
print(set([10 , 20 , 15 , 20]))   #{10, 20, 15} in any order
print(set((25 , 10.8 , 'Hyd' , 10.8)))   #{25, Hyd, 10.8}  in any order
print(set(range(10 , 20 , 3)))   #{10,13,16,19} in any order
print(set(25))  #error, set of sequence is possible but 25 in int which is non sequence
print(set([25 , 10.8 , [] , 'Hyd']))  #error

17.
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))   #<class 'list'>
print(type(b))   #<class 'tuple'>
print(type(c))   #<class 'dict'>
print(type(d))   #<class 'set'>
print(a) #[ ]
print(b)  #( )
print(c)  #{}
print(d)  #set()


18.
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
print(a)  #{25, 10.8, 'Hyd', True, None} in any order
print(len(a)) #5
a . remove(25)  
print(a)  #{10.8, 'Hyd', True, None} in any order
a . append(100)   #error
a . add(set())   #error
a . add(())    #error
a . add([])    #error
print(a)   #{10.8, 'Hyd', True, None} in any order
a . add({}) #error

19.
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)  #{25, True, 'Hyd', 10.8} in any order
print(How  to  print  set)
print('Iterate  thru  set  with  for  loop')
for x in a:
	print(a)   #25
		   #True
		   #Hyd
		   #10.8  in anny order	 		
How  to  iterate  thru  set  with  for  loop
