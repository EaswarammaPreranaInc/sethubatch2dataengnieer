 # add()  method  demo  program  (Home  work)
a = set()
a . add(True)					# {True}
a . add(25)					# {True,25}
a . add(10.8)					# {True,25,10.8}
a . add(1)					# {True,25,10.8,1}
a . add('Hyd')					# {True,25,10.8,1,'Hyd'}
a . add(25)					# set does not allowes duplicates
a . add(None)					# set does not allowes duplicates
a . add('Hyd')					# set does not allowes duplicates
a . add(1.0)					# set does not allowes duplicates
print(a)					# {True,25,10.8,1,'Hyd',None}
a . add(10 , 20 , 30)				# error
a . add([10,20,30])				# error


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
print(a)						# {25,10.8,'Hyd',True}
print(id(a))						# address of set
a . add(tpl)						# {25,10.8,'Hyd',True,(10,20,30)}
a . add('Sec')						# {25,10.8,'Hyd',True,(10,20,30),'Sec'}
print(a)						# {25,10.8,'Hyd',True,(10,20,30),'Sec'}
print(id(a))						# address of set a
print(len(a))						# 6
a . add([100 , 200 , 300])				# error
a . add(set())						# error
a . add({ })						# error


 # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)						# {(10,20,15,18)}
print(s)						# {(10,20,15,18)}
print(len(s))						# 1


 # update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)						# {10,20,15,18} 
print(len(s))						# 4
print(s)						# {10,20,15,18} any order
s . update(25)						# error



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
s . update(a , b , c)
print(s)						# {50,20,70,60,30,10,40}
print(len(s))						# 7
s . add(a , b , c)					# error


 # Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)						# {'R','a','m',' ','o'}
print(len(a))						# 5
a . update(3 + 4j , 10.8 , True)			# error


 # copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)						# {10,20,15,18}
b = a . copy()						# {10,20,15,18}
print(b)						# {10,20,15,18}
print(a  is  b)						# false
print(a  ==  b)						# True
c = a
print(a  is  c)						# True


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
print(a)							# {25,10.8,'Hyd','True}
print(a . pop())						# 25 deleting the value and returns values 
print(a . pop())						# 10.8 deleting the value and returns values 
print(a . pop())						# 'Hyd' deleting the value and returns values 
print(a . pop())						# 'True' deleting the value and returns values 
print(a . pop())
print(a)							# set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))						# error


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
print(a)							# {25, 10.8, 'Hyd', True}
a . remove('Hyd')						# removes 'Hyd'
print(a)							# {25, 10.8, True}
a . remove('Sec')						# error becoz no value of Sec


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''


 # discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)							# {25,10.8,'Hyd',True}
a . discard('Hyd')						# {25,10.8,True}
print(a)							# {25,10.8,True}
a . discard('Sec')						
print(a)							# nothing
a . remove('Sec')						# error


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''


 # clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)							# {10,20,15,18}
a . clear()							# clears all the values of set
print(a)							# set()
print(len(a))							# 0


'''
clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''


 # Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))						# {10,20,30,40,50,60}
print(a | b)							# error
print(b . union(a))						# error
print(a + b)							# error