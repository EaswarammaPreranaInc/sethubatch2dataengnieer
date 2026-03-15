'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]
'''
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '')
	time . sleep(3)
	print(' ]')
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()

from threading import *
import time
l=Lock()
def disp(s):
    l.acquire()
    try:
        print('[', s, end='')
        time.sleep(3)
        print(']')
    finally:
        l.release()
t1 = Thread(target=disp, args=('Hyd',))
t2 = Thread(target=disp, args=('Sec',))
t3 = Thread(target=disp, args=('Cyb',))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

'''
Modify  following  program  such  that  final  balance  should  be  1300
'''
from  threading  import  *
import  time
class   Account:
	def  _init_(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def  credit(self , amt):
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal
		time . sleep(1)
		self . bal = x + amt
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final balance :  ' , ac . bal)

from threading import Thread, Lock, current_thread
import time
class Account:
    def __init__(self, acno1, bal1):
        self.acno = acno1
        self.bal = bal1
        self.lock = Lock()  
    def credit(self, amt):
        s = current_thread().name
        print(f'{s} is depositing Rs.{amt} into account {self.acno}')
        self.lock.acquire()
        try:
            x = self.bal
            time.sleep(1)  
            self.bal = x + amt
        finally:
            self.lock.release()
ac = Account(25, 1000.0)
print('Initial Balance:', ac.bal)
t1 = Thread(target=ac.credit, name='Rama', args=(100,))
t2 = Thread(target=ac.credit, name='Sita', args=(200,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Final balance:', ac.bal)

#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire()
print('Locked')
r . acquire()
print('Locked')
r . release()
print('Unlocked')
r . release()
print('Unlocked')
r . release()
print('End')

output:
Locked
Locked
Unlocked
Unlocked
End

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

output:
Locked
Error

#  Find  outputs (Home  work)
from threading import *
import time
def   f1():
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

output:
One is under execution
Two is under execution
Three is under execution
One finished execution
Two finished execution
Three finished execution
Four is under execution
Five is under execution
Six is under execution
Four finished execution
Five finished execution
Six finished execution
Seven is under execution
Eight is under execution
Nine is under execution
Seven finished execution
Eight finished execution
Nine finished execution

#  Find  outputs
from  threading  import *
import  time
def    fact(n):
	sem . acquire()
	if   n  >  0:
		x = n * fact(n - 1)
	else:
		x = 1
	sem . release()
	return   x
# End of the function
def    disp(n):
	print(n , ' != ' , fact(n))
# End of the function
sem = Semaphore(8)
t1 = Thread(target = disp , args = (4,))
t2 = Thread(target = disp , args = (7,))
t1 . start()
t2 . start()

output:
4!=24
7!=5040

#  Find  outputs  (Home  work)
from  threading  import  *
import  time
def  f1():
	l1 . acquire()
	print('1st  thread  locks  object  l1')
	time . sleep(1)
	l2 . acquire()
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def  f2():
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

output:
1st thread locks object l1
2nd thread locks object l2
Deadlock

#  Find  outputs  (Home  work)
How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get())
print('End')

from queue import LifoQueue
stack = LifoQueue()
for i in [10, 20, 30, 40, 50]:
    stack.put(i)
print('Deleted elements')
while not stack.empty():
    print(stack.get())
print('End')

#  Find  outputs  (Home  work)
How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
How  to  remove  each  element  of  object  pq  and  also  print
print(pq . get())
print('End')

from queue import PriorityQueue
import random
pq = PriorityQueue()
for i in range(5):
    n = random.randint(1, 100)  
    pq.put(n)
    print('Inserted:', n)
print('Deleted elements')
while not pq.empty():
    print(pq.get())
print('End')

# Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
How  to  remove  each  tuple  of  object  'q'  and  also  print                                  while not q.empty():
                                                                                                       print(q.get())
#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
How  to  remove  each  tuple  of  stack  object  and  also  print                                while not stack.empty():
                                                                                                         print(stack.get())

#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
How  to  remove  each  tuple  of  object  pq  and  also   print                                  while not pq.empty():
                                                                                                         print(pq.get())
# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
How  to  remove  each  tuple  of  object  pq  and  also  print                                 while not pq.empty:
                                                                                                      print(pq.get())

#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()
print(main . daemon)
main . daemon = True
new = Thread(target = f1)
print(new . daemon)
new . daemon = True
print(new . daemon)
new . start()
new . daemon = True
time . sleep(5)
print('End  of  main  thread')

output:
False
False
True
child thread
child thread
child thread
End of  main  thread

''(Home  work)
Find  outputs

Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop  for  each  thread
'''
from  threading  import  *
def    f1():
	name = current_thread() . name
	for  i  in  range(1 , 11):
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
print('main  thread  is  dead')

output:
main thread is dead
(Interleaved output of One, Two, Three for first 5 iterations)
One is dead
Two is dead

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   _next_   method')
How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
How  to  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  : ' ,  ???)
print('List  of  chars  in  reverse  order  :  ' ,  ???)
print('Reverse  string   :   ' , ???)

import time
a = input('Enter any string : ')   
r1 = reversed(a)
print(type(r1))         
print(r1)               
print('Iterate thru reversed object with next() function')
r2 = reversed(a)        
try:
    while True:
        print(next(r2))
except StopIteration:
    pass
print('Iterate thru reversed object with __next__() method')
r3 = reversed(a)
try:
    while True:
        print(r3.__next__())
except StopIteration:
    pass
print('Iterate thru reversed object with for loop')
r4 = reversed(a)
for ch in r4:
    print(ch)
print('Unpack reversed object : ', *reversed(a))
print('List of chars in reverse order : ',list(reversed(a)))
print('Reverse string:', ''.join(reversed(a)))

# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))                                                   <class 'reversed'>
print(b)                                                         <reversed object at 0x000001A2...>
print(id(b))                                                     1724839209488
print(*b)                                                        D Y H
print(b[0])                                                      Error
print(b[1 : 3])                                                  Error
print(b * 2)                                                     Error
print(len(b))                                                    Error

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)

output:
<class 'reversed'>
True
Hyd
10.8
25

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate   thru  list_reverseiterator  object  with   next()   function')
How  to  iterate   list_reverseiterator  object  with   next()   function
print('Iterate  thru  list_reverseiterator  object  with   _next_()   method')
How  to  iterate   list_reverseiterator  object  with   _next_()  method
print('Iterate  thru  list_reverseiterator  object  with   for  loop')
How  to  iterate   list_reverseiterator  object  with   for  loop
print('Unpack  list_reverseiterator  object  :  ' , ???)
print('Reverse  list  :  '  ,  ???)

import time
a = [25, 10.8, 'Hyd', True]
r1 = reversed(a)
print(type(r1))      
print(r1)            
print('Iterate thru list_reverseiterator object with next() function')
r2 = reversed(a)
try:
    while True:
        print(next(r2))
        time.sleep(1)
except StopIteration:
    pass
print('Iterate thru list_reverseiterator object with __next__() method')
r3 = reversed(a)
try:
    while True:
        print(r3.__next__())
        time.sleep(1)
except StopIteration:
    pass
print('Iterate thru list_reverseiterator object with for loop')
r4 = reversed(a)
for x in r4:
    print(x)
    time.sleep(1)
print('Unpack list_reverseiterator object : ', *reversed(a))
print('Reverse list : ', list(reversed(a)))

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)

output:
Error

# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
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

output:
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
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''

a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
r = reversed(a.items())
rev_dict = dict(r)
print('Original dictionary :', a)
print('Reversed dictionary :', rev_dict)

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary

import time
a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print('Keys in reverse order')
for k in reversed(a.keys()):
    print(k)
    time.sleep(1)
print('Values in reverse order')
for v in reversed(a.values()):
    print(v)
    time.sleep(1)
print('Tuples in reverse order')
for t in reversed(a.items()):
    print(t)
    time.sleep(1)
print('Elements of each tuple in reverse order')
for t in reversed(a.items()):
    print(tuple(reversed(t)))
    time.sleep(1)
print('Keys and values in reverse order')
for k, v in reversed(a.items()):
    print(k, ':', v)
    time.sleep(1)
