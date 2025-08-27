#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # prints list 'a' i.e., [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)  # unpacks all elements from the list and prints them i.e., 25<space>10.8<space>Hyd<space>True<space>(3+4j)<space>None<space>Hyd<space>25
print(type(a)) # prints type of list i.e., <class 'list'>
print(id(a))  # prints address of the list
print(len(a))  # prints number of elemnts in the list i.e., 8
a[2] = 'Sec' # replaces 'Hyd' at index 2 with 'Sec' 
print(a) # prints the list i.e., [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) # prints the list from indexes 2 to 4 in steps of 1 i.e., ['Sec', True, (3+4j)]



# append()  and  remove()  methods  (Home  work)
a = [ ] # Creates an empty list
print(a)  #  prints list i.e., []
a . append(25) # appends element 25 into empty list 
a . append(10.8) # appends element 10.8 into list 
a . append('Hyd') # appends element Hyd into list 
a . append(True) # appends element True into list
print(a) # prints list i.e., [25, 10.8, 'Hyd', True]
a . remove('Hyd') # removes element 'Hyd' from list 'a'
print(a)  # prints list i.e., [25, 10.8, True]
a . remove('25')  # Error because element '25' is not in list
print(a)  # prints the list 'a' i.e., [25, 10.8, True]



#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # prints the list object 'a' i.e., [25, 10.8, 'Hyd']
print(id(a)) # prints address of the list object
print(a * 3) # prints the list object 3 times i.e., [25, 10,8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)  # prints the list object 2 times i.e., [25, 10,8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # prints the list object 1 times i.e., [25, 10,8, 'Hyd']
print(a * 0) # prints the empty list i.e., []
print(a * -1) # prints the empty list i.e., []
print(a * 4.0) # Error because sequence cannot be multiplied by float 
a = a * 3 # Ref 'a' points to modified to list of 9 elements
print(a) # prints the list object 3 times i.e., [25, 10,8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) # prints the address of the list 'a' i.e., [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
a = [25] # Ref 'a' is modified to list of single element
print(a * a) # Error because sequence cannot be multiplied with non-int type 'list'



# list()  function  demo  program
a = list('Hyd') # converts string to list
print(a) # prints list 'a' i.e., ['H', 'y', 'd']
print(type(a)) # prints the type of i.e., <class 'list'>
print(len(a)) # prints number of elements in the list i.e., 3
b = (10 , 20 , 15 , 18) # Ref 'a' points to tuple of 4 elements
print(list(b))  # converts tuple into a list and prints the list 'b' i.e., [10, 20, 15, 18]
print(list(range(5))) # converts range object into a list and prints the list from indexes 0 to 4 in steps of 1 i.e., [0, 1, 2, 3, 4]
print(list(25)) # Error because int object has no index



# Find  outputs
a = [ ] # creates an empty list
print(type(a))  # prints type of list 'a' i.e., <class 'list'>
print(a) # prints the list 'a' i.e., []
print(len(a)) # prints number of elements in the list 'a' i.e., 0
b = list() # Empty list
print(b) # prints the empty list 'b' i.e., []
print(len(b)) # prints number of elements in the list i.e., 0



# Slice  demo  program (Home  work)
#        0     1      2        3       4      5      6      7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8    -7      -6      -5      -4     -3     -2      -1
print(list[2 : 7]) # list[2 : 7 : 1 ] prints the list object from indexes 2 to 6 in steps of 1 i.e., [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])  # list[0 : 8 : 1 ] prints the list object from indexes 0 to 7 in steps of 1 i.e., [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # list[-1 : -9 : -1 ] prints the list object from indexes -1 to -8 in steps of 1 i.e., ['Hyd', 10.8, None, True, "hyd, (3+4j), 10.8, 25 ]
print(list[ : : 2]) # list[0 : 8 : 2 ] prints the list object from indexes 0 to 7 in steps of 2 i.e., [25, (3+4j), True, 10.8]
print(list[1 : : 2]) # list[1 : 8 : 2 ] prints the list object from indexes 1 to 7 in steps of 2 i.e., [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # list[-2 : -9 : -2 ] prints the list object from indexes -2 to -8 in steps of -2 i.e., [10.8, True, (3+4j), 25]
print(list[1 : 4]) # list[1 : 4 : 1 ] prints the list object from indexes 1 to 3 in steps of 1 i.e., [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # list[-4 : -1 : 1 ] prints the list object from indexes -4 to -2 in steps of 1 i.e., [True, None, 10.8,]
print(list[3 : -3]) # list[3 : -3 : 1 ] prints the list object from indexes 3 to -4 in steps of 1 i.e., ['Hyd', True]
print(list[2 : -5]) # list[2 : -5 : 1 ] prints the list object from indexes 2 to -6 in steps of 1 i.e., [(3+4j)]
print(list[-1:-5]) # list[-1 : -5 : 1 ] prints the list object from indexes -1 to -6 in steps of 1 i.e., []



#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] 
print('x : ' , x) # prints x : Hyd
print('y : ' , y) # prins y : True
for  x  in  list[2:7]: # list from indexes 2 to 6 in steps of 1 i.e.,(3 + 4j)<nextline>Hyd<nextline>True<nextline>None<nextline>10.8<nextline>
	print(x)
	


#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))  # prints list object 'a' and address of the list object i.e.,[10, 20, 30, 40, 50]<space>address of list
a[1 : 4] = [60 , 70] # replaces elements at index 1,2, and 3  with two elements 60, 70
print(a , id(a))  # prints list object 'a' and address of the list object i.e., [10, 60, 70, 50]<space>same address of list
a[2: 4] = [100 , 200 ,  300] # replaces elements of list from indexes 2 to 3 with 100, 200, 300
print(a , id(a)) # prints list object 'a' and address of the list object i.e., [10, 60, 100, 200, 300]<space>same address list



#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Error because list index is out of range
print(a[1:]) #  list without first element i.e., empty list



# Find  outputs  (Home  work)
a = (25) # Ref 'a' points to int object
b = 25, # Ref 'b' points to tuple
c = 25 # Ref 'c' points to int object
d = (25,) # Ref 'd' points to tuple
print(type(a)) # prints type of object 'a' i.e., <class 'int'>
print(type(b)) # prints type of object 'b' i.e., <class 'tuple'>
print(type(c)) # prints type of object 'c' i.e., <class 'int'>
print(type(d)) # prints type of object 'd' i.e., <class 'tuple'>
print(a * 4) # object 'a' is multiplied by 4 and prints 100
print(b * 4) # object 'b' is repeated 4 times i.e., (25, 25, 25, 25)
print(c * 4) # object 'c' is multiplied by 4 and prints 100
print(d * 4) # object 'd' is repeated 4 times i.e., (25, 25, 25, 25)



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') # converts string to tuple 
print(a) # prints tuple 'a' i.e., ('H', 'y', 'd')
print(type(a)) # prints type of the object i.e., <class 'tuple'>
print(len(a)) # prints number of elements in tuple i.e., 3
b = [10 , 20 , 15 , 18] # Ref 'b' points to list
print(tuple(b)) # converts list 'b' into tuple and prints tuple 'b' i.e., (10, 20, 15, 18)
print(tuple(range(5))) # converts range object to tuple and prints the tuple in range 5 i.e., (0, 1, 2, 3, 4)
print(tuple(25)) # Error because int object is not indexed,it is a sequence,sequence cannot have index



# Find  outputs (Home  work)
a = () # Ref 'a' points to empty tuple
print(type(a)) # prints type of the 'a' i.e., <class 'tuple>
print(a)  # prints tuple 'a' i.e., empty tuple ()
print(len(a)) # prints number of elements in the tuple i.e., 0
b = tuple() # Empty tuple
print(b) # prints tuple 'b' i.e. ()
print(len(b)) # prints number of elements in the tuple i.e., 0



# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30) # Ref 'a' points to tuple
print(a) # prints tuple 'a' i.e., (10, 20, 30)
print(id(a)) # prints address of tuple 'a' 
a = a * 2 # Ref a is modified to new tuple of 6 elements
print(a) # prints tuple 'a' i.e., (10, 20, 30, 10, 20, 30)
print(id(a)) # prints the address of the tuple 'a'



#  set   demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # prints set in any order 'a' i.e., {None, True, 25, 10.8, 'Hyd', (3+4j)}
print(type(a)) # prints type of 'a' i.e.,<class 'set'>
print(len(a)) # prints number of elements in the tuple 'a' .e., 6
print(a[2]) # Error because set is not indexed
print(a[1 : 4]) # Error because set is not indexed,so cannot be sliced
a[2] = 'Sec' #Error because set cannot be modified because it has no index
print(a * 2) # Error because set cannot have duplicates so it cannot be repeated
print(a * a) # Error because set multiplication with another set is invalid and sets cannot be multiplied



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # True and False values in set are treated as 1 and 0 respectively,after removing duplicates it prints set 'a' i.e., {False, 1, 'Hyd', ''}
print(len(a)) # prints number of elements in the set i.e., 4
print(type(a)) # prints type of i.e., <class 'set'>



#  set()  function demo  program
a = set('Rama rAo') # converts the string into a set of unique characters,removes duplicates 
print(a) # prints set 'a' i.e., {'m', 'o', 'A', 'r', 'a', 'R', ' '}
print(len(a)) # prints number of elements in the set 'a' i.e., 7
print(set([10 , 20 , 15 , 20])) # Prints set after removing duplicates i.e., {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # Prints set after removing duplicates i.e., {'Hyd', 25, 10.8}
print(set(range(10 , 20 , 3))) # converts range object set and prints set in range 10 to 19 in steps of 3 i.e., {16, 10, 19, 13}
print(set(25)) # Error because single integer cannot be converted to set and 25 is not a sequence
print(set([25 , 10.8 , [] , 'Hyd'])) # Error because set only allows immutable elements



# Find  outputs  (Home  work)
a =   [ ] # creates empty list 'a'
b =   ( ) # creates empty tuple 'b'
c =   {} # creates empty dictionary 'c'
d =   set() # creates empty set 'd'
print(type(a)) # prints type of object 'a' i.e., <class 'int'>
print(type(b)) # prints type of object 'b' i.e., <class 'tuple'>
print(type(c)) # prints type of object 'c' i.e., <class 'dict'>
print(type(d)) # prints type of object 'd' i.e., <class 'set'>
print(a) # prints list 'a' i.e., []
print(b) # prints tuple 'b' i.e., ()
print(c) # prints dict 'c' i.e., {}
print(d) # prints set 'd' i.e.,set()



# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() # creates empty set
a . add(25) # inserts element 25 to set 'a'
a . add(10.8) # inserts element 10.8 to set 'a'
a . add('Hyd') # inserts element 'Hyd' to set 'a'
a . add(True) # inserts element True to set 'a'
a . add(None) # inserts element None to set 'a'
a . add('Hyd') # 'Hyd' is duplicate ,it will be ignored
a . add(1) # 1 is treated as duplicate of True, so ignored
print(a) # prints object 'a' i.e., {None, True, 10.8, 'Hyd', 25}
print(len(a)) # prints number of elemnts in the set 'a' i.e., 5
a . remove(25) # removes element 25 from set 'a'
print(a) # prints set 'a' after removing element 25 i.e., {None, True, 10.8, 'Hyd'}
a . append(100) # Error because set has no append method
a . add(set()) # Error because set only allows immutable elements
a . add(()) # inserts empty tuple because tuple is immutable
a . add([]) # Error because list is mutable and it cannot be added to set
print(a) # prints set 'a' i.e., {None, True, 10.8, (), 'Hyd'}
a . add({}) # Error because dictionary is mutable and cannot be added to sets



# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a) # prints set 'a' i.e. {25, 10.8, True, 'Hyd'} in any order
for item in a:
    print(item) # prints items in the set i.e., 25<nextline>10.8<nextline>True<nextline>Hyd<nextline>
