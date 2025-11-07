                                NAME:M.SAICHARAN                  HOMEWORK
                                DATE:06-11-2025

1.#Modify  following  porgram  such  that
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

#Program:
import time
def square(x):
    return x * x
list1 = [10, 20, 15, 18, 5]
m = map(square, list1)
print(type(m))
print(m)
for value in m:
    print(value)
    time.sleep(1)


2.# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
#Output:
10
20
15
5
18


3.# Find  outputs (Home  work)
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

#Output:
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


4.#Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
			           1.8 * 40 +32
		                   1.8 * 50 + 32
			           1.8 * 25 + 32
#Program:
celsius = [30, 40, 50, 25]
fahrenheit = list(map(lambda c: 1.8 * c + 32, celsius))
print("Celsius Temperatures :", celsius)
print("Fahrenheit Temperatures :", fahrenheit)



5.# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
#Program:
import time
powers = list(range(10))
m = map(lambda x: 2 ** x, powers)
while True:
    try:
        print(next(m))
        time.sleep(1)
    except StopIteration:
        break


6.#Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
			              Area  of  radius  2.8
				      Area  of  radius  4.2
				      Area  of  radius  1.9

#Program:
import time
radii = [3.5, 2.8, 4.2, 1.9]
areas = map(lambda r: 3.14159 * r * r, radii)
for r, a in zip(radii, areas):
    print(f"Area of radius {r} = {a:.2f}")
    time.sleep(1)



7.#Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
#Program:
t1 = (10, 20, 30, 40)
t2 = (1, 2, 3, 4, 5, 6)
t3 = tuple(map(lambda x, y: x + y, t1, t2))
print("1st Tuple :", t1)
print("2nd Tuple :", t2)
print("3rd Tuple (Result) :", t3)



8.#Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
#Program:
list1 = [10, 20, 15, 18, 19, 17]
list2 = [1, 5, 3, 2]
list3 = list(map(lambda x, y: x * y, list1, list2))
print("1st List :", list1)
print("2nd List :", list2)
print("3rd List (Result) :", list3)



9.# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
#Output:
100
400
144
324
196



10.# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
#Output:
40
30
36
50
34


11.#Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
#Program:
from functools import reduce
a = [10, 20, 15, 30, 25, 40, 35]
largest = reduce(lambda x, y: x if x > y else y, a)
print("List :", a)
print("Largest element of list :", largest)


12.# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)

#Output:
1574



13.#Producer-Consumer  problem  with  synchronization

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

#Program:
from threading import Thread, Condition
import time
import random
class Buffer:
    def __init__(self):
        self.x = None             
        self.write = True         
        self.cond = Condition()  
    def store(self, value):
        with self.cond:
            while not self.write:         
                self.cond.wait()
            self.x = value                
            print(f'Producer produced: {self.x}')
            self.write = False            
            self.cond.notify()            
            time.sleep(1)
    def ret(self):
        with self.cond:
            while self.write:             
                self.cond.wait()
            print(f'Consumer consumed: {self.x}')
            self.write = True             
            self.cond.notify()            
            time.sleep(1)
def f1(buf):
    for i in range(1, 6):
        buf.store(i)
def f2(buf):
    for i in range(1, 6):
        buf.ret()
buf = Buffer()
p = Thread(target=f1, args=(buf,))
c = Thread(target=f2, args=(buf,))
p.start()
c.start()
p.join()
c.join()
print("End of main thread")

'''