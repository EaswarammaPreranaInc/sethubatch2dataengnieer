# Producer-Consumer  problem
from threading import *
import time
from random import randint

class buffer:
    def __init__(self, cond):
        self.write = True
        self.cond = cond

    def store(self, y):
        self.cond.acquire()
        if self.write:
            s = current_thread().name
            self.x = y
            print(s, 'stores', self.x)
            self.write = False
            self.cond.notify()
        else:
            self.cond.wait()
        self.cond.release()

    def ret(self):
        self.cond.acquire()
        if self.write == False:
            s = current_thread().name
            print(s, 'retrieves', self.x)
            print()
            self.write = True
            self.cond.notify()
        else:
            self.cond.wait()
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

# End  of  the  function
cond = Condition()
buf = buffer(cond)
p = Thread(target=f1, name='producer', args=(buf,))
c = Thread(target=f2, name='consumer', args=(buf,))
p.start()
c.start()

print('Press ctrl + break or Fn+B to stop')

'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10 , 20 , 15 , 18 , 5]
def square(x):
     return x*x
m = map(square ,  list)
print(type(m))
print(m)
for x in m:
    print(x)
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
#10 20 15 5 18 

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
disp(m1) # India China USA UK 
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2) #150.5 200.2 300.3 210.4

'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
c=eval(input("Enter celsius temperatures list: "))
m=map(lambda x:x*1.8+32,c)
for x in m:
     print(x)

# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9 
#  using  map   iterator (Home  work)
m=map(lambda x:2**x,range(0,10))
for x in m:
     print(x)
    
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
r=eval(input("Enter the radii list: "))
m=map(lambda x:math.pi*(x**2),r)
for x in m:
     print(x)

'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
t1=eval(input("Enter 1st tuple:"))
t2=eval(input("Enter 2nd tuple:"))
m=map(lambda x,y:x+y,t1,t2)
l=[]
for x in m:
     l.append(x)
res=tuple(l)
print(res)

'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
l1=eval(input("Enter 1st list:"))
l2=eval(input("Enter 2nd list:"))
m=map(lambda x,y:x*y,l1,l2)
l=[]
for x in m:
     l.append(x)
print(l)

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
#10*10 20*20 12*12 18*18 14*14 

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
#40 30 36 50 34

'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
from functools import reduce
l=eval(input("Enter the list: "))
res=reduce(lambda x, y:max(x,y),l)
print(res)

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)#20*20+15*15+18*18+25*25 

