'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]
'''
from  threading  import *
import  time
def   disp(s):
    l.acquire() # change
    print('[' , s , end = '')
    time . sleep(3)
    print(' ]')
    l.release() # change

l = Lock() # change
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
	def  _init_(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def  credit(self , amt):
		l.acquire() # change
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal
		time . sleep(1)
		self . bal = x + amt
		l.release() # change
  
l = Lock() # change
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
print('Locked')
r . acquire()
print('Locked')
r . release()
print('Unlocked')
r . release()
print('Unlocked')
r . release()
print('End')
'''

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

    
    
#  Find  outputs  (Home  work)
from queue  import   LifoQueue
stack = LifoQueue()
for i in range(1,6):
    stack.put(10 * i)
# How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while stack . empty():
    print(stack.get())
# How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get()) # 
print('End')

    
    
#  Find  outputs  (Home  work)
from  queue  import   PriorityQueue

How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
How  to  remove  each  element  of  object  pq  and  also  print
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
while not q.empty():
    print(q.get())
    
# How  to  remove  each  tuple  of  object  'q'  and  also  print




#  Find  outputs  (Home  work)
from  queue  import   LifoQueue

stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not q.empty():
    print(q.get())
    
# How  to  remove  each  tuple  of  stack  object  and  also  print

    
    
    
#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
print("Deleted Tuples")
while not pq.empty():
    print(pq.get())
# How  to  remove  each  tuple  of  object  pq  and  also   print

    
    
    
# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
# How  to  remove  each  tuple  of  object  pq  and  also  print

    
    
#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()
print(main . daemon) # False
main . daemon = True
new = Thread(target = f1)
print(new . daemon)
new . daemon = True
print(new . daemon)
new . start()
new . daemon = True
time . sleep(5)
print('End  of  main  thread')

    
    
    
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
t1 . start()
t2 . start()
t3 . start()
print('main  thread  is  dead')

    
    
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
print('Reverse  string   :   ' , ???)
[03-11-2025 14:24] SRINIVAS Sir SSSSDP: # Find  outputs (Home  work)
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
[03-11-2025 14:24] SRINIVAS Sir SSSSDP: # Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
[03-11-2025 14:28] SRINIVAS Sir SSSSDP: #  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
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
[03-11-2025 14:29] SRINIVAS Sir SSSSDP: #  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)
[03-11-2025 14:29] SRINIVAS Sir SSSSDP: # Can  dictionary  be  reversed  ? (Home  work)
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
[03-11-2025 14:30] SRINIVAS Sir SSSSDP: '''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''
[03-11-2025 14:31] SRINIVAS Sir SSSSDP: # Find outputs
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