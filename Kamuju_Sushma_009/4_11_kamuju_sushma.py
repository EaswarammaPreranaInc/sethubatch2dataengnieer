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
# there is no possibility of deadlock, t1 is executing f1 
#function which locked l1 and then t2 executes f2 and tries to lock 
#l1 which is already locked so it waits. then main thread 
#gets the chnace which waits for t1 to expire. then t1 executes f1 without any 
#interruptions , then t2. so no deadlock.