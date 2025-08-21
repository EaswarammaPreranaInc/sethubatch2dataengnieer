# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')  :
 [25 , 10.8 , 'Hyd' , True] 
print(type(a))  : <class 'str'> . default string 
print(a)   :  [25 , 10.8 , 'Hyd' , True] 
b = eval(a) 
print(b)   :  [25 , 10.8 , 'Hyd' , True] 
print(type(b)) : <class 'str'> 
 

#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) : true 
print(a  ==  b)  : true 
b[2] = 12
print(a)   : [10, 20, 15, 18]  


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]  
b = [100 , 200 , 150]
print(a + b)  : [10, 20, 15, 18, 100, 200, 150]
print(a + 5) : error , only append method  used 
print(a + '5')  : error
print([10 , 20] + (30 , 40))  : error

#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))  : [1, 2, 3]   15208680
a += b
print(a , id(a))  : [1, 2, 3, 4, 5, 6]    17839352


#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))  :  [1, 2, 3]   15208680
#a  = a + b
a+=b
print(a , id(a))  :  [1, 2, 3, 4, 5, 6]    17839352


# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]#  [25 , 10.8 , 'Hyd' , True] 
print(e)  #  [25 , 10.8 , 'Hyd' , True] 
print(type(e)) # , <class 'list'>

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b))  :< class 'list'>
x , *y = list
print('x : ' , x)  --> x:25 
print('y : ' , y)  --> y:[10.8 , 'Hyd', True]
*p , q = list
print('p : ' , p) --> p : [25, 10.8, 'Hyd']
print('q : ' , q) --> q: True


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a) --> a: 25
print('b : ' , b) --> b:10.8
print('c : ' , c) --> c: 'hyd'
print('d : ' , d) --> d: treu
print('e : ' , e) --> error
a , b , *c , d , e , f = list


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) : 25
print('b : ' , b) : 10.8
print('_ :  ' , _): 'Hyd'
print('d : ' , d) : True


#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) --> a: 25 
print('b : ' , b)--> b:10.8
print('_ : ' , _) --> _:3+4j
print('d : ' , d) --> d: True
print('_: ' , _) --> _: 3+4j 


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list
--> list name cant assigned to any variable 


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)  --> a:3+4j(re assigning )
print('b : ' , b)  --> b: 10.8
print('d : ' , d)  --> d:true

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list
print('a :  ' , a)   --> a: [25 , 10.8]
print('b :  ' , b)  -->  b: 'Hyd'
print('c :  ' , c)   --> c: True


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)  --> a:25
print('b : ' , b)  -->b:10.8
print('c : ' , c)  --> c:'Hyd'
print('d : ' , d) --> d:True 
a , b , c , d = list


# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) : true 
print(a  is   b) : false
print(a < c) : true
print(a > d) : true 
print(a >= c) : false
print(a <= d) : false
print(a != c) :true
print(a != b) : false
print(a == c) : false



# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) : false
print(a  is   b) : false