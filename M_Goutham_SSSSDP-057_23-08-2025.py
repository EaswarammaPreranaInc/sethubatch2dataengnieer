a = set() #Reference a points to an empty set
a . add(True) #Bool object True is added to the set
a . add(25) #int object 25 is added to the set
a . add(10.8) #float object 10.8 is added to the set
a . add(1) #int object 1 is not added because True is already present (True == 1)
a . add('Hyd') #str object 'Hyd' is added to the set
a . add(25) #int object 25 is not added because 25 already exists in the set
a . add(None) #None object is added to the set
a . add('Hyd') #str object 'Hyd' is not added because 'Hyd' already exists in the set
a . add(1.0) #float object 1.0 is not added because 1.0 == 1 == True (already present)
print(a) #Prints the set with unique elements in any order

a . add(10 , 20 , 30) #TypeError: add() takes exactly one argument, multiple arguments are not allowed
a . add([10,20,30]) #TypeError: unhashable type: 'list' (list is mutable, so it cannot be added to a set)


'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable-object)  valid ? ---> No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  --->
															Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
															(Like  append()  method  of  list  class)
'''



# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True} #Reference a points to set of elements
tpl = (10 , 20 , 30) #Reference tpl points to tuple of elements
print(a) #Returns the set a in any ordered because set is unordered
print(id(a)) #Returns the address of set a
a . add(tpl) #Tuple is added to set a anywhere in the set
a . add('Sec') #Str 'sec' is added to set a 
print(a) #Returns the set with updated elements
print(id(a)) #Returns the address of set a and same address
print(len(a)) #Returns the length of set a i.e 6
a . add([100 , 200 , 300]) #Error #We cannot add mutuable elements to the set 
a . add(set()) #Error #we cannot add set in the set 
a . add({ }) #Error #We cannot add dict into the set bacause dict is a mutuable obj



# Find  outputs (Home  work)
s = set() #Reference s points to an empty set
tpl = (10 , 20 , 15 , 18) #Reference tpl points to the tuple of elements
s . add(tpl) #Here tuple is added to the set
print(s) #Returns the set with 1 element i.e {(10 , 20 , 15 , 18)}
print(len(s)) #Returns length of set i.e 1



# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20) #Reference tpl points  to the tuple of elements
s = set() #Reference s points to the empty set
s . update(tpl) #Here it takes the elements from the tuple and adds to the set one by one and remove the duplicates
print(len(s)) #Returns the length of set i.e 4
print(s) #Returns the set with 4 elements in any order i.e {10, 18, 20, 15}
s . update(25) #Error #Non-sequence cannot be added argument should be sequence only

'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more
'''



# Find  outputs  (Home  work)
a = [10 , 20 , 30] #Reference a points to list of elements
b = {30 , 40,50 } #Reference b points to set of elements
c = (50 , 60 , 70) #Reference c points to tuple of elements
s = set() #Reference s points to an empty set 
s . update(a , b , c) #Here to the set s the sequences a b c are added one by one into the set and removes duplicates 
print(s) #Returns the updated set with elements 
print(len(s)) #Returns the length of the set s i.e 7
s . add(a , b , c) #Error #Because add() takes only one argument.




# Find  outputs  (Home  work)
a = set() #Reference a points to an empty set 
a. update('Rama Rao') #Here str is added to the set one by one 
print(a) #Returns the a with elements i.e {'m', 'a', 'o', 'R', ' '}
print(len(a)) #Returns the length of the set i.e 5
a . update(3 + 4j , 10.8 , True) #Error #We cannot add complex object 




# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18} #Reference a points to the set of elements
print(a) #Returns the set of elements of a i.e {10 , 20 , 15 , 18}
b = a . copy() #Here the set a is copied to reference b 
print(b) #Returns same elements of set a
print(a  is  b) #False #Here references are compared 
print(a  ==  b) #True #Here elements in the set are compared
c = a #shallow copy i.e reference copy
print(a  is  c) #True #Because both a and c are pointing to the same object 

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
a = {25 , 10.8 , 'Hyd' , True} #Reference a points to set of elements 
print(a) #Returns the elements of set a in any order i.e {25 , 10.8 , 'Hyd' , True}
print(a . pop()) #Here pop will deletes the 1st element in the set and returns the deleted element
print(a . pop()) #Here pop will deletes the 1st element in the updated set and returns the deleted element
print(a . pop()) #Here pop will deletes the 1st element in the updated set and returns the deleted element
print(a . pop()) #Here pop will deletes the 1st element in the updated set and returns the deleted element
print(a . pop()) #Error #For the empty set we cannot use pop() 
print(a) #Returns the empty set
b = {10 , 20 , 30 , 40} #Reference b points the set b 
print(b . pop(2)) #Error #As set don't have index so it raises an error

'''
pop()  method
----------------
1) What  does  pop(No-args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  --->  Zero
'''



# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True} #Reference a points to the set of elements
print(a) #Returns the set i.e {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') #Here Str 'Hyd' is removed from the set
print(a) #Returns the updated set i.e {25 , 10.8 , True} 
a . remove('Sec') #Error #We cannot give the element that is not in the set

'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''




# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True} #Reference a points to the set a
print(a) #Returns the set a i.e  {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd') #Removes the str element 'Hyd' from the set
print(a) #Returns the set without 'Hyd'
a . discard('Sec') #do's nothing as there is no element 'Sec' in the set
print(a) #Returns the {25 , 10.8 , True}
a . remove('Sec') #Error #as remove() throws error when invalid element is given to remove

'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''




# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18} #Reference a points to set a
print(a) #Returns the set in any order of the elements i.e {10, 18, 20, 15} 
a . clear() #Removes all the elements from the set and set becomes empty
print(a) #Returns an empty set i.e {}
print(len(a)) #Returns length of set i.e 0

'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''




# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40} #Reference a points to the set a
b = [30 , 40 , 50 , 60] #Reference b points the list b 
print(a . union(b)) #Here elements in the list are added to the set a without duplicates
print(a | b) #Error #pipe operator must be used only in between two sets not other sequences
print(b . union(a)) #Error #As there is no union() in the list
print(a + b) #Error #We cannot concatinate the two different sequences 