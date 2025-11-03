#  Find  outputs  
from  threading  import  RLock
r = RLock() # RLock locks the multiple time by the same thread but not by the different thread
r . acquire() # locked by the main thread
print('Locked')
r . acquire() # again locked by the main thread
print('Locked')
r . release() # unlocked by the main thread
print('Unlocked')
r . release() # unlocked
print('Unlocked')
#r . release() # error: as it is not locked we cannot perform unlock operation
print('End')
'''
o/p:
Locked
Locked
Unlocked
Unlocked
End
'''


#Find  outputs 
from threading import *
l = Lock()
l.acquire() # locked by the main thread
print('Locked')
#l.acquire() # cannot lock twice
#print('Locked')
l.release() # unlocked
print('Unlocked')
#l.release()
#print('Unlocked')
print('End')
'''
o/p:
Locked
Unlocked
End
'''


#  Find  outputs 
from threading import *
import time
def   f1():
        sem . acquire()
        name = current_thread() . name
        print(name , 'is   under   execution')
        time . sleep(1)
        print(name , 'finished  execution')
        sem . release()
sem = Semaphore(3) # it can lock 3 times either by same thread or different thread. Three threads can run at the same time.
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t4 = Thread(target = f1 , name = 'Four')
t5 = Thread(target = f1 , name = 'Five')
t6 = Thread(target = f1 , name = 'Six')
t7 = Thread(target = f1 , name = 'Seven')
t8 = Thread(target = f1 , name = 'Eight')
t9 = Thread(target = f1 , name = 'Nine')
t1.start()
t2.start()
t3.start() # first three threads will start running together. The other threads wait until one of the running threads finishes.
t4.start() # when one thread finishes then next waiting thread starts. The order of the outputs cannot be predicted.
t5.start()
t6.start()
t7.start()
t8.start()
t9.start() 


#  Find  outputs
from  threading  import *
import  time
def    fact(n):
	sem.acquire() # lockes the thread n times
	if   n  >  0:
		x = n * fact(n-1)
	else:
		x = 1
	sem . release()
	return   x
# End of the function
def    disp(n):
	print(n,' != ',fact(n))
# End of the function
sem = Semaphore(8)
t1 = Thread(target = disp , args = (4,))
t2 = Thread(target = disp , args = (7,))
t1.start()
t2.start()
'''
o/p:
4  !=  24
7  !=  5040
'''


#  Find  outputs  
from  threading  import  *
import  time
def  f1():
	l1.acquire()
	print('1st  thread  locks  object  l1')
	time.sleep(1)
	l2.acquire()
	print('1st  thread  is  under  execution')
	l2.release()
	l1.release()
	print('End  of  the  1st  thread')
def  f2():
	l2.acquire()
	print('2nd   thread  locks  object  l2')
	time.sleep(1)
	l1.acquire()
	print('2nd   thread  is  under  execution')
	l1.release()
	l2.release()
	print('End  of  the  2nd   thread')
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1.start() # t1 runs f1()
t2.start() # t2 runs f2()
time.sleep(1)
print('Deadlock') # t1 lockes l1 and waits for l2 ,  t2 lockes l2 and waits for l1 . Both are waiting for each other .This is called Deadlock.



#  Find  outputs 
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()
print(main . daemon) # False
#main.daemon = True # error : main thread cannot be Daemon thread
new = Thread(target = f1)
print(new . daemon)
new.daemon = True
print(new . daemon)
new.start()
#new.daemon = True # cannot set daemon status of active thread
time.sleep(5)
print('End  of  main  thread')
'''
o/p:
False
False
True
child  thread
child  thread
child  thread
End  of  main  thread
'''


'''
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
t1.start() # normal thread
t2.start() # normal thread
t3.start() # daemon thread . t3 stops immediately when main thread ends. only t1 and t2 finishes completely. cannot predict order of the outputs.
print('main  thread  is  dead')


