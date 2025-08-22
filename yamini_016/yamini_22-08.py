#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15) 	# prints the 1st occurance of 15
	while  True:		# this while condition is always true until any error is occured
		print('15 is found at index : ' , i) # prints the next indexes of 15
		i = a . index(15 , i + 1) 	# searches for 15 from recently found index to the end
except:
		print(F'15  is  found  {a . count(15)}  times') # after last 15 when there are no more index method throws error instead this statement is printed with the count


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35		# error
print(a) 	# same tuple is being printed
print(id(a))	# the id of tuple is printed
#How  to  modify  30  in  tuple  to  35
a=a[:2]+(35,)+a[3:] # here we are slicing till 2nd index and adding 35 to the tuple and remaining elements are concatenated
print(a) # prints the modified tuple
print(id(a))	 #now as is pointing to new tuple id is modified


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # error as tuple dosent have remove method
del  a[2] 	 # error as del operator doesn't work for tuple
a . pop(2)  # error as pop operator doesn't work for tuple
print(a) # prints the same tuple as no modification is done
print(id(a))     # prints the id of tuple 'a' which is same as before
#How  to  remove  30  from  tuple  'a'
a=a[:2]+a[3:] # here slicing is used to remove 30 from tuple a[:2] gives (10, 20) and a[3:] gives (40, 50)
print(a) # prints the modified tuple    
print(id(a)) # prints the id of modified tuple 'a' which is different from previous id

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) 	# prints the nested tuple
print(type(a))	# type of a is tuple
print(len(a))	# returns 3 as there are 3 inner tuples
print(a[0] 	# How  to  print  1st  inner  tuple)
print(a[1]	# How  to  print  2nd  inner  tuple)
print(a[2]	# How  to  print  3rd  inner  tuple)
print(a[0][1]	# How  to  print  20)
print(a[1][2]	# How  to  print  50)
print(a[2][3]	# How  to  print  90)

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])	#How  to   print  inner  tuple)
print(*a)	#How  to   print  inner  tuple  in  another  way)
print(a[0][0]	#How   to  print   10)
print(a[0][1]	#How   to  print   20)
print(a[0][2]	# How   to  print   30)
b = ((),)
print(a[0])	# How  to   print  inner  tuple  of  tuple  'b')
print(*a)	#How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # prints the nested tuple as it is ((10 , 20 , 30))
print(*a) # unpacks the tuple and prints the 1st element of the tuple which is also a tuple (10 , 20 , 30)
b = (())
print(b)	# prints the nested tuple (())
print(*b)	# # unpacks the tuple and prints the element of the tuple ()

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')	# we will enter a set {10 , 20 , 15 , 18 , 20 , 12 , 18} but it takes as string set
print(a)	# prints the string as it is in same order with duplicates as it is a string
print(type(a)) 	# class str
b = eval(a)	# it removes duplicates and prints the set in any order like {10,15,20,12,18}
print(b)	# prints the set b
print(type(b))	# class set

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # prints the tuple within the set
print({[10 , 20 , 30]})    # error because se t can not have mutable elements like list
print({{10 , 20 , 30}})    # error because set can not have mutable elements like set
print({{}}) # error because set can not have mutable elements like dictionary

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function',)
print(a)
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
for x in a:
	print(x)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}	# set packing with individual elements
print(s) # prints the elements in any order
print(len(s)) # as there are 5 elements in set len is 5
print(type(s))	 # class set

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s	# set unpacking to individual elements to a,b,c,d
print(a)	# we dont know in which order the elements arre stored so we cant assign the elements until the order is known
print(b)	
print(c)
print(d)

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s # in the order the elements are stored the 1st element is assigned to a and remaining elemnts are assigned to b as a list
print(a)
print(b)
print(type(b)) # always a class list

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s # in the order the elements are stored 1st elemnt is assigned to a and last element to c and remaining elements to b in form of list
print(a)
print(b)
print(c)

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # prints set after removing duplicates {10,20}
x , y = s # we have 2 objects and 2 elements in set so those elements are assigned to x,y
print(x) # maybe 10
print(y) # maybe 20

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10) # range object is created from 100 to 150 in steps of 10
b = set(a) # converts range object to set
print(b) # prints {100, 110, 120, 130, 140, 150} in any order
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18] # list with duplicate values
d = set(c) # converts list to set removing duplicates
print(d) # prints {10, 12, 15, 18, 20, 50} in any order
e = set('Rama  rAo') # converts string to set removing duplicates and spaces
print(e) # prints {'m', 'a', 'R', ' ', 'o', 'r'} in any order
print(set(25)) # error as argument of set() should be sequence
print(set()) # prints empty set i.e set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
