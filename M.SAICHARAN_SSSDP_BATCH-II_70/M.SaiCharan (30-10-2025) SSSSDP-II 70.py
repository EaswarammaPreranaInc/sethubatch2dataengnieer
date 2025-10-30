                            NAME: M.SAICHARAN                 HOMEWORK
                            DATE: 30-10-2025
'''
1.Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')

#Program:
from threading import *
import time
def disp():
    # Wait until main thread finishes
    main_thread.join()
    for i in range(10):
        print('new thread')
main_thread = current_thread()
new = Thread(target=disp)
new.start()
for i in range(10):
    print('main thread')
    time.sleep(0.5)



2.# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started')
main . join()
print(name , 'is ended')

#Output:
main thread is started


'''
3.Modify  following   program  such  that  t1  should  execute  double()  function  and
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

#Program:
from threading import *
import time
def double():
    for i in range(1, 7):
        print('Double :', 2 * i)
        time.sleep(1)

def square():
    for i in range(1, 7):
        print('Square :', i * i)
        time.sleep(1)
t1 = Thread(target=double)
t2 = Thread(target=square)
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print("Total execution time:", end - start)
