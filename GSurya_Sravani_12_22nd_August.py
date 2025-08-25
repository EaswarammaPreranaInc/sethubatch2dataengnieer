#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
  i = a . index(15)
	while  True:
	    print('15 is found at index : ' , i)
	    i = a . index(15 , i + 1)
except:
   print(F'15  is  found  {a . count(15)}  times')#15 is found at index 3
15 is found at index 7
15 is found at index9
15 is found 3times 

 #  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)#(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))# address of tuple object a
How  to  modify  30  in  tuple  to  35#a[:2]+(35,)+a[3:]
print(a)##(10 ,  20 ,  35 ,   40 ,  50)
print(id(a))# newaddress of tuple a

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)#error
del  a[2]#error
a . pop(2)#error
print(a)#(10 , 20 , 30 , 40 , 50)
print(id(a))# address of tuple a
How  to  remove  30  from  tuple  'a'
print(a)#a=a[:3]+a[4:]
print(id(a))# new address of tuple object a
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)# ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#tuple class
print(len(a))#3
print(How  to  print  1st  inner  tuple)#a[0]
print(How  to  print  2nd  inner  tuple)#a[1]
print(How  to  print  3rd  inner  tuple)#a[2]
print(How  to  print  20)#a[0][1]
print(How  to  print  50)#a[1][3]
print(How  to  print  90)#a[3][3]

 # Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)#for x in a:
                     Print(x)
print(How  to   print  inner  tuple  in  another  way)#print(*a)
print(How   to  print   10)#print(a[0])
print(How   to  print   20)#print(a[1])
print(How   to  print   30)#print(a[2])
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
# for x in b:
           Print(x)
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)#print(*a)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#((10 , 20 , 30))
print(*a)#(10 , 20 , 30)
b = (())
print(b)#(())
print(*b)#()

 # What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{10 , 20 , 15 , 18 ,  12 }
print(type(a))# class set
b = eval(a)
print(b)#{10 , 20 , 15 , 18 ,  12 }
print(type(b))#set class

 #  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
print({[10 , 20 , 30]})#error
print({{10 , 20 , 30}})#error
print({{}})#error

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#
Print(*a)
print(a)#{25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')#
# for x in a:
           Print(i)
How  to  iterate  set  with  for  loop#
For i in a:
     Print(i)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)# {'hyd' , true , 25, 1}
print(len(s))#4
print(type(s))#set class


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#hyd
print(b)#25
print(c)#true
print(d)#10.8


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#{hyd,[25,true,10.8]}
print(b)#[25,true,10.8]
print(type(b))#list

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)#{hyd}
print(b)#[25,true]
print(c)#{10.8}

 # Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{20 , 10 , 20 , 10}
x , y = s
print(x)#{20}
print(y)#{10}

 # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d){10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)#{'r','a','m','a',' ','r','a','o'}
print(set(25))#error
print(set())#{}