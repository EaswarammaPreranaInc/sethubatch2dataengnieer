

#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
'''
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''

#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
'''
child thread
main thread 
child thread
main thread
... simultaneous output
'''

# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread(target=f1)#never executes the child thread because there is no target neither f1() is called
child . start()
for  i   in   range(10):
        print('main  thread') #main thread is executed directly

# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start() #threads can only be started once 

# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
child . start() #executes the child thread 10 times
a . m1() #execute the print statement 10 times child thread
for  i  in  range(10):
	print('main  thread') #executes 10 times


 # Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())#exxecutes child thread 10 times 
child . start()
for  i  in  range(10):
        print('main  thread')


#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
a = c1()
child = Thread(target=a.m1)#How  to  specify  the  target  as  class  method
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)

 # Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread() 
t . start() #there is no start method in Thread class
for  i  in  range(10):
        print('main  thread')

# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()#executes nothing as there is no target defined
t . start()
for  i  in  range(10):
        print('Main  Thread')


# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child . run() #executes because there is a run method and this is not a threading , just a concrete class method
for  i  in  range(10):
        print('main  thread')


# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()#Nothing is executed as there is no target and an argument is missing
child . start()
for  i  in  range(10):
	print('Main  Thread')


# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()#prints run method as i have overidden the original run method from thread class 
print('Main  Thread')


# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child . start()#concurrently executed with values written inbetween
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)


 # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')
#Output: Main Thread

'''
Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  --->

2) What  are  the  outputs  for  t2 . start() ?  --->

3) What  are  the  outputs  for  t3 . start() ?  --->

4) What  are  the  outputs  for  t4 . start() ?  --->

5) What  are  the  outputs  for  t5 . start() ?  --->

6) What  are  the  outputs  for  t6 . start() ?  --->

7) What  are  the  outputs  for  t7 . start() ?  --->

8) What  are  the  outputs  for  t8 . start() ?  --->

9) What  are  the  outputs  for  t9 . start() ?  --->

10) What  are  the  outputs  for  t10 . start() ?  --->

11) What  are  the  outputs  for  t11 . start() ?  --->

12) What  are  the  outputs  for  t12 . start() ?  --->

13) What  are  the  outputs  for  t13 . start() ?  --->
'''
from  threading  import  *
class  MyThread(Thread):
        def  run(self):
                for  i  in  range(10):
                        print('run   method  of  MyThread  class')
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  MyThread  class')
class  c1(Thread):
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  class  c1')
        def   f1(self):
                 for  i  in  range(10):
                         print('f1  method  of  class  c1')
# end of class
def   f1():
        for  i  in  range(10):
                print('f1  function')
#end of f1 function
t1 = Thread(target = f1)
t2 = Thread(target = c1() . m1)
t3 = Thread()
t4 = MyThread()
t5 = MyThread(target = f1)
t6 = c1(target =  f1)
t7 = c1()
t8 = MyThread(target = c1() . m1)
t9 = c1(target = c1() . m1)
t10 = MyThread(target = t4 . run)
t11 = c1(target = t7 . run)
t12 = c1(target = t4 . m1)
t13 = c1(target = t7 . f1)
# Run  with  any  one  of  the  following  stmts
t1 . start()  # What  does  thread  t1  do ? #prints f1 function 10 times
t2 . start()  #  What  does  thread  t2  do ?#prints m1 method 10 times
t3 . start()   #  What  does  thread  t3  do ?# does nothing
t4 . start()   #  What  does  thread  t4  do ? #run method of MyThread class 10 times
t5 . start()   #  What  does  thread  t5  do ? #run method of MyThread class 10 times
t6 . start()  #  What  does  thread  t6  do ? #f1 method of class c1 is executed 10 times
t7 . start() #  What  does  thread  t7  do ? #nothing executes
t8 . start()   #  What  does  thread  t8  do ? #run method of MyThread class 10 times
t9 . start()   #  What  does  thread  t9  do ? #m1 method of c1 class executed 10 times
t10 . start()  #  What  does  thread  t10  do ? #run method of MyThread class 10 times
t11 . start()   #  What  does  thread  t11  do ? #nothing executed as method is not called
t12 . start()  #  What  does  thread  t12  do ? #m1 method of MyThread class 10 timess
t13 . start()   #  What  does  thread  t13  do ? #f1 method of class c1 10 times



 #  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method')
	def   run(self):
		print('Run Method')
child = MyThread()
child . start() 
print('Main  Thread')
'''
Run Method
Start Method
Main Thread
'''

from threading import *

# main thread executes all the following statements
main = current_thread()
#Print name of main thread
print("Main thread name:", main.name)
#Modify name of main thread to 'Hyd'
main.name = 'Hyd'
#Print new name of main thread
print("Modified main thread name:", main.name)
#Define a child thread function
def f1():
    t = current_thread()  # get current (child) thread
    print("Child thread name:", t.name)

#Modify name of child thread to 'Cyb'
t.name = 'Cyb'
print("Modified child thread name:", t.name)
#Create a new child thread with name 'Sec'
child = Thread(target=f1, name='Sec')
# Start the child thread
child.start()
child.join()
#Print number of threads under execution
print("Number of threads under execution:", active_count())



# Find  outputs (Home  work)
from threading import *

# create three new threads t1, t2, t3
t1 = Thread()   # create first thread object
t2 = Thread()   # create second thread object
t3 = Thread()   # create third thread object
print('Names of Threads')   # print message
# print name of each thread
print(t1.name)   # prints default name like Thread-1
print(t2.name)   # prints default name like Thread-2
print(t3.name)   # prints default name like Thread-3
# modify name of each thread to "One", "Two", and "Three"
t1.name = "One"     # set new name for t1
t2.name = "Two"     # set new name for t2
t3.name = "Three"   # set new name for t3
print('New Names of Threads')   # print message
print(t1.name)   # prints modified name "One"
print(t2.name)   # prints modified name "Two"
print(t3.name)   # prints modified name "Three"
# print number of threads under execution
print("Number of threads under execution:", active_count())   # prints 1 because only main thread is active
