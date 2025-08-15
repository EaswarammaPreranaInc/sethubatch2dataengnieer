
#  Find  outputs  (Home  Work)

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25] #Here a list object is Assigned to reference a
print(a) #Returns the list-object i.e [25, 10.8, 'Hyd', True, 3+4j, None, 'Hyd', 25]
print(*a) #Returns the elements in the list-object with default space <space> 25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a)) #Returns the type of object i.e <class 'list'>
print(id(a)) #Returns the address of list-object
print(len(a)) #Returns the number of elements in the list object
a[2] = 'Sec' #Replace the element in index 2 with 'sec' i.e [25,10.8, 'sec', True, 3+4j, None, 'Hyd', 25]
print(a) #Returns the list-object
print(a[2 : 5]) #Returns the new list-object with elements from 2 to 4 in steps of 1 i.e ['sec', True, (3+4j) ]



# append()  and  remove()  methods  (Home  work)

a = [ ] #Here an empty list-object is assigned to reference a 
print(a) #Returns the list-object i.e []
a . append(25) #By using append method int 25 is added at the end of the list
a . append(10.8) #Same here also float 10.8 is added at the end of the list
a . append('Hyd') #Same here also string 'hyd' is added at the end of the list
a . append(True) #Same here also bool True is added at the end of the list
print(a) #Returns the list-object i.e [25, 10.8, 'Hyd', True]
a . remove('Hyd') #String 'Hyd' is removed from the list #Here removing is done based on the 1st occurance
print(a) #Returns the list-object i.e [25, 10.8, True]
a . remove('25') #Here int 25 is removed from the list-object
print(a) #Returns the list object i.e [10.8, True]



#  Find  outputs  (Home  work)

a = [25 , 10.8 , 'Hyd'] #Here list-object is assigned to reference a 
print(a) #Returns the list-object i.e [25, 10.8, 'Hyd']
print(id(a)) #Returns the address of the list-object
print(a * 3) #Returns the list object 3 times in one list i.e [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) #Returns the list object 2 times in one list i.e [25, 10.8, 'Hyd', 25, 10.8]
print(a * 1) #Returns the list object once i.e [25, 10.8, 'Hyd']
print(a * 0) #Returns an empty list i.e []
print(a * -1) #Returns the empty list 
print(a * 4.0) #Error as we are using float to mutiply the list it is not possible
a = a * 3 #Here we are multiplying the list 3 times and assigning it to the same reference(obj)
print(a) #Returns the list-obj i.e [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) #Returns the address of the list-object that is multiplied 3 times
a = [25] #Reassigning a new list-object to reference a 
print(a * a) #Gives an error that we are multiplying the list with list so it raises error



# list()  function  demo  program

a = list('Hyd') #Here a list-object is created by converting string 'Hyd' to list i.e ['H', 'y', 'd']
print(a) #Returns the list-object i.e ['H', 'y', 'd']
print(type(a)) #Returns the type of object i.e <class 'list'>
print(len(a)) #Returns the number of elements in the list-object i.e 3
b = (10 , 20 , 15 , 18) #Here a tuple-object is assigned to reference b
print(list(b)) #Returns the list-object by converting tuple to list i.e [10, 20, 15, 18]
print(list(range(5))) #Returns the list-object by converting range-object to list i.e [0, 1, 2, 3, 4]
print(list(25)) #Invalid statement becoz int 25 is not a sequence so it raises error


# Find  outputs

a = [ ] #Here an empty list-object is assigned to reference a
print(type(a)) #Returns the type of object i.e <class 'list'>
print(a) #Returns the list-object i.e []
print(len(a)) #Returns the number of elements in the list-object i.e 0
b = list() #Here an empty list-object is created using list() function and assigned to reference b
print(b) #Returns the list-object i.e []
print(len(b)) #Returns the number of elements in the list-object i.e 0



# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1

print(list[2 : 7]) #Returns the list-object with elements from index 2 to 6 i.e [ (3+4j), 'Hyd', True, None, 10.8 ]
print(list[ : : ]) #Returns the entire list-object i.e [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #Returns the reversed list-object i.e ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2]) #Returns the list-object with every 2nd element starting from index 0 i.e [25, (3+4j), True, 10.8]
print(list[1 : : 2]) #Returns the list-object with every 2nd element starting from index 1 i.e [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) #Returns the list-object from index -2 to 0 in steps of -2 i.e [10.8, True, (3+4j), 25]
print(list[1 : 4]) #Returns the list-object with elements from index 1 to 3 i.e [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) #Returns the list-object with elements from index -4 to -2 i.e [True, None, 10.8]
print(list[3 : -3]) #Returns the list-object with elements from index 3 to 4 i.e ['Hyd', True]
print(list[2 : -5]) #Returns the list-object with elements from index 2 to 2 i.e [(3+4j)]
print(list[-1:-5]) #Returns the empty list-object becoz direction is forward and start index is after end index



#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] #Here list[3:5] returns ['Hyd', True] and multiple assignment is done where x='Hyd' and y=True
print('x : ' , x) #Returns the value of x i.e x :  Hyd
print('y : ' , y) #Returns the value of y i.e y :  True
for  x  in  list[2:7]: #For loop is used to iterate from index 2 to 6 and in each iteration value is assigned to x
	print(x) #Returns the value of x for every iteration i.e 3+4j, 'Hyd', True, None, 10.8
	


#  Find  outputs  (Home  work)
#     0     1     2    3     4

a = [10 , 20 , 30 , 40 , 50] #Here a list-object is assigned to reference a
print(a , id(a)) #Returns the list-object and its address i.e [10, 20, 30, 40, 50] and <address>
a[1 : 4] = [60 , 70] #Here elements from index 1 to 3 are replaced with 60 and 70 i.e [10, 60, 70, 50]
print(a , id(a)) #Returns the modified list-object and same address becoz list is mutable i.e [10, 60, 70, 50] and <same address>
a[2: 4] = [100 , 200 ,  300] #Here elements from index 2 to 3 are replaced with 3 elements i.e [10, 60, 100, 200, 300]
print(a , id(a)) #Returns the modified list-object and same address i.e [10, 60, 100, 200, 300] and <same address>


#  Find  outputs  (Home  work)

a =  [25] #Here a list-object with one element 25 is assigned to reference a
print(a[1]) #Invalid statement becoz index 1 is out of range so it raises error
print(a[1:]) #Returns the empty list-object becoz starting index is out of range i.e []



# Find  outputs  (Home  work)

a = (25) #Here a is not a tuple-object becoz no comma is used so it is int type
b = 25, #Here b is a tuple-object becoz comma is used after the element
c = 25 #Here c is a normal int type variable
d = (25,) #Here d is a tuple-object becoz comma is used inside the brackets
print(type(a)) #Returns the type of a i.e <class 'int'>
print(type(b)) #Returns the type of b i.e <class 'tuple'>
print(type(c)) #Returns the type of c i.e <class 'int'>
print(type(d)) #Returns the type of d i.e <class 'tuple'>
print(a * 4) #Returns the int value multiplied 4 times i.e 100
print(b * 4) #Returns the tuple-object repeated 4 times i.e (25, 25, 25, 25)
print(c * 4) #Returns the int value multiplied 4 times i.e 100
print(d * 4) #Returns the tuple-object repeated 4 times i.e (25, 25, 25, 25)



# tuple()  function  demo  program  (Home  work)

a = tuple('Hyd') #Here the string 'Hyd' is converted to tuple-object with each character as element
print(a) #Returns the tuple-object i.e ('H', 'y', 'd')
print(type(a)) #Returns the type of object i.e <class 'tuple'>
print(len(a)) #Returns the number of elements in the tuple-object i.e 3
b = [10 , 20 , 15 , 18] #Here a list-object is created and assigned to reference b
print(tuple(b)) #Returns the tuple-object i.e (10, 20, 15, 18)
print(tuple(range(5))) #Returns the tuple-object with values from 0 to 4 i.e (0, 1, 2, 3, 4)
print(tuple(25)) #Invalid statement becoz 25 is not a sequence so raises error


'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No-args)  do ?  ---> Returns  an  empty  tuple
'''



# Find  outputs (Home  work)

a = () #Here an empty tuple-object is assigned to reference a
print(type(a)) #Returns the type of object i.e <class 'tuple'>
print(a) #Returns the empty tuple-object i.e ()
print(len(a)) #Returns the number of elements in the tuple-object i.e 0
b = tuple() #Here tuple() with no arguments returns empty tuple-object and assigned to b
print(b) #Returns the empty tuple-object i.e ()
print(len(b)) #Returns the number of elements in the tuple-object i.e 0


# Tricky program
# Find  outputs (Home  work)

a = (10 , 20 , 30) #Here a tuple-object is assigned to reference a
print(a) #Returns the tuple-object i.e (10, 20, 30)
print(id(a)) #Returns the address of tuple-object
a = a * 2 #Here a new tuple-object is created by repeating elements 2 times i.e (10, 20, 30, 10, 20, 30)
print(a) #Returns the new tuple-object i.e (10, 20, 30, 10, 20, 30)
print(id(a)) #Returns the new address becoz tuple is immutable and new object is created


#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'} #Here a set-object is created with unique and unordered elements
print(a) #Returns the set-object with duplicate values removed and order is not preserved
print(type(a)) #Returns the type of object i.e <class 'set'>
print(len(a)) #Returns the number of unique elements in the set-object

print(a[2]) #Invalid statement becoz set does not support indexing so raises error
print(a[1 : 4]) #Invalid statement becoz set does not support slicing so raises error

a[2] = 'Sec' #Invalid statement becoz set does not support item assignment so raises error
print(a * 2) #Invalid statement becoz set does not support multiplication so raises error
print(a * a) #Invalid statement becoz set does not support multiplication so raises error



# Tricky  program
# Find  outputs (Home  work)

a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0} #Here a set-object is created with different types of elements, but duplicate values are removed based on equality
print(a) #Returns the set-object with unique values only i.e {'Hyd'} becoz 1, True, 1.0 are same and 0, False, 0.0 are same and '' is considered as empty string
print(len(a)) #Returns the number of unique elements in the set-object i.e 2
print(type(a)) #Returns the type of object i.e <class 'set'>



#  set()  function demo  program

a = set('Rama rAo') #Here the string 'Rama rAo' is converted to set-object with unique characters and order not preserved
print(a) #Returns the set-object with unique characters from the string i.e {'R', 'A', 'a', 'o', 'm', ' ', 'r'}
print(len(a)) #Returns the number of unique characters in the set-object
print(set([10 , 20 , 15 , 20])) #Returns the set-object by removing duplicates i.e {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) #Returns the set-object by removing duplicate 10.8 i.e {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) #Returns the set-object with values from 10 to 19 in steps of 3 i.e {10, 13, 16, 19}
print(set(25)) #Invalid statement becoz 25 is not a sequence so raises error
print(set([25 , 10.8 , [] , 'Hyd'])) #Invalid statement becoz list is unhashable so raises error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set
'''


Day-4 #Home Work-17
# Find  outputs  (Home  work)

a =   [ ] #Here an empty list-object is assigned to reference a
b =   ( ) #Here an empty tuple-object is assigned to reference b
c =   {} # actually it is not set it is an empty dict-object is assigned to reference c
d =   set() #Here set() with no arguments returns empty set-object and assigned to d
print(type(a)) #Returns the type of object i.e <class 'list'>
print(type(b)) #Returns the type of object i.e <class 'tuple'>
print(type(c)) #Returns the type of object i.e <class 'dict'>
print(type(d)) #Returns the type of object i.e <class 'set'>
print(a) #Returns the list-object i.e []
print(b) #Returns the tuple-object i.e ()
print(c) #Returns the dict-object i.e {}
print(d) #Returns the set-object i.e set()



# Tricky  program

# add()  and  remove()  methods  (Home  work)
a = set() #Here an empty set-object is created and assigned to reference a
a . add(25) #By using add() method int 25 is added into the set
a . add(10.8) #Here float 10.8 is added into the set
a . add('Hyd') #Here string 'Hyd' is added into the set
a . add(True) #Here bool True is added into the set
a . add(None) #Here None is added into the set
a . add('Hyd') #Here again 'Hyd' is added but no change because duplicates are not allowed in set
a . add(1) #Here 1 is same as True so no change in set
print(a) #Returns the set-object with unique values only
print(len(a)) #Returns the number of unique elements present in the set
a . remove(25) #Removes the value 25 from the set
print(a) #Returns the set-object after removing 25
a . append(100) #Invalid statement because append() is not available for set so raises error
a . add(set()) #Invalid statement because set is unhashable type so raises error
a . add(()) #Here empty tuple is added into the set because tuple is hashable
a . add([]) #Invalid statement because list is unhashable type so raises error
print(a) #Not executed due to error in previous line
a . add({}) #Invalid statement because {} is unhashable so raises error



# How  to  print  set  in  two  differnet ways  (Home  work)

a = {25 , True , 'Hyd' , 10.8} #Here a set-object is created with elements 25, True, 'Hyd', 10.8

print('set  with  print  function') #Just a heading for understanding purpose
print(a) #Returns the set-object with all elements

print('Iterate  thru  set  with  for  loop') #Just a heading for understanding purpose
for i in a: #Using for loop to iterate through each element in the set
    print(i) #Prints each element in separate line
