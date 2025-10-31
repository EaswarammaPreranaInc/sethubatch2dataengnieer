# Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread() . join(10)
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')
	time . sleep(2)

# Output :
main  thread
main  thread
main  thread
main  thread
main  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
main  thread
new  thread
new  thread
new  thread
main  thread
main  thread
main  thread
main  thread


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

# Output :
Main thread,child thread never executes forever because main thread waits for child thread expiry and vice versa 


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

# Output :
[ Hyd[ Sec[ Cyb]
]
]


#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def    _init_(self , acno1 , bal1):
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
print('Initial  Balance :  ' , ac . bal)
t1 = Thread(target = ac . credit ,  args = [100] ,  name = 'Rama')
t2 = Thread(target = ac  . credit , args = (200,) , name = 'Sita')
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final  Balance  :   ' , ac . bal)

# Output :
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100  into account   25
Sita  is  depositing  Rs. 200  into account   25
Final  Balance  :    1200.0

       or
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100  into account   25
Sita  is  depositing  Rs. 200  into account   25
Final  Balance  :    1100.0
