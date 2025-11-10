
'''
Producer-Consumer  problem  with  synchronization

1) Add  two  more  variables  to  buffer  object  i.e.  write  variable  and  cond  object

2) What  does  buf . write = True  indicate ?  --->  Thread  'p'  can  write  a  value  to  the  buffer  object
     What  does  buf . write = False  indicate ?  ---> Thread  'p'  can  not  write  a  value  to  the  buffer  object

3) Initialize  write  variable  and  cond  object  in  the  constructor  of  buffer  class

4) What  does  thread  'p'  do  (4  events) ?  --->
     a) Write  a  vaclue  to  buf . x  when  buf . write = True
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
		self.cond=Condition()
	def   store(self ,  y):
		self.cond.acquire()
		while  not self.write:
			self.cond.wait()
		s = current_thread() . name
		self . x  =  y
		print(s  ,  'stores' ,  self . x)
		self.write=False
		self.cond.notify()
		self.cond.release()
	def   ret(self):
		self.cond.acquire()
		while self.write:
			self.cond.wait()
		s = current_thread() . name
		print(s  ,  'retrieves' ,  self . x)
		self.write=True
		self.cond.notify()
		self.cond.release()
def   f1(buf):
	i = 1
	while  True:
		buf . store(i)
		i += 1
		time . sleep(randint(1 , 4))
def  f2(buf):
	while  True:
		buf . ret()
		time . sleep(randint(1 , 4))
# End  of  the  function
buf = buffer()
p  = Thread(target = f1 , name = 'producer' , args = (buf,))
c  = Thread(target = f2 , name = 'consumer' , args = (buf,))
p . start()
c . start()
print('Press  ctrl + break  or  Fn+B  to  stop')

''' 
producer stores 1
consumer retrieves 1
Press  ctrl + break  or  Fn+B  to  stop
producer stores 2
consumer retrieves 2
producer stores 3
consumer retrieves 3
producer stores 4
consumer retrieves 4
producer stores 5
consumer retrieves 5
producer stores 6
consumer retrieves 6...so on'''






'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
def f1(x):
	return x*x
m = map(f1 ,  list)
print(type(m))
print(m)
for i in m:
	print(i)
	time.sleep(1)
''' 
<class 'map'>
<map object at 0x0000027D10AD22C0>
100
400
225
324
25
'''






# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
''' 
10
20
15
5
18'''






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
m1 = map(lambda  x  :  x['country'] , list)
print('Map   m1')
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)

''' 
Map   m1
India
China
USA
UK
Map   m2
150.5
200.2
300.3
210.4'''






'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
							        1.8 * 40 +32
								    1.8 * 50 + 32
								    1.8 * 25 + 32
'''

temp=eval(input('Enter list of celsius temperatures : '))
print('Equivalent Fahrenheit temperatures')
def c_to_f(c):
    return 1.8*c+32
faren=map(c_to_f,temp)
for i in faren:
    print(i)
'''    
Enter list of celsius temperatures : [10,20,15,18]
Equivalent farenheit temperatures
50.0
68.0
59.0
64.4
'''





# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)

def power(x):
    return 2**x
print('Powers of 2')
n=range(10)
res=map(power,n)

for i in res:
    print(i)
'''
Powers of 2
1
2
4
8
16
32
64
128
256
512
'''






'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
                                      Area  of  radius  2.8
                                      Area  of  radius  4.2
                                      Area  of  radius  1.9

'''
import math
r=eval(input('Enter list of radii'))
def radius(x):
    return math.pi*x**2
res=map(radius,r)
for i in res:
    print(f'{i:.2f}')
'''
Enter list of radii:
[3.5,2.8,4.2,1.9]
Area of each radius in the list
38.48
24.63
55.42
11.34
'''




'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored

'''

def add(x, y):
    return x + y

t1 = eval(input('Enter first tuple : '))
t2 = eval(input('Enter second tuple : '))
res = tuple(map(add, t1, t2))  
print('Addition tuple :')
print(res)
'''Enter first tuple :
(10,20,30,40)
Enter second tuple :
(1,2,3,4,5,6)
Addition tuple :
(11, 22, 33, 44)'''





'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

'''

def multiply(x, y):
    return x * y

l1 = eval(input('Enter first list : '))
l2 = eval(input('Enter second list : '))
res = list(map(multiply, l1, l2))   
print('Multiplication list :')
print(res)
'''
Enter first list :
[10,20,15,18,19,17]
Enter second list :
[1,5,3,2]
Multiplication list :
[10, 100, 45, 36]
'''





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
100
400
144
324
196
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
40
30
36
50
34'''






'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function

Enter list of numbers (or) strings:[10,20,15,30,25,40,35]
Largest element : 40
Press any key to continue
'''
from functools import *
l=eval(input('enter list of numbers or strings: '))
def large(x,y):
    if x>y:
        return x
    else:
        return y
r=reduce(large,l)
print('Largest element:' ,r)
Largest element: 40






# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
''' 
1574'''