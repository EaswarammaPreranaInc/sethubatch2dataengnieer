
# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a)) # <class str>>
print(a) # [25 , 10.8 , 'Hyd' , True]
b = eval(a)
print(b) # [25 , 10.8 , 'Hyd' , True]
print(type(b)) # <class list>


#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) # True
print(a  ==  b) # True
b[2] = 12
print(a)  # [10, 20, 12, 18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10, 20, 15, 18, 100, 200, 150]
print(a + 5) # list concatenate with list
print(a + '5') # list concatenate with list
print([10 , 20] + (30 , 40)) # list concatenate with list


#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) # [1,2,3] id(a)
a += b
print(a , id(a)) # [1,2,3,4,5,6] id(a)


#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) # [1,2,3] id(a)
a  = a + b
print(a , id(a)) # [1,2,3,4,5,6] id different from above a  


# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e) # [25,10.8,'Hyd',True]
print(type(e)) # <class list>


# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b)) # <class list>
x , *y = list
print('x : ' , x) # x : 25
print('y : ' , y) # y:[10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) # [25,10.8 , 'Hyd']
print('q : ' , q) # True


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # error
a , b , *c , d , e = list # error
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list # error


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a:25
print('b : ' , b) # b:10.8
print('_ :  ' , _) # _:Hyd
print('d : ' , d) # d:True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) # (3+4j)
print('b : ' , b) # 10.8
print('d : ' , d) # True


#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) # a:25
print('b : ' , b) # b:10.8
print('_ : ' , _) # _ :(3+4j)
print('d : ' , d) # d:True
print('_: ' , _)# _:(3+4j)


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list
print('a :  ' , a) # a:[25 , 10.8]
print('b :  ' , b) # b:Hyd
print('c :  ' , c) # c:True


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # a:25
print('b : ' , b) # b:10.8
print('c : ' , c) # c:Hyd
print('d : ' , d) # d:True
a , b , c , d = list # error


# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True
print(a  is   b) # False
print(a < c) # True
print(a > d) # True
print(a >= c) # False
print(a <= d) # False
print(a != c) # True
print(a != b) # False 
print(a == c) # False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False
print(a  is   b) # False





