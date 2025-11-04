'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  				       [Hyd]
						               [Sec]
						               [Cyb]
'''
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '')
	#time . sleep(3)
	print(' ]')
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
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal
		#time . sleep(1)
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




#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire()
print('Locked')  						#  Locked
r . acquire()
print('Locked')  						#  Locked
r . release()
print('Unlocked')  						#  Unlocked
r . release()
print('Unlocked') 	 					#  Unlocked
r . release()    						#  Error
print('End')  							#  End



# Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire()
print('Locked')  					#  Locked
l . acquire()
print('Locked')  					#  Not executed bcoz same thread not exected again lock
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

'''
	output
	
One is   under   execution
Two is   under   execution
Three is   under   execution
Two finished  execution
One finished  execution
Four is   under   execution
Five is   under   execution
Three finished  execution
Six is   under   execution
Four finished  execution
Five finished  execution
Seven is   under   execution
Eight is   under   execution
Six finished  execution
Nine is   under   execution
Nine finished  execution
Eight finished  execution
Seven finished  execution
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
t1 . start()  							#  4!=24
t2 . start()	  						#  7!=5040



#  Find  outputs  (Home  work)
from  threading  import  *
import  time
def  f1():
	l1 . acquire()
	print('1st  thread  locks  object  l1')  		#  1st thread locks object l1
	time . sleep(1)
	l2 . acquire() 						#  already locked
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def  f2():
	l2 . acquire()
	print('2nd   thread  locks  object  l2')    		#  2nd thread locks object l2
	time . sleep(1)  
	l1 . acquire()  					#  Already locked
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
print('Deadlock')  #  Deadlock



#  Find  outputs  (Home  work)
stack=[]
for i in range(1,6):
    stack.append(i*10)				#  How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
for j in stack:
    print(stack.pop())				#  How  to  remove  each  element  of   stack  object  and  also  print
#print(stack . get())  				#  Error due to list not have get method
print('End')



#  Find  outputs  (Home  work)
from random import *
from queue import *
pq=PriorityQueue()
for i in range(5):
    pq.put(randint(1,100))  			#  How  to  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
						#  How  to  remove  each  element  of  object  pq  and  also  print
for i in range(5):
    print(pq.get())
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
    print(q.get())						#  How  to  remove  each  tuple  of  object  'q'  and  also  print



#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get())  					#  How  to  remove  each  tuple  of  stack  object  and  also  print



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
    print(pq.get())  						#  How  to  remove  each  tuple  of  object  pq  and  also  print



#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')  			#  Child thread
		time . sleep(2)
main = main_thread()
print(main . daemon)  						#  False
#main . daemon = True  						#  Error
new = Thread(target = f1)
print(new . daemon) 						#  False
new . daemon = True
print(new . daemon)  						#  True
new . start()
new . daemon = True  						#  Error
time . sleep(5)
print('End  of  main  thread')



'''
(Home  work)
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

#  Diff Out/Put for every Run


