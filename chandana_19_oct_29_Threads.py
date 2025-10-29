# Find  outputs 
from  threading  import  *
def  f1():
	print(current_thread().name) # print  name  of  child  thread
# main  thread  executes  following  statements
new=Thread(target=f1) # create  a  new  thread  with  name  'new'   and  target  f1
new.start() # start  the  new  thread
print(current_thread().name) # print  name  of   main  thread


# Find  outputs 
t1=Thread(name='Hyd') # create  a  thread  t1  with  name  'Hyd'
t2=Thread() # create  another  thread  t2  without  a  name
print(current_thread().name)# print  name  of  main  thread
print(t1.name) # print  name  of  thread  t1
print(t2.name) # print  name  of  thread  t2
current_thread().name='India' # modify  name  of  main  thread  to  'India'
t1.name='sec' # modify  name  of  thread  t1  to  'Sec'
t2.name='cyb' # modify  name  of  thread  t2  to  'Cyb'
print(current_thread().name) # print  name  of  main  thread
print(t1.name) # print  name  of  thread  t1
print(t2.name) # print  name  of  thread  t2
print(active_count()) # print  number  of  threads  under  execution



# Find  outputs  
from threading import  *
def   f1(x):
	s=current_thread().name
	while True:
		print(s,' :' ,x) # infinite loop because condition is always true
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args =(10,))
t2 = Thread(target = f1 , name = 'Sec' , args =[20])
t1.start() # starts t1 thread
t2.start() # starts t2 thread
print(active_count()) # prints no,of thread under execution
print('Press  ctrl + break  or  Fn + b  to  stop ')



# Find  outputs 
from  threading  import  Thread,current_thread
from  random  import  randint
def   f1(n):
	ctr=0
	s = current_thread().name
	while  True:
		x = randint(1,100) 
		ctr += 1
		print(F'{s} guess {x} in attempt : {ctr}')
		if   x ==n:
			break
	#end of while loop
	print(F'{s} finish in {ctr} attempts')
# End  of  function   f1()
t1 = Thread(target = f1 ,args = [75] ,name = 'Rama')
t2 = Thread(target = f1 ,args = [50] ,name = 'Sita')
t1.start() # t1  executes  f1(75)
t2.start() # t2  executes  f1(50)
'''
o/p:
Rama guess 34 in attempt :1
Sita guess 23 in attempt :1
Rama guess 45 in attempt :2
Rama guess 12 in attempt :2 so on
'''


# Find  outputs 
from threading import *
def   disp():
	for i in range(10):
		print('new  thread')
#  child  thread  is  dead
new = Thread(target =disp)
new.start()
new.join() # main thread waits until the child thread is completely finished
for  i  in  range(10):
	print('main  thread')
# main   thread is  dead
'''
o/p:
10 times new thread
10 times main thread
'''



#  Find  outputs 
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread')
		time.sleep(2) # pauses the thread execution for 2 seconds
new = Thread(target =disp)
new.start()
new.join(10) # main thread waits only 10 seconds for new to finish and after 10 seconds main thread resumes even though the child thread is in execution 
for  i  in  range(10): # cannot predict the output
	print('main  thread')
	


# Find  outputs 
from threading import *
import time
def   double():
	for i  in  range(1 , 7):
		print('Double : ',2 * i)
		time.sleep(1)  # pause thread execution for 1 second
def   square():
	for i in range(1 , 7):
		print('Square : ',i * i)
		time.sleep(1)  # pause thread execution for 1 second
start = time.time() # record start time
double()
square()
end = time.time() # record end time
print(end -start) # 6+6=12
'''
o/p:
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
12'''



# Find  outputs  
from  threading  import  *
import  time
def   display():
        name = current_thread().name
        print(name , 'is  started')
        time . sleep(3)
        print(name , 'is  ended')
# End  of  the  function
print(active_count())
t1 = Thread(target = display,name = 'One')
t2 = Thread(target = display,name = 'Two')
t3 = Thread(target = display,name = 'Three')
print(active_count()) # returns no,of threads currently running
t1.start()
t2.start()
t3.start()
print(active_count())
t1.join()
t2.join()
t3.join()
print(active_count())
'''
o/p:
1
1
One is  started
Two is  started
Three is  started
4
One is  ended
Two is  ended
Three is  ended
1
'''


# Find  outputs  
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , 'is  started')
	time . sleep(3)
	print(name , 'is  ended')
# End  of  the  function
t1 = Thread(target = disp,name = 'One')
t2 = Thread(target = disp,name = 'Two')
t3 = Thread(target = disp,name = 'Three')
t1.start()
t2.start()
t3.start()
list = enumerate() # returns a list of all active therad objects at that moment
for  t  in   list:
	print(t.name)
t1.join()
t2.join()
t3.join()
list = enumerate()
for t in list:
	print(t.name)
'''
o/p:
One is  started
Two is  started
Three is  started
MainThread
One
Two
Three
One is  ended
Two is  ended
Three is  ended
MainThread
'''


# is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =current_thread().name
	print(name ,'is started')
	time.sleep(3)
	print(name ,'is  ended')
t1 = Thread(target = disp , name ='One')
t2 = Thread(target = disp , name ='Two')
t3 = Thread(target = disp , name ='Three')
t1.start()
t2.start()
t3.start()
print(t1.is_alive()) # returns True if a thread is still running, otherwise False
print(t2.is_alive())
print(t3.is_alive())
t1.join()
t2.join()
t3.join()
print(t1.is_alive())
print(t2.is_alive())
print(t3.is_alive())
'''
o/p:
One is started
Two is started
Three is started
True
True
True
One is  ended
Two is  ended
Three is  ended
False
False
False
'''



#Find  outputs 
from  threading  import  *
import  time
def   table(n):
	print('Table : ',n)
	for i in range(1 , 11):
		print(F'{n} * {i} = {n * i}')
		time.sleep(1)
t1 = Thread(target = table , args =(7,))
t2 = Thread(target = table , args =(4,))
t1.start()
t2.start() # both thread starts simultaneoulsy so, output cannot be predicted
