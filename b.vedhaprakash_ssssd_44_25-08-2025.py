# Homework questions on 25/08/2025

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) # intersects the common elements in a and b into c 
print(c) # {30,40}
print(type(c)) # <class 'set'>
d = a & b # {30,40}
print(d) # {30,40}
print(type(d)) # <class 'set'>
print(c  is  d) # False
print(c  ==  d) #True


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
								Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  --->  a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''
#############################################

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) # {10, 20}
print(c) #{10, 20}
print(type(c)) #<class 'set'>
d = a - b #{10, 20}
print(d) ##{10, 20}
print(type(d)) #<class 'set'>
print(c  is  d) #False 
print(c  ==  d) #True


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->
							Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''

###############################################

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b) # returns set with all elements of sets and and b but without common elements 
print(c) # {10,20,50,60}
print(type(c)) # <class 'set'>
d = a ^ b # {10,20,50,60}
print(d) #{10,20,50,60}
print(type(d)) # <class 'set'>
print(c   is   d) # False
print(c  ==   d) # True


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''

#####################################

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # returns squares of numbers from 0 to 9 i.e is {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a)) # <class 'set'>



#####################################
#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) # How  to  print  value  25  in  dict  'a')
print(a['Ename']) # How  to  print  'Rama Rao'  in  dict  'a')
print(a['Sal']) # How  to  print  value  1000.65   in  dict  'a')


##################################

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # 
a[ 'Sal'] = 2000 # How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita' # How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35 # How  to  modify  25   to  35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000 }
print(id(a)) # something id but not same as previous set 

#########################

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M' # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = 'True' # How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  ,'Gender' : M , 'Married' : True}

##########################

# Find  outputs (Home  work)
a = { } # {} 
a['Rama'] = 10  # How  to  append  10 : 'Rama'  to  dictionary  'a'
a['Sita'] = 20 # How  to  append  20 : 'Sita'  to  dictionary  'a'
a['Rajesh'] = 15 # How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a['Kiran'] = 18 # How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) # {'Rama'  :  10,  'Sita'  :  20  ,  'Rajesh'  :  15  ,'Kiran' : 18 }

###################################


#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.pop('Sal') =  1000.65 # How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'}

################################33

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False 
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25  not  in  a) # True 

##################################

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a) # {10: 'A', 20: 'B', 15: 'C'
print(b) # # dictionary with duplicate key resolved
print(type(b)) # < class 'dict'>

#######################

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(b) # 
print(a  is  b) # False
print(a  ==  b) # True
c = a # 
print(a  is   c) # True
print(a  ==  c) # True

#################################

# Find outputs (Home Work)

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)           # {10, 14, 15, 18, 19, 20, 25}
print(type(d))     # <class 'set'>
e = {**a, **b, **c}
print(e)           # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))     # <class 'dict'>

####################################

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # error 
c = {**a , **b} # {10: 60, 30: 50}
print(c) # {10: 60, 30: 50}
#d = a | b # error
#print(d) # error


##################

# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3 
b = {} # {}
print(len(b))  # 0

'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
'''

###############################

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90 
print(sum(a . values())) # 120
print(sum(a)) # 90
print(sum(a . items())) # error

#########################

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40 
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) # (40,5)
print(min(a . items())) # (7,28)
print(max(a)) # 40
print(min(a)) # 7

############################

#  dict()  function  demo program (Home  work))
# dict() function demo program (Home work)

a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
b = dict(a)
print(b)   # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}  # duplicate key keeps last value

c = [['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray']]
d = dict(c)
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}  # duplicate key keeps last value

e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(dict(e))  # Error: each element must have exactly 2 items

f = [[10], [20], [30]]
print(dict(f))  # Error: each element must have exactly 2 items

print(dict([10, 20]))  # Error: not a nested sequence

g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))# {10: [20, 30], 40: [50, 60], 70: [80, 90]}

h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))  # Error: unhashable type: 'list' (keys must be immutable)

i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))# {(10, 20): 30, (40, 50): 60, (70, 80): 90}  # tuple key allowed


'''
dict()  function
------------------
1) What  is  the  argument  of  dict()  function ?  --->
											Nested  sequence  such  as  list  of  tuples , list  of  lists , tuple  of  tuples , tuple  of  lists,
											set  of  tuples  and  so  on

2) What  does  dict(nested-sequence)  do ?  --->  Converts  nested  sequence  to  dictionary

3) How  many  elements  can  be  in  each  inner  sequence ?  --->  Exactly  two  elements
    What  are  the  two  elements  of   each  inner  sequence ?  ---> key  and   value

4) Is  dict(sequence)  valid ?  --->  No  becoz  argument  is  not  a  nested  sequence
'''
##################################################################
# sorted() function (Home work)
a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b)  # [5, 10, 15, 18, 20]
c = sorted(a.values())
print(c)  # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a.items())
print(d)  # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f = sorted(a, reverse=True)
print(f)  # [20, 18, 15, 10, 5]
print(a)  # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

