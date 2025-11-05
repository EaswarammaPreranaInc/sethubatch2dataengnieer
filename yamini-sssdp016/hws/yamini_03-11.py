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
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
l=Lock()
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
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
l=Lock()
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
r . release()       # errorr as object is not locked
print('End')

'''
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
l . acquire()       #  the object is permamnant waiting state for unlocking l object
l . release()   # l object is released
print('Unlocked')
l . release()   # error as object cant be relaesed without locking
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
sem = Semaphore(3)  # a maximum of 3 threads can lock the object
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
t1 executes f1 locks the object and prints one is   under   execution
t1 sleeps
main thread starts t2
t2 executes f1 locks the object and prints two  is   under   execution
t2sleeps
main thread starts t3
t3 executes f1 locks the object and prints three  is   under   execution
t3 sleeps
now all 3 threads are in sleep
main thread starts t4 
t4 tries to lock the object but already 3 threads locked the object
so t4 waits
next 1 sec no execution
after 1 sec any one of t1,t2,t3, gets chance to execute
t1,t2,t3 continues exection in any order
in same way for t4,t5,t6
t7,t8,t9
'''

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

'''
a max of 8 threads can lock object
main thread starts t1 disp(4) go to disp
disp calls fact function
n=4
locks the object
locks the object 5 times and executes
unlocks the object and returns the caluculated value to func call
so disp(4) is printed
if in between time is elapsed main thread starts t2 disp(7)
disp calls fact function
n=7
locks the object 
already fact(4) locked object 5 times so 3 are remaining
fact(7) can lock object 3 times and waits t1 to unlock remaining times
'''

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

'''
main thread creates 2 lock objects
t1 executes f1
t1 locks l1 object
t1 sleeps for 1 sec
main thread gets chance
t2 executes f2
t2 locks l2 object
t2 sleeps for 1 sec
main thread gets chance
main thread sleeps for 1 sec
after 1 sec any one of t1,t2, or main thread gets chance
if t1 gets chance it tries to lock object l2 but it is already locked by t2
if t2 gets chance it tries to lock object l1 but it is already locked by t1
so deadlock and t1,t2, waits forever

'''

#  Find  outputs  (Home  work)
from queue import  LifoQueue
stack = LifoQueue()
for i in range(5):
    stack.put(10*i)  
#How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not stack . empty(): #
    print(stack . get()) #How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get())
print('End')


#  Find  outputs  (Home  work)
from random import  * 
from queue import  *
pq = PriorityQueue() #How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
for i in range(5):
    pq.put(randint(1,100))
print('Deleted  elements')
while not  pq . empty():
    print(pq . get())#How  to  remove  each  element  of  object  pq  and  also  print
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
    print(q.get())       # How  to  remove  each  tuple  of  object  'q'  and  also  print


#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get()) 
#How  to  remove  each  tuple  of  stack  object  and  also  print


#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty():
    print(pq.get()) 
#How  to  remove  each  tuple  of  object  pq  and  also   print

# Find  outputs
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
#How  to  remove  each  tuple  of  object  pq  and  also   print

#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')  # prints child thread 3 times and goes to sleep
		time . sleep(2) # main thread executes
main = main_thread()    # returns main thread object and main points to main thread object 
print(main . daemon)    # false because main thread is always non deamon
main . daemon = True    # error beacause main thread execution is already started
new = Thread(target = f1)   # new thread is created which is non deamon
print(new . daemon) # false because new thread is non deamon
new . daemon = True # converts new thread to deamon
print(new . daemon) # true because new thread is deamon
new . start()   # execution starts and executees f1 function 
new . daemon = True # error as new thread is already started
time . sleep(5) # main thread executes
print('End  of  main  thread')  # prints
# main thread is dead
#so deamon thread new thread is forcely killed

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))	# class <reversed>
print(r1)	# type and address of reversed object
print('Iterate  thru  reversed  object  with   next   function')
while True:	
    try:
        print(next(r1))
    except:
        break	#How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   __next__   method')
r2 = reversed(a)
while True:	
    try:
        print(r2.__next__())
    except:
        break

#How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
r3=reversed(a)
for i in r3:
    print(i)
#How  to  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  : ' , )
print(*reversed(a))
print('List  of  chars  in  reverse  order  :  '   )
print(list(reversed(a)))
print('Reverse  string   :   ' )
print(''.join(reversed(a)))


# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)	# empty reversed class object is created
print(type(b))	# class <reversed>
print(b)	# typr and address of b
print(id(b))	# adress of b
print(*b)	# unpacks b and prints each char in reversed order
print(b[0])	# error as b is always empty object
print(b[1 : 3]) # error as b is always empty object
print(b * 2)	# error as iterators cant be repeated
print(len(b))	# error for len fun argument should be sequence

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)	# an empty reversed object is created
print(type(b))	# class <reversed as tuple is immutable
for  x  in   b:
	print(x)	# true 'Hyd' 10.8 25
	time . sleep(1)


#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1))	# class <list_reversediterator>
print(r1) 	# type and adress of r1 is printed
print('Iterate   thru  list_reverseiterator  object  with   next()   function')
#How  to  iterate   list_reverseiterator  object  with   next()   function
while True:	
    try:
        print(next(r1))
    except:
        break	
print('Iterate  thru  list_reverseiterator  object  with   _next_()   method')
#How  to  iterate   list_reverseiterator  object  with   _next_()  method
r2 = reversed(a)
while True:	
    try:
        print(r2.__next__())
    except:
        break
print('Iterate  thru  list_reverseiterator  object  with   for  loop')
#How  to  iterate   list_reverseiterator  object  with   for  loop
r3=reversed(a)
for i in r3:
    print(i)
print('Unpack  list_reverseiterator  object  :  ' , *reversed(a	))
print('Reverse  list  :  '  ,  list(reversed(a)))

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)	# error set is unordered and not indexed and hence it cant be reversed

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
r1 = reversed(a . keys())	# keys of dictionary a are reversed 
disp(r1)	# 18 15 20 10
r2 = reversed(a . values())	# values of dictionary a are reversed 
disp(r2)	#Amar Kiran Sita Rama
r3 = reversed(a . items())	# key value tuples are reversed
disp(r3) #(18, 'Amar') (15, 'Kiran') (20, 'Sita') (10, 'Rama')
r4 = reversed(a)	# keys of dictionary a are reversed 
disp(r4)	#18 15 20 10


'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''

a= {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
b=dict()
c=reversed(a.items())
for i,j in c:
       b[i]=j
print(a)
print(b)
 

       

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for i in reversed(a.keys()):
	print(i)	#Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
for i in reversed(a.values()):
	print(i)		#Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
for i in reversed(a.items()):
	print(i)	#Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
for i,j in reversed(a.items()):
	print(i,j,sep='...')	#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
for i,j in reversed(a.items()),reversed(a.values()):
	print(i,j,sep='...')	#Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary

