'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						   [Sec]
						   [Cyb]
'''

from  threading  import *
import  time
l=Lock()
def   disp(s):
	l.acquire()
	print('[',s,end ='')
	time.sleep(3)
	print(']')
	l.release()
t1 = Thread(target = disp,args = ('Hyd',))
t2 = Thread(target = disp,args = ('Sec',))
t3 = Thread(target = disp,args = ('Cyb',))
t1.start()
t2.start()
t3.start()
'''
o/p:
[ Hyd]
[ Sec]
[ Cyb]
'''


'''
Modify  following  program  such  that  final  balance  should  be  1300
'''
from  threading  import  *
import  time
l=Lock()
class   Account:
	def  __init__(self,acno1,bal1):
		self.acno = acno1
		self.bal = bal1
	def  credit(self , amt):
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac.acno}')
		l.acquire()
		x = self.bal
		time.sleep(1)
		self.bal = x + amt
		l.release()
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac.bal )
t1 = Thread(target = ac.credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac.credit , name = 'Sita' , args = (200,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Final balance :  ',ac.bal)
'''
o/p:
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100   into  account   25
Sita  is  depositing  Rs. 200   into  account   25
Final balance :   1300.0
'''


