#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)# [ [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]]
print(*a)# [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(type(a)) #List class
print(id(a)) address of list object 
print(len(a))8
a[2] = 'Sec'
print(a)# [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])#[Sec' , True , 3 + 4j , None]
 # append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)#empty list
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)[25,10.8,'hyd','True']
a . remove('Hyd')
print(a)#[25,10.8,'True']
a . remove('25')
print(a)#[10.8,'True']
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)#[25 , 10.8 , 'Hyd']
print(id(a))#addresa of list object
print(a * 3)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)#[25 , 10.8 , 'Hyd']
print(a * 0)#error
print(a * -1)#error
print(a * 4.0)#error
a = a * 3
print(a)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))address of list class
a = [25]
print(a * a)#error

# list()  function  demo  program
a = list('Hyd')
print(a)#[Hyd]
print(type(a))#list class
print(len(a))#1
b = (10 , 20 , 15 , 18)
print(list(b))#[10 , 20 , 15 , 18]
print(list(range(5)))#[0 1 2 3 4]
print(list(25))#[25]
  
# Find  outputs
a = [ ]
print(type(a))#list class
print(a)#empty list
print(len(a))#0
b = list()
print(b)#empty list
print(len(b))#0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])[3 + 4j , 'Hyd' , True , None , 10.8 ]
print(list[ : : ])#[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#this prints reverse of the string
print(list[ : : 2])#[25, (3+4j), True, 10.8]
print(list[1 : : 2])#[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#[10.8, True, 3+4j, 25]
print(list[1 : 4])#[10.8, 3+4j, 'Hyd']
print(list[-4 : -1])#[True, None, 10.8]
print(list[3 : -3])#['Hyd', True]
print(list[2 : -5])#[ ]
print(list[-1:-5])#error


#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)#['Hyd' ]
print('y : ' , y)#[True]
for  x  in  list[2:7]:
	print(x)#[3+4j , 'Hyd' , True , None , 10.8 ]
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #([10 , 20 , 30 , 40 , 50], address of list object)
a[1 : 4] = [60 , 70]
print(a , id(a))#[60 , 70],address of list object
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#[300]
#  Find  outputs  (Home  work)
a =  [25]
print(a[1])#error
print(a[1:])#error
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#tuple class
print(type(b))#tuple class
print(type(c))#int class
print(type(d))#tuple class
print(a * 4)#error
print(b * 4)#25252525
print(c * 4)#100
print(d * 4)#25252525



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)#('Hyd')
print(type(a))#address of tuple object
print(len(a))#1
b = [10 , 20 , 15 , 18]
print(tuple(b))#(10 , 20 , 15 , 18)
print(tuple(range(5)))#(0 1 2 3 4)
print(tuple(25))#(25)

# Find  outputs (Home  work)
a = ()
print(type(a))#tuple class
print(a)#empty tuple
print(len(a))#0
b = tuple()
print(b)#()
print(len(b))0
 # Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)#(10,20,30)
print(id(a))address of tuple class
a = a * 2
print(a)#(10,20,30)(10,20,30)
print(id(a))#new address of tuple

#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))#set class
print(len(a))8
print(a[2])#cannot identify because it is not stored in order
print(a[1 : 4])#error
a[2] = 'Sec'#cannot modify
print(a * 2)#no repetition 
print(a * a)#no repetition 
 # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))#8
print(type(a))#set class

#  set()  function demo  program
a = set('Rama rAo')
print(a)#{'Rama rAo'}
print(len(a))#1
print(set([10 , 20 , 15 , 20]))#error no list in a set
print(set((25 , 10.8 , 'Hyd' , 10.8)))#error no set in a set
print(set(range(10 , 20 , 3))){10,13,16,19}
print(set(25)){25}
print(set([25 , 10.8 , [] , 'Hyd'])#error no list in set

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#list class
print(type(b))#tuple class
print(type(c))#set class
print(type(d))#empty set
print(a)#empty list
print(b)#empty set
print(c)#empty set
print(d)#()


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
print(a)#{25,10.8,'Hyd','True','None',1}
print(len(a))6
a . remove(25)
print(a)#{10.8,'Hyd','True','None',1}
a .append(100)#{10.8,'Hyd','True','None',1,100}
a . add(set())
a . add(())
a . add([])
print(a)#error
a . add({})#error

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(How  to  print  set)#print(a)
print('Iterate  thru  set  with  for  loop')#
For i in a:
      Print(a[i])
How  to  iterate  thru  set  with  for  loop