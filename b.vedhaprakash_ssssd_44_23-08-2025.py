## 23/08/2025 homework ANSWERES

a = set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)
a.add('Hyd')
a.add(25)
a.add(None)
a.add('Hyd')
a.add(1.0)
print(a)  # {True, 25, 10.8, 'Hyd', None}
a.add(10, 20, 30)   # Error
a.add([10, 20, 30]) # Error

###########
a = {25, 10.8, 'Hyd', True}
tpl = (10, 20, 30)

print(a) # {25, 10.8, 'Hyd', True}
print(id(a)) # (some memory address 
a.add(tpl) # adds (10, 20, 30)
a.add('Sec') # adds 'Sec'
print(a) # {25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}
print(id(a)) # same memory address as before (unchanged)
print(len(a)) # 6
a.add([100, 200, 300]) # Type error:  'list'
a.add(set()) # TypeError: 'set'
a.add({}) # TypeError:'dict'
################

Find  outputs (Home  work)

s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) # ((10 , 20 , 15 , 18))
print(s) #{(10 , 20 , 15 , 18)}
print(len(s))# 1 here tuple added as 1 whole element 
###############
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) # {(10,20,15,18)}
print(len(s)) #4
print(s) #{(10,20,15,18)}
s . update(25) # integer can't be added



'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                         (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more
'''
#######################
a = [10, 20, 30]
b = {30, 40, 50}
c = (50, 60, 70)
s = set() # {} created empty list

s.update(a, b, c) # {10, 20, 30, 40, 50, 60, 70}
print(s) # {10, 20, 30, 40, 50, 60, 70}
print(len(s)) # 7

s.add(a, b, c) # TypeError: because only 1 arguments is inserted 

#####################
a = set()
a.update('Rama Rao') 
print(a) # {'R', 'a', 'm', ' ', 'o'}
print(len(a)) # 5
a.update(3 + 4j, 10.8, True) # TypeError: 'complex' object is not iterabl

#################

a = {10, 20, 15, 18}
print(a) # {10, 20, 15, 18}

b = a.copy() # copies elements of a into a new set
print(b) # {10, 20, 15, 18}

print(a is b) # False  (different objects, different memory address)
print(a == b) # True   (same elements, so equal)

c = a
print(a is c) # True   (reference copy, both point to same object)


###############################################################

# pop() method demo program (Home work)
a = {25, 10.8, 'Hyd', True}
print(a)  # {25, 10.8, 'Hyd', True}  # Correct, but order may vary
print(a.pop())  # Arbitrary element (not guaranteed to be 25)
print(a.pop())  # Arbitrary element (not guaranteed to be 10.8)
print(a.pop())  # Arbitrary element (not guaranteed to be 'Hyd')
print(a.pop())  # Throws error if set is empty
print(a)  # set() if empty, otherwise remaining elements 
b = {10, 20, 30, 40}
print(b.pop(2))  # ERROR no indexes in set because unordered

pop()  method
----------------
1) What  does  pop(No-args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  --->  Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  --->  Zero
'''


#################################################################

# remove() method demo program (Home work)
a = {25, 10.8, 'Hyd', True}
print(a)  # {25, 10.8, 'Hyd', True}  #but order may vary
a.remove('Hyd')  # {25, 10.8, True}  #  removes 'Hyd'
print(a)  # {25, 10.8, True}  #order may vary
a.remove('Sec')  # error  #  - raises KeyError since 'Sec' is not in the set


'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  --->  Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  --->  Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''

##################################

# clear() method demo program (Home work)
a = {10, 20, 15, 18}
print(a)      # {10, 15, 18, 20} 
a.clear()
print(a)      # set()
print(len(a)) # 0

clear()  method
------------------
What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  set  and  set  becomes  empty
'''
#################################################################


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10 , 20 , 30 , 40,50,60}
print(a | b) #error
print(b . union(a)) # error
print(a + b) # error
