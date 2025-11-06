'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]
'''
from  threading  import *
import  time

def   disp(s):
	l.acquire()
	print('[' , s , end = '')
	time . sleep(3)
	print(' ]')
	l.release()
l=Lock()
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()

'''
Modify  following  program  such  that  final  balance  should  be  1300
'''
from  threading  import  *
import  time
class   Account:
	def  __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def  credit(self , amt):
		l.acquire()
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal
		time . sleep(1)
		self . bal = x + amt
		l.release()
l=Lock()
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final balance :  ' , ac . bal)

#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire()
print('Locked') #Locked
r . acquire()
print('Locked') #Locked
r . release()
print('Unlocked') #unlocked
r . release() #error already released
print('Unlocked')
r . release()
print('End')

# Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire()
print('Locked') #locked
l . acquire() #error cannot be locked again
print('Locked')
l . release()
print('Unlocked') #unlocked
l . release()
print('Unlocked')
print('End') 

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
# one is under execution 
# two is under execution
#three is under execution 
# one is finihed 
# two is finished
#three is finished 

# four is under execution 
# five is under execution
#six is under execution 
# four is finihed 
# five is finished
#six is finished 

# seven is under execution 
# eight is under execution
#nine is under execution 
# seven is finihed 
# eight is finished
#nine is finished 

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
t1 = Thread(target = disp , args = (4,)) #24
t2 = Thread(target = disp , args = (7,))# 5040
t1 . start()
t2 . start()

#  Find  outputs  (Home  work)
from  threading  import  *
import  time
#1st thread locks object l1
#2nd thread locks the object l2
#t1 is wating for unlocking of l2where it locked l1 and t2 is wating for
#  unlocking of l1 and locked l2
#so deadlock
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

#  Find  outputs  (Home  work)
from queue import LifoQueue
s=LifoQueue()
for i in range(1,6):
	s.put(i*10)
# How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
# How  to  remove  each  element  of   stack  object  and  also  print
while not s.empty():
	print(s.get())
print('End')

#  Find  outputs  (Home  work)
from queue import PriorityQueue
from random import randint
pq=PriorityQueue()
for i in range(5):
	pq.put(randint())
# How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
# How  to  remove  each  element  of  object  pq  and  also  print
while not pq.empty():
    print(pq . get())
print('End')

# Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
# How  to  remove  each  tuple  of  object  'q'  and  also  print
while not q.empty():
	print(q.get())
	
#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
# How  to  remove  each  tuple  of  stack  object  and  also  print
while not stack.empty():
	print(stack.get())
	
#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
# How  to  remove  each  tuple  of  object  pq  and  also   print
while not pq.empty():
	print(pq.get())
	
#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()
print(main . daemon) #False
main . daemon = True
new = Thread(target = f1) 
print(new . daemon)#False
new . daemon = True
print(new . daemon) #True
new . start() # child thread child thread, 
new . daemon = True # not possible to chnage daemon after executing it.
time . sleep(5)
print('End  of  main  thread')
#child thread or end of main thread
#child thread
#child thread 

'''(Home  work)
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
t1 . start() # one 1, one 2, one 3, one 4, one 5
t2 . start() # two 1 , two 2, two 3, two 4, two 5
t3 . start() # three 1, three 2, three 3, three 4, three 5
print('main  thread  is  dead') # main thread is thread 
# one 6 to 10 
#two 6 to 10 
# three 6 to 10 

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1)) # reversed
print(r1)#reversed address
print('Iterate  thru  reversed  object  with   next   function')
# How  to  iterate  reversed  object  'r'  with  next()  function
while True:
	try:
		print(next(r1))
	except:
		pass
r2=reversed(a)
while True:
	try:
		print(r2.__next__())
	except:
		pass
print('Iterate  thru  reversed  object  with   __next__   method')
# How  to  iterate  reversed  object   with  __next__()   method
print('Iterate  thru  reversed  object  with   for  loop')
r3=reversed(a)
for x in r3:
	print(x)
# How  to  iterate  reversed  object   with  for  loop
r4=reversed(a)
r5=reversed(a)
r6=reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
print('List  of  chars  in  reverse  order  :  ' ,  list(r5))
print('Reverse  string   :   ' , str(r6))

# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b)# reversed address say 1000
print(id(b)) #1000
print(*b) #D Y H
print(b[0]) #error not indexed
print(b[1 : 3]) # error not indexed
print(b * 2)# cannot be repeated because it is empty
print(len(b)) # arg should be seq only 

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for  x  in   b:
	print(x) #True Hyd 10.8 25
	time . sleep(1)

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1)) # <class 'list_reversed'>
print(r1)# <class 'list_reversed'> address
print('Iterate   thru  list_reverseiterator  object  with   next()   function')
while True:
	try:
		print(next(r1))
	except:
		pass 
r2 = reversed(a)
# How  to  iterate   list_reverseiterator  object  with   next()   function
print('Iterate  thru  list_reverseiterator  object  with   __next__()   method')
while True:
	try:
		print(r2__next__())
	except:
		pass 

# How  to  iterate   list_reverseiterator  object  with   __next__()  method
print('Iterate  thru  list_reverseiterator  object  with   for  loop')
r3 = reversed(a)
# How  to  iterate   list_reverseiterator  object  with   for  loop
for x in r3:
	print(x)
r4 = reversed(a)
r5 = reversed(a)
print('Unpack  list_reverseiterator  object  :  ' , *r4)
print('Reverse  list  :  '  ,  list(r5))

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) # no error

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
# 10 20 15 18 , rama sita kiran amar ,(10,rama) (20, sita) (15 kiran) (18 amar) 
# in any order

'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?
Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}
Hint 1:  Both  input  and  output  are  dictionaries
Hint 2:  Use  reversed  iterator
'''
d={'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
res={}
r=reversed(d)
for x in r:
	res[x]=d[x]
print(res)
# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
# Write  for  loop  to  reverse  keys  of  dictionary
r1=reversed(a)
for x in r1:
	print(x)
print('Values  in  reverse  order')
# Write  for  loop  to  reverse  values  of  dictionary
r1=reversed(a.values())
for x in r1:
	print(x)
print('Tuples  in   reverse  order')
# Write  for  loop  to  reverse   tuples   of  dictionary
r1=reversed(a.items())
for x in r1:
	print(x)
print('Elements  of  each   tuple  in  reverse  order')
# Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
r1=reversed(a)
for x,y in r1:
	print(y,x,sep='...')
print('Keys  and  values  in   reverse   order')
# Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
r1=reversed(a)
for x,y in r1:
	print(x,y,sep='...')
