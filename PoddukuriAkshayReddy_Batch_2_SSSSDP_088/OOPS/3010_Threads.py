'''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp():
    main_thread().join() # new thread waits for main thread to die
    for  i  in  range(10):
        print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')
'''
10 times main thread
10 times new thread
'''



# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started')
main . join()
print(name , 'is ended')

'''
main Thread is started
ERROR: cannot join current thread
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
double()
square()
end = time . time()
print(end - start) #  What  is   the   execution  time ?
'''
Double :  2
Double :  4
Double :  6
Double :  8
Double :  10
Double :  12
Square :  1
Square :  4
Square :  9
Square :  16
Square :  25
Square :  36
12.126964092254639
'''