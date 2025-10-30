'''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp():
	for  i  in  range(10):
		main=main_thread()
		main.join()
		print('new  thread')
		
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')

# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started')
main . join()
print(name , 'is ended')

'''
main thread object is returned by main_thread func to main
name=MainThread
MainThread is started
current thread(i.e main thread) waits for main thread to complete
so execution is stopped here
'''



'''
Modify  following   program  such  that  t1  should  execute  double()  function  and
t2  should  execute  square()  function
'''
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
#  End  of  the  function
start = time . time()
t1=Thread(target=double)
t2=Thread(target=square)
t1.start()
t2.start()
end = time . time()
print(end - start) #  What  is   the   execution  time ?