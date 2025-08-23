#BATHINI RAJU

 # add()  method  demo  program  (Home  work)
a = set()
a . add(True) #True
a . add(25) #25
a . add(10.8) #10.8
a . add(1) #1
a . add('Hyd') #'Hyd'
a . add(25) #25
a . add(None) #None
a . add('Hyd') #Already present
a . add(1.0) # Already present
print(a) #{ 25, 10.8, 'Hyd', True, None}
a . add(10 , 20 , 30) # error because add() method takes single argument only
a . add([10,20,30]) # error because list is mutable object


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
a = {25 , 10.8 , 'Hyd' , True}

tpl = (10 , 20 , 30)
print(a) #{ 25, 10.8, 'Hyd', True}
print(id(a)) # id of a 1000
a . add(tpl) # (10, 20, 30)
a . add('Sec') # 'Sec'
print(a) #{ 25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}
print(id(a)) # id of a 1000
print(len(a)) # 6
a . add([100 , 200 , 300]) # error because list is mutable object
a . add(set()) # error because set is mutable object
a . add({ }) # error because dict is mutable object


 # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) # (10, 20, 15, 18)
print(s) #{ (10, 20, 15, 18) }
print(len(s)) # 1

 # update()  method  demo program  (Home  work)
 
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set() #Empty set
s . update(tpl) #Inserts elements of tpl in set s
print(len(s)) # 4
print(s) #{ 10, 15, 18, 20 }
s . update(25) #error because argument should be sequence only


'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more
'''

 # Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set() #Empty set
s . update(a , b , c) #Inserts elements of a, b, c in set s
print(s) #{ 10, 15, 18, 20, 30, 40, 50, 60, 70 }
print(len(s)) # 9
s . add(a , b , c) # error because add() method takes single argument only

# Find  outputs  (Home  work)

a = set() #Empty set
a . update('Rama Rao') #Inserts elements of 'Rama Rao' in set a
print(a) #{ 'R', 'a', 'm', ' ', 'o' }
print(len(a)) # 6
a . update(3 + 4j , 10.8 , True)
print(a) #{ 3 + 4j, 10.8, True, 'R', 'a', 'm', ' ', 'o' }


 # copy()  method  demo  program  (Home  work)
 
a = {10 , 20 , 15 , 18}
print(a) #{ 10, 15, 18, 20 }
b = a . copy()
print(b) #{ 10, 15, 18, 20 }
print(a  is  b) # False
print(a  ==  b) # True
c = a # shallow copy
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
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{ 25, 10.8, 'Hyd', True}
print(a . pop()) # 25
print(a . pop()) # 10.8
print(a . pop()) # 'Hyd'
print(a . pop()) # True
print(a . pop()) # error
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) #Error  no indexing in sets


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
print(a) # { 25, 10.8, 'Hyd', True}
a . remove('Hyd')
print(a) # { 25, 10.8, True}
a . remove('Sec') # error


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # { 25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a) # { 25, 10.8, True}
a . discard('Sec')
print(a) # { 25, 10.8, True}
a . remove('Sec') #error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''


 # clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # { 10, 15, 18, 20 }
a . clear()
print(a) # set()
print(len(a)) # 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
 # Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # { 10, 20, 30, 40, 50, 60 }
print(a | b) #Error
print(b . union(a)) #Error
print(a + b) # Unsupported Types set and list