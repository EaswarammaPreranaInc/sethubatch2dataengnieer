#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1) #'15'is found three times
except:
		print(F'15  is  found  {a . count(15)} times') 
#How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35#tuple cannnot be modified due to it is immutable
print(a)#(10,20,30,40,50)
print(id(a))#address of the tuple
a=a[0:3:1]+(35,)+a[3:5:1] #How  to  modify  30  in  tuple  to  35
print(a)#(10,20,35,40,50)
print(id(a)) #address of the new tuple
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)#eeror: remove method is not there in tuple
#del  a[2]#error:del operator is not there in tuple
#a . pop(2)#error:pop method is not there because tuple is immutable
print(a)#(10,20,30,40,50)
print(id(a))#address of the tuple object
b=list(a)#How  to  remove  30  from  tuple  'a'
print(b)
b.remove(30)#remove 30 from the list
print(b)#[10,20,40,50]
a=tuple(b)#covert to list to tuple
print(a)#(10,20,40,50)
print(id(a))#address of the new tuple	
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#((10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90))
print(type(a))#<class 'tuple'>
print(len(a))#3
print(a[0])#(How  to  print  1st  inner  tuple)
print(a[1])#(How  to  print  2nd  inner  tuple)
print(a[2])#(How  to  print  3rd  inner  tuple)
print(a[0][1])#How  to  print  20)
print(a[1][2])#How  to  print  50)
print(a[2][3])#How  to  print  90)

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple)
#print(How  to   print  inner  tuple  in  another  way)
print(a[0][0])#How   to  print   10)
print(a[0][1])#How   to  print   20)
print(a[0][2])#How   to  print   30)
b = ((),)
print(b[0])#How  to   print  inner  tuple  of  tuple  'b')
#print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#(10,20,30)
print(*a)#unpacks the elements i.e 10 20 30
b = (())
print(b)#()
print(*b) #unpack the elementsi,e nothing
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')#{10,20,30,40,}
print(a)#{10,20,30,40,}
print(type(a))#<class 'set'>
b = eval(a) #convert set to tuple
print(b)#(10,20,30,40)
print(type(b))#<class 'tuple'>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10,20,30)}
#print({[10 , 20 , 30]})#list is mutable
#print({{10 , 20 , 30}})#error
#print({{}})#error
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{hyd,True,25,1,}
print(len(s))#5
print(type(s)) #<class 'set'>