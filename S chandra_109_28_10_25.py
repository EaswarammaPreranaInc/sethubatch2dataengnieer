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
t1 . start() #  What  does  thread  t1  do ?
#t2 . start()  #  What  does  thread  t2  do ?
#t3 . start()   #  What  does  thread  t3  do ?
#t4 . start()   #  What  does  thread  t4  do ?
#t5 . start()   #  What  does  thread  t5  do ?
#t6 . start()  #  What  does  thread  t6  do ?
#t7 . start() #  What  does  thread  t7  do ?
#t8 . start()   #  What  does  thread  t8  do ?
#t9 . start()   #  What  does  thread  t9  do ?
#t10 . start()  #  What  does  thread  t10  do ?
#t11 . start()   #  What  does  thread  t11  do ?
#t12 . start()  #  What  does  thread  t12  do ?
t13 . start()   #  What  does  thread  t13  do ?
#########################################################
| Thread | What executes                             | Output                                                           |
| :----- | :---------------------------------------- | :--------------------------------------------------------------- |
| t1     | target=f1                                 | `f1 function` ×10                                                |
| t2     | `c1().m1()` runs before start             | `m1 method of class c1` ×10                                      |
| t3     | default run                               | no output                                                        |
| t4     | MyThread.run()                            | `run method of MyThread class` ×10                               |
| t5     | MyThread.run() overrides target           | `run method of MyThread class` ×10                               |
| t6     | Thread.run() executes target=f1           | `f1 function` ×10                                                |
| t7     | no target/run                             | no output                                                        |
| t8     | `c1().m1()` before start + MyThread.run() | `m1 method of class c1` ×10 + `run method of MyThread class` ×10 |
| t9     | `c1().m1()` before start                  | `m1 method of class c1` ×10                                      |
| t10    | MyThread.run()                            | `run method of MyThread class` ×10                               |
| t11    | target=t7.run (does nothing)              | no output                                                        |
| t12    | target=t4.m1                              | `m1 method of MyThread class` ×10                                |
| t13    | target=t7.f1                              | `f1 method of class c1` ×10                                      |



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
#####################################

Because start() and run() execute in different threads, the order of output is not guaranteed — threading is concurrent.

Possible outputs (order may vary):
Run Method
Start Method
Main Thread



# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
How  to  print  name  of  main  thread
How  to  modify  name  of  main  thread  to   'Hyd'
How  to  print  new  name  of  main  thread
How  to  create  a  new  child  thread  with  name  "Sec"
How  to  print  name  of  child  thread
How  to  modify  name  of  child  thread  to   'Cyb'
How  to  print  new  name  of  child  thread
How  to  print  number  of  threads  under  execution

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from threading import *

# main thread executes all the following statements
main = current_thread()   # returns reference to current thread (main thread)

# Print name of main thread
print("Name of main thread:", main.name)

# Modify name of main thread to 'Hyd'
main.name = 'Hyd'

# Print new name of main thread
print("Modified name of main thread:", main.name)

# Define a simple child thread class
class MyThread(Thread):
    def run(self):
        print("Child Thread is running")

# Create a new child thread with name 'Sec'
t = MyThread(name='Sec')

# Print name of child thread
print("Name of child thread:", t.name)

# Modify name of child thread to 'Cyb'
t.name = 'Cyb'

# Print new name of child thread
print("Modified name of child thread:", t.name)

# Start child thread
t.start()

# Print number of threads currently executing
print("Number of threads currently executing:", active_count())

#######################################
Name of main thread: MainThread
Modified name of main thread: Hyd
Name of child thread: Sec
Modified name of child thread: Cyb
Child Thread is running
Number of threads currently executing: 2


# Find  outputs (Home  work)
from threading import *
How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
How  to  print  name  of  each  thread
How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
How  to  print  number  of  threads  under  execution   --->  1
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
from threading import *

# Create three new threads (not yet started)
t1 = Thread()
t2 = Thread()
t3 = Thread()

print('Names of Threads:')
# Print default names of each thread
print(t1.name)
print(t2.name)
print(t3.name)

# Modify names of each thread
t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three'

print('New Names of Threads:')
print(t1.name)
print(t2.name)
print(t3.name)

# Print number of threads under execution
# Only main thread is running, because we haven't started t1, t2, t3
print("Number of threads under execution:", active_count())

########################################
Expected Output:
Names of Threads:
Thread-1
Thread-2
Thread-3
New Names of Threads:
One
Two
Three
Number of threads under execution: 1

