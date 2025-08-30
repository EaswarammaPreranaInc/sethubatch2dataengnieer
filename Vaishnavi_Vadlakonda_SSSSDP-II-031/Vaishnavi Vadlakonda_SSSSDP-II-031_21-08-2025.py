# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # prints (25, 10.8, (3 + 4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) # prints type list i.e., <class 'tuple'>
a[3] = 'Sec' # Error because tuple is immutable
a[3 : 6] = 60, 70, 80 # Error because tuple is immutable








#  Find  outputs
a = (1,2,3) # Ref 'a' points to tuple 
b = (4,5,6) # Ref 'b' points to tuple
print(a , id(a)) # prints tuple 'a' and address of the tuple i.e., (1,2,3)<space>address of the tuple
a += b # a and b tuples are concatenated and assigned to 'a'
print(a, id(a)) # prints tuple 'a' of 6 elements and address of the tuple i.e., (1,2,3,4,5,6)<space>new address of the tuple of 6 elements








      


#  Find  outputs
a = (1,2,3) # Ref 'a' points to tuple 
b = (4,5,6) # Ref 'b' points to tuple
print(a , id(a)) # prints tuple 'a' and address of the tuple i.e., (1,2,3)<space>address of the tuple
a = a + b # a and b tuples are concatenated and assigned to 'a'
print(a, id(a)) # prints tuple 'a' and address of the tuple i.e., (1,2,3,4,5,6)<space>address of the tuple with 6 elements
      








#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ') # reads string input from user
print(a) # '(10 , 20 , 30 , 40)'
print(type(a)) # prints type of 'a' i.e., <class 'str'>
b = eval(a) # converts string input to tuple and assigned to 'b'
print(b) # prints tuple (10, 20, 30, 40)
print(type(b)) # prints type of 'b' i.e., <class 'tuple'>
print(len(b)) # prints number of elements in tuple 'b' i.e., 4










# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60) # Ref 'a' points to tuple 
a[1][0] = 70 # replaces 20 at index [1][0] with 70
print(a) # prints tuple i.e., (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90, 100] # Error because tuple is immutable,it cannot be modified
print(a) # prints tuple i.e., (10, [70, 30, 40], 50, 60)










# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60] # Ref 'a' points to list
a[1][0] = 70 # Error because tuple is immutable and cannot be modified
print(a) # prints list 'a' i.e, [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80, 90] # replaces (20, 30, 40) at index 1 with [80, 90]
print(a) # prints list 'a' i.e., [10, [80, 90], 50, 60]










# Find  outputs   (Home  work)
a = 25 # Ref 'a' points integer object 25
b = 10.8 # Ref 'b' points to float object 10.8
c = 'Hyd' # Ref 'c' points to string object 'Hyd'
d = True # Ref 'd' points to boolean object True
x = a , b , c , d # packs all elements to a tuple 'x'
print(x) # prints tuple 'x' i.e., (25, 10.8, 'Hyd', True)
print(type(x)) # prints type of'x' i.e., <class 'tuple'>









# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True  # Ref 'x' points to tuple
a , b , c , d = x # upacks all elements of tuple 'x'
print(a) # prints 25
print(b) # prints 10.8
print(c) # prints Hyd
print(d) # prints True
p , q , r =  x # Error because of too many values
a, b, c, d, e = x # Error because of few values









# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True # Ref 'x' points to tuple
a , *b , c = x
print(a) # prints 25
print(b) # prints [10.8, 'Hyd']
print(c) # prints True









# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True # Ref 'tpl' points to tuple
a , b , *c , d , e = tpl
print(a) # prints 25
print(b) # prints 10.8
print(c) # prints empty list i.e., []
print(d) # prints 'Hyd'
print(e) # prints True










# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j   # Ref 'x' points to tuple
a , b , _ , d , _= x 
print(a) # prints 25
print(b) # prints 10.8
print(_) # prints (3 + 4j)
print(d) # prints True
print(_) # prints (3 + 4j)



 







# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10) # Ref 'a' points to range object from index 100 to index 149 in steps og 10
b = tuple(a) # converts range object 'a' to tuple and assigned to 'b'
print(b) # prints tuple 'b' i.e., (100, 110, 120, 130, 140)
print(type(b)) # prints type of 'b' i.e., <class 'tuple'>
c = [10 , 20 , 15, 18] # Ref 'c' points to list
d = tuple(c) # converts list 'c' to tuple and assigned to 'd'
print(d) # prints tuple 'd' i.e., (10, 20, 15, 18)
e = tuple('Vamsi') # converts string 'Vamsi' to tuple and assigned to 'e'
print(e) # prints tuple 'e' i.e., ('V', 'a', 'm', 's', 'i')
print(tuple(25)) # Error because argument must be non-sequence
print(tuple()) # prints empty tuple i.e., ()
