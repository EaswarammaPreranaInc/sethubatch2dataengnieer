#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)#[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)#unpacks list into elements i,e 25<spcae>10.8<spcae>'Hyd'<spcae>True<spcae>3 + 4j<spcae>None<spcae>'Hyd'<spcae>25
print(type(a))#<class 'list'>
print(id(a))#address of the object
print(len(a))#8
a[2] = 'Sec'#element at index 2of list 'a' is modified to 'sec'
print(a)#[25 , 10.8 , 'sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])#a[2:5:1] i.e ['Sec', True, (3+4j)]
print()#nothing
# append()  and  remove()  methods  (Home  work)
a = [ ]#emptylist 
print(a) #[]
a . append(25) #26 is append to empty list
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)#[25, 10.8,'Hyd' True]
a . remove('Hyd')#'Hyd' removed from list 'a'
print(a)
#a . remove('25')#error
print(a)#[25, 10.8, True]
print()#nothing
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)#[25, 10.8, True]
print(id(a))# address of the object
print(a * 3)#list repeats three times i.e [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)#[25, 10.8, 'Hyd']
print(a * 0)#[]
print(a * -1)#[]
#print(a * 4.0)#error
a = a * 3#Ref 'a' is modifid to list of '9'elements 
print(id(a)) #address of the object
a = [25]
#print(a * a)#error
print()
# list()  function  demo  program
a = list('Hyd')#converts string to list
print(a)#['H','y','d']
print(type(a))# <class 'list'>
print(len(a))#3
b = (10 , 20 , 15 , 18)
print(list(b))#converts tuple to list i.e [10, 20, 15, 18]
print(list(range(5)))[0,1,2,3,4]
#print(list(25))#error
print()
# Find  outputs
a = [ ]
print(type(a))#<'class' 'list'>
print(a)#[]
print(len(a))#0
b = list()
print(b)#[]
print(len(b))#0
print()#nothing
# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])#[2:7:1] i.e[(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])#[0:8:1]i.e[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#[-1:-9:-1] i.e['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])#[0:8:2]i.e [25, (3+4j), True, 10.8]
print(list[1 : : 2])#[1:8:2]i.e ['Hyd', None, 'Hyd', 10.8]
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#[-2:-9:-2] i.e [10.8, True, (3+4j), 25]
print(list[1 : 4])#[1:4:1] i.e [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) #[-4:-1:-1] i.e [True, None, 10.8]
print()#nothing
#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) #x:Hyd
print('y : ' , y) #y:True
for  x  in  list[2:7]:
	print(x)#3+4j<nextline>True<nextline>None<nextline>10.8 
print()
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#[10 , 20 , 30 , 40 , 50], address of the object
a[1 : 4] = [60 , 70]
print(a , id(a))##[10 , 60 , 70 , 50], address of the object
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#[10, 60, 100, 200, 300] address of the object
print()#nothing
#  Find  outputs  (Home  work)
a =  [25]
#print(a[1])#error index '1' does not exist
print(a[1:]) #list without first element i.e[]
print()
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#<class 'int'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'int'>
print(type(d))#<class 'tuple'>
print(a * 4)#100
print(b * 4)#(25,25,25,25)
print(c * 4)#100
print(d * 4)#(25,25,25,25)
print()
# Find  outputs (Home  work)
a = ()
print(type(a))#<class 'tuple'>
print(a)#(#0)
print(len(a))
b = tuple()
print(b)#(#0)
print(len(b))
print()#nthing
# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)#(10 , 20 , 30)
print(id(a))#address of the object
a = a * 2
print(a)#(10, 20, 30, 10, 20, 30)
print(id(a))#address of the object
print()
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))#<class 'set'>
print(len(a))#6
#print(a[2])#error
#print(a[1 : 4])#error
#a[2] = 'Sec'#error
#print(a * 2)#error
#print(a * a)#error
print()
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{False, 1, 'Hyd', ''}
print(len(a))#4
print(type(a))#<class 'set'>
print()
#  set()  function demo  program
a = set('Rama rAo')
print(a)#{' ', 'R', 'a', 'o', 'r', 'm', 'A'}
print(len(a))#7
print(set([10 , 20 , 15 , 20]))#{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))#{16, 10, 19, 13}
#print(set(25))#error
#print(set([25 , 10.8 , [] , 'Hyd']))#error
print()
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#<class 'list'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'dict'>
print(type(d))#<class 'set'>
print(a)#[]
print(b)#()
print(c)#{}
print(d)#Set()
print()
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
print(a)
print(len(a))
a . remove(25)
print(a)
#a . append(100)#error
#a . add(set())#error
a . add(())
#a . add([])#error
print(a)
#a . add({})#error
print()
