# add()  method  demo  program  (Home  work)
a = set() # Ref 'a' points to empty set
a . add(True) # True is added to empty set
a . add(25) # 25 is added to set 'a'
a . add(10.8) # 10.8 is added to set 'a'
a . add(1) # 1 cannot be added because True already present in set 'a'
a . add('Hyd') # 'Hyd' is added to set 'a'
a . add(25) # 25 cannot be added because 25 is already present in set 'a'
a . add(None) # None is added to set 'a'
a . add('Hyd') # "Hyd" cannot be added because "Hyd" is already present in set 'a'
a . add(1.0) # 1.0 cannot be added because True is already present in set 'a'
print(a) # prints {True, 25, 10.8, 'Hyd', None} in any order
a . add(10 , 20 , 30) # Error because add method holds single argument
a . add([10,20,30]) # Error because set cannot hold mutable elements













# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True} # Ref 'a' points set
tpl = (10 , 20 , 30) # Ref tpl points to tuple of 3 elements
print(a) # prints 'a' i.e.,  {25, 10.8, 'Hyd', True} in any order
print(id(a)) # prints address of set 'a' 
a . add(tpl) # adds tpl to set 'a'
a . add('Sec') # adds 'Sec' to set 'a'
print(a) # {25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'} in any order
print(id(a)) # prints address of new set of 6 elements
print(len(a)) # prints number of elements in set 'a'i.e., 6
a . add([100 , 200 , 300]) # Error because set cannot hold mutable elements
a . add(set()) # Error because set cannot hold mutable elements
a . add({ }) # Error because set cannot hold mutable elements












# Find  outputs (Home  work)
s = set() # Ref 's' points to empty set
tpl = (10 , 20 , 15 , 18) # Ref 'tpl' points of 4 elements
s . add(tpl) # adds tpl to empty set 's'
print(s) # prints set 's' i.e., {(10, 20, 15, 18)}
print(len(s)) # prints number of elements in set 's' i.e., 1













# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20) # Ref 'tpl' points to tuple of 6 elements
s = set() # Ref 's' points to empty set
s . update(tpl) # updates elements of tpl to empty set 's'
print(len(s)) # prints number of elements in set 's' i.e., 6
print(s) # prints set 's' i.e., {10, 20, 15, 18} in any order
s . update(25) #  Error argument should be sequence only 














# Find  outputs  (Home  work)
a = [10 , 20 , 30] # Ref 'a' points to list [10, 20, 30]
b = {30 , 40,50 } # Ref 'b' points to set {30 , 40, 50}
c = (50 , 60 , 70) # Ref 'c' points to tuple (50, 60, 70)
s = set() # Ref 's' points to empty set
s . update(a , b , c) # Ref 's' is updated with elements of 'a', 'b' and 'c'
print(s) # prints 's' i.e., {10, 20, 30, 40, 50, 60, 70}
print(len(s)) # prints number of elements in the set 's' i.e., 7
s . = add(a, b, c) # Error because set cannot hold mutable elements

  









# Find  outputs  (Home  work)
a = set() # Ref 'a' points empty set
a . update('Rama Rao') # Ref 'a' is updated with string 
print(a) # prints 's' i.e., {'R', 'a', 'm', ' ', 'o'} in any order
print(len(a)) # prints number of elements in the set 's' i.e., 5
a . update(3 + 4j, 10.8, True) # Error because complex object cannot be added to set










# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18} # Ref 'a' points to set of 4 elements
print(a) # prints set 's' i.e., {10, 20, 15, 18} in any order
b = a . copy() # elements of set 'a' are copied to set 'b',deep copy
print(b) # prints set 'b' i.e., {10, 20, 15, 18} in any order
print(a  is  b) # False because Ref 'a' and Ref 'b' points to different sets
print(a  ==  b) # True because elements of set 'a' and 'b' are same
c = a # REference 'a' is copied to 'c', wherever 'a' points to the same set 'c' also points
print(a  is  c) # True because Ref 'a' and 'c' points to same set












# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True} # Ref 'a' points to set of 4 elements
print(a) # prints set 'a' i.e., {25, 10,.8, 'Hyd', True} in any order
print(a . pop()) # Removes 25 from set 's' and returns the 25
print(a . pop()) # Removes 10.8 from set 's' and returns the 10.8
print(a . pop()) # Removes 'Hyd' from set 's' and returns the 'Hyd'
print(a . pop()) # Removes True from set 's' and returns the True
print(a . pop()) # Error because empty set throws error
print(a) # prints set 'a' i.e., set()
b = {10 , 20 , 30 , 40} # Ref 'b' points to set of 4 elements
print(b . pop(2)) # Error because set is not indexed














# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True} # Ref 'a' points to set of 4 elements
print(a) # prints set 'a' i.e., {25, 10.8, 'Hyd', True} in any order
a . remove('Hyd') # removes element 'Hyd' from set 's'
print(a) # prints set 's' i.e., {25, 10.8, True} in same order because it is same set
a . remove('Sec') # Error because there is no element 'Sec













# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True} # Ref 'a' points to set of 4 elements
print(a) # prints set 's' i.e., {25, 10.8, 'Hyd', True} in any order
a . discard('Hyd') # removes element 'Hyd' from set 's'
print(a) # prints set 's' i.e., {25, 10.8, True} in same order because it is same set
a . discard('Sec') # does nothing because element 'Sec' is not present in set 's' and discard method does nothing
a . remove('Sec') # Error because element 'Sec' is not present in set 's' and remove method thows error















# clear()  method  demo  program (Home  work)
a = {10, 20, 15, 18} # Ref 'a' points to set of 4 elements
print(a) # prints set 'a' i.e., {10, 20, 15, 18} in any order
a . clear() # removes all the elements in the set 'a' and set becomes empty
print(a) # prints set 'a' i.e., set()
print(len(a)) # prints number of elements in the set 'a' i.e., 0















# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40} # Ref 'a' points to set of 4 elements
b = [30 , 40 , 50 , 60] # Ref 'b' points to list of 4 elements
print(a . union(b)) # Concatenates set 'a' and list 'b' and prints new set of 6 elements {10, 20, 30, 40, 50, 60} in any order
print(a | b) # Error because set and list cannot be concatenated with pipe operator
print(b . union(a)) # Error because list has no method union
print(a + b) # Error because set and list cannot be concatenated with '+' operator














