'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]
'''
from threading import *
import time
l = Lock()
def disp(s):
	l.acquire()
	print('[' , s , end = '')
	time.sleep(3)
	print(' ]')
	l.release()
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()
'''
Outputs
[Hyd]
[Sec]
[Cyb]
'''









'''
Modify  following  program  such  that  final  balance  should  be  1300
'''
from threading import  *
import time
l = Lock()
class Account:
	def __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def credit(self , amt):
		l.acquire()
		s = current_thread() . name
		print(F'{s} is depositing Rs. {amt} into account {ac . acno}')
		x = self . bal
		time . sleep(1)
		self . bal = x + amt
		l.release()
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final balance : ' , ac . bal)
'''
Initial  Balance : 1000.0
Rama is depositing Rs. 100 into account 25
Sita is depositing Rs. 200 into account 25
Final balance : 1300.0
'''









#  Find  outputs  (Home  work)
from threading import RLock
r = RLock()
r . acquire()
print('Locked')
r . acquire()
print('Locked')
r . release()
print('Unlocked')
r . release()
print('Unlocked')
r . release() # Error, because RLock object is locked only 2 times
print('End')
'''
Outputs
Locked
Locked
Unlocked
Unlocked
'''









# Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire()
print('Locked')
l . acquire()
print('Locked')
l . release()
print('Unlocked')
l . release()
print('Unlocked')
print('End')
'''
Outputs
Outputs
Locked
Locked
Unlocked
Unlocked
End
'''









#  Find  outputs (Home  work)
from threading import *
import time
def f1():
	sem . acquire()
	name = current_thread() . name
	print(name , 'is   under   execution')
	time . sleep(1)
	print(name , 'finished  execution')
	sem . release()
sem = Semaphore(3)
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t4 = Thread(target = f1 , name = 'Four')
t5 = Thread(target = f1 , name = 'Five')
t6 = Thread(target = f1 , name = 'Six')
t7 = Thread(target = f1 , name = 'Seven')
t8 = Thread(target = f1 , name = 'Eight')
t9 = Thread(target = f1 , name = 'Nine')
t1 . start()
t2 . start()
t3 . start()
t4 . start()
t5 . start()
t6 . start()
t7 . start()
t8 . start()
t9 . start()
'''
Outputs
One is under execution
Two is under execution
Three is under execution
One finished  execution
Four is under execution
Three finished  execution
Two finished execution
Five is under execution
Six is under execution
Six finished  execution
Seven is under execution
Five finished execution
Eight is under execution
Four finished execution
Seven finished execution
Nine is under execution
Nine finished execution
Eight finished execution
'''









#  Find  outputs
from threading import *
import time
def fact(n):
	sem . acquire()
	if n > 0:
		x = n * fact(n - 1)
	else:
		x = 1
	sem . release()
	return   x
# End of the function
def disp(n):
	print(n , ' != ' , fact(n))
# End of the function
sem = Semaphore(8)
t1 = Thread(target = disp , args = (4,))
t2 = Thread(target = disp , args = (7,))
t1 . start()
t2 . start()
'''
Outputs
4! = 24
7! = 5040
'''









#  Find  outputs  (Home  work)
from threading import *
import time
def f1():
	l1 . acquire()
	print('1st  thread  locks  object  l1')
	time . sleep(1)
	l2 . acquire()
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def f2():
	l2 . acquire()
	print('2nd   thread  locks  object  l2')
	time . sleep(1)
	l1 . acquire()
	print('2nd   thread  is  under  execution')
	l1 . release()
	l2 . release()
	print('End  of  the  2nd   thread')
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1 . start()
t2 . start()
time . sleep(1)
print('Deadlock')
'''
Outputs
1st  thread  locks  object  l1
2nd   thread  locks  object  l2
Deadlock
'''









#  Find  outputs  (Home  work)
from queue import *  
stack = LifoQueue()  
for i in range(1, 6):
	stack.put(10*i) # How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not stack.empty():
    print(stack.get()) # How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get())
print('End')
'''
Outputs
Deleted  elements
50
40
30
20
10
thread waits
'''









#  Find  outputs  (Home  work)
from random import * 
from queue import *
pq = PriorityQueue()
for i in range(5):
	pq.put(randint(1,5)) # How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
while not pq.empty():
	print(pq.get()) # How  to  remove  each  element  of  object  pq  and  also  print
print(pq . get())
print('End')
'''
Outputs
Deleted  elements
3
5
3
2
1
thread waits
'''









# Find  outputs  (Home  work)
from queue import Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while not q.empty(): 
    print(q.get()) # How  to  remove  each  tuple  of  object  'q'  and  also  print
'''
Outputs
('Hyd' , 10)
('Delhi' , 20)
('Chennai' , 15)
('Pune' , 5)
('Mumbai' , 12)
'''









#  Find  outputs  (Home  work)
from queue import LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty(): 
    print(stack.get()) # How  to  remove  each  tuple  of  stack  object  and  also  print
'''
Outputs
('Mumbai' , 12)
('Pune' , 5)
('Chennai' , 15)
('Delhi' , 20)
('Hyd' , 10)
'''









# Find  outputs
from queue import  PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty(): 
    print(pq.get()) # How  to  remove  each  tuple  of  object  pq  and  also   print
'''
Outputs
('Chennai' , 15)
('Delhi' , 20)
('Hyd' , 10)
('Mumbai' , 12)
('Pune' , 5)
'''









# Find  outputs
from queue import PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while not pq.empty(): 
    print(pq.get()) # How  to  remove  each  tuple  of  object  pq  and  also  print
'''
Outputs
Deleted tuples
('Hyd' , 5)
('Hyd' , 10)
('Hyd' , 12)
('Hyd' , 15)
('Hyd' , 20)
'''









#  Find  outputs (Home  work)
from threading import *
import time
def f1():
	for i in range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()
print(main . daemon) # False
main . daemon = True # Error, because mainthread is always non daemon
new = Thread(target = f1)
print(new . daemon) # False
new . daemon = True 
print(new . daemon) # True
new . start()
new . daemon = True # Error, cannot set running thread to daemon
time . sleep(5)
print('End  of  main  thread')
'''
Outputs
False
False
True
child  thread
child  thread
child  thread
End  of  main  thread
'''









'''(Home  work)
Find  outputs

Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop  for  each  thread
'''
from threading import *
def f1():
	name = current_thread() . name
	for i in range(1 , 11):
		print(name , ' : ' , i)
	print(name , 'is  dead')
# End  of  the  function
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t3 . daemon = True
t1 . start()
t2 . start()
t3 . start()
print('main  thread  is dead')
'''
Outputs
One : 1
One : 2
One : 3
One : 4
One : 5
Two : 1
Two : 2
Two : 3
Two : 4
Two : 5
Three : 1
Three : 2
Three : 3
Three : 4
Three : 5
main  thread  is dead
Two : 6
Two : 7
Two : 8
Two : 9
Two : 10
One : 6
One : 7
One : 8
One : 9
One : 10
'''









#  How  to  print  reversed  object  in  different  ways  (Home  work)
#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
try:
    while True:
        print(next(r1))
except StopIteration:
	print() # How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   _next_   method')
r2 = reversed(a)
try:
	while True:
		print(r2.__next__())
except StopIteration:
	print() # How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
r3 = reversed(a)
for i in r3:
	print(i) # How  to  iterate  reversed  object   with  for  loop
r4 = reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
r5 = reversed(a)
print('List  of  chars  in  reverse  order  :  ' ,  list(r5))
r6 = reversed(a)
print('Reverse  string : ' , ''.join(reversed(a)))
'''
Outputs
Enter  any  string  :  Hyd
<class 'reversed'>
<reversed object at 0x000001D58FC89B40>
Iterate  thru  reversed  object  with   next   function
d
y
H

Iterate  thru  reversed  object  with   _next_   method
d
y
H

Iterate  thru  reversed  object  with   for  loop
d
y
H
Unpack  reversed  object  :  d y H
List  of  chars  in  reverse  order  :   ['d', 'y', 'H']
Reverse  string :  dyH
'''









# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0]) # Error, there is no index for reversed object
print(b[1 : 3]) # Error, there is no index for reversed object
print(b * 2) # Error, cannot multiply reversed and int 
print(len(b)) # Error, there is no len() function for reversed
'''
Outputs
<class 'reversed'>
type and address of object b
Address of object b
D Y H
'''









# Can  tuple  be  reversed ?   (Home  work)
import time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for x in b:
	print(x)
	time . sleep(1)
'''
Outputs
<class 'reversed'>
True
Hyd
10.8
25
'''
	








#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate   thru  list_reverseiterator  object  with   next()   function')
try:
	while True:
		print(next(r1))
except StopIteration:
	print() # How  to  iterate   list_reverseiterator  object  with   next()   function
print('Iterate  thru  list_reverseiterator  object  with   _next_()   method')
r2 = reversed(a)
try:
	while True:
		print(r2.__next__())
except StopIteration:
	print() # How  to  iterate   list_reverseiterator  object  with   _next_()  method
print('Iterate  thru  list_reverseiterator  object  with   for  loop')
r3 = reversed(a)
for i in r3:
	print(i) #  How  to  iterate   list_reverseiterator  object  with   for  loop
r4 = reversed(a)
print('Unpack  list_reverseiterator  object  :  ' , *r4)
r5 = reversed(a)
print('Reverse  list : ' , list(r5))
'''
Outputs
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x000002317A629A80>
Iterate   thru  list_reverseiterator  object  with   next()   function        
True
Hyd
10.8
25

Iterate  thru  list_reverseiterator  object  with   _next_()   method
True
Hyd
10.8
25

Iterate  thru  list_reverseiterator  object  with   for  loop
True
Hyd
10.8
25
Unpack  list_reverseiterator  object  :   True Hyd 10.8 25
Reverse  list :  [True, 'Hyd', 10.8, 25]
'''
	  








#  Can  set  be  reversed  ?  (Home  work) Yes
a = {10, 20, 15 , 18}
r = reversed(a)









# Can  dictionary  be  reversed  ? (Home  work)
import time
def disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(1)
		except:
			break
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
r1 = reversed(a . keys())
disp(r1)
r2 = reversed(a . values())
disp(r2)
r3 = reversed(a . items())
disp(r3)
r4 = reversed(a)
disp(r4)
'''
Outputs
18
15
20
10
Amar
Kiran
Sita
Rama
(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')
18
15
20
10
'''









'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed iterator
'''
a = eval(input("Enter dictionary:"))
r = reversed(a.items())
b = {}
for x, y in r:
	b[x] = y
print(b)
'''
Outputs
{'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
'''









# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
r1 = reversed(a.keys())
for i in r1:
	print(i) # Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
r2 = reversed(a.values())
for i in r2:
	print(i) # Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
r3 = reversed(a.items())
for i in r3:
	print(i) # Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order') 
r4 = reversed(a.items())
for x in r4:
	print((x[1], x[0])) # Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
r5 = reversed(a.items())
for x, y in r5:
	print(y, x) # Write  for  loop  to  reverse  keys  and  corresponding  values of dictionary