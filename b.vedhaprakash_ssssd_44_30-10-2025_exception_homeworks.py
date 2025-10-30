# ---------------- homework on 30/10/2025 ---------------#

'''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
import threading # We must import 'threading' to get the main thread object

def   disp():
    # 1. Get the main thread object
    main_thread = threading.main_thread() 
    
    # 2. Call join() on the main thread object.
    #    This blocks the 'new' thread until the 'main_thread' finishes execution.
    main_thread.join() 
    
    for  i  in  range(10):
        print('new  thread') # 5. This loop will only execute *after* the main thread is finished

new = Thread(target = disp)
new.start() # 3. The 'new' thread starts, enters disp(), and immediately waits at main_thread.join()

for  i  in  range(10):
    print('main  thread') # 4. The main thread's loop runs first and completes

# 6. The main thread finishes. This unblocks the .join() call in the 'new' thread,
#    which then begins its own loop.

----------------------------------------------------------
# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started') # MainThread  is started
main . join() # This line causes a deadlock. The main thread is told to wait for itself to finish.
print(name , 'is ended') # This line will never be executed.

------------------------------------------------------------
'''
Modify  following   program  such  that  t1  should  execute  double()  function  and
t2  should  execute  square()  function
'''
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
#  End  of  the  function
start = time . time()

# 1. Create thread t1 pointing to the double function
t1 = Thread(target=double)

# 2. Create thread t2 pointing to the square function
t2 = Thread(target=square)

# 3. Start both threads to run concurrently
t1.start()
t2.start()

# 4. Wait for t1 to finish execution
t1.join()
# 5. Wait for t2 to finish execution
t2.join()

end = time . time()
print(end - start) #  What  is   the   execution  time ?
# The execution time will be approximately 6 seconds .
# Each function takes 6 seconds (6 loops * 1 sec sleep).
# Because they run at the same time (concurrently) instead of one after
# the other, the total time is just the time of the longest function.
