# How  to  resolve  deadlock ?
from  threading  import  *
import  time
def  f1():
	l1 . acquire()
	time . sleep(1)
	l2 . acquire()
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
#  End  of  the  function
def  f2():
	l1 . acquire()
	time . sleep(1)
	l2 . acquire()
	print('2nd   thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  2nd   thread')
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('End  of  main  thread')
##############################
(no output after starting threads)

or sometimes:

(Program runs forever / hangs)



##################################################
Option 1: Maintain a consistent lock order

from threading import *
import time

def f1():
    with l1:
        time.sleep(1)
        with l2:
            print('1st thread is under execution')
    print('End of the 1st thread')

def f2():
    with l1:     # same order: l1 → l2
        time.sleep(1)
        with l2:
            print('2nd thread is under execution')
    print('End of the 2nd thread')

l1 = Lock()
l2 = Lock()

t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()
t1.join()
t2.join()

print('End of main thread')
########################################
1st thread is under execution
End of the 1st thread
2nd thread is under execution
End of the 2nd thread
End of main thread





$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Option 2: Use try...acquire(timeout=)

from threading import *
import time

def f1():
    while True:
        if l1.acquire(timeout=1):
            time.sleep(1)
            if l2.acquire(timeout=1):
                print('1st thread is under execution')
                l2.release()
                l1.release()
                break
            else:
                l1.release()
                time.sleep(1)
    print('End of the 1st thread')

def f2():
    while True:
        if l2.acquire(timeout=1):
            time.sleep(1)
            if l1.acquire(timeout=1):
                print('2nd thread is under execution')
                l1.release()
                l2.release()
                break
            else:
                l2.release()
                time.sleep(1)
    print('End of the 2nd thread')

l1 = Lock()
l2 = Lock()

t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()
t1.join()
t2.join()
print('End of main thread')
#####################################
Possible Output:

1st thread is under execution
End of the 1st thread
2nd thread is under execution
End of the 2nd thread
End of main thread

or (depending on timing):

2nd thread is under execution
End of the 2nd thread
1st thread is under execution
End of the 1st thread
End of main thread


