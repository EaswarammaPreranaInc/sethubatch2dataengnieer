# add()  method  demo  program  (Home  work)
a = set()
a . add(True)  #  inserts element True to set a
a . add(25)  #  inserts element 25 to set a
a . add(10.8)  #  inserts element 10.8 to set a
a . add(1)  #  inserts element 1 to set a
a . add('Hyd')  #  inserts element 'Hyd' to set a
a . add(25)  #  inserts element 25 to set a
a . add(None)  #  inserts element None to set a
a . add('Hyd')  #  inserts element 'Hyd' to set a
a . add(1.0)  #  inserts element 1.0 to set a
print(a)  #  {True,25,10.8,'Hyd',None)  in any order
a . add(10 , 20 , 30)  #  Error due to add method allow only one elemenet
a . add([10,20,30])  #  Error


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
print(a)  #   {25 , 10.8 , 'Hyd' , True}
print(id(a)) #  address of set 
a . add(tpl)  #  inserts element tuple (10,20,30) to set a
a . add('Sec')  #  inserts element 'Sec' to set a
print(a)  #  {25 , 10.8 , 'Hyd' , True,(10,20,30),'Sec'} in any order
print(id(a))  #  Address of set a
print(len(a))  #  5
a . add([100 , 200 , 300])  #  Error
a . add(set()) #  Error
a . add({ })  #  Error


# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)  #  inserts (10,20,15,18) to set s
print(s)  #  {(10,20,15,18)}
print(len(s))  #  1


# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)  #  {10 , 20 , 15, 18 }
print(len(s))  #  4
print(s)  #  {10 , 20 , 15, 18 }  in any order
s . update(25) #  Error due to argument should be sequence only



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
s = set()
s . update(a , b , c)  #  {10,20,30,40,50,60,70}
print(s)  #  {10,20,30,40,50,60,70}
print(len(s))  #  7
s . add(a , b , c)  #  Error due to single argument should insert


# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)  #  {'R','a','m','o'}
print(len(a))  # 4
a . update(3 + 4j , 10.8 , True)  #  Error due to non sequences update



# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  # {10 , 20 , 15 , 18}
b = a . copy()  #  copy the elements of a to b
print(b)  #  {10 , 20 , 15 , 18}
print(a  is  b) #  False
print(a  ==  b)  #  True
c = a  
print(a  is  c)  #  True


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
print(a)  #  {25 , 10.8 , 'Hyd' , True}
print(a . pop())  #  Removes the 1st element in set a 25
print(a . pop())  #  Removes the 1st  of new set element in set a 10.8
print(a . pop())  #  Removes the 1st of new set element in set a 'Hyd'
print(a . pop())  #  Removes the 1st  of new set element in set a True
print(a . pop())  #  Error  due to no elements in set to remove
print(a)  #  set {}
b = {10 , 20 , 30 , 40}
print(b . pop(2))  #  Error due to set is not indexed


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
print(a)  #  {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')  #  {25,'10.8',True }
print(a)  #  #  {25,'10.8',True }
a . remove('Sec') #  Error due to 'Sec' not in set a to remove


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #  {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')  #  {25 , 10.8 , True}
print(a)  #  {25 , 10.8 , True}
a . discard('Sec')  #  Nothing
print(a)  #  {25 , 10.8 , True}
a . remove('Sec') #  Error due to 'Sec' not in set a to remove


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''


# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  #   {10 , 20 , 15 , 18}
a . clear()   #  clears the all elements
print(a)  #  set {}
print(len(a))  #  0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))  #  {10,20,30,40,50,60}
print(a | b)  #  Error
print(b . union(a))  #  error due to list not have union method
print(a + b)  #  Error due to set and list not  added

