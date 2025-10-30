Program 1
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
main_thread().join()
for  i  in  range(10):
	print('main  thread')

# Output :
main  thread
main  thread
main  thread
main  thread
main  thread
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
new  thread
new  thread
new  thread


Program 2
# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started')
main . join()  # raise RuntimeError "cannot join current thread"
print(name , 'is ended')

# Output :
MainThread  is started
MainThread is ended


Program 3
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

# Output :
Double :  2
Square :  1
0.0014498233795166016
Double :  4
Square :  4
Double :  6
Square :  9
Double :  8
Square :  16
Double :  10
Square :  25
Double :  12
Square :  36
