#1) index()  and  count()  methods  demo  program   
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)# 2 5 8
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')#15  is  found  3  times
		




# 2)  How  to  modify  an  element  of  tuple ?   
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35#tuple is immutable
print(a)#(10, 20, 30, 40, 50)
print(id(a))#Address of a
a=a[0:3:1]+(35,)+a[3:5:1]#How  to  modify  30  in  tuple  to  35
print(a)#(10, 20, 30, 35, 40, 50)
print(id(a))#different address of a




# 3) Nested   tuple 
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))#<class 'tuple'>
print(len(a))#3
print(a[0])# (10, 20) ,  How  to  print  1st  inner  tuple
print(a[1])#(30, 40, 50) , How  to  print  2nd  inner  tuple
print(a[2])#(60, 70, 80, 90) ,  How  to  print  3rd  inner  tuple
print(a[0][1])#20 , How  to  print  20
print(a[1][2])#50 , How  to  print  50
print(a[2][3])#90 , How  to  print  90




# 4) How  to  delete  an  element  of  tuple ?  
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) # error remove method is not their in tuple
#del  a[2]# error cannot use del operatior
#a . pop(2)#error pop method is not their in tuple
print(a)#(10, 20, 30, 40, 50)
print(id(a))#Address of a
a=list(a)#How  to  remove  30  from  tuple  'a'
a.remove(30)
a=tuple(a)
print(a)#(10, 20, 40, 50)
print(id(a))#different address of a




# 5) Find  outputs 
a = ((10 , 20 , 30),)
print(a[0])#(10,20,30) , How  to   print  inner  tuple
print(*a)#(10,20,30) , How  to   print  inner  tuple  in  another  way
print(a[0][0])# 10 , How   to  print   10
print(a[0][1])#20 , How   to  print   20
print(a[0][2])#30 , How   to  print   30
b = ((),)
print(b[0])# () , How  to   print  inner  tuple  of  tuple  'b'
print(*b)#() , How  to   print  inner  tuple  of  tuple  'b'  in  another  way




# 6) Find  outputs 
a = ((10 , 20 , 30))
print(a)#(10, 20, 30)
print(*a)#10 20 30
b = (())
print(b)#()
print(*b)#empty tuple





# 7) What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{18, 20, 10, 12, 15}
print(type(b))#<class 'set'>




# 8)  Find  outputs 
print({(10 , 20 , 30)})#{(10, 20, 30)}
#print({[10 , 20 , 30]})#error
#print({{10 , 20 , 30}})#error
#print({{}})#error



#9)  How  to  print  set  in  differnet ways  
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)#{25, 10.8, 'Hyd', True}
print('Iterate  elements  of  set  with  for  loop')
for x in a:
	print(x)#How  to  iterate  set  with  for  loop
'''
25
10.8
Hyd
True'''



#10)  Find  outputs 
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{True, 'Hyd', 25}
print(len(s))#3
print(type(s))#<class 'set'>



# 11) Find  outputs  
s = {'Hyd',  25,  True,  10.8 }
print(s)#{25, 10.8, 'Hyd', True}
a , b , c , d = s
print(a)#25
print(b)#10.8
print(c)#Hyd
print(d)#True



# 12) Find  outputs  
s = {'Hyd',  25,  True,  10.8 }
print(s)#{25, 10.8, 'Hyd', True}
a , *b = s
print(a)#25
print(b)#[10.8, 'Hyd', True]
print(type(b))#<class 'list'>



#13) Find  outputs 
s = {'Hyd',  25,  True,  10.8 }
print(s)#{25, 10.8, 'Hyd', True}
a , *b , c = s
print(a)#25
print(b)#[10.8, 'Hyd']
print(c)#True



# 14) Find  outputs  
s = {20 , 10 , 20 , 10}
print(s)#{10, 20}
x , y = s
print(x)#10
print(y)#20




# 15) set()  function    
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)#{'o', 'A', 'm', 'R', 'r', ' ', 'a'}
#print(set(25))#error because 25 is non-sequence
print(set())#set()

