#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#    0    1    2     3   4     5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)} times')

'''
Outputs:
2
5		
8
15 is found 3 times
'''


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0     1     2       3     4
a[2] = 35 # Error because tuple is immutable
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # prints address of tuple 'a'
a = a[0 : 3] + (35,) + a[3 : 6] # How  to  modify  30  in  tuple  to  35
print(a) # prints tuple of 6 elements i.e., (10, 20, 30, 35, 40, 50)
print(id(a)) # prints address of new tuple of 6 elements i.e., new address of new tuple


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # Error because tuple is immutable
del  a[2] # Error because tuple is immutable
a . pop(2) # Error because tuple is immutable
print(a) # prints tuple i.e., (10, 20, 30, 40, 50)
print(id(a)) # prints address of tuple 'a'
a = a[0 : 2] + a[3: 6] # How  to  remove  30  from  tuple  'a'
print(a) # prints new tuple of 4 elements
print(id(a)) # prints address of new tuple of 4 elements



#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) ) # Ref 'a' points tuple of tuples
print(a) # prints tuple 'a' i.e, ((10, 20),  (30, 40, 50),  (60, 70, 80, 90))
print(type(a)) # prints type of 'a' i.e., <class 'tuple'>
print(len(a)) # prints number of elements in tuple 'a' i.e., 3
print(a[0]) # How to print 1st inner tuple
print(a[1]) # How to print 2nd inner tuple
print(a[2]) # How to print 3rd inner tuple
print(a[0][1]) # How to print 20
print(a[1][2]) # How to print 50
print(a[2][3]) # How to print 90
	  


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),) # Ref 'a' points to tuple
print(a[0]) # How to print inner tuple
print(*a) # How to print inner tuple in another way
print(a[0][0]) # How to print 10
print(a[0][1]) # How to print 20
print(a[0][2]) # How to print 30
b = ((),)
print(b[0]) # How to print inner tuple of tuple 'b'
print(*b) # How to print inner tuple of tuple 'b' in another way
	  


#  Find  outputs (Home  work)
a = ((10 , 20 , 30)) # Ref 'a' points to tuple of tuple
print(a) # prints tuple i.e., ((10, 20, 30))
print(*a) # prints inner tuple i.e., (10, 20, 30)
b = (()) # Ref 'a' points to tuple of empty tuple
print(b) # prints 'b' i.e.,  ()
print(*b) # prints inner tuple of 'b' i.e., ()



# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ') # reads string input from user
print(a) # prints 'a' i.e., '{10 , 20 , 15 , 18 , 20 , 12 , 18}'
print(type(a)) # prints type of 'a' i.e., <class 'str'>
b = eval(a) # converts string to set 
print(b) # prints ''b' i.e., {10, 20, 15, 18, 20, 12, 18}
print(type(b)) # prints type of 'b' i.e., <class 'set'>


#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # prints set of tuple i.e., {(10, 20, 30)}
print({[10 , 20 , 30]}) # prints set of list i.e., {[10, 20, 30]}
print({{10 , 20 , 30}}) # prints set of set i.e., {{10, 20, 30}}
print({{}}) # prints set of empty set i.e., {{}}



# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # prints set 'a' in any order
print('Iterate  elements  of  set  with  for  loop')
for i in a:
	print(i) # prints in any order
# How to iterate set with for loop

'''
Outputs:

set with print function
{25 , True , 'Hyd' , 10.8} 
Iterate elements of set with for loop
25
10.8
Hyd
True
'''


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # prints set 's' i.e., {'Hyd', True, 25, 1} in any order
print(len(s)) # number of elements in set 's' i.e., 4
print(type(s)) # prints type of 's' i.e., <class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } # Ref 's' points to set of 4 elements
print(s) # prints set 's' i.e., {'Hyd',  25,  True,  10.8} inn any order
a , b , c , d = s  # unpacking the set 's'
print(a) # prints 'a' i.e., 'Hyd'
print(b) # prints 'b' i.e., 25
print(c) # prints 'c' i.e., True
print(d) # prints 'd' i.e., 10.8


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } # Ref 's' points to set of 4 elements
print(s) # prints set 's' i.e., {'Hyd',  25,  True,  10.8} in any order
a , *b = s # unpacking set 's'
print(a) # prints 'a' i.e., 'Hyd'
print(b) # prints 'b' i.e., [25, True, 10.8]
print(type(b)) # prints type of 'b' i.e., [25, True, 10..8]


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } # Ref 's' points to set of 4 elements
print(s) # prints set 's' i.e., {'Hyd',  25,  True,  10.8} in any order
a , *b , c = s # unpacking set 's' 
print(a) # prints 'a' i.e., 'Hyd' 
print(b) # prints 'b' i.e., [25, True]
print(c) # prints 'c' i.e., 10.8


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10} # Ref 'a' points to set of 4 elements
print(s) # prints set 's' i.e., {20, 10} in any order
x , y = s # unpacking set 's' 
print(x) # prints 'x' i.e., 20 or 10
print(y) # prints 'y' i.e., 10 0r 20



# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10) # Ref 'a' points to range object from index 100 to index 149 in steps of 10
b = set(a) # range object 'a' is converted to set and assigned to 'b'
print(b) # prints set 'b' i.e., {100, 110, 120, 130, 140} in any order
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18] # Ref 'c' points to list of 9 elements
d = set(c) # list 'c' converts to set and assigned to 'd'
print(d) # prints set 'd' i.e., {10, 20, 15, 18, 10, 50, 20, 12, 18} any order
e = set('Rama  rAo') # string 'Rama rAo' converts to set and assigned to 'e'
print(e) # prints set 'e' i.e., {'R', 'a', 'm', 'a', ' ','r', 'A', 'o'} in any order
print(set(25)) # Error because set argument must be sequence of no arguments
print(set()) # prints empty set
