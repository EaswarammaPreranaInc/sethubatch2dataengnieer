#Home Work-1
# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))# <class 'tuple'>
a[3] = 'Sec' #error, tuple is immutable
a[3 : 6] = 60 , 70 , 80 #error, tuple is immutable

#Home Work-2
#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a)) #(1,2,3) 2000 .. say address of that tuple object be 2000
a += b # new object is created
print(a , id(a)) #(1,2,3,4,5,6) 2001 .. say address of that tuple object be 2000

#Home Work-3
#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a)) #(1,2,3) 2000 .. say address of that tuple object be 2000
a = a+ b #new object is created, 
print(a , id(a)) #(1,2,3,4,5,6) 2001 .. say address of that tuple object be 2000

#Home Work-4
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #'(10 , 20 , 30 , 40)'
print(type(a)) # <class 'string'>
b = eval(a) 
print(b) #(10 , 20 , 30 , 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4

#Home Work-5
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 
print(a) #(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] #error, tuple is immutable
print(a) 

#Home Work-6
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 # a[1] is tuple which is immutable, so error
print(a) #[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a) #[[80 , 90] , (20 , 30 , 40) , 50 , 60]

#Home Work-7
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25,10.8,'Hyd',True)
print(type(x)) #<class 'tuple'>

#Home Work-8
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x 
print(a)#25
print(b)#10.8
print(c)#'Hyd'
print(d)#True
p , q , r =  x #error, we provided 3 references but tuple has 4 values 
a , b , c , d  , e = x # error, we provided 5 references but tuple has 4 values

#Home Work-9
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) #[10.8,'Hyd']
print(c) #True

#Home Work-10
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) #25
print(b) #10.8
print(c) #[]
print(d) #'Hyd'
print(e) #True

#Home Work-11
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#(3+3j)
print(d)#True
print(_)#(3+4j)

#Home Work-12
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) #(100,110,120,130,140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) 
print(d) #(10,20,15,18)
e = tuple('Vamsi') 
print(e) #('V','a','m','s','i')
print(tuple(25)) #error, argument should be sequence only
print(tuple()) #()


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  ---> Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''
