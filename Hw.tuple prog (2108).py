1.

 # Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)  #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) # <class tuple>
a[3] = 'Sec'  #Error
a[3 : 6] = 60 , 70 , 80.   #Error


2

 #  Find  outputs
a = (1,2,3) #ref a points to the tuple object
b = (4,5,6) #ref b points to the tuple object
print(a , id(a))  #(1,2,3) 1000say
a += b #    a=a+b
print(a , id(a))  # (1,2,3,4,5,6)  2000say


3


#  Find  outputs
a = (1,2,3)   #ref a points to the tuple object
b = (4,5,6)  # ref b points to the tuple object
print(a , id(a))  #(1,2,3) 1001(say)
a = a + b  # Add both tuple and assign to new reference a
print(a , id(a)) #(1,2,3,4,5,6) 1002(say)


4

 #  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #(10 , 20 , 30 , 40)
print(type(a))  #<class.str>
b = eval(a)  #convert str into tuple and assign to b
print(b)  #(10 , 20 , 30 , 40)
print(type(b))  #<class.tuple>
print(len(b))   #4


5

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)  #(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]  #error
print(a)  #(10 , [70 , 30 , 40] , 50 , 60)


6

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 # Error
print(a)  #[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)  #[10 , [80,90] , 50 , 60]


7

 # Find  outputs   (Home  work)
a = 25   #ref a points to int object
b = 10.8  #ref b points to float object
c = 'Hyd'  #ref c points to str object
d = True   #ref d points to bool object
x = a , b , c , d
print(x)  #(25,10.8,'Hyd',True)
print(type(x))  #<class tupl>


8

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True  #act as tuple
a , b , c , d = x
print(a)  #25
print(b)  #10.8
print(c)  #Hyd
print(d)  #True
p , q , r =  x  #Error
a , b , c , d  , e = x   #Error


9


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a ,b , c = x #   Assign the tuple to the a,*b,c
print(a)  #25
print(b)  #[10.8 ,'Hyd']
print(c)   #True


10


 # Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl  #error due to few elements
print(a)
print(b)
print(c)
print(d)
print(e)

11


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)   #25
print(b)  #10.8
print(_)  #3+4j
print(d)  #True
print(_)   #3+4j


12


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10) # range from 100-149 in steps of 10 i.e.100,110,120,130,140
b = tuple(a)#(100,110,120,130,140)
print(b)   #(100,110,120,130,140)
print(type(b))  # <Class tuple>
c = [10 , 20 , 15, 18]#. Ref c points to list
d = tuple(c) # converts list to tuple
print(d)# (10,20,15,18)
e = tuple('Vamsi')# convert str to tuple
print(e)    #('V','a','m','s','i')
print(tuple(25)) # error arg should be sequence
print(tuple())  # empty tuple


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  ---> Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''