220825


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a) # error 
print(id(a)) # id of tuple
# How  to  modify  30  in  tuple  to  35
print(a[:2]+(35)+a[3:])
print(a) # (10 ,  20 ,  35 ,   40 ,  50)
print(id(a)) # id of  new tuple a 


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # error
del  a[2] # error
a . pop(2) # error
print(a)
print(id(a)) # id of tuple a
# How  to  remove  30  from  tuple  'a'
a = (a[:2]+a[3:])
print(a) # (10,20,40,50)
print(id(a)) # id of new tuple of 4 elements

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class tuple>
print(len(a)) # 3
print(a[0]) #How  to  print  1st  inner  tuple)
print(a[1]) #How  to  print  2nd  inner  tuple)
print(a[2]) #How  to  print  3rd  inner  tuple)
print(a[0][1]) # How  to  print  20)
print(a[1][2]) # How  to  print  50)
print(a[2][3]) # How  to  print  90)

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) # How  to   print  inner  tuple)
print(*a) # How  to   print  inner  tuple  in  another  way)
print(a[0][0]) # How   to  print   10)
print(a[0][1]) # How   to  print   20)
print(a[0][2]) # How   to  print   30)
b = ((),)
print(b[0]) # How  to   print  inner  tuple  of  tuple  'b')
print(*b) # How  to   print  inner  tuple  of  tuple  'b'  in  another  way)


#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # ((10 , 20 , 30))
print(*a) # 10,20,30
b = (())
print(b) # ()
print(*b) #  nothing

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #  <class str>
b = eval(a) 
print(b) # {10,20,15,18,12}
print(type(b)) # <class tuple>


#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # (10,20,30)
print({[10 , 20 , 30]}) # error
print({{10 , 20 , 30}}) # error
print({{}}) # error


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for item in a:
	print(item,end=' ')
# How  to  iterate  set  with  for  loop


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd','True',25,}
print(len(s)) # 3
print(type(s)) # <class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) # Hyd
print(b) # [25,  True,  10.8]
print(type(b)) #  <class list>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8}
a , *b , c = s
print(a) # Hyd
print(b) # [25,  True,]
print(c) # [10.8]



# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20 , 10}
x , y = s
print(x) # 10
print(y) # 20



# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {100,110,120,130,140}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)  # {'R','a','m',' ','r','A','o'}
print(set(25)) # error
print(set()) # set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''