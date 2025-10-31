#Find outputs 
from threading import *
import  time
def    disp():
	main_thread().join(10) # new thread waits for 10 secounds for  the main thread to finish.
	# and if it is not finished it continues running and new thread also gets chance. so, output is not predictable 
	for i in range(10):
		print('new  thread')
new = Thread(target =disp)
new.start()
for i in range(10):
	print('main  thread')
	time.sleep(2)
	

#  Find  outputs 
from threading import *
import time
def  disp():
	main_thread().join() # new thread waits for the main thread to finish execution
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp)
child.start()
child.join() # main thread waits for the child thread to finish execution . No output is generated
for  i  in  range(10):
	  print('main  thread')
	 


# Find  outputs 
from  threading  import *
import  time
def   disp(s):
	print('[',s,end = '')
	time.sleep(3)
	print(']')
t1 = Thread(target = disp, args = ('Hyd',))
t2 = Thread(target = disp, args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1.start()
t2.start()
t3.start() # three threads starts at the same time and executes disp and waits for the 3 sec. Any thread may resume after 3 sec output is not predictable.



#  Find  outputs 
from  threading  import *
import  time
class   Account:
	def    __init__(self , acno1 , bal1):
		self.acno = acno1
		self.bal = bal1 # balance=1000.0
	def    credit(self,amt):
		s = current_thread().name
		print(F'{s}  is  depositing  Rs. {amt}  into account   {self . acno}')
		x = self.bal
		time.sleep(1)
		self.bal  =  x + amt
# End  of  the  class
ac = Account(25 , 1000.0) # object is created and __init__ is executed. 
print('Initial  Balance : ',ac.bal)
t1 = Thread(target = ac.credit ,  args = [100] ,name = 'Rama')
t2 = Thread(target = ac.credit , args = (200,) ,name = 'Sita')
t1.start() 
t2.start() # two threads t1 and t2 deposit money at the same time and both read the same initial balance
t1.join()
t2.join()
print('Final  Balance  : ', ac.bal) # the final balance should be 1300 but the output vary for every run. because of the concurrent execution incorrect results are printed.


