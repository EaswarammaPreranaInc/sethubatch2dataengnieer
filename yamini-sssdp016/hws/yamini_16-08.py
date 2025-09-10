# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ') #25 , 10.8 , 'Hyd' , True
print(type(a)) # class str
print(a) # '25'.'10.8','Hyd','True'
b = eval(a) # converts string input to list
print(b) # [25 , 10.8 , 'Hyd' , True]
print(type(b)) # class list

#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a       #assigning a to b
print(a  is  b) # comparing  references
print(a  ==  b) # comparing objects
b[2] = 12 # modifying 2nd value of b to 12
print(a) # printing a

#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18] # assigning the list to a
b = [100 , 200 , 150] # assigning the list to b
print(a + b) # concatenating the lists
print(a + 5) # cant add a element to list using + operator
print(a + '5') # cant add a element to list using + operator
print([10 , 20] + (30 , 40)) # cant add tuple to a list

#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) # prints list a and the id adress of a
a += b # concatenating the two lists and assigning to a
print(a , id(a)) # prints the concattenated list with same id


#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))# prints list a and the id address of a
a  = a + b #concatenating the two lists and assigning to a
print(a , id(a)) # prints the concatenated list with same id

# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d] # combining all the objects and assign them aslist to e
print(e) # prints the list object e
print(type(e))  # class <list>

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b)) # class list
x , *y = list
print('x : ' , x)  #  x :  25
print('y : ' , y) #  y : [10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) # p : [25,10.8,'Hyd']
print('q : ' , q) # q : True

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # error because we have 5 objects and only 4 elements in list
a , b , *c , d , e = list # assigns all the values to objects and assigns the remaining objects to c
print('a : ' , a)   # a : 25
print('b : ' , b)   # b : 10.8
print('c : ' , c)   # c : []
print('d : ' , d)   # d : Hyd
print('e : ' , e)   # e : True
a , b , *c , d , e , f = list # error because we have 6 objects and only 4 elements in list

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list # assigns the 4 objects to the elements of the list
print('a : ' , a) # a: 25
print('b : ' , b) # b: 10.8
print('_ :  ' , _) # _='Hyd'
print('d : ' , d)# d: True

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list # assigns a to 25 b to 10.8  a reference is updated to 'Hyd' d value is True a reference is again modified to 3+4j
print('a : ' , a) # a : 3+4j
print('b : ' , b) # b : 10.8
print('d : ' , d) # d : True

#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list # assigns a to 25 b to 10.8 _ to 'Hyd' d to True initially created _ is deleted and new _ is created with value 3+4j
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('_ : ' , _) # _ : 3+4j
print('d : ' , d) #d : True
print('_: ' , _) # _ = 3+4j

# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list # there are 2 unpackings in this statement which is not possible

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list # assigns 1st list object to a , 'hyd' to b and True to c
print('a :  ' , a) # a : [25,10.8]
print('b :  ' , b) # b : Hyd
print('c :  ' , c) # c : True


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list # assigns the elements of 1st list 25,10.8 to a and b c to 'Hyd' d to True
print('a : ' , a) # a: 25
print('b : ' , b) # b: 10.8
print('c : ' , c) # c: Hyd
print('d : ' , d) # d: True
a , b , c , d = list # w e have 4 objects in the left bus in the list we have only 3 objects

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # compare the elements of the objects a and b
print(a  is   b) # compares the references both are not same as list is mutable and not reusable false
print(a < c) # 1st non matching characters 15 and 25 are compared 15<25 true
print(a > d) # 1st non matching characters 15 and 7 are compared 15> 7 true
print(a >= c) # 1st non matching characters 15 and 25 15>=25 is false
print(a <= d) # 1st non matching characters 15 and 7 15<=7 is false
print(a != c) # 1st non matching characters 15 and 25 15!=25 is true
print(a != b) # there is no na=on matching character both are equal but a!=b is false
print(a == c) # 1st non matching characters 15 and 25 15==25 is false

# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # compares the elements of the lists as both are not same false
print(a  is   b) # compares the references as they both are not pointing to same object false



