#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)		#[25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)		# 25 10.8 'Hyd' True (3+4j) None 'Hyd' 25
print(type(a))		# class list
print(id(a))		# prints address
print(len(a))		#8
a[2] = 'Sec'		
print(a)		#25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25
print(a[2 : 5])


# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)
a . append(25)		
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)		#[25 , 10.8 , 'Hyd' , True]
a . remove('Hyd')	
print(a)		#[25 , 10.8 , True]
a . remove('25')
print(a)		#error string 25 is not in list 


#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)		# [25 , 10.8 , 'Hyd']
print(id(a))		#prints address of list object
print(a * 3)		#[25, 10.8, True, 25, 10.8, True, 25, 10.8, True]
print(a * 2)		#[25, 10.8, True, 25, 10.8, True]
print(a * 1)		#[25, 10.8, True]
print(a * 0)		#[]
print(a * -1)		[]
print(a * 4.0)		#error because float is given
a = a * 3
print(a)		#[25, 10.8, True, 25, 10.8, True, 25, 10.8, True]
print(id(a))		#prints different address of list object
a = [25]
print(a * a)		#error cannot multiply sequence type with non-int  




# list()  function  demo  program
a = list('Hyd')
print(a)		#['H', 'y' ,'d']
print(type(a))		#class list
print(len(a))		#3
b = (10 , 20 , 15 , 18)
print(list(b))		#[10, 20, 15, 18]
print(list(range(5)))   #[0,1,2,3,4]
print(list(25))         #error




# Find  outputs
a = [ ]
print(type(a))  	#class list
print(a)		#[]
print(len(a))		#0
b = list()
print(b)		#[]
print(len(b))		#0




# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) 	#[(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])	#[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])	#['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])	#[25, (3+4j), True, 10.8]
print(list[1 : : 2])	#[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])  #[10.8, True, (3+4j), 25]
print(list[1 : 4])	#[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])	#[True, None, 10.8]
print(list[3 : -3])	#['Hyd', True]
print(list[2 : -5])	#[(3+4j)]
print(list[-1:-5])	#[]




#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)	#x : 'Hyd'
print('y : ' , y)	#y : True
for  x  in  list[2:7]:
	print(x)        #(3+4j)
			 Hyd
			 True
			 None
			 10.8




#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))		#[10, 20, 30, 40, 50] 2463612255296
a[1 : 4] = [60 , 70]		#[10, 60, 70, 50] 2463612255296
print(a , id(a))
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))



#  Find  outputs  (Home  work)
a =  [25]	#Error list index out of range
print(a[1])
print(a[1:])



# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))		#class int
print(type(b))		#class tuple
print(type(c))		#class int
print(type(d))		#class tuple
print(a * 4)		#100
print(b * 4)		#(25, 25, 25, 25)
print(c * 4)		#100
print(d * 4)		#(25, 25, 25, 25)



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')		#('H', 'y', 'd')
print(a)			#class tuple
print(type(a))
print(len(a))			#3
b = [10 , 20 , 15 , 18]		#
print(tuple(b))			#(10, 20, 15, 18)
print(tuple(range(5)))		#(0, 1, 2, 3, 4)
print(tuple(25))		error



'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''


# Find  outputs (Home  work)
a = ()
print(type(a))  	#class tuple
print(a)		#()
print(len(a))		#0
b = tuple()           
print(b)		#()
print(len(b))		#0



# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)		#(10,20,30)
print(id(a))		#prints address
a = a * 2		#(10,20,30,10,20,30)
print(a)
print(id(a))		#prints new address of tuple object



#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)		#{True, 'Hyd', 25, 10.8, None, (3+4j)}
print(type(a))		#class set
print(len(a))		#6
print(a[2])		#error set has no index
print(a[1 : 4])		#error slicing is not possible because of no indexes
a[2] = 'Sec'		#error
print(a * 2)		#error
print(a * a)		#error



