: '''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
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
#########################################
from threading import *
import time

def disp():
    for i in range(10):
        print('new thread')
        time.sleep(0.2)

new = Thread(target=disp)
new.daemon = True   # new thread will wait for main thread to end
new.start()

for i in range(10):
    print('main thread')
    time.sleep(0.2)






: # Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started')
main . join()
print(name , 'is ended')
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
from threading import *
import time

def disp():
    for i in range(5):
        print('child thread running')
        time.sleep(1)

child = Thread(target=disp)
main = main_thread()
print(main.name, 'is started')

child.start()
child.join()  # main waits for child to complete

print(main.name, 'is ended')

######################################

MainThread is started
child thread running
child thread running
child thread running
child thread running
child thread running
MainThread is ended








: '''
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

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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
print("Execution time:", end - start)

###########################################

Double : 2
Square : 1
Double : 4
Square : 4
...

