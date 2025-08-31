'''#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
output:
 15 is found at index:2
 15 is found at index:5
 15 is found at index:8
 15 is found 3 times

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#a[2] = 35#error
print(a)#(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))#754
a=a[:3]+(35,)+a[3:5]#How  to  modify  30  in  tuple  to  35
print(a)#(10, 20, 30, 35, 40, 50)
print(id(a))#520

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
a . remove(30)#error
del  a[2]#error
a . pop(2)#error
print(a)#(10 , 20 , 30 , 40 , 50)
print(id(a))#516
a=a[:2]+a[3:5]#How  to  remove  30  from  tuple  'a'
print(a)#(10, 20, 40, 50)
print(id(a))#712

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class tuple>
print(len(a))#3
print(a[0])#(10,20)
print(a[1])#(30,40,50)
print(a[2])#(60,70,80,90)
print(a[0][1])#20
print(a[1][2])#50
print(a[2][3])#90

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])#(10 , 20 , 30)
print(*a)#(10 , 20 , 30)
print(a[0][0])#10
print(a[0][1])#20
print(a[0][2])#30
b = ((),)
print(b[0])#()
print(*b)#()

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#(10 , 20 , 30)
print(*a)#10,20,30
print(type(a))#<class tuple>
b = (())
print(b)#()
print(*b)#
print(type(b))#<class tuple>

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))#<class str>
b = eval(a)
print(b)#{10,20,15,18,12}
print(type(b))#<class set>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10,20,3)}
print({[10 , 20 , 30]})#error
print({{10 , 20 , 30}})#error
print({{}})#error

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(set(a))#(print 'set  with  print  function')
print(a)
for i in a:
    print(i)#print('Iterate  elements  of  set  with  for  loop')

output:
{True, 10.8, 'Hyd', 25}
{True, 10.8, 'Hyd', 25}
True
10.8
Hyd
25
    

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{True,'Hyd',25}
print(len(s))#3
print(type(s))#<class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#{'Hyd'}
print(b)#{True}
print(c)#10.8
print(d)#{25}

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{25,True,'Hyd',10.8}
a , *b , c = s
print(a)#{25}
print(b)#{10.8,'Hyd'}
print(c)#{True}

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{10,20}
x , y = s
print(x)#10
print(y)#20'''

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)#{'a','m','A','o','R','r'}
#print(set(25))#error
print(set())#set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''