What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   
a = input('Enter  list  :  ')
print(type(a)) #<class 'str'>
print(a) #[25,10.8,'hyd',true]
b = eval(a)
print(b) #[25,10.8,'hyd',true]
print(type(b)) #<class 'list'>

print(a) a = [10, 20, 15, 18] 
b = a, b = [10, 20, 15, 18]
print(a is b) # True
print(a == b) # True
b[2] = 12
print(a) # [10, 20, 12, 18]

a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)              # [10, 20, 15, 18, 100, 200, 150]
print(a + 5)              # Error: int cannot be concatenate to list 
print(a + '5')            # Error: str cannot be concatenate to list
print([10 , 20] + (30 , 40))  # Error: tuple cannot be concatenate to list

a = [1,2,3]
b = [4,5,6]
print(a , id(a))   # [1, 2, 3] <138894487783872 >
a += b
print(a , id(a))   # [1, 2, 3, 4, 5, 6] <same_id>,  bcz new list is not created

a = [1,2,3]
b = [4,5,6]
print(a , id(a))   # [1, 2, 3] <134494720543168 >
a = a + b
print(a , id(a))   # [1, 2, 3, 4, 5, 6] <134494719362048 >

a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e) # [25, 10.8, 'Hyd', True]
print(type(e)) # <class 'list'>



list = [25 , 10.8 , 'Hyd' , True]
a , *b , c = list
print('a : ' , a) # a :  25
print('b : ' , b) # b : [10.8, 'Hyd']
print('c : ' , c) # c :  True
print(type(b)) # <class 'list'>
x , *y = list
print('x : ' , x) # x :  25
print('y : ' , y) # y : [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p) # p : [25, 10.8, 'Hyd']
print('q : ' , q) # q :  True

list = [25 , 10.8 , 'Hyd' , True]
a,b,c,d,e = list,  #  not enough values to unpack
a,b,*c,d,e = list
print('a : ' , a)  # a :  25
print('b : ' , b)  # b :  10.8
print('c : ' , c)  # c :  []
print('d : ' , d)  # d :  Hyd
print('e : ' , e)  # e :  True
a,b,*c,d,e,f=list,  # not enough values to unpack

list = [25 , 10.8 , 'Hyd' , True]
a , b , _ , d = list
print('a : ' , a)   # a :  25
print('b : ' , b)   # b :  10.8
print('_ :  ', _)   # _ :   Hyd
print('d : ' , d)   # d :  True

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)   # a :  (3+4j)
print('b : ' , b)   # b :  10.8
print('d : ' , d)   # d :  True

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , _ , d , _ = list
print('a : ' , a)   # a :  25
print('b : ' , b)   # b :  10.8
print('_ : ' , _)   # _ :  (3+4j)
print('d : ' , d)   # d :  True
print('_: ' , _)    # _:  (3+4j)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e = list # Error: multiple unpacking is not allowed in list

list = [[25 , 10.8] , 'Hyd' , True]   # Nested list
a , b , c = list
print('a :  ' , a)   # a :   [25, 10.8]
print('b :  ' , b)   # b :   Hyd
print('c :  ' , c)   # c :   True

list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)   # a :  25
print('b : ' , b)   # b :  10.8
print('c : ' , c)   # c :  Hyd
print('d : ' , d)   # d :  True
a , b , c , d = list # Error: not enough values to unpack 

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)   # True 
print(a is b)   # False 
print(a < c)    # True 
print(a > d)    # True  
print(a >= c)   # False 
print(a <= d)   # False 
print(a != c)   # True  
print(a != b)   # False 
print(a == c)   # False 

a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)   # False  
print(a is b)   # False 
