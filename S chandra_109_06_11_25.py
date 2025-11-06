: '''
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
#################################################
from threading import *
import time

class Buffer:
    def _init_(self):
        self.x = None
        self.write = True       # True → producer can write, False → cannot write
        self.cond = Condition() # condition object for sync

    def store(self, v):   # Producer
        with self.cond:
            while not self.write:   # wait if writing is not allowed
                self.cond.wait()
            self.x = v
            print('Producer stored :', v)

            self.write = False      # producer cannot write again immediately
            self.cond.notify()      # notify consumer
            self.cond.wait()        # wait until consumer reads value

    def ret(self):      # Consumer
        with self.cond:
            while self.write:       # if write=True → no new value yet
                self.cond.wait()
            print('Consumer retrieved :', self.x)

            self.write = True       # allow producer to write next value
            self.cond.notify()      # notify producer
            self.cond.wait()

def f1(buf):       # Producer thread
    for i in range(5):
        buf.store(i)
        time.sleep(1)

def f2(buf):       # Consumer thread
    for i in range(5):
        buf.ret()
        time.sleep(2)

buf = Buffer()
t1 = Thread(target=f1, args=(buf,))
t2 = Thread(target=f2, args=(buf,))
t1.start()
t2.start()
t1.join()
t2.join()








: '''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  list)
print(type(m))
print(m)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
	time . sleep(1)

###################################
import time

def square(x):
    return x * x

lst = [10, 20, 15, 18, 5]
m = map(square, lst)

for i in m:
    print(i)
    time.sleep(1)








: # Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break

######################################

10
20
15
5
18





: # Find  outputs (Home  work)
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
######################
Map   m1
India
China
USA
UK
Map   m2
150.5
200.2
300.3
210.4






: '''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
####################################
def to_fahrenheit(c):
    return 1.8 * c + 32

celsius = [30, 40, 50, 25]
m = map(to_fahrenheit, celsius)

for temp in m:
    print(temp)
#####################
86.0
104.0
122.0
77.0






: # Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
##############################
import time

def power(n):
    return 2 ** n

m = map(power, range(10))   # 0 to 9

for v in m:
    print(v)
    time.sleep(1)
#############################
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






: '''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
##############################
def area(r):
    return 3.14159 * r * r

radius = [3.5, 2.8, 4.2, 1.9]
m = map(area, radius)

for a in m:
    print(a)
#########################
38.4849275
24.6304784
55.4171886
11.3412281







: '''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
#####################
t1 = (10, 20, 30, 40)
t2 = (1, 2, 3, 4, 5, 6)

m = map(lambda x, y: x + y, t1, t2)
t3 = tuple(m)
print(t3)
#####################
(11, 22, 33, 44)






: '''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
########################

l1 = [10, 20, 15, 18, 19, 17]
l2 = [1, 5, 3, 2]

m = map(lambda x, y: x * y, l1, l2)
l3 = list(m)
print(l3)
###################
[10, 100, 45, 36]




: # map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#################################
import time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda y: y % 2 == 0, map(lambda x: x ** 2, a))

for v in f:
    print(v)
    time.sleep(1)
######################
100
400
144
324
196






: # filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break

######################################
import time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda y: y + y, filter(lambda x: x >= 15, a))

for v in m:
    print(v)
    time.sleep(1)
#########################
40
30
36
50
34





: '''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
#########################################

from functools import reduce

a = [10, 20, 15, 30, 25, 40, 35]

largest = reduce(lambda x, y: x if x > y else y, a)
print("Largest element =", largest)
##########################
Largest element = 40





: # Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
##################################
Step-by-step evaluation:
 filter(lambda x: x >= 15, a)

Keeps only numbers ≥ 15 from list a

[20, 15, 18, 25]

 map(lambda y: y ** 2, ...)

Squares each value:
20² = 400
15² = 225
18² = 324
25² = 625
So map output = [400, 225, 324, 625]

 reduce(lambda x, y: x + y, ...)

Adds all values:

400 + 225 = 625
625 + 324 = 949
949 + 625 = 1574

Final Output:
1574
