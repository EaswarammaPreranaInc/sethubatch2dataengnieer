'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop

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
'''

#Program:
import time
numbers = [10, 20, 15, 18, 5]
def square(x):
    return x * x
m = map(square, numbers)
print(type(m))
print(m)
for value in m:
    print(value)
    time.sleep(1)






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

#Output:
10
20
15
5
18






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






'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
				   1.8 * 40 +32
				   1.8 * 50 + 32
				   1.8 * 25 + 32

#sample output:

Enter list of Celsius temperatures: [10, 20, 15, 18]
Equivalent farenheit temperatures
50.0
68.0
59.0
64.4
'''

#Program:
import time
celsius = eval(input("Enter list of Celsius temperatures: "))
farenheit = map(lambda c: 1.8 * c + 32, celsius)
print("Equivalent farenheit temperatures")
for f in farenheit:
    print(f)
    time.sleep(0.5)






'''
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)

#sample output:

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

#Program:
import time
print("Powers of 2")
powers = map(lambda x: 2 ** x, range(10))
for p in powers:
    print(p)
    time.sleep(0.5)






'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
				      Area  of  radius  2.8
				      Area  of  radius  4.2
				      Area  of  radius  1.9

#sample output:

Enter list of radii : [3.5,2.8, 4.2,1.9]
Area of each radius in list the
38.48
24.63
55.42
11.34
'''

#Program:
import time
radii = eval(input("Enter list of radii : "))
print("Area of each radius in list the")
area = map(lambda r: 3.14159 * r * r, radii)
for a in area:
    print(round(a, 2))
    time.sleep(0.5)






'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored

#sample output:

Enter first first tuple : (10, 20, 30, 40) 
Enter second tuple : (1,2,3,4,5,6) 
Addition tuple : (11, 22, 33, 44)
'''

#Program:
t1 = eval(input("Enter first tuple : "))
t2 = eval(input("Enter second tuple : "))
result = tuple(map(lambda x, y: x + y, t1, t2))
print("Addition tuple :", result)






'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

#sample output:

Enter first list : [10,20,15,18,19,17]
Enter second list : [1,5, 3,2]
Multiplication list : [10, 100, 45, 36]
'''

#Program:
list1 = eval(input("Enter first list : "))
list2 = eval(input("Enter second list : "))
result = list(map(lambda x, y: x * y, list1, list2))
print("Multiplication list :", result)






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

#Output:
100
400
144
324
196






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

#Output:
40
30
36
50
34






'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function

#sample output:
Enter list of numbers (or) strings: [10,20,15,30,25,40,35] 
Largest element: 40
'''

#Program:
from functools import reduce
n = eval(input("Enter list of numbers (or) strings: "))
x = reduce(lambda a, b: a if a > b else b, n)
print("Largest element:", x)






# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)													# 1574






#Producer-Consumer  problem  with  synchronization

#Program:

from threading import *
import time
from random import randint
class buffer:
    def __init__(self):
        self.write = True
        self.cond = Condition()
        self.x = None
    def store(self, y):
        s = current_thread().name
        self.cond.acquire() 
        try:
            while not self.write:
                self.cond.wait()
            self.x = y
            print(s, 'stores', self.x)
            self.write = False
            self.cond.notify()
        except:
            self.cond.release()
    def ret(self):
        s = current_thread().name
        self.cond.acquire()
        try:
            while self.write:
                self.cond.wait()
            print(s, 'retrieves', self.x)
            self.write = True
            self.cond.notify()
        except:
            self.cond.release()
def f1(buf):
    i = 1
    while True:
        buf.store(i)
        i += 1
        time.sleep(randint(1, 4))
def f2(buf):
    while True:
        buf.ret()
        time.sleep(randint(1, 4))
buf = buffer()
p = Thread(target=f1, name='producer', args=(buf,))
c = Thread(target=f2, name='consumer', args=(buf,))
p.start()
c.start()
print('Press ctrl + break or Fn+B to stop')
