from threading import *
def   disp():
	main_thread() . join()
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main thread')


# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started') # MainThread is started
main . join() # error as there is only 1 thread
print(name , 'is ended')


'''
Modify  following   program  such  that  t1  should  execute  double()  function  and
t2  should  execute  square()  function
'''
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		#time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		#time . sleep(1)
#  End  of  the  function
start = time . time()
t1 = Thread(target = double)
t2 = Thread(target = square)
t1 . start()
t2 . start()
t1 . join()
t2 . join()
end = time . time()
print(end - start) 
