
#1st program
#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}times')
#output
'''
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3times
'''
#2nd program
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35#error, tuple is immutable
print(a)#(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))#address of the tuple(10 ,  20 ,  30 ,   40 ,  50)
#How  to  modify  30  in  tuple  to  35
a=a[:3]+(35,)+a[3:]
print(a)#(10 ,  20 ,  30 , 35 ,  40 ,  50)
print(id(a))#address of the tuple(10 ,  20 ,  30 , 35 ,  40 ,  50)


#3rd program
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)#error
#del  a[2]#error
#a . pop(2)#error
print(a)#(10 , 20 , 30 , 40 , 50)
print(id(a))#address of the tuple (10 , 20 , 30 , 40 , 50)
#How  to  remove  30  from  tuple  'a'
a=list(a)
a.remove(30)
a=tuple(a)
print(a)#(10 , 20 , 40 , 50)
print(id(a))#address of the tuple (10 , 20 , 40 , 50)


#4th program
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class'tuple'>
print(len(a))#3
print(a[0])#How  to  print  1st  inner  tuple
print(a[1])#How  to  print  2nd  inner  tuple
print(a[2])#How  to  print  3rd  inner  tuple
print(a[0][1])#How  to  print  20
print(a[1][2])#How  to  print  50
print(a[2][3])#How  to  print  90

#5th program
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple)
print(*a)#How  to   print  inner  tuple  in  another  way)
print(a[0][0])#How   to  print   10)
print(a[0][1])#How   to  print   20)
print(a[0][2])#How   to  print   30)
b = ((),)
print(b[0])#How  to   print  inner  tuple  of  tuple  'b')
print(*b)#How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

#6th program
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#((10 , 20 , 30))
print(*a)#10 , 20 , 30
b = (())
print(b)#(())
print(*b)# empty tuple

#7th program
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))#<class'str'>
b = eval(a)
print(b)#{10 , 20 , 15 , 18 , 12 }
print(type(b))#<class'set'>


#8th program
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
#print({[10 , 20 , 30]})#error set cannot contain mutable elements
#print({{10 , 20 , 30}})#error nested set is not permitted
#print({{}})#error dict is not permitted as it is mutable


#9th program
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)#{25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
for x in a:
    print(x)

#10th program
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd',True,25}
print(len(s))#3
print(type(s))#<class'set'>

#11th program
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#'hyd'
print(b)#25
print(c)#True
print(d)#10.8 in any order

#12th program
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#25(suppose)
print(b)#['Hyd',True,10.8] in any order
print(type(b))#<class'list'>

#13th program
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }in any order
a , *b , c = s
print(a)#25(suppose)
print(b)#[True,10.8]in any order
print(c)#'Hyd'(suppose)

#14th program
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{20 , 10 } in any order
x , y = s
print(x)#20(suppose)
print(y)#10

#15th program
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150} in any order
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)#{'R','a','m',' ','r','A','o'} in any order
#print(set(25))#error
print(set())#set()
