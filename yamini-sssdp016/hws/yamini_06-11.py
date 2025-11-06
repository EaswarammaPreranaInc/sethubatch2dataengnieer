'''
Producer-Consumer  problem  with  synchronization

1) Add  two  more  variables  to  buffer  object  i.e.  write  variable  and  cond  object

2) What  does  buf . write = True  indicate ?  --->  Thread  'p'  can  write  a  value  to  the  buffer  object
     What  does  buf . write = False  indicate ?  ---> Thread  'p'  can  not  write  a  value  to  the  buffer  object

3) Initialize  write  variable  and  cond  object  in  the  constructor  of  buffer  class

4) What  does  thread  'p'  do  (4  events) ?  --->
     a) Write  a  value  to  buf . x  when  buf . write = True
	 b) Modify  buf . write = False  becoz  thread  'p'  can  not  write  another  value  to  object  buf   immediately
	 c) Notify  thread  'c'  that  a  new  value  is  available  in  object   buf
	 d) Thread  'p'  waits  due  to   buf . write = False

5) What  does  thread  'c'  do  (4  events) ?  --->
	 a) Prints  buf . x  when  buf . write = False
	 b) Modify  buf . write = True  becoz  thread  'c'  can  not  print  same  value  again
	 c) Notify  thread  'p'  that  value  is  retrieved  from  object   buf
	 d) Thread  'c'  waits  due  to  buf . write = True

6) Modify  store()  and  ret()  methods  as  indicated  above
    and  also  add  constructor  to  buffer  class

7) Functions  f1() , f2()  and  the  code  outside  remains  same
'''

from  threading  import  *
import  time
from  random  import  randint
class  buffer:
	def __init__(self):
		self.write=True
		self.c=Condition()
	def   store(self ,  y):
		s = current_thread() . name
		self . x  =  y
		print(s  ,  'stores' ,  self . x)
	def   ret(self):
		s = current_thread() . name
		print(s  ,  'retrieves' ,  self . x)
def   f1(buf):
	i = 1
	while  True:
		buf.c.acquire()
		buf . store(i)
		i += 1
		buf . write = False
		buf.c.notify()
		buf.c.wait()
		time . sleep(randint(1 , 4))
def  f2(buf):
	while  True:
		buf.c.acquire()
		buf . ret()
		buf . write = True
		buf.c.notify()
		buf.c.wait()
		time . sleep(randint(1 , 4))
# End  of  the  function
buf = buffer()
p  = Thread(target = f1 , name = 'producer' , args = (buf,))
c  = Thread(target = f2 , name = 'consumer' , args = (buf,))
p . start()
c . start()
print('Press  ctrl + break  or  Fn+B  to  stop')



'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''

	
import  time
list = [10 , 20 , 15 , 18 , 5]
def f1(x):
	return x*x
m = map(f1,  list)
print(type(m))
print(m)
for x in m:
	print(x)


# Find  outputs (Home  work)
import   time
def  disp(m):
	while   True:
		try:
			print(next(m))
			time . sleep(1)
		except  StopIteration:
			break
list = [    { 'country' : 'India' , 'sale' : 150.5} ,
              { 'country' : 'China' , 'sale' : 200.2} ,
              { 'country' : 'USA' , 'sale' : 300.3} ,
              { 'country' : 'UK' , 'sale' : 210.4} ]
m1 = map(lambda  x  :  x['country'] , list) # lambda function returns each value of country from the dictonary x
print('Map   m1')
disp(m1)    # india,china,usa,uk
m2 = map(lambda  x  :  x['sale']  , list)   # lambda func returns each value of sales from dictonary x
print('Map   m2')
disp(m2)    # 150.5,200.2,300.3,210.4


'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''

l=eval(input())
m=map(lambda x:  1.8 * x+ 32, l)
for x in m:
    print(x)

# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)

import time
m=map(lambda x: 2**x,range(0,10))
print('powers of 2 :')
for i in m:
    print(i)
    time.sleep(1)

'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''


from time import *
l=eval(input('Enter list of radii'))
m=map(lambda x: 3.14159 * x * x,l)
print('Area of each radius in the list')
for x in m:
    print(x)

'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''

a=eval(input())
b=eval(input())
z1=zip(a,b)
m=map(lambda x : x[0]+x[1],z1)
for x in m:
    print(x)

'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''

a=eval(input())
b=eval(input())
z1=zip(a,b)
m=map(lambda x : x[0]*x[1],z1)
for x in m:
    print(x)

# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
1st inner map
lambda function select all the numbers and performs x**2
after performing filter is applied on the map result
now 100,400,144,324,196 are selected and remaining are ignored
	'''

# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
here 1st inner filter is applied on condition x>=15
so all the numbers with value >=15 i.e 20,15,18,25,17 are selected
now map is executed and all the values are doubled
so 40,30,36,50,34 are yielded and printed
'''

'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
from functools import reduce
l=eval(input())
def f1(x,y):
    
    return x if x>y else y
res=reduce(f1,l )
print(res)

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)

'''
1st filter os executed
filter(lambda  x  :  x  >= 15 , a)
so the values of list which asre >=15 are returned i.e 20,15,18,25
now map is selected 
map(lambda  y :  y ** 2 , filter)
each element is raised to power of 2
400,225,324,625 are yielded
now finally reduce function
it adds all the elements yieled
so 400+225+324+625=1574 is printed
'''

# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)  # lambda func returns the second element of tuple x
while   True:
	try:
		print(next(m))  # 10,20,15,5,18
		time . sleep(1)
	except  StopIteration:
		break

