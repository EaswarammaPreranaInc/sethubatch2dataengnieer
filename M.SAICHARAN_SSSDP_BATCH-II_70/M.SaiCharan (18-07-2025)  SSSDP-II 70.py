1.#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)		# [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)		# 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))		# <class 'list'>
print(id(a))		# Address
print(len(a))		# 8
a[2] = 'Sec'		
print(a)		# [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])		# ['Sec', True, (3+4j)]




2.# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)		# Empty list -----> [ ]
a . append(25)		# 25 is added to the list
a . append(10.8)	# 10.8 is added to the list
a . append('Hyd')	# 'Hyd' is added to the list
a . append(True)	# True is added to the list
print(a)		# [25, 10.8, 'Hyd', True]
a . remove('Hyd')	# 'Hyd' is removed from the list
print(a)		# [25, 10.8, True]
a . remove('25')	# we cannot remove '25' from the list, because in list int is present not the string 
print(a)		# Error




3.#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)		# [25, 10.8, 'Hyd']
print(id(a))		# Address
print(a * 3)		# [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)		# [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)		# [25, 10.8, 'Hyd']
print(a * 0)		# []
print(a * -1)		# []
print(a * 4.0)		# Error
a = a * 3
print(a)		# [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))		# Address
a = [25]
print(a * a)		# Error




4.# list()  function  demo  program
a = list('Hyd')
print(a)			# ['H', 'y', 'd']
print(type(a))			# <class 'list'>
print(len(a))			# 3
b = (10 , 20 , 15 , 18)
print(list(b))			# [10, 20, 15, 18]
print(list(range(5)))		# [ 0, 1, 2, 3, 4]
print(list(25))			# Error




5.# Find  outputs
a = [ ]
print(type(a))		# <class 'list'>
print(a)		# []
print(len(a))		# 0
b = list()
print(b)		# []
print(len(b))		# 0




6.# Slice  demo  program (Home  work)
#        0      1    2         3      4      5      6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7    -6        -5     -4     -3     -2       -1

print(list[2 : 7])	# [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])	# [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])		# list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  			   [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])	# ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])	# [25, (3+4j), True, 10.8]
print(list[1 : : 2])	# [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])	# list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   			   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])	# [10.8, True, (3+4j), 25]
print(list[1 : 4])	# [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])	# [True, None, 10.8]
print(list[3 : -3])	# ['Hyd', True]
print(list[2 : -5])	# [(3+4j)]
print(list[-1:-5])	# []




7.#  Find  outputs  (Home  work)
#        0    1      2      3       4      5      6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']

x ,  y = list[3 : 5]
print('x : ' , x)		# x : Hyd
print('y : ' , y)		# y : True
for  x  in  list[2:7]:
	print(x)		# (3+4j)
				# Hyd
				# True
				# None
				# 10.8





8.#  Find  outputs  (Home  work)
#     0   1     2   3    4
a = [10 , 20 , 30 , 40 , 50]

print(a , id(a))		# [10, 20, 30, 40, 50]  Address may be 1000
a[1 : 4] = [60 , 70]
print(a , id(a))		# [10, 60, 70, 50] Same Address
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))		# [10, 60, 100, 200, 300] Same address




9.#  Find  outputs  (Home  work)
a =  [25]
print(a[1])	# Error
print(a[1:])	# []




10.# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))		# <class 'int'>
print(type(b))		# <class 'tuple'>
print(type(c))		# <class 'int'>
print(type(d))		# <class 'tuple'>
print(a * 4)		# 100
print(b * 4)		# (25, 25, 25, 25)
print(c * 4)		# 100
print(d * 4)		# (25, 25, 25, 25)




11.# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)			# ('H', 'y', 'd')
print(type(a))			# <class 'tuple'>
print(len(a))			# 3
b = [10 , 20 , 15 , 18]
print(tuple(b))			# (10, 20, 15, 18)
print(tuple(range(5)))		# (0, 1, 2, 3, 4)
print(tuple(25))		# Error




12.# Find  outputs (Home  work)
a = ()
print(type(a))		# <class 'tuple'>
print(a)		# ()
print(len(a))		# 0
b = tuple()
print(b)		# ()
print(len(b))		# 0




13.# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)		# (10, 20, 30)
print(id(a))		# Address may be (2000)
a = a * 2
print(a)		# (10, 20, 30, 10, 20, 30)
print(id(a))		# Address may be (2050)




14.#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)		# {None, True, 25, 10.8, 'Hyd', (3+4j)}
print(type(a))		# <class 'set'>
print(len(a))		# 6
print(a[2])		# Error
print(a[1 : 4])		# Error
a[2] = 'Sec'
print(a * 2)		# Error
print(a * a)		# Error




15.# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)		# {False, 1, 'Hyd', ''}
print(len(a))		# 4
print(type(a))		# <class 'set'>




16.#  set()  function demo  program
a = set('Rama rAo')
print(a)					# {' ', 'a', 'm', 'r', 'A', 'o', 'R'}
print(len(a))					# 7
print(set([10 , 20 , 15 , 20]))			# {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))		# {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))			# {16, 10, 19, 13}
print(set(25))					# Error
print(set([25 , 10.8 , [] , 'Hyd']))		# Error




17.# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))		# <class 'list'>
print(type(b))		# <class 'tuple'>
print(type(c))		# <class 'set'>
print(type(d))
print(a)		# []
print(b)		# ()
print(c)		# {}
print(d)		# set()




18.# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()		# Empty set()
a . add(25)		# Add 25 to set
a . add(10.8)		# Add 10.8 to set
a . add('Hyd')		# Add 'Hyd' to set
a . add(True)		# Add True to set
a . add(None)		# Add None to set
a . add('Hyd')		# No adding of repeating element
a . add(1)		# No adding of repeating element
print(a)		# {True, 10.8, 'Hyd', None, 25}
print(len(a))		# 5
a . remove(25)		# remove 25 from set
print(a)		# {True, 10.8, 'Hyd', None}
a . append(100)		# Error
a . add(set())		# Error
a . add(())		# Add set() to set
a . add([])		# Error
print(a)		# {True, 10.8, 'Hyd', None, ()}
a . add({})		# Error




19.# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')		# 'set with print function'
print(How  to  print  set)			# print(a)
print('Iterate  thru  set  with  for  loop')	# 'Iterate  thru  set  with  for  loop'
How  to  iterate  thru  set  with  for  loop	# for item in a:
    							print(item)