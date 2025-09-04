
# 1) Find  outputs  (Home  Work)

a = [25, 10.8, 'Hyd', True, 3+4j, None, 'Hyd', 25]  # Creates a list 

print(a)	# Output: [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)	# unpacked elements separated by spaces Output: 25 10.8 Hyd True (3+4j) None Hyd 25 
print(type(a))	# Output: <class 'list'>
print(id(a))	# address of the object
print(len(a))	# total elements in list: 8  
a[2] = 'Sec'	# replaces 'Hyd' with 'sec'
print(a)	# Output: [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2:5])	# Slices index 2 to 4 in step of 1: ['Sec', True, (3+4j)]




# 2) append()  and  remove()  methods  (Home  work)

a = []		# Creates empty list.
print(a)	# Output: []
a.append(25)	# inserts 25 to the list
a.append(10.8)	# inserts 10.8 to the list
a.append('Hyd') # inserts 'Hyd' to the list
a.append(True)	# inserts true to the list
print(a)	# Output: [25, 10.8, 'Hyd', True]
a.remove('Hyd')	# Removes first occurrence of 'Hyd'.
print(a)	# Output: [25, 10.8, True]
a.remove('25')	# Error: there no string '25'




# 3) Find  outputs  (Home  work)

a = [25, 10.8, 'Hyd']	# Creates a list 

print(a)	# Output: [25, 10.8, 'Hyd']
print(id(a))	# address of the list a.
print(a * 3)	# Output: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)	# Output: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)	# Output: [25, 10.8, 'Hyd']
print(a * 0)	# Output: [] (empty list).
print(a * -1)	# Output: [] (negative repeats give empty).
print(a * 4.0)	# Error: list can't be multiplied by non-int.
a = a * 3	
print(a)	# Output: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))	# new address of object a.
a = [25]
print(a * a)	# Error as we can't multiply list by list.




# 4) list()  function  demo  program

a = list('Hyd')
# Converts string 	# list of characters.
print(a)		# Output: ['H', 'y', 'd']
print(type(a))		# Output: <class 'list'>
print(len(a))		# Output: 3
b = (10, 20, 15, 18)
print(list(b))		# Output: [10, 20, 15, 18]
print(list(range(5)))	# Output: [0, 1, 2, 3, 4]
print(list(25))		# Error: int is non sequence so list fuction does not converts.




# 5) Find  outputs

a = []		# Creates empty list.
print(type(a))	# Output: <class 'list'>
print(a)	# Output: []
print(len(a))	# Output: 0
b = list()
print(b)	# Output: []
print(len(b))	# Output: 0




# 6) Slice  demo  program (Home  work)
#        0      1      2        3      4      5      6       7
list = [ 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7     -6       -5     -4      -3    -2      -1

print(list[2 : 7])    # list[2 :  7 :  1]  --->  List  from  indexes  2  to  6  in  steps  of  1   i.e.  [3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])    # list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1   i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])        # list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1   i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])  # list[-1: -9 : -1]  --->  List  from  indexes -1  to -8  in  steps  of -1   i.e.  ['Hyd', 10.8 , None, True, 'Hyd', 3 + 4j,  10.8,  25   ]
print(list[ : : 2])   # list[0 :  8 :  2]  --->  List  from  indexes  0  to  7  in  steps  of  2   i.e.  [25 ,  3 + 4j ,  True ,  10.8 ]
print(list[1 : : 2])  # list[1 :  8 :  2]  --->  List  from  indexes  1  to  7  in  steps  of  2   i.e.  [10.8 ,  'Hyd' ,  None , 'Hyd']
print(list[ : : -2])  # list[-1: -9 : -2]  --->  List  from  indexes -1  to -8  in  steps  of -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])# list[-2: -9 : -2]  --->  List  from  indexes -2  to -8  in  steps  of -2   i.e.  [10.8, True, 3+4j, 25]
print(list[1 : 4])    # list[1 :  4 :  1]  --->  List  from  indexes  1  to  7  in  steps  of  1   i.e.  [10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[-4 : -1])  # list[1 :  4 :  1]  --->  List  from  indexes -4  to  7  in  steps  of  1   i.e.  [10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[3 : -3])   # list[1 :  4 :  1]  --->  List  from  indexes  3  to  7  in  steps  of  1   i.e.  [10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[2 : -5])   # list[1 :  4 :  1]  --->  List  from  indexes  2  to  7  in  steps  of  1   i.e.  [10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[-1:-5])    # list[-1 :-5 : -1]  --->  stop<start so empty list i.e., []




# 7) Find  outputs  (Home  work)

#        0    1      2       3      4      5       6      7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']	# Creates a list.

x, y = list[3:5]  	# Unpacks indexes 3 & 4 : x='Hyd', y=True
print('x:', x)	  	# Output: x: Hyd
print('y:', y)	  	# Output: y: True
for x in list[2:7]:
    print(x)	   	# Output: 3+4j  Hyd  True  None  10.8




# 8) Find  outputs  (Home  work)

#     0    1    2    3    4
a = [10 , 20 , 30 , 40 , 50]	# Creates a list.
print(a, id(a))			# Output: [10, 20, 30, 40, 50] and gives address of the list object a
a[1:4] = [60, 70]		# Replaces 20,30,40 with 60,70 Output: [10, 60, 70, 50]
print(a, id(a))			# Output: [10, 60, 70, 50] address of the modified list object a
a[2:4] = [100, 200, 300]	# 100,200,300 Replaces 70,50 : [10, 60, 100, 200, 300]




# 9) Find  outputs  (Home  work)

a = [25]
print(a[1])	# Error as only index 0 exists
print(a[1:])	# Output: [] slice out of range but gives empty list





# 10) Find  outputs  (Home  work)

a = (25)       	# int object
b = 25,        	# 25, makes it a tuple 
c = 25         	# it is a only int 
d = (25,)      	# it is a proper tuple 
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'tuple'>
print(type(c))  # Output: <class 'int'>
print(type(d))  # Output: <class 'tuple'>
print(a * 4)    # 25 * 4 : 100
print(b * 4)    # (25,) repeated 4 times : (25, 25, 25, 25)
print(c * 4)    # 25 * 4 : 100
print(d * 4)    # (25,) repeated 4 times : (25, 25, 25, 25)





# 11) tuple()  function  demo  program  (Home  work)

a = tuple('Hyd')   	# Converts string to tuple of characters : ('H', 'y', 'd')
print(a)           	# ('H', 'y', 'd')
print(type(a))     	# <class 'tuple'>
print(len(a))      	# 3
b = [10, 20, 15, 18]
print(tuple(b))    	# Converts list to tuple : (10, 20, 15, 18)
print(tuple(range(5)))  # (0, 1, 2, 3, 4)
print(tuple(25))  	# Error as 'int' object is non sequence




# 12) Find  outputs (Home  work)

a = ()		 # empty tuple
print(type(a))   # <class 'tuple'>
print(a)         # ()
print(len(a))    # 0
b = tuple()
print(b)         # ()
print(len(b))    # 0





# 13) Tricky program
# Find  outputs (Home  work)

a = (10, 20, 30)# creates a tuble
print(a)        # (10, 20, 30)
print(id(a))    # address of the object a
a = a * 2	# New tuple created by repeating → (10, 20, 30, 10, 20, 30)
print(a)        # (10, 20, 30, 10, 20, 30)
print(id(a))    # New address of the object a




# 14) set  object  demo  program  (Home  work)

a = {25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'} # Sets removes duplicates.

print(a)        # we dont know the order : {True, 10.8, None, (3+4j), 25, 'Hyd'}
print(type(a))  # <class 'set'>
print(len(a))   # no. of unique elements in the set : 6
print(a[2])     # Error 'set' object is not indexed
print(a[1:4])   # Error: sets does not allows slicing
a[2] = 'Sec'    # Error as we cannot modify the set
print(a * 2)    # Error as can't multiply a set
print(a * a)    # Error set does not supports *





# 15) Tricky  program
# Find  outputs (Home  work)

a = {1, 'Hyd', False, True, 0.0, '', 1.0, 0} # Sets remove duplicates: False = 0 = 0.0, True = 1 = 1.0 : {'Hyd', 1, ''}
print(a)        
print(len(a))    # no. of unique elements in the set : 3 
print(type(a))   # <class 'set'>





# 16) set()  function demo  program

a = set('Rama rAo') 			# Converts string to set
print(a)         			# we don't know order: e.g., {'a','A','m',' ','r','R','o'}
print(len(a))    			# no. of unique elements in the set : 7
print(set([10, 20, 15, 20]))         	# Removes duplicates : {10, 20, 15}
print(set((25, 10.8, 'Hyd', 10.8)))  	# Removes duplicate 10.8 → {25, 10.8, 'Hyd'}
print(set(range(10, 20, 3)))         	# {10, 13, 16, 19}
print(set(25))    			# Error as set does not coverts the non sequence object
print(set([25, 10.8, [], 'Hyd']))    	# Error as set objects should be immutable only




# 17) Find  outputs  (Home  work)

a = []
b = ()
c = {}
d = set()
print(type(a))   # <class 'list'>
print(type(b))   # <class 'tuple'>
print(type(c))   # <class 'dict'> 
print(type(d))   # <class 'set'>
print(a)         # []
print(b)         # ()
print(c)         # {}
print(d)         # set()




# 18) Tricky  program
# add()  and  remove()  methods  (Home  work)

a = set()	# empty set
a.add(25)	# adds 25 to the set
a.add(10.8)	# adds 10.8 to the set
a.add('Hyd')	# adds 'Hyd' to the set
a.add(True)     # True = 1, if 1 or True already exists, won't add separately
a.add(None)	# adds nonetype to the set
a.add('Hyd')    # 'Hyd' is already is there so Duplicate are ignored
a.add(1)        # 1 = True, ignored
print(a)        # Order not known, e.g., {True, 10.8, None, 25, 'Hyd'}
print(len(a))   # no. of unique elements in the set : 5
a.remove(25)	# 25 will be removed from the set
print(a)        # output : {True, 10.8, None, 'Hyd'}
a.append(100)   # error asset object has no append method
a.add(set())    # error as we cannot have nested set
a.add(())       # adds empty tuple to the set
a.add([])       # error as set should have only immutable object
a.add({})       # error as set should have only immutable object





# 19) How  to  print  set  in  two  differnet ways  (Home  work)

a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)	# How  to  print  set

print('Iterate  thru  set  with  for  loop')
for i in a:
    print(i)    # How  to  iterate  thru  set  with  for  loop