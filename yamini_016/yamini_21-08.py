# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25 # tuple is assigned to reference a
print(a) # prints a
print(type(a)) # class tuple
a[3] = 'Sec' # error because tuple is immutable
a[3 : 6]=60,70,80 ## error because tuple is immutable

#  Find  outputs
a = (1,2,3) # tuple is assigned to object a
b = (4,5,6) # tuple is assigned to object b
print(a , id(a)) # prints a and its id
a += b # elements of b is added to a it is refr=erence assignment
print(a,id(a)) # prints the updated tuple and its id


#  Find  outputs
a = (1,2,3) # tuple is assigned to a
b = (4,5,6) # tuple is assigned to b
print(a , id(a)) # prints a and its id
a = a + b # a is pointed new concatenated tuple
print(a,id(a)) # prints a and its id which i modified

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ') # takes input as string tuple
print(a) # prints a as it is
print(type(a)) # class str as input function takes default input as string
b = eval(a) # converts string tuple to tuple
print(b) # prints the tuple
print(type(b)) # class tuple
print(len(b)) # counts the elements of the tuple

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)  # ttuple of list is assigned to a
a[1][0] = 70 # the element of inner list is modified
print(a) # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90,100] # error as 1st index is the element of tuple so modification not possible
print(a) # (10, [70, 30, 40], 50, 60)

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60] # we have list of tuple assigned to a
a[1][0] = 70 # as a[1] is a tuple we cant modify the elements of tuple
print(a) # [10, [70, 30, 40], 50, 60]
a[1] = [80,90] # replaces the existing tuple with a list [80,90]
print(a) # [10, [80, 90], 50, 60]

# Find  outputs   (Home  work)
a = 25 # assigns 25 to object a
b = 10.8 # assigns 10.8 to object b
c = 'Hyd' # assigns 'Hyd' to object c
d = True # assigns True to object d
x = a , b , c , d # multiple assignment of objects a,b,c,d
print(x) # prints (25, 10.8, 'Hyd', True)
print(type(x)) # class tuple

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True # assigns all the values to x
a , b , c , d = x  # multiple assignment to objects
print(a) # prints 1st element of tuple i.e 25
print(b) # prints 2nd element of tuple i.e 10.8
print(c) # prints 3rd element of tuple i.e Hyd
print(d) # prints 4th element of tuple i.e True
p , q , r =  x # error as we have 3 objects but we have 4 elements in tuple
a , b ,c,d,e=x # error as we have 5 objects but we have 4 elements in tuple 

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x # 1st assigns a object to 25 and c to True and then using * operator for b it packs the remaoning elements to b in a form pf ;ist
print(a) # prints 25
print(b) # prints [10.8 , 'Hyd']
print(c) # prints True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl # 1st assigns a object to 25 ,b to 10.8 , d to 'Hyd' and e to True and then using * operator for c it packs the remaoning elements to c in a form of list i.e []
print(a) # prints 25
print(b) # prints 10.8
print(c) # prints []
print(d) # prints 'Hyd'
print(e) # prints True

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x  # # 1st assigns a object to 25 ,b to 10.8 , _ to 'Hyd' , d to True , here 2nd anonymous object is created so intial object is deleted and final value of _is 3+4j
print(a) # prints 25 
print(b) # prints 10.8
print(_) # prints 3+4j
print(d) # prints True
print(_) # prints 3+4j


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10) # creates a range of values from 100 to 149 in steps of 10 i.e 100,110,120,130,140
b = tuple(a) # converts the range object to tuple
print(b) # prints tuple (100,110,120,130,140)
print(type(b)) # class tuple
c = [10 , 20 , 15, 18] # list is assigned to c
d = tuple(c) # converting or type casting list to tuple
print(d) # prints tuple (10,20,15,18)
e = tuple('Vamsi') # converting or type casting string to tuple 
print(e) # prints tuple ('v','a','m','s','i')
print(tuple(25)) # error as argument of tuple() should be sequence
print(tuple()) # empty tuple object is printed

'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  ---> Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''

