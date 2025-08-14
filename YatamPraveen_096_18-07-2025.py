#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)    #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)    #25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a))    #<class 'list'>
print(id(a))     #returns the address of list object.
print(len(a))        #8
a[2] = 'Sec'
print(a)      #[25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])      #['Sec' , True , 3 + 4j]





# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)      #[]
a . append(25)     #list a becomes [25]
a . append(10.8)    #list a becomes [25, 10.8]
a . append('Hyd')   #list a becomes [25, 10.8, 'Hyd']
a . append(True)       #list a becomes [25, 10.8, 'Hyd', True]
print(a)        #[25, 10.8, 'Hyd', True]
a . remove('Hyd')    #list a becomes [25, 10.8, True]
print(a)
a . remove('25')    #returns error as list a doesn't contain string '25'
print(a)       #[25, 10.8, True]





#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)        #[25 , 10.8 , 'Hyd']
print(id(a))      #Returns the id of list object a( let 1000 be an example).
print(a * 3)    #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2)    #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1)       #[25 , 10.8 , 'Hyd']
print(a * 0)      #No output(maybe empty list)
print(a * -1)       #No output(maybe empty list)
print(a * 4.0)      #Returns error as list repetition does not occur with float values
a = a * 3
print(a)     #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a))    #Returns the id of list object a( not 1000 because a=a*3 creates a new object and assigns a to this new object. So we get address of this new object).
a = [25]
print(a * a)      #Returns an error as we can't repeat a list by list times





# list()  function  demo  program
a = list('Hyd')
print(a)              #['H', 'y', 'd']
print(type(a))     #<class 'list'>
print(len(a))        #3
b = (10 , 20 , 15 , 18)
print(list(b))      #[10, 20, 15, 18]
print(list(range(5)))    #[0, 1, 2, 3, 4]
print(list(25))         #Returns error as list(non sequence) is not valid.

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
print(type(a))   #<class 'list'>
print(a)            #[]
print(len(a))     #0
b = list()
print(b)            #[]
print(len(b))     #0





# Slice  demo  program (Home  work)
#        0      1       2         3         4       5      6       7
list = [25 ,   10.8 , 3 + 4j ,  'Hyd' ,   True ,  None , 10.8 , 'Hyd']
#       -8     -7       -6       -5        -4      -3      -2    -1
print(list[2 : 7])     #[3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])     #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])      #['Hyd', 10.8, None, True, 'Hyd', 3+4j, 10.8, 25]
print(list[ : : 2])       #[25 , 3 + 4j , True, 10.8 , 'Hyd']
print(list[1 : : 2])    #[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])    #[10.8, True, 3+4j, 25]
print(list[1 : 4])    #[10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])   #[True , None , 10.8]
print(list[3 : -3])     #['Hyd', True]
print(list[2 : -5])   #[3+4j]
print(list[-1:-5])     #[]





#  Find  outputs  (Home  work)
#        0     1     2       3      4      5     6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)      #x: Hyd
print('y : ' , y)      #y: True
for  x  in  list[2:7]:
	print(x)

#3+4j
  Hyd
  True
  None
  10.8





#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))     #[10 , 20 , 30 , 40 , 50] Address of list object
a[1 : 4] = [60 , 70]
print(a , id(a))        #[10, 60,  70, 50] Address of list object which is same as in previous output.
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))         #[10, 60, 100, 200, 300] Address of list object which is same as in previous output.





#  Find  outputs  (Home  work)
a =  [25]
print(a[1])      #Returns error as max index of a is 0
print(a[1:])     #[]





# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))   #<class 'int'>
print(type(b))   #<class 'tuple'>
print(type(c))   #<class 'int'>
print(type(d))   #<class 'tuple'>
print(a * 4)       #100
print(b * 4)       #(25, 25, 25, 25)
print(c * 4)       #100
print(d * 4)       #(25, 25, 25, 25)





# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)            #('H', 'y', 'd')
print(type(a))  #<class 'tuple'>
print(len(a))     #3
b = [10 , 20 , 15 , 18]
print(tuple(b))    #(10 , 20 , 15 , 18)
print(tuple(range(5)))  #(0, 1, 2, 3, 4)
print(tuple(25))     #Returns error as non sequences can't be typecasted to tuple.

'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''





# Find  outputs (Home  work)
a = ()
print(type(a))   #<class 'tuple'>
print(a)            #()
print(len(a))     #0
b = tuple()
print(b)            #()
print(len(b))     #0





# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)     #(10, 20, 30)
print(id(a))   #Returns address of tuple object.
a = a * 2
print(a)      #(10, 20, 30, 10, 20, 30)
print(id(a))   #Returns address of new tuple object which is repetition of previous tuple.





#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)   #{25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))   #<class 'set'>
print(len(a))     #6
print(a[2])       # Returns error as indexing is not possible in sets.
print(a[1 : 4])       # Returns error as indexing is not possible in sets.
a[2] = 'Sec'     #Causes error as there is no concept of indexing in set.
print(a * 2)    #Returns error as sets can't be repeted.
print(a * a)    #Returns error as repetition is supposed to be by an integer.





# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)       #{1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))      #8
print(type(a))    #<class 'set'>





#  set()  function demo  program
a = set('Rama rAo')
print(a)        #{R, a, m, ' ' , r, A, o}
print(len(a))      #7
print(set([10 , 20 , 15 , 20]))   #{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))     #{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))  #{10, 13, 16, 19}
print(set(25))     #Returns error as 25 is non sequence.
print(set([25 , 10.8 , [] , 'Hyd']))    #Returns error as set can't contain list.

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
print(type(a))   #<class 'list'>
print(type(b))   #<class 'tuple'>
print(type(c))   #<class 'dict'>
print(type(d))   #<class 'set'>
print(a)             #[]
print(b)             #()
print(c)             #{}
print(d)             #set()





# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)          #Adds 25 to empty set a.
a . add(10.8)        #Adds 10.8 at end of set a.
a . add('Hyd')       #Adds 'Hyd' at end of set a.
a . add(True)        #Adds True at end of set a.
a . add(None)       #Adds None at end of set a.
a . add('Hyd')        #since Hyd is already present, this is ignored.
a . add(1)              #Adds 1 at  end of set a.
print(a)                 #{25, 10.8, 'Hyd, True, None, 1}
print(len(a))          #6
a . remove(25)      #Removes 25
print(a)                  #{10.8, 'Hyd, True, None, 1}
a . append(100)     #Set doesn't have an append method.
a . add(set())          #Returns error as nested set is not possible.
a . add(())               #Adds empty tuple to set
a . add([])              #Returns error as set can't have list as element.
print(a)                  #{10.8, 'Hyd, True, None, 1, 100}
a . add({})              #Returns error as set can't have dictionary as element.





# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')              #print(a)
print(How  to  print  set)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop

#for i in a:
      print(i)