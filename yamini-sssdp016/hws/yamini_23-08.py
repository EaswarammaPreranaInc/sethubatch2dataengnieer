# add()  method  demo  program  (Home  work)
a = set()
a . add(True) # adds True 
a . add(25) # adds 25
a . add(10.8) # adds 10.8
a . add(1)  # adds 1 but as True is already present it is not added again
a . add('Hyd') # adds 'Hyd'
a . add(25) # adds 25 but as 25 is already present it is not added again
a . add(None) # adds None
a . add('Hyd') # adds 'Hyd' but as 'Hyd' is already present it is not added again
a . add(1.0) # adds 1.0 but as True is already present it is not added again
print(a) # {True, 25, 10.8, 'Hyd', None} in any order
a . add(10 , 20 , 30) # error as add method takes only one argument
a . add([10,20,30]) # error as set can not have mutable elements like list
 

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # prints the set a
print(id(a)) # prints the id address of set a
a . add(tpl) # adds the tuple tpl as an element to set a
a . add('Sec') # adds the string 'Sec' as an element to set a
print(a) # prints the set a after adding the elements
print(id(a)) # prints the id address of set a it is same as earlier because we are modifying the same object
print(len(a)) # prints the number of elements in set a i,e 6
a . add([100 , 200 , 300]) # error because set can not have mutable elements like list
a . add(set()) # error because set can not have mutable elements like set
a.add({}) # error because set can not have mutable elements like dictionary

# Find  outputs (Home  work)
s = set() # empty set
tpl = (10 , 20 , 15 , 18) # tuple
s . add(tpl) # adding the tuple to set
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1 as we have only one element in set

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set() # empty set
s . update(tpl) # adds all elements of tpl to set s removing duplicates
print(len(s)) # 4 as there are 4 unique elements in tpl
print(s) # prints {10, 20, 15, 18} in any order
s . update(25) # error as 25 is not sequence


# Find  outputs  (Home  work)
a = [10 , 20 , 30] # list is assigned to a
b = {30 , 40,50 } # set is assigned to b
c = (50 , 60 , 70) # tuple is assigned to c
s = set() # empty set is assigned to s
s . update(a , b , c) # adds all the elements of a , b , c to set s
print(s) # prints the set s with all unique elements of a , b , c i.e {70, 40, 10, 50, 20, 60, 30}
print(len(s))    # prints the length of set s i.e 7
s . add(a , b , c) # error because add method takes only one argument

# Find  outputs  (Home  work)
a = set() # empty set
a . update('Rama Rao') # adds each character of string as individual element to set
print(a) # prints {'m', 'a', 'R', ' ', 'o', 'r'} in any order
print(len(a)) # as there are 6 unique elements in set len is 6
a . update(3 + 4j , 10.8 , True) # error as the argument of update function should be sequence

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18} # set with 4 elements
print(a) # {10, 20, 15, 18} in any order
b = a . copy() # b={10 , 20 , 15 , 18} new set with same elements as a
print(b) # {10, 20, 15, 18} in any order
print(a  is  b) # false as both doesn't point to same object
print(a  ==  b) # true as elements of a and b are same
c = a # c points to same object where a points
print(a  is  c) # true both points to same object


'''
copy()  method
------------------
1) What  does  copy()  method  do ?  --->  Returns  a  new  set  with  same  elements

2) a = b
    What  does  the  statement  do ?  --->  Reference  copy
																  i.e.  id  is  copied

3) What  is  shallow  clone ?  --->  Reference  copy
     What  is  deep  clone ?  ---> Object  copy
'''

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {10.8, 25, 'Hyd', True} maybe
print(a . pop()) # removes and returns the 1st element from the set maybe 25
print(a . pop()) # removes and returns the 1st element from the set maybe 10.8
print(a . pop()) # removes and returns the 1st element from the set maybe 'Hyd'
print(a . pop()) # removes and returns the 1st element from the set maybe True
print(a . pop()) # error as set is empty now
print(a) # error as set is deleted now
b = {10 , 20 , 30 , 40} # {40, 10, 20, 30} maybe
print(b . pop(2)) # error as set is not indexed


'''
pop()  method
----------------
1) What  does  pop(No-args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  --->  Zero
'''

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {10.8, 25, 'Hyd', True}
a . remove('Hyd') # 'Hyd' is removed
print(a) # {10.8, 25, True}
a . remove('Sec') # error as 'Sec' is not present in set


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {10.8, 25, 'Hyd', True}
a . discard('Hyd') # 'Hyd' is removed
print(a) # {10.8, 25, True}
a . discard('Sec') # 'Sec' is not present so nothing happens
print(a) # {10.8, 25, True}
a . remove('Sec') # error as 'Sec' is not present


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear() # removes all the elements of the set
print(a) # empty set
print(len(a)) # as there are no elements len is 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40} # set a
b = [30 , 40 , 50 , 60] # list b
print(a . union(b)) # prints the union of set a and list b {40, 10, 50, 20, 60, 30}
print(a | b) # prints the union of set a and list b {40, 10, 50, 20, 60, 30}
print(b . union(a)) # error because the program searches for union method in list class but it is not there
print(a + b) # error because we cant add set to list