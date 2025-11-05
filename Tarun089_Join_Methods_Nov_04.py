# Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread() . join(10) # new thread waits for main thread to finish or 10 secs
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')
	time . sleep(2)
# sec 	
# 0 main thread
# 2 main Thread 
# 4 main thread 
# 6 main thread 
# 8 main thread 
# 10 main thread 
# new thread  5 times 
# 12 main thread 
# new thread 5 times 
# 3 times main thread  
 
#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join()
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp)
child . start()
child . join()
for  i  in  range(10):
	  print('main  thread')
#child thread 10 times
#main thread 10 times

# Find  outputs (Home  work)
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '')
	time . sleep(3)
	print(']')
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()
# 0 [Hyd [Sec [Cyb 
# 3 ]]]

#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def    __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def    credit(self , amt):
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}  into account   {self . acno}')
		x = self . bal
		time . sleep(1)
		self . bal  =  x  +  amt
# End  of  the  class
ac = Account(25 , 1000.0)
print('Initial  Balance :  ' , ac . bal) #1000.0
t1 = Thread(target = ac . credit ,  args = [100] ,  name = 'Rama') 
t2 = Thread(target = ac  . credit , args = (200,) , name = 'Sita')
t1 . start() # credit(100)
# rama is depositing Rs.100 into account 25 

t2 . start()
#sita is depositing Rs. 200 into account 25 
t1 . join()
t2 . join()
print('Final  Balance  :   ' , ac . bal)
