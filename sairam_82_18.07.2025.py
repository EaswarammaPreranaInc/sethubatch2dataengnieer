#1)  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]   #  List  due  to  []
print(a)  #  [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]  
print(*a)  # Unpacks  list  into  elements  i.e.  25  <space>  10.8  <space>  Hyd  <space>  True <space> 3+4j  <space>  None <space>  Hyd  <space>  25
print(type(a))#  <class  'list'>
print(id(a)) #  Address  of   list 
print(len(a))  #  8
a[2] = 'Sec'  #  Element  at index  2  is  modified  to  'Sec'
print(a) #  [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]   
print(a[2 : 5])  #  List  from  indexes  2  to  4  in  steps  of   1  i.e.  ['Sec' , True ,  3+4j]

#2) # append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) #a
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[25, 10.8, 'Hyd', True]
a . remove('Hyd')
print(a) #[25, 10.8, True]
a . remove('25') #error
print(a)

#3) Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #address of list object
print(id(a)) #address of list is printed
print(a * 3) #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) #[25, 10.8, 'Hyd']
print(a * 0) #[] empty string
print(a * -1) #empty string
print(a * 4.0) #error the it should not float only int
a = a * 3 #[25 10.8 'Hyd' 25 10.8 'Hyd' 25 10.8 'Hyd']
print(a) #object code printed
print(id(a)) #address of list obj will be printed
a = [25]
print(a * a) # error

#4) list()  function  demo  program
a = list('Hyd') #a is assigned to list obj
print(a) #['H', 'y' 'd']
print(type(a)) #<class 'list'>
print(len(a)) #2
b = (10 , 20 , 15 , 18) #
print(list(b)) #[10, 20, 15, 18] 
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(25)) #error


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list
2) Is  list(non-sequence)  valid ?  --->   No  becoz  argument  should  be  sequence  only
3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []
4) Finally  list()  function  does  typecasting
'''


#5) Find  outputs
a = [ ] # a is reference is assigned to a list object
print(type(a)) #<class 'list'>
print(a) #id will be printed
print(len(a)) #0
b = list() 
print(b) #[]
print(len(b)) #0

#6) Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) #[3+4j, 'Hyd', True, None, 10,8, ]
print(list[ : : ]) #[25, 10.8, (3+4j), 'Hyd', None, 10.8, 'Hyd', ]
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #['Hyd', 10.8, none, 'Hyd', 3+4j, 10.8, 25]
print(list[ : : 2]) #[25, 3+4j, True, 10.8] 
print(list[1 : : 2]) #[10.8, 'Hyd', None, 'Hyd'] 
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) #[10.8, True, 3+4j, 25]
print(list[1 : 4]) #[10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) #[True, None, 10.8, ]
print(list[3 : -3]) #['Hyd', True]
print(list[2 : -5]) #[3+4j]
print(list[-1:-5]) #

#7)  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] # x is assigned to 'Hyd', y will be assigned to True
print('x : ' , x) #Hyd
print('y : ' , y) #True
for  x  in  list[2:7]: #3+4j <nextline> 'Hyd' <nextline> True <nextline> none <next> 10.8<next> 'Hyd'
	print(x)  #(3+4j)<nextline> 'Hyd' <nextline> True <nextline> none <next> 10.8


#8)  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50] # a is assigned to the list object
print(a , id(a)) #[10, 20, 30, 40, 50 and address wof list obj is printed
a[1 : 4] = [60 , 70]  #inlis [ 60, 70] is replaced at  elements  20 30 40 50
print(a , id(a)) # [10, 60, 70]
a[2: 4] = [100 , 200 ,  300] # elements replaced
print(a , id(a)) #[10,60, 100, 200, 300]

#9)  Find  outputs  (Home  work)
a =  [25] # a is assigned to the list object
print(a[1]) # err0r the list doesn't contain  1 index 
print(a[1:]) # error the list doesn't contain  1 index 



#10) Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) #<class 'int'>
print(type(b)) #<class 'tuple>
print(type(c)) #<class 'int'>
print(type(d)) #<class 'tuple'>
print(a * 4)   #100
print(b * 4)  #(25 25 25 25)
print(c * 4)  #100
print(d * 4)   #(25 25 25 25)

#11) tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') # a tuople object is refered to a
print(a) # (H, y, d)
print(type(a)) # <class <tuple'>
print(len(a)) # 2
b = [10 , 20 , 15 , 18] # b is assigned to the list object 
print(tuple(b)) # (10, 20, 15, 18)
print(tuple(range(5)))  #(0, 1, 2, 3, 4)
print(tuple(25))  #error due to index 25 is not present in the tuple
'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple
2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only
3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''

#12)Find  outputs (Home  work)
a = ()
print(type(a)) #<class 'tuple'>
print(a) #()
print(len(a)) #0
b = tuple() #()
print(b) #()
print(len(b)) #0

#13) Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) #(10, 20, 30)
print(id(a)) 
a = a * 2
print(a) #(10, 20, 30, 10, 20, 30)
print(id(a))

#14) set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{None, True, 'Hyd', 25, 10.8, (3+4j)}
print(type(a)) #<class 'set'>
print(len(a)) #6
print(a[2]) #Error
print(a[1 : 4]) #Error
a[2] = 'Sec' #Error
print(a*2)
print(a*a)

#15) Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{'Hyd', 1, False, ''}
print(len(a)) #4
print(type(a)) #<class 'set'>

#16) #  set()  function demo  program
a = set('Rama rAo')
print(a) #{'R', 'a', 'm ', 'a', 'r', 'A', 'o'}
print(len(a)) #7
print(set([10 , 20 , 15 , 20])) #{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{'Hyd', 25, 10.8}
print(set(range(10 , 20 , 3))) #{'Hyd', 25, 10.8}
print(set(25)) #Error
print(set([25 , 10.8 , [] , 'Hyd'])) #Error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set
'''

#17)
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #<class 'list'>
print(type(b)) #<class 'typle'>
print(type(c)) #<class 'dict'>
print(type(d)) #<class 'set'>
print(a) #[]
print(b) #()
print(c) #{}
print(d) #set()

#18) Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) #{None, True, 10.8, 'Hyd', 25}
print(len(a)) #5
a . remove(25) #{None, True, 10.8, 'Hyd'}
print(a) #{None, True, 10.8, 'Hyd'}
a . append(100)
a . add(set())
a . add(())
a . add([])
print(a) #{None, True, 10.8, 'Hyd'}
a.add({})

#19) 
a = {25, True, 'Hyd', 10.8}
print("Set with print function:") #Print the set directly using print()
print(a)
print("Iterate thru set with for loop:") #Print each element by iterating through the set with a loop
for element in a:
    print(element)
