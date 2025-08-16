# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ') # reads input from user i.e.,  '[25 , '10.8 , 'Hyd' , True]'
print(type(a)) # prints <class str>
print(a) # prints string '[25, 10.8, 'Hyd', True]'
b = eval(a) # converts string into list i.e, [25, 10.8, 'Hyd', True]
print(b) # prints list [25, 10.8, 'Hyd', True]
print(type(b)) # prints type of object 'b' i.e., <class list>











#  Find  outputs (Home  work)
a = [10, 20, 15, 18] # Ref 'a' points to list
b = a # Ref 'b' points to ref 'a'
print(a  is  b) # prints True
print(a  ==  b) # prints True
b[2] = 12 # replaces 15 at index 2 of list with 12
print(a)  # prints list i.e., [10, 20, 15, 18]










#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18] # Ref 'a' points to list [10 , 20 , 15 , 18]
b = [100 , 200 , 150] # Ref 'b' points to list [100 , 200 , 150]
print(a + b) # Concatenates lists a and b and prints [10 , 20 , 15 , 18, 100 , 200 , 150]
print(a + 5) # Error because cannot concatenate list and int
print(a + '5') # Error because list can only concatenate with list
print([10 , 20] + (30 , 40)) # Error because list and tuple cannot be concatenated











#  Tricky  program
#  Find  outputs
a = [1,2,3] # Ref 'a' points to list of 3 elements
b = [4,5,6] # Ref 'b' points to list of 3 elements
print(a , id(a)) # prints object 'a' [1, 2, 3] and address of list 
a += b # Concatenates lists a and b i.e., [1, 2, 3, 4, 5, 6]
print(a, id(a)) # prints object 'a' i.e,  [1, 2, 3, 4, 5, 6] and different address of list of 6 elements












#  Tricky  program
#  Find  outputs
a = [1,2,3] # Ref 'a' points to list of 3 elements [1, 2, 3]
b = [4,5,6] # Ref 'b' points to list of 3 elements [4, 5, 6]
print(a , id(a)) # prints object 'a' i.e., [1 ,2, 3] and address of the list of 3 elements
a  = a + b # Concatenates lists a and b
print(a, id(a)) # prints object 'a' i.e., [1, 2, 3, 4, 5, 6] and address of the list of 6 elements














# List  packing
a = 25 # Ref 'a' points to int object 25
b = 10.8 # Ref 'b' points to float object 10.8
c = 'Hyd' # Ref 'c' points to str object 'Hyd'
d = True # Ref 'd' points to bool object True 
e = [a , b , c , d] # Ref 'e' points list of 6 elements
print(e) # prints list i.e., [25, 10.8, 'Hyd', True]
print(type(e)) # prints type of 'e' i.e., <class list>













# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True] # Ref 'list' points to list of 4 elements
a , *b , c = list
print('a : ' , a)  # prints a :  25
print('b : ' , b) # prints b : [10.8 , 'Hyd']
print('c : ' , c) #  prints c :  True
print(type(b)) # prints type of 'b' i.e., <class list>
x , *y = list
print('x : ' , x) # prints x : 25
print('y : ' , y) # prints y : [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p) # prints p : [25, 10.8, 'Hyd']
print('q : ' , q) # prints q : True











# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # Error because of few values to unpack
a , b , *c , d , e = list # Error because of few values to unpack
print('a : ' , a) # Error because 'a' is not defined
print('b : ' , b) # Error because 'b' is not defined
print('c : ' , c) # Error because 'c' is not defined
print('d : ' , d) # Error because 'd' is not defined
print('e : ' , e) # Error Error because 'e' is not defined
a , b , *c , d , e , f = list # Error because few values to unpack












# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # prints a : 25
print('b : ' , b) # prints b : 10.8
print('_ :  ' , _) # prints _ : Hyd
print('d : ' , d) # prints d : True












# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #  prints a : (3 + 4j)
print('b : ' , b) # prints b : 10.8
print('d : ' , d) # prints d : True









#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) # prints a : 25
print('b : ' , b) # prints b : 10.8
print('_ : ' , _) # prints _ : (3 + 4j)
print('d : ' , d) # prints d = True
print('_: ' , _) # prints _ : (3 + 4j)












# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e =list # Error because there should not be multiple *s












# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list  
print('a :  ' , a) # prints a : [25, 10.8]
print('b :  ' , b) # prints b : 'Hyd'
print('c : ' , c) # prints c : True












# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # prints a : 25
print('b : ' , b) # prints b : 10.8
print('c : ' , c) # prints c : 'Hyd'
print('d : ' , d) # prints d : True
a, b, c, d = list # Error because few values to unpack








# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # prints True
print(a  is   b) # prints False
print(a < c) # prints True
print(a > d) # prints True
print(a >= c) # prints False
print(a <= d) # prints False
print(a != c) # prints False
print(a != b) # prints True
print(a == c) # prints False










# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # prints False
print(a is b) # prints False