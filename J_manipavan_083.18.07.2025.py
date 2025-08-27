#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)		#prints [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)		#print 25 10.8 'Hyd' True 3 + 4j None 'Hyd' 25
print(type(a))		#<class "list">
print(id(a))		#id of object a
print(len(a))		#length of a '8'
a[2] = 'Sec'		#'Hyd' changed to 'Sec'
print(a)		#25 10.8 Sec True 3 + 4j None Hyd 25
print(a[2 : 5])		#Hyd True 3 + 4j



#append()  and  remove()  methods  (Home  work)
a = [ ]	
print(a)		#prints empty list
a . append(25)		#25 append to list a
a . append(10.8)	#10.8 append to list a
a . append('Hyd')	#Hyd append to list a
a . append(True)	#True append to list a
print(a)		#[25 , 10.8 , 'Hyd' , True]
a . remove('Hyd')	#hyd will remove from list a
print(a)		#[25 , 10.8  , True]
a . remove('25')	#25 will be removed
print(a)		#[ 10.8 , True]



#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)		#[25 , 10.8 , 'Hyd']
print(id(a))		#address of object a
print(a * 3)		#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)		#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)		#[25 , 10.8 , 'Hyd']
print(a * 0)		#[]
print(a * -1)		#[]
print(a * 4.0)		#error due to float
a = a * 3		#a changed to[25 ,10.8,'Hyd',25 , 10.8 , 'Hyd',25 , 10.8,'Hyd']	
print(a)		#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a))		#address of object a
a = [25]		#a is now [25]
print(a * a)		#error a is not int





# list()  function  demo  program
a = list('Hyd')		#Convert sequence Hyd to list
print(a)		#['Hyd']
print(type(a))		#<class 'list'>
print(len(a))		#1
b = (10 , 20 , 15 , 18)	#b is Tuble 
print(list(b))		#[10,20, 15, 18]
print(list(range(5)))	#[0, 1, 2, 3, 4] 
print(list(25))		#[25]



# Find  outputs
a = [ ]		
print(type(a))	#<class 'list'>
print(a)	#[]
print(len(a))	#0
b = list()
print(b)	#[]	
print(len(b))	#0




 Slice  demo  program (Home  work)
#        0      1  2         3         4   5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7  -6        -5         - -3       -2        -1
print(list[2 : 7])# List  from  indexes  2  to  6  in  steps  of  1  i.e.  [ 3 + 4j , 'Hyd' , True , None , 10.8 ]

print(list[ : : ]) #List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'] 

print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])#[25, (3+4j), True, 10.8]
print(list[1 : : 2])#[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#[10.8, True, (3+4j), 25]
print(list[1 : 4])#[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])#[True, None, 10.8]
print(list[3 : -3])#['Hyd', True]
print(list[2 : -5])#[3+4j]
print(list[-1:-5]) #[]





list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]		#x='Hyd' y=True 
print('x : ' , x)		#x : Hyd
print('y : ' , y)		#y : True
for  x  in  list[2:7]:
	print(x)	#3+4j <next line> Hyd <next line> True <next line> None <next line> 10.8


#  Find  outputs  (Home  work)
#    0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))		#[10 , 20 , 30 , 40 , 50] address of object a
a[1 : 4] = [60 , 70] 		#replace a[1]=60 , a[2]=70 and a[3]=empty
print(a , id(a))		#[10, 60, 70,50] and new add of obj a
a[2: 4] = [100 , 200 ,  300]	
print(a , id(a))		#[10, 60,100,200,300] and new add of obj a







#  Find  outputs  (Home  work)
a =  [25] 
print(a[1])	#error list index out of range
print(a[1:])	#[]




# Find  outputs  (Home  work)
a = (25)    	#ref a point to obj int 25
b = 25,		##ref b point to obj tuple 25
c = 25		#ref c point to obj int 25
d = (25,)	#ref d point to obj tuple 25
print(type(a))	#<class "int">
print(type(b))	#<class "Tuple">
print(type(c))	#<class 'int'>
print(type(d))	#<class 'tuple'>
print(a * 4)	#100
print(b * 4)	#(25,25,25,25)
print(c * 4)	#100
print(d * 4)	#(25,25,25,25)






# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')	#ref a point to obj Tuple 'hyd'
print(a)		#('Hyd')
print(type(a))		#<class 'tuple'>
print(len(a))		#1
b = [10 , 20 , 15 , 18]	#ref a point to obj list
print(tuple(b))		#(10 , 20 , 15 , 18)
print(tuple(range(5)))	#error	
print(tuple(25))	#(25)





# Find  outputs (Home  work)
a = ()		#ref a point to obj Tuple 	
print(type(a))	<class 'tuple' 	>
print(a)	#()
print(len(a))	#0
b = tuple()	
print(b)	#()
print(len(b))	#0





# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)	#(10 , 20 , 30)
print(id(a))	#address of object a
a = a * 2	#a is change to object a*2(10 , 20 , 30,10 , 20 , 30)	
print(a)	#(10 , 20 , 30,10 , 20 , 30)
print(id(a)) 	#new address of object a



#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)	#{25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a))	#<class 'set'
print(len(a))	#6
print(a[2])	#error	set not have index
print(a[1 : 4])	#error  
a[2] = 'Sec'	#error 
print(a * 2)	#error  can't cantain dup
print(a * a)	#error




# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)		#{ 1, 'Hyd', False,''}
print(len(a))		#4
print(type(a))		#<class 'set'>




#  set()  function demo  program
a = set('Rama rAo')
print(a)	#{'R' 'a' 'm' ' ' 'r'}
print(len(a))	#5
print(set([10 , 20 , 15 , 20]))		#{0,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))	#{25,10.8,'Hyd'}
print(set(range(10 , 20 , 3))) #{10,13,16,19}
print(set(25))	#{25}
print(set([25 , 10.8 , [] , 'Hyd']))#{25,10.8, ,'hyd'}





# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #<class 'list'>
print(type(b)) #<class 'tuple'>
print(type(c)) #<class 'set'>
print(type(d))	#<class 'set'>
print(a)	#[]
print(b)	#()
print(c)	#{}
print(d)	#{}





# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()	#empty set created
a . add(25)	#25 is add to set a
a . add(10.8)	#10.8 is add to set a
a . add('Hyd')	#'Hyd' is add to set a
a . add(True)	#True is add to set a
a . add(None)	#None is add to set a
a . add('Hyd')	#'hyd' will not add already in set and dont throw any error
a . add(1)	#True is equal to  will not add already in set and dont throw any error
print(a)	#{25,10.8,'Hyd',True,None}
print(len(a)) 	#5
a . remove(25)	#25 will remove from set a
print(a)	#{10.8,'Hyd',True,None}
a . append(100)	#error set does have append
a . add(set())	#error nested set not alloewd
a . add(())	#error
a . add([]) 	#error
print(a)	#{10.8,'Hyd',True,None}
a . add({})	#error




#How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') #print(a)
print(How  to  print  set')
print('Iterate  thru  set  with  for  loop') #for i in a:
						print(i)


