#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a)) # <class 'list'>
print(id(a)) Address
print(len(a))#8
a[2] = 'Sec' #Replace 'Hyd' with 'Sec'
print(a) [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #['Sec' , True , 3 + 4j]
----------------------------------------------------------------
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) #Empty list
a . append(25) # 25 is inserted in list 'a'.
a . append(10.8)# 10.8 is inserted at last.
a . append('Hyd')# 'Hyd' is inserted at last.
a . append(True))# True is inserted at last.
print(a)# [25 , 10.8 , 'Hyd' , True]
a . remove('Hyd') # 'Hyd' is removed from the list.
print(a)#[25 , 10.8 ,True]
a . remove('25') #Error
print(a) #[25 , 10.8 ,True]
----------------------------------------------------------------
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #[25 , 10.8 , 'Hyd']
print(id(a))#address of a
print(a * 3) #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)#[25 , 10.8 , 'Hyd']
print(a * 0) #[]
print(a * -1)#[]
print(a * 4.0)#Error
a = a * 3 # Elements of list is repeated 3 times in a single list
print(a) #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a)) Address of newly created list
a = [25] #only 'a' have 25 in the list
print(a * a) #Error
----------------------------------------------------------------
# list()  function  demo  program
a = list('Hyd') # coverts string obj to list(Type-casting)
print(a)#['H','y','d']
print(type(a)) <class 'list'>
print(len(a)) #3
b = (10 , 20 , 15 , 18) 
print(list(b))# Type-casting from tuple to list #[10,20,15,18]
print(list(range(5))) #[0,1,2,3,4]
print(list(25))#[25]


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->   No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
----------------------------------------------------------------
# Find  outputs
a = [ ] 
print(type(a)) # <class 'list'>
print(a) #[]
print(len(a)) #0
b = list() #[]
print(b)#[]
print(len(b))#0
----------------------------------------------------------------

# Slice  demo  program 
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])#prints list elements from index 2 to 6 into new list:[3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])#prints the whole list as it is..as there is no specification in slicing:[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#prints the reverse order of the elements of the list.['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25] 
print(list[ : : 2])#prints the elements list from 0 to end in steps of 2:[10.8,'Hyd',True,10.8]
print(list[1 : : 2])#prints the elements of list from 1 to end in steps of 2:[10.8,'Hyd',None,'Hyd']
print(list[ : : -2]) # prints List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#[10.8, True, (3+4j), 25]:prints the indexes from -2 to -8 in the steps of 2.
print(list[1 : 4])#prints the list from indexes 1 to 3:[10.8,3+4j,'Hyd']
print(list[-4 : -1])#prints the elemets from -4 to -2 in steps of -1:[True, None, 10.8]
print(list[3 : -3])#['Hyd' , True]
print(list[2 : -5])#[3 + 4j , 'Hyd']
print(list[-1:-5])#prints empty list because it has  start > stop
#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 ,   10.8 ,  3+4j ,    'Hyd' ,    True ,   None ,    10.8 ,   'Hyd']
x ,  y = list[3 : 5]#appends elements of list from index 3 to 4 to x = 'Hyd',y=True
print('x : ' , x)#prints x : 'Hyd' 
print('y : ' , y)#prints y : True 
for  x  in  list[2:7]:
	print(x)#prints elements of list in range of 2 to 6 in steps of 1:[2,3,4,5,6]
--------------------------------------------------------------------------------------------
#  Find  outputs 
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#prints [10 , 20 , 30 , 40 , 50]<space>address of the list.
a[1 : 4] = [60 , 70]
print(a , id(a))#removes the indexes 1,2,3 and inserts 60 and 70 and the remaining elements..[10,60,70,50] 
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#removes 20,30 elements and replaces 100,200,300 ../output:[10,20,100,200,300]
------------------------------------------------------------------------------------------------------------
#  Find  outputs  
a =  [25]
print(a[1])#gives error bcoz there is no index 1
print(a[1:])#gives empty list

--------------------------------------------------------------------------------------------
# Find  outputs 
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#class<int>
print(type(b))#class<tuple>
print(type(c))#class<int>
print(type(d))#class<tuple>
print(a * 4)#100
print(b * 4)#(25,25,25,25)
print(c * 4)#100
print(d * 4)#(25,25,25,25)
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)#prints ('Hyd')
print(type(a))#class<tuple>
print(len(a))#1
b = [10 , 20 , 15 , 18]
print(tuple(b))#prints [10 , 20 , 15 , 18]
print(tuple(range(5)))#prints 0 to 4 in steps of 1:(0,1,2,3,4)
print(tuple(25))#prints 0 to 24 in steps of 1:(0,1,2----------24)

--------------------------------------------------------------------------------------------
# Find  outputs 
a = ()
print(type(a))#prints class<tuple>
print(a)#prints empty tuple
print(len(a))#prints 1
b = tuple()
print(b)#prints tuple method() is printed
print(len(b))#prints 0
--------------------------------------------------------------------------------------------
# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)#(10,20,30)
print(id(a)) #Address of a (2000)
a = a * 2 # repeated 2 times
print(a) # (10,20,30,10,20,30)
print(id(a)) # Different Address
--------------------------------------------------------------------------------------------
#  set  object  demo  program  
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#prints {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))#class <set>
print(len(a))#8
print(a[2])#error because indexing is not possible in set
print(a[1 : 4])#error because when there is no indexing slicing is not possible
a[2] = 'Sec'#no indexing so throws error
print(a * 2)#error because set doesnot allow duplicates
print(a * a)#error because nested set is not permitted and set accepts only immutable objects but set is mutable
-----------------------------------------------------------------------------------------------------------------
# Tricky  program
# Find  outputs 
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#prints set a:{1 , 'Hyd' , '' , 0}
print(len(a))#prints 4
print(type(a))#class <set>
#  set()  function demo  program
a = set('Rama rAo')
print(a)#prints {'R','a','m','r','A','o'}
print(len(a))# 6
print(set([10 , 20 , 15 , 20]))#output : {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))#{10,13,16,19}
print(set(25))#{0,1,2,3,------24}
print(set([25 , 10.8 , [] , 'Hyd']))#error because list is mutable and set supports immutable objects to enter into it.
------------------------------------------------------------------------------------------------------------------------
# Find  outputs  

a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#class<list>
print(type(b))#class<tuple>
print(type(c))#class<set>
print(type(d))#class<set>
print(a)#empty list is printed
print(b)#empty tuple is printed
print(c)#empty set is printed
print(d)#empty set method() is printed

# Tricky  program
# add()  and  remove()  methods 
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)#prints {25,10.8,'Hyd',True,None}
print(len(a))# 5
a . remove(25)
print(a)#{10.8,'Hyd',True,None}
a . append(100)#error because set method doesnot have append method instead add() is used.
a . add(set())
a . add(())
a . add([])
print(a)#error because set doesnot allow mutable objects like list and set 
a . add({})#error because set doesnot allow mutable objects like list and set.