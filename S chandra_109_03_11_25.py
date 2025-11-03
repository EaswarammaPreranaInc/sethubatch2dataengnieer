
: #  Find  outputs  (Home  work)
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
##################
Locked
Locked
Unlocked
Unlocked
Traceback (most recent call last):
  ...
RuntimeError: cannot release un-acquired lock





: # Find  outputs  (Home  work)
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
####################
Locked





: #  Find  outputs (Home  work)
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
########################
Output (approximate order):

One is under execution
Two is under execution
Three is under execution
One finished execution
Four is under execution
Two finished execution
Five is under execution
Three finished execution
Six is under execution
...





: #  Find  outputs
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
######################
4 != 24
7 != 5040






: #  Find  outputs  (Home  work)
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

##################
1st thread locks object l1
2nd thread locks object l2
Deadlock





: #  Find  outputs  (Home  work)
How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get())
print('End')
######################
from queue import LifoQueue

stack = LifoQueue()

# Inserting using for loop
for i in [10, 20, 30, 40, 50]:
    stack.put(i)

print('Deleted elements')
while not stack.empty():
    print(stack.get())

print('End')
##########################
Deleted elements
50
40
30
20
10
End




: #  Find  outputs  (Home  work)
How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
How  to  remove  each  element  of  object  pq  and  also  print
print(pq . get())
print('End')
###################################
from queue import PriorityQueue
import random

pq = PriorityQueue()

# Insert 5 random elements
for i in range(5):
    n = random.randint(1, 100)
    pq.put(n)

print('Deleted elements')
while not pq.empty():
    print(pq.get())

print('End')
######################
Deleted elements
7
45
63
84
91
End




: # Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
How  to  remove  each  tuple  of  object  'q'  and  also  print
### while not q.empty():
    print(q.get())
#################################
('Hyd', 10)
('Delhi', 20)
('Chennai', 15)
('Pune', 5)
('Mumbai', 12)




: #  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
How  to  remove  each  tuple  of  stack  object  and  also  print
while not stack.empty():
    print(stack.get())
##############################
('Mumbai', 12)
('Pune', 5)
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)



: #  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
How  to  remove  each  tuple  of  object  pq  and  also   print
while not pq.empty():
    print(pq.get())
###############################
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)
('Mumbai', 12)
('Pune', 5)




: # Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
How  to  remove  each  tuple  of  object  pq  and  also  print

print('Deleted tuples')
while not pq.empty():
    print(pq.get())
########################
Deleted tuples
('Hyd', 5)
('Hyd', 10)
('Hyd', 12)
('Hyd', 15)
('Hyd', 20)




: #  Find  outputs (Home  work)
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
print('End  of  main  thread')
########################################
False
True
True
child thread
child thread
child thread
End of main thread





: '''(Home  work)
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
print('main  thread  is  dead')
###########################################
from threading import *

def f1():
    name = current_thread().name
    for i in range(1, 11):
        print(name, ':', i)
    print(name, 'is dead')

t1 = Thread(target=f1, name='One')
t2 = Thread(target=f1, name='Two')
t3 = Thread(target=f1, name='Three')
t3.daemon = True

t1.start()
t2.start()
t3.start()

print('main thread is dead')

#################################
main thread is dead
One : 1
Two : 1
Three : 1
One : 2
Two : 2
Three : 2
One : 3
Two : 3
Three : 3
One : 4
Two : 4
Three : 4
One : 5
Two : 5
Three : 5





: #  How  to  print  reversed  object  in  different  ways  (Home  work)
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
print('Reverse  string   :   ' , ???)
##############################
import time
a = input('Enter any string: ')   # assume HYD
r1 = reversed(a)

print(type(r1))       # <class 'reversed'>
print(r1)             # iterator object address

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
for ch in reversed(a):
    print(ch)

print('Unpack reversed object:', *reversed(a))
print('List of chars in reverse order:', list(reversed(a)))
print('Reverse string:', ''.join(reversed(a)))
##############################
Enter any string: HYD
<class 'reversed'>
<reversed object at 0x...>
Iterate thru reversed object with next() function
D
Y
H
Iterate thru reversed object with __next__() method
D
Y
H
Iterate thru reversed object with for loop
D
Y
H
Unpack reversed object: D Y H
List of chars in reverse order: ['D', 'Y', 'H']
Reverse string: DYH





: # Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0])
print(b[1 : 3])
print(b * 2)
print(len(b))
##################
Output and Explanation
<class 'reversed'>
<reversed object at 0x...>
140720385654224   # (example id)
D Y H
print(b[0])         TypeError: 'reversed' object is not subscriptable
print(b[1:3])       same error
print(b * 2)        unsupported operand
print(len(b))       no __len__() defined
So only the print(*b) line works (prints characters in reverse order once).




: # Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
#############################
<class 'reversed'>
True
Hyd
10.8
25





: #  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
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
print('Reverse  list  :  '  ,  ???)
##########################################
import time

a = [25, 10.8, 'Hyd', True]
r1 = reversed(a)

print(type(r1))      # <class 'list_reverseiterator'>
print(r1)            # iterator address

print('Iterate thru list_reverseiterator object with next() function')
r2 = reversed(a)
try:
    while True:
        print(next(r2))
        time.sleep(0.5)
except StopIteration:
    pass

print('Iterate thru list_reverseiterator object with __next__() method')
r3 = reversed(a)
try:
    while True:
        print(r3.__next__())
        time.sleep(0.5)
except StopIteration:
    pass

print('Iterate thru list_reverseiterator object with for loop')
for x in reversed(a):
    print(x)
    time.sleep(0.5)

print('Unpack list_reverseiterator object:', *reversed(a))
print('Reverse list:', list(reversed(a)))
######################################
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x...>
Iterate thru list_reverseiterator object with next() function
True
Hyd
10.8
25
Iterate thru list_reverseiterator object with __next__() method
True
Hyd
10.8
25
Iterate thru list_reverseiterator object with for loop
True
Hyd
10.8
25
Unpack list_reverseiterator object: True Hyd 10.8 25
Reverse list: [True, 'Hyd', 10.8, 25]





: #  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)
#######################
TypeError: 'set' object is not reversible





: # Can  dictionary  be  reversed  ? (Home  work)
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

#####################################
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






: '''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''
#####################################
Original: {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
Reversed: {'Sal': 10000.0, 'Emp Name': 'Rama Rao', 'Empno': 25}






: # Find outputs
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
Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
#####################################
Keys in reverse order
18
15
20
10
Values in reverse order
Kiran
Rajesh
Sita
Rama rao
Tuples in reverse order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')
Elements of each tuple in reverse order
('Kiran', 18)
('Rajesh', 15)
('Sita', 20)
('Rama rao', 10)
Keys and values in reverse order
{18: 'Kiran', 15: 'Rajesh', 20: 'Sita', 10: 'Rama rao'}
