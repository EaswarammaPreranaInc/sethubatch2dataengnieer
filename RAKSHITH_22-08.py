#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)    
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')


Output:- 
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15 is found 3 times 


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35   # Error tuple does not allow item assignment
print(a)    # (10,20,30,40,50)
print(id(a))    # Address of the tuple 10000
#SHow  to  modify  30  in  tuple  to  35
a=a[:2]+(35,)+a[3:]  # reference a is pointing to new tuple
print(a)    # (10,20,35,40,50)
print(id(a))    # Address of the new tuple 100001

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)  # Error tuple does not allow item deletion
#del  a[2]       # Error tuple is not shrinkable because it's immutable
#a . pop(2)      # Error tuple does not have attribute pop()
print(a)        # (10,20,30,40,50)
print(id(a))    # Address of the tuple 10000
#How  to  remove  30  from  tuple  'a'
a=a[:2]+a[3:]   # reference a is pointing to the new object tuple
print(a)    # (10,20,40,50)
print(id(a))    # Address of the new tuple 1000001

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)    # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))  # <class 'tuple'>
print(len(a))   # 3
print(a[0])     # (10,20)    #How  to  print  1st  inner  tuple
print(a[1])     #(30,40,50)  #How  to  print  2nd  inner  tuple
print(a[2])     # (60,70,80,90) #How  to  print  3rd  inner  tuple
print(a[0][1])   # 20          #How  to  print  20
print(a[1][2])   # 50          # How  to  print  50
print(a[2][3])   # 90          # How  to  print  90
print('Next')

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) # (10,20,30) How  to   print  inner  tuple
print(*a)    #(10,20,30)  How  to   print  inner  tuple  in  another  way
print(a[0][0])  # 10      How   to  print   10
print(a[0][1])  # 20      How   to  print   20
print(a[0][2])  # 30     How   to  print   30
b = ((),)
print(b[0])     # ()    How  to   print  inner  tuple  of  tuple  'b'
print(*b)       # ()    How  to   print  inner  tuple  of  tuple  'b'  in  another  way


#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)    # (10,20,30)
print(*a)   # 10 20 30
b = (())    
print(b)    # (())
print(*b)   # 


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')    # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)        # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))  # <class 'str'>
b = eval(a)     # converts list set to set
print(b)        # {10 , 12 , 15 , 20, 18}
print(type(b))  # <class 'set'>



#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10 , 20 , 30)}
print({[10 , 20 , 30]}) # set elements should not be mutable
print({{10 , 20 , 30}}) #  set elements should not be mutable
print({{}})          # set elements should not be mutable


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)    # {'Hyd',True , 10.8 ,25}
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
for i in a:
    print(i) # 25<nextline> True <nextline>  10.8 <nextline> 'Hyd' <nextline>
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)    # {25,True,'Hyd'})
print(len(s))   # 3
print(type(s))  # <class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)    # {25,10.8,True , 'Hyd'}
a , b , c , d = s
print(a)    # 25
print(b)    # 10.8 
print(c)    # True
print(d)    # Hyd


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)    # {25,10.8,True , 'Hyd'}
a , *b = s  
print(a)    # 25 
print(b)    # ['Hyd',10.8,True]
print(type(b))  # <class 'list'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)    # {25,10.8,True , 'Hyd'}
a , *b , c = s
print(a)    # 25
print(b)    # [10.8,True]
print(c)    # Hyd


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)    # {10,20}
x , y = s
print(x)    # 10
print(y)    # 20

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)  
print(b)    # {110,130,100,140,120,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)    # {18,12,20,10,15,50}
e = set('Rama  rAo')
print(e)    # {'a','R','o','m','A','r',' '}
#print(set(25))  # Error argument should be sequence
print(set())    # set()



set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
