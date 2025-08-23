# add()  method  demo  program  (Home  work)
a = set() # ref 'a' is pointing to set obj
a . add(True) # True is inserted into set -- {True}
a . add(25) # inserted into 'a' -- {True, 25} # inserted into any order
a . add(10.8) # {True, 25, 10.8}
a . add(1) # {25, True, 1, 10.8}
a . add('Hyd') # {25, True, 1, 'Hyd', 10.8}
a . add(25) # set dont contain duplicates even 25 is inserted
a . add(None) # {25, True, 1, 'Hyd',None , 10.8}
a . add('Hyd') # {25, True, 1, 'Hyd',None , 10.8}
a . add(1.0) # {25, True, 1, 'Hyd',None , 10.8} 
print(a) # {25, True, 1, 'Hyd',None , 10.8}
a . add(10 , 20 , 30) # error
a . add([10,20,30]) # error


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
a = {25 , 10.8 , 'Hyd' , True} # set obj
tpl = (10 , 20 , 30) # tuple obj
print(a) # {'Hyd', 25 , 10.8 , True}
print(id(a)) # address of 'a'
a . add(tpl) # (10 , 20 , 30) is inserted into set
a . add('Sec') # inserted into set
print(a) # {25 , 10.8 , 'Hyd' ,(10 , 20 , 30),  True, 'Sec'}
print(id(a)) # same address 
print(len(a)) # 6
a . add([100 , 200 , 300]) # error
a . add(set()) # error
a . add({ }) # error


# Find  outputs (Home  work)
s = set() # empty set obj
tpl = (10 , 20 , 15 , 18) # tuple obj
s . add(tpl) # {(10 , 20 , 15 , 18)}
print(s) # {(10 , 20 , 15 , 18)}
print(len(s)) # 1


# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20) # tuple 
s = set() # empty set obj
s . update(tpl) # inserts elements of tuple
print(len(s)) # 4
print(s) # {10, 18, 20, 15}
s . update(25) # error



'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more
'''


# Find  outputs  (Home  work)
a = [10 , 20 , 30] # list obj
b = {30 , 40,50 } # set obj
c = (50 , 60 , 70) # tuple obj
s = set() # set obj
s . update(a , b , c) # elements of a, b, c are inserted into set
print(s) # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
s . add(a , b , c) # error


# Find  outputs  (Home  work)
a = set() # empty set obj
a . update('Rama Rao') # elements are inserted 
print(a) # {'o', 'a', 'm', 'R', ' '}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # error


# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18} # set obj
print(a) # {10 , 15 , 18, 20}
b = a . copy() # deep copy is done 
print(b) # {10 , 15 , 18, 20}
print(a  is  b) # False
print(a  ==  b) # True
c = a # ref is copied
print(a  is  c) # True


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
a = {25 , 10.8 , 'Hyd' , True} # set obj
print(a) # {25 , 10.8 , 'Hyd' , True} 
print(a . pop()) # 25
print(a . pop()) # 10.8
print(a . pop()) # Hyd
print(a . pop()) # True
print(a . pop()) # error
print(a) # set()
b = {10 , 20 , 30 , 40} # set obj
print(b . pop(2)) # error --no args req


'''
pop()  method
----------------
1) What  does  pop(No-args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  --->  Zero
'''


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True} # set obj
print(a) # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') # removes Hyd from set 
print(a) # {25 , 10.8 , True}
a . remove('Sec') # error


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True} # set obj
print(a) # {25 , 'Hyd' , True, 10.8}
a . discard('Hyd') # removes 'Hyd' from set
print(a) # {25 , True, 10.8}
a . discard('Sec') # does nothing
print(a) # {25 , True, 10.8}
a . remove('Sec') # error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''


# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18} # set obj
print(a) # {10 , 20 , 15 , 18} in unordered
a . clear() # removes all elements in set
print(a) # set()
print(len(a)) # 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40} # set obj
b = [30 , 40 , 50 , 60] # list obj
print(a . union(b)) # concatinates 'a' and 'b' {10 , 20 , 30 , 40, 50 , 60}
print(a | b) # {10 , 20 , 30 , 40, 50 , 60}
print(b . union(a)) # error
print(a + b) # error
