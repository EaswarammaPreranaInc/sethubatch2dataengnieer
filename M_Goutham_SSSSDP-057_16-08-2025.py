# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a)) # the input type is <class 'str'> because default input() takes str as input
print(a) #[25 , 10.8 , 'Hyd' , True]
b = eval(a) #List of int , float, str, bool elements
print(b) #[25 , 10.8 , 'Hyd' , True]
print(type(b)) #<class 'List'>


#  Find  outputs (Home  work)
a = [10, 20, 15, 18] #List of elements are assigned to reference a
b = a #reference b points to same referenece a
print(a  is  b) #True
print(a  ==  b) #True
b[2] = 12 #Here in the list index 2 element 15 is replaced with 12
print(a) #prints the updated list i.e [10, 20, 12, 18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18] #reference a points to a list
b = [100 , 200 , 150] #reference b points to a list
print(a + b) #[10, 20, 15, 18, 100, 200, 150] here both a and b lists are concatinated 
print(a + 5) #Error that we cannot concatinate sequence with non-sequence
print(a + '5') #Error that we cannot concatinate the str with list
print([10 , 20] + (30 , 40)) #Error we cannot concatinate list with tuple we can only concatinate list with list


#  Tricky  program
#  Find  outputs
a = [1,2,3] #Reference a points to list of int elements
b = [4,5,6] #Reference b points to list of int elements
print(a , id(a)) #Returns the list and address of list 
a += b #a = a+b #Here we are concatinating the list b into list a
print(a , id(a)) #Returns the concatinated list and same address


 #  Tricky  program
#  Find  outputs
a = [1,2,3] #Reference a points to list of int elements
b = [4,5,6] #Reference b points to list of int elements
print(a , id(a)) #Returns the list and address of list 
a = a + b #Here we are concatinating the list b into list a
print(a , id(a)) #Returns the concatinated list and different address because in the above line we are re-assigned new object to both lists



# List  packing
a = 25 #Reference a points to int 25
b = 10.8 #Reference b points to float 10.8
c = 'Hyd' #Reference c points to str 'Hyd'
d = True #Reference d points to bool obj True
e = [a , b , c , d] #Reference e points to list of elements which are a,b,c,d #here we are packing all the a b c d into a list of elements
print(e) #Returns the list of elements [25, 10.8, 'Hyd', True]
print(type(e)) #Returns the type i.e <class 'list'>


# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list # a = 25 ,b = [10.8, 'Hyd'], c = True
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b)) #<class 'list'>
x , *y = list #x = 25 and y = [10.8 , 'Hyd' ,  True]
print('x : ' , x) #x : 25
print('y : ' , y) #y : [10.8 , 'Hyd' ,  True]
*p , q = list #p = [25 , 10.8 , 'Hyd'] and q = True
print('p : ' , p) # p : [25 , 10.8 , 'Hyd'] 
print('q : ' , q) # q : True


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True] #Reference list points to list of elements
a , b , c , d , e = list  #Error because the objects are more than elements in the list 
a , b , *c , d , e = list #here list is unpacked and a = 25 ,b = 10.8 and *c = [] #Empty list ,d = 'Hyd' , e = True
print('a : ' , a) #Returns a : 25
print('b : ' , b) #Returns b : 10.8
print('c : ' , c) #Returns c : []
print('d : ' , d) #Returns d : 'Hyd'
print('e : ' , e) #Returns e : True
a , b , *c , d , e , f = list #Error objects are more than list elements


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True] #Reference list points to list of elements
a , b , _  , d = list  #Refereneces a, b,_:anonymous object and d points to each element in the list i.e a = 25, b = 10.8, _ = 'Hyd', d = True 
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('_ :  ' , _) # _ : 'Hyd'
print('d : ' , d) # d : True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j] #Reference list points to list of elements
a , b , a , d , a = list #Here initially a = 25 and next a = 'Hyd' and next a = 3 + 4j and finally reference a points to 3+4j
print('a : ' , a) # a : 3 + 4j
print('b : ' , b) # b : 10.8
print('d : ' , d) # d : True


#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j] #Reference list points to list of elements
a , b ,  _ , d , _  = list #Here a = 25 and b = 10.8 and _ = 'Hyd' ,d = True and again _ = (3+4j) here initially _ points to 'Hyd' and in the last it changes to (3+4j)
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('_ : ' , _) # _ : (3+4j)
print('d : ' , d) # d : True
print('_: ' , _) # _ : (3+4j)


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j] #Reference list points to list of elements
# a , *b , c , *d , e  = list #Error #Because when unpacking the list we can only use one '*' we cannot use more than one


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list #a = [25, 10.8] , b = 'Hyd' and c = True
print('a :  ' , a) # a : [25, 10.8]
print('b :  ' , b) # b : 'Hyd'
print('c :  ' , c) # c : True


 # Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True] #Reference list points to list of elements
[a , b] , c , d = list # a = 25 and b = 10.8 , c = 'Hyd' , d = True
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('c : ' , c) # c : 'Hyd'
print('d : ' , d) # d : True
a , b , c , d = list #Here a b c d references will points to each element in the above list and a points  to list to twp elements


# Comparing  Lists
a = [10 , 20 , 15 , 18] 
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #Here == operator compares the elements #Returns True
print(a  is   b) #Here 'is' operator compares the addresses #Returns False
print(a < c) #True
print(a > d) #True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18] 
b = [20 , 18 , 15 , 10]
print(a == b) #Returns the False #Elements are compared and 1st element of 1st list is not equal to the 1st element of second list
print(a  is  b) #Returns False #Because two references are compared 