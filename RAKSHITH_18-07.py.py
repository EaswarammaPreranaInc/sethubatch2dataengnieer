# Find outputs (Home Work)

a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Hyd', 25]  
print(a)        # Prints [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)       # Unpacks and prints each element of the list separated by space  25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))  # Prints the type of 'a' <class 'list'>
print(id(a))    # Prints the address of the list object 'a'
print(len(a))   # Prints the total number of elements in the list 8
a[2] = 'Sec'    # Modifies the 3rd element from 'Hyd' to 'Sec'
print(a)        # Prints the modified list [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2:5])   # Prints a sliced list from index 2 to 4 → ['Sec', True, (3+4j)]


# append() and remove() methods (Home work)

a = [ ]          # Creates an empty list named 'a'
print(a)         # Prints the empty list []
a.append(25)     # Appends the integer 25 to the list a = [25]
a.append(10.8)   # Appends the float 10.8 to the list a = [25, 10.8]
a.append('Hyd')  # Appends the string 'Hyd' to the list a = [25, 10.8, 'Hyd']
a.append(True)   # Appends the boolean value True to the list a = [25, 10.8, 'Hyd', True]
print(a)         # Prints  [25, 10.8, 'Hyd', True]
a.remove('Hyd')  # Removes the first occurrence of the string 'Hyd' from the list a
print(a)         # Prints the updated list → [25, 10.8, True]
a.remove('25')   # Error: list.remove(x) x not in list
print(a)         # This line will not be executed due to the error above


# Find outputs (Home work)

a = [25, 10.8, 'Hyd']
print(a)        # Prints [25, 10.8, 'Hyd'] 
print(id(a))    # Prints the address of the list object 'a'
print(a * 3)    # Prints [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)    # Prints [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)    # Prints [25, 10.8, 'Hyd']
print(a * 0)    # Prints [] (empty list)
print(a * -1)   # Negative repetition results in an empty list []
print(a * 4.0)  # Error Multiplying a list by a float is not allowed in Python.
a = a * 3       
print(a)        # Prints [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))    # Prints the address of the new list. 
a = [25]        # Reassigns 'a' to a new list with a single element [25]
print(a * a)    # Error you can't multiply a list by another list


# list() function demo program

a = list('Hyd')        # Converts the string 'Hyd' into a list of characters ['H', 'y', 'd']
print(a)               # Prints ['H', 'y', 'd']
print(type(a))         # Prints the type of 'a'<class 'list'>
print(len(a))          # Prints the number of elements in the list a is 3
b = (10, 20, 15, 18)               
print(list(b))         # Converts the tuple into a list [10, 20, 15, 18]
print(list(range(5)))  # Converts the range(0, 5) into a list [0, 1, 2, 3, 4]
print(list(25))        # Error int object (25) is not Mom sequence which can't be converted


# Find  outputs

a = [ ]                  # Creates an empty list and assigns it to variable 'a'
print(type(a))           # Prints the type of 'a' <class 'list'>
print(a)                 # Prints the list 'a' [] (an empty list)
print(len(a))            # Prints the number of elements in 'a' 0
b = list()               # Creates an empty list using the list() assigns it to reference 'b'
print(b)                 # Prints the list 'b' [] (an empty list)
print(len(b))            # Prints the number of elements in 'b' 0


# Slice demo program (Home work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1

print(list[2 : 7])            # Prints elements from index 2 to 6 in steps of 1 [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])            # Prints all elements using full slice [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])                # prints all elements [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1])          # Prints elements in reverse order ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])           # Prints element from 0 to 7 in steps of 2 [25, (3+4j), True, 10.8]
print(list[1 : : 2])          # Prints element from 1 to 7 in steps of 1 [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])          # Prints element from -1 to -8 in steps of -1 ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])        # Prints element from -2 to -8 in steps of -2 [10.8, True, (3+4j), 25]
print(list[1 : 4])            # Prints elements from 1 to 3 in steps of 1 [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])          # Prints elements from -4 to -2 in steps of -1 [True, None, 10.8]
print(list[3 : -3])           # Prints elements from 3 to 4 in steps of 1 ['Hyd', True]
print(list[2 : -5])           # Prints elements from 2 to 2 in steps of 1 [(3+4j)]
print(list[-1:-5])            # Empty list, slicing in forward direction from -1 to -5 []


# Find outputs (Home work)

#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']

x , y = list[3 : 5]    # Slices elements at index 3 and 4 
print('x : ' , x)      # Prints the value of x which is x : Hyd
print('y : ' , y)      # Prints the value of y which is y : True
for x in list[2:7]:    # Iterates through elements from index 2 to 6 (3+4j), 'Hyd', True, None, 10.8
    print(x)           # Prints elements (3+4j) <newline> 'Hyd' <newline> True <newline> None <newline> 10.8


# Find outputs (Home work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]            
print(a , id(a))                        # Prints the list and its address
a[1 : 4] = [60 , 70]                    # Replaces elements at index 1 to 3 (20, 30, 40) with 60 and 70
print(a , id(a))                        # Prints modified list and same address
a[2 : 4] = [100 , 200 , 300]            # Replaces elements at index 2 to 3 (70, 50) with 100, 200, 300
print(a , id(a))                        # Prints updated list and same address


# Find outputs (Home work)
a = [25]                 
print(a[1])              # Error index 1, which does not exist
print(a[1:])             # Prints [] slicing from index 1 not available returns an empty list


# Find  outputs  (Home  work)

a = (25)               # 'a' is an integer, not a tuple, as it does not have a comma
b = 25,                # 'b' is a tuple with a single element 25
c = 25                 # 'c' is a plain integer with value 25
d = (25,)              # 'd' is also a tuple with one element 25
print(type(a))         # Prints the type of a <class 'int'>
print(type(b))         # Prints the type of b <class 'tuple'>
print(type(c))         # Prints the type of c <class 'int'>
print(type(d))         # Prints the type of d <class 'tuple'>
print(a * 4)           # Integer multiplication 25 * 4 = 100
print(b * 4)           # Tuple repetition (25,) * 4 = (25, 25, 25, 25)
print(c * 4)           # Integer multiplication 25 * 4 = 100
print(d * 4)           # Tuple repetition (25,) * 4 = (25, 25, 25, 25)


# tuple()  function  demo  program  (Home  work)

a = tuple('Hyd')         # Converts the string 'Hyd' into a tuple of characters ('H', 'y', 'd')
print(a)                 # Prints the tuple ('H', 'y', 'd')
print(type(a))           # Prints the type of 'a' <class 'tuple'>
print(len(a))            # Prints the number of elements in the tuple 3
b = [10, 20, 15, 18]
print(tuple(b))          # Converts the list into a tuple (10, 20, 15, 18)
print(tuple(range(5)))   # Converts the range(0, 5) into a tuple (0, 1, 2, 3, 4)
print(tuple(25))         # Error int object is non sequence, so it cannot be converted to a tuple


# Find  outputs (Home  work)

a = ()                     # Creates an empty tuple using parentheses
print(type(a))             # Prints the type of 'a' <class 'tuple'>
print(a)                   # Prints the empty tuple ()
print(len(a))              # Prints the length of the tuple 0
b = tuple()                # Creates an empty tuple using the tuple() function
print(b)                   # Prints the empty tuple ()
print(len(b))              # Prints the length of the tuple 0


# Tricky program
# Find  outputs (Home  work)

a = (10, 20, 30)           # Creates a tuple 'a' with elements (10, 20, 30)
print(a)                   # Prints the tuple (10, 20, 30)
print(id(a))               # Prints the address of the tuple 'a'
a = a * 2                  # Duplicates the tuple and assigns it to 'a' (10, 20, 30, 10, 20, 30)
print(a)                   # Prints the new tuple (10, 20, 30, 10, 20, 30)
print(id(a))               # Prints the new address, which will be different from previous tuple 'a'


# set object demo program (Home work)

a = {25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'}  
print(a)              # Prints the set of object a
print(type(a))        # Prints the type of 'a' <class 'set'>
print(len(a))         # Prints the number of unique elements in the set which is 6
print(a[2])           # Error Sets are unordered and do not support indexing
print(a[1 : 4])       # Error Slicing is not supported on set objects
a[2] = 'Sec'          # Error Sets are mutable but do not support item assignment
print(a * 2)          # Error Set multiplication is not supported
print(a * a)          # Error cannot multiply a set by another set


# Tricky program
# Find outputs (Home work)

a = {1, 'Hyd', False, True, 0.0, '', 1.0, 0}
print(a)              # Prints the set {False, 1, '', 'Hyd'}
print(len(a))         # Prints the number of unique elements in the set which is 4
print(type(a))        # Prints the type of 'a' <class 'set'>


# set() function demo program

a = set('Rama rAo')                   # Converts the string 'Rama rAo' into a set of unique characters
print(a)                              # Prints the set of unique characters from the string print(len(a))                         # Prints the number of unique characters in the set which is 8
print(set([10, 20, 15, 20]))          # Converts the list to a set by removing duplicates {10, 20, 15}
print(set((25, 10.8, 'Hyd', 10.8)))   # Converts the tuple to a set by removing duplicates {25, 10.8, 'Hyd'}
print(set(range(10, 20, 3)))          # Converts the range(10, 20, 3) to set {10, 13, 16, 19}
print(set(25))                        # Error can't convert an integer into a set
print(set([25, 10.8, [], 'Hyd']))     # Error list [] can't be added to a set


# Find outputs (Home work)

a = []              # Creates an empty list
b = ()              # Creates an empty tuple
c = {}              # Creates an empty dictionary 
d = set()           # Creates an empty set using set() constructor
print(type(a))      # Prints class of object a <class 'list'> 
print(type(b))      # Prints class of object a <class 'tuple'> 
print(type(c))      # Prints class of object a <class 'dict'> 
print(type(d))      # Prints class of object a <class 'set'> 
print(a)            # Prints [] – empty list
print(b)            # Prints () – empty tuple
print(c)            # Prints {} – empty dictionary
print(d)            # Prints set() – empty set


# Tricky program
# add() and remove() methods (Home work)

a = set()             # Creates an empty set
a.add(25)             # Adds 25 to the set
a.add(10.8)           # Adds 10.8 to the set
a.add('Hyd')          # Adds 'Hyd' to the set
a.add(True)           # Adds True 
a.add(None)           # Adds None to the set
a.add('Hyd')          # Duplicate, will be ignored
a.add(1)              # 1 is equal to True → Already exists, so ignored
print(a)              # Prints the set {True, 10.8, 'Hyd', 25, None}
print(len(a))         # Prints the number of unique elements 5
a.remove(25)          # Removes 25 from the set
print(a)              # Prints the updated set {True, 10.8, 'Hyd', None}
a.append(100)         # Error 'set' object has no attribute 'append'
a.add(set())          # Error set is cannot be added to another set
a.add(())             # Tuple is added to the set
a.add([])             # Error list is cannot be added to a set
print(a)              # Will not execute due to above errors
a.add({})             # Error dict is cannot be added to a set


# How  to  print  set  in  two  differnet ways  (Home  work)

a = {25, True, 'Hyd', 10.8}   
print('Set with print function:')
print(a)                           
print('Iterate through set with for loop:')
for x in a:                
    print(x)          

