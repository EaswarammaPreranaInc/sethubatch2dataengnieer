# Modify  following  program  such  that  results  are  synchronized
# i.e.  Outputs  should  be  [Hyd]
# 			   [Sec]
# 	                   [Cyb]

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
t3 . start()

#Program:
from threading import *
import time
lock = Lock()   
def disp(s):
    with lock:    
        print('[', s, end='')
        time.sleep(3)
        print(' ]')
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
2.#Modify  following  program  such  that  final  balance  should  be  1300
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
print('Final balance :  ' , ac . bal)

#Program:
from threading import *
import time
class Account:
    def __init__(self, acno1, bal1):     
        self.acno = acno1
        self.bal = bal1
        self.lock = Lock()               
    def credit(self, amt):
        s = current_thread().name
        with self.lock:                   
            print(f'{s} is depositing Rs. {amt} into account {self.acno}')
            x = self.bal
            time.sleep(1)
            self.bal = x + amt
            print(f'{s} completed deposit. Updated balance = {self.bal}')
ac = Account(25, 1000.0)
print('Initial Balance:', ac.bal)
t1 = Thread(target=ac.credit, name='Rama', args=(100,))
t2 = Thread(target=ac.credit, name='Sita', args=(200,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Final balance:', ac.bal)


3.#  Find  outputs  (Home  work)
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
r . release()#Error
print('End')

#Output:
# Locked
# Locked
# Unlocked
# Unlocked


4.# Find  outputs  (Home  work)
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

#Output:
# locked


5.#  Find  outputs (Home  work)
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

#Output:
# One is under execution
# Two is under execution
# Three is under execution
# One finished execution
# Four is under execution
# Two finished execution
# Five is under execution
# Three finished execution
# Six is under execution
# Four finished execution
# Seven is under execution
# Five finished execution
# Eight is under execution
# Six finished execution
# Nine is under execution
# Seven finished execution
# Eight finished execution
# Nine finished execution


6.#  Find  outputs
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

#Output:
4 != 24
7 != 5040


7.#  Find  outputs  (Home  work)
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

#Output:
# 1st thread locks object l1
# 2nd thread locks object l2
# Deadlock


8.#  Find  outputs  (Home  work)
from queue import * 
stack=Queue()
for i in range(1,6): # How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
    stack.put(10 * i)
print('Deleted  elements')
while not stack.empty(): # How  to  remove  each  element  of   stack  object  and  also  print
    print(stack.get())
print(stack . get())
print('End')

#Output
# Deleted  elements
# 10
# 20
# 30
# 40
# 50


9.#  Find  outputs  (Home  work)
# How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
# print('Deleted  elements')
# How  to  remove  each  element  of  object  pq  and  also  print
# print(pq . get())
# print('End')

#Program:
from queue import PriorityQueue
import random
# Create PriorityQueue object
pq = PriorityQueue()
# Insert 5 random elements into pq using for loop
for i in range(5):
    n = random.randint(1, 100)
    pq.put(n)
    print("Inserted:", n)
print("Deleted elements")
# Remove each element of pq and print it
while not pq.empty():
    print(pq.get())
print("End")



10.# Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while not q.empty():
    print(q.get())
print('End')#How  to  remove  each  tuple  of  object  'q'  and  also  print

#Output:
('Hyd', 10)
('Delhi', 20)
('Chennai', 15)
('Pune', 5)
('Mumbai', 12)
End


11.#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get())
print('End')#How  to  remove  each  tuple  of  stack  object  and  also  print

#Output:
('Mumbai', 12)
('Pune', 5)
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)
End


12.#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty():
    print(pq.get())
print('End')#How  to  remove  each  tuple  of  object  pq  and  also   print

#Output:
# pq.put((10, 'Hyd'))
# pq.put((20, 'Delhi'))
# Then output will come in ascending order of numbers.


13.# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while not pq.empty():
    print(pq.get())
print('End')#How  to  remove  each  tuple  of  object  pq  and  also  print

#Output:
('Hyd', 5)
('Hyd', 10)
('Hyd', 12)
('Hyd', 15)
('Hyd', 20)
End


14.#  Find  outputs (Home  work)
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
new . daemon = True #RuntimeError
time . sleep(5)
print('End  of  main  thread')

#Output:
False
False
True


'''(Home  work)
15.#Find  outputs

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

# Output :
One  :  1
One  :  2
Two  :  1
One  :  3
One  :  4
One  :  5
One  :  6
One  :  7
Three  :  1
Three  :  2
main  thread  is  dead
One  :  8
One  :  9
Three  :  3
One  :  10
Three  :  4
One is  dead
Three  :  5
Two  :  2
Three  :  6
Three  :  7
Two  :  3
Three  :  8
Two  :  4
Two  :  5
Two  :  6
Three  :  9
Three  :  10
Three is  dead
Two  :  7
Two  :  8
Two  :  9
Two  :  10
Two is  dead



16.#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate thru reversed object with next() function')
# Convert iterator to iterable again
r2 = reversed(a)
try:
    while True:
        print(next(r2))
        time.sleep(1)
except StopIteration:
    pass
print('Iterate thru reversed object with _next_() method')
r3 = reversed(a)
try:
    while True:
        print(r3._next_())
        time.sleep(1)
except StopIteration:
    pass
print('Iterate thru reversed object with for loop')
for ch in reversed(a):
    print(ch)
    time.sleep(1)

print('Unpack reversed object :', *reversed(a))
print('List of chars in reverse order :', list(reversed(a)))
print('Reverse string :', ''.join(reversed(a)))

# Output :
# Enter any string: HYD
# <class 'reversed'>
# <reversed object at 0x000001DF92EF8AF0>
# Iterate thru reversed object with next() function
# D
# Y
# H
# Iterate thru reversed object with _next_() method
# D
# Y
# H
# Iterate thru reversed object with for loop
# D
# Y
# H
# Unpack reversed object : D Y H
# List of chars in reverse order : ['D', 'Y', 'H']
# Reverse string : DYH


17.# Find  outputs (Home  work)
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

# Output :
# <class 'reversed'>
# <reversed object at 0x000002827BDCF670>
# 2759447082608
# D Y H


18.# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)

# Output :
# <class 'reversed'>
# True
# Hyd
# 10.8
# 25


19.#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
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
print('Iterate thru list_reverseiterator object with _next_() method')
r3 = reversed(a)
try:
    while True:
        print(r3._next_())
        time.sleep(1)
except StopIteration:
    pass
print('Iterate thru list_reverseiterator object with for loop')
for item in reversed(a):
    print(item)
    time.sleep(1)
print('Unpack list_reverseiterator object :', *reversed(a))
print('Reverse list :', list(reversed(a)))


20.#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)  # Error due Set not be reversible


21.#Can  dictionary  be  reversed  ? (Home  work)
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

# Output :
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


Tricky  program
22.#Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator

#Program:
# Input dictionary
d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
# Get reversed iterator of keys
r = reversed(d)
# Build reversed dictionary
rev_d = {key: d[key] for key in r}
print('Original dictionary:', d)
print('Reversed dictionary:', rev_d)

# Output :
Original dictionary: {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
Reversed dictionary: {'Sal': 10000.0, 'Emp Name': 'Rama Rao', 'Empno': 25}



23.# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
r1 = reversed(list(a.keys()))     # convert keys view to list before reversing
while True:
    try:
        print(next(r1))
        time.sleep(1)
    except StopIteration:
        break
print('Values in reverse order')
r2 = reversed(list(a.values()))   # convert values view to list before reversing
while True:
    try:
        print(next(r2))
        time.sleep(1)
    except StopIteration:
        break
print('Tuples in reverse order')
r3 = reversed(list(a.items()))    # convert items view to list before reversing
for x in r3:
    print(x)
    time.sleep(1)
print('Elements of each tuple in reverse order')
for k, v in reversed(list(a.items())):
    print(v, k)
    time.sleep(1)
print('Keys and values in reverse order')
for k, v in reversed(list(a.items())):
    print(f"{k} : {v}")
    time.sleep(1)

# Output :
Keys in reverse order
18
15
20
10
Values in reverse order
Kiran
Rajesh
Sita
Rama Rao
Tuples in reverse order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama Rao')
Elements of each tuple in reverse order
Kiran 18
Rajesh 15
Sita 20
Rama Rao 10
Keys and values in reverse order
18 : Kiran
15 : Rajesh
20 : Sita
10 : Rama Rao