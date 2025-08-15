#Home Work 1
#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) #25 10.8 Hyd True 3+4j None Hyd 25 , as separator is not mentioned the default space separator will be applied
print(type(a)) # <class list>
print(id(a)) #address of the list object, say 1000
print(len(a)) #8
a[2] = 'Sec' #yes modification is allowed
print(a) # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #elements of list 'a' from index 2 to 4 in steps of 1 which is ['Sec' , True , 3 + 4j ]

#Home Work-2
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) #[]
a . append(25) #[25]
a . append(10.8) #[25, 10.8]
a . append('Hyd') #[25, 10.8, 'Hyd']
a . append(True) #[25, 10.8, 'Hyd', True]
print(a) #[25, 10.8, 'Hyd', True]
a . remove('Hyd')
print(a)  #[25, 10.8, True]
a . remove('25')  
print(a) #[10.8, True]

#Home Work-3
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #[25 , 10.8 , 'Hyd']
print(id(a)) #address of the list object, say 3000
print(a * 3) #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd]
print(a * 1) #[25 , 10.8 , 'Hyd']
print(a * 0) #[]
print(a * -1) #[]
print(a * 4.0) #error, for repeating we should use int values only
a = a * 3 
print(a)  #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) #address of the newly created object, say 3030
a = [25] 
print(a * a)#error: doind repetition like this is not possible

#Home Work-4
# list()  function  demo  program
a = list('Hyd')
print(a) #['Hyd']
print(type(a))# <class 'list'>
print(len(a))#1
b = (10 , 20 , 15 , 18)
print(list(b))#[10, 20, 15, 18]
print(list(range(5))) #[0,1,2,3,4]

print(list(25))#[25]

'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->   No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''

#Home Work -5
# Find  outputs
a = [ ]
print(type(a))#<class 'list'>
print(a)#[]
print(len(a))#0
b = list()
print(b)#[]
print(len(b))#0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # from 2 to 6 in steps of 1 , which is [ 3 + 4j , 'Hyd' , True , None , 10.8 ]
print(list[ : : ])#from 0 to 7 in steps of 1 , which is [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #from -1 to -8 in steps of -1, which is ['Hyd', 10.8, None, True, 'Hyd', 3+4j, 10.8, 25]
print(list[ : : 2]) # from 0 to 7 in steps of 2, which is [25, 3+4j, True, 10.8]
print(list[1 : : 2]) # from 1 to 7 in steps of 2, which is [10.8, Hyd, None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) #from -2 to -8 in steps of -2 which is [10.8, True, 3+4j, 25]
print(list[1 : 4])#from 1 to 3 in steps of 1, which is [10.8, 3+4j, 'Hyd']
print(list[-4 : -1]) # from -4 to -2 in steps of 1, which is [ True , None , 10.8 ]

print(list[3 : -3]) #from 3 to -4 in steps of 1 , which is []
print(list[2 : -5])# from 2 to -6 in steps of 1 which is []
print(list[-1:-5])#from -1 to -6 in steps of 1 which is []

#Home Work -6
#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]# 3 to 4 in steps of 1
print('x : ' , x) # x:Hyd
print('y : ' , y) #y:True
for  x  in  list[2:7]:
	print(x) # from 2 to 6 in steps of 1 which is 
3+4j
Hyd
True
None
10.8

#Home Work -7
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10 , 20 , 30 , 40 , 50] 7000 (say the address of the list object is 7000)
a[1 : 4] = [60 , 70]  
print(a , id(a)) #[10 , 60, 70 , 50]
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10 , 20 , 100, 200, 300, 50] 7000 (the address does not change because list can be modified

#Home Work-8
#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) #error, the index available is only 0
print(a[1:]) #[] from 1 to 0 which is empty list

#Home Work -9
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) #<class int>
print(type(b)) #<class 'tuple'>
print(type(c)) #<class int>
print(type(d)) #<class 'tuple'>
print(a * 4) #100
print(b * 4) #(25, 25, 25, 25)
print(c * 4) #100
print(d * 4) #(25, 25, 25, 25)

#Home Work -10
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) #('Hyd')
print(type(a)) #<class 'tuple'>
print(len(a)) #1
b = [10 , 20 , 15 , 18]
print(tuple(b)) #(10, 20, 15, 18)
print(tuple(range(5))) #(0, 1, 2, 3, 4)
print(tuple(25)) #error int object cannot be converted to tuple


'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''

#Home Work-11
# Find  outputs (Home  work)
a = ()
print(type(a)) #<class 'tuple'>
print(a) #()
print(len(a)) #0
b = tuple()
print(b) #()
print(len(b)) #0

#Home Work -12
# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)#(10, 20, 30)
print(id(a)) #address of the tuple object say 1200
a = a * 2 
print(a) #(10, 20, 30, 10, 20, 30)
print(id(a)) #address does changes to say 1222, as tuple is immutable a new object will be created and say the address of the new object is 1222

#Home Work -13
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a)) # <class 'set'>
print(len(a)) #6
print(a[2]) #error: set elements are not indexed
print(a[1 : 4])#error: set elements are not indexed so slicing is not possible
a[2] = 'Sec'#error: set elements are not indexed
print(a * 2)#error: repetition is not allowed because set does not allow duplicates
print(a * a)#error

#Home Work-14
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))#8
print(type(a)) #<class 'set'>

#Home Work 15
#  set()  function demo  program
a = set('Rama rAo')
print(a) #{Rama rAo}
print(len(a))#1
print(set([10 , 20 , 15 , 20]))#{10, 20, 15} (can be any order)
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # 10 to 19 in steps of 3 which are 10, 13, 16, 19 so {10, 13, 16, 19}
print(set(25)) #error
print(set([25 , 10.8 , [] , 'Hyd']))#set cannot have mutable elements as its elements


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set
'''

#Home Work 16
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))# <class 'list'>
print(type(b)) #<class 'tuple'>
print(type(c)) #<class 'set'>
print(type(d)) #<class 'set'>
print(a)#[]
print(b)#()
print(c)#{}
print(d)#{}

#Home Work 17
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
print(a) #{25, 10.8, 'Hyd', True, None}
print(len(a)) #5
a . remove(25)
print(a) #{10.8, 'Hyd', True, None}
a . append(100)
a . add(set()) #error, set cannot have mutable elements 
a . add(())
a . add([]) #error, set cannot have mutable elements 
print(a) #{10.8, 'Hyd', True, None, 100, (), };
a . add({})##error, set cannot have mutable elements 

#Home Work 18
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print(*a)

print(How  to  print  set)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
for x in a:
    print(x)