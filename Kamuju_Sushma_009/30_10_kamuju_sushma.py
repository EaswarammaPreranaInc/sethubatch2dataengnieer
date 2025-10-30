'''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp():
    main_thread().join()
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')
	
# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started') #MainThread is started
main . join() #main thread is waiting for main thread,
# this can never break. so program never terminates.
print(name , 'is ended')

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
t2=Thread(target=double)
t1.start()
t2.start()
# square()
end = time . time()
print(end - start) #  What  is   the   execution  time ? 
# 20 if t1 and t2 finished before main_thread else less than 20 which is
# execution time of main thread 