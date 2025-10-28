#1

'''
1) t1.start()   # Output:  'f1 function' printed 10 times
2) t2.start()   # Output:  'm1 method of class c1' printed 10 times
3) t3.start()   # Output:  (No output, does nothing)
4) t4.start()   # Output:  'run method of MyThread class' printed 10 times
5) t5.start()   # Output:  'f1 function' printed 10 times
6) t6.start()   # Output:  'f1 function' printed 10 times
7) t7.start()   # Output:  (No output, does nothing)
8) t8.start()   # Output:  'm1 method of class c1' printed 10 times
9) t9.start()   # Output:  'm1 method of class c1' printed 10 times
10) t10.start() # Output:  'run method of MyThread class' printed 10 times
11) t11.start() # Output:  (No output, does nothing)
12) t12.start() # Output:  'm1 method of MyThread class' printed 10 times
13) t13.start() # Output:  'f1 method of class c1' printed 10 times

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





#2

from threading import *
class MyThread(Thread):
    def start(self):
        super().start()
        print('Start Method')
    def run(self):
        print('Run Method')

child = MyThread()
child.start()
print('Main Thread')
'''
#output:
Run Method
Start Method
Main Thread
'''




#3
from threading import *

#  Get the main thread object
main = current_thread()

# Print name of main thread
print(main.name)  # Output: MainThread

# Modify name of main thread to 'Hyd'
main.name = 'Hyd'

# Print new name of main thread
print(main.name)  # Output: Hyd

# Function for new thread to run
def dummy():
    pass

# Create a new child thread with name "Sec"
child = Thread(target=dummy, name='Sec')
child.start()

# Print name of child thread
print(child.name)  # Output: Sec

# Modify name of child thread to 'Cyb'
child.name = 'Cyb'

# Print new name of child thread
print(child.name)  # Output: Cyb

# Print number of threads under execution
print(active_count())  # Output: Number >= 1 




#4
from threading import *
def dummy():
    pass
t1 = Thread(target=dummy)
t2 = Thread(target=dummy)
t3 = Thread(target=dummy)

print('Names of Threads')
print(t1.name)  # Output: Thread-1 
print(t2.name)  # Output: Thread-2
print(t3.name)  # Output: Thread-3

t1.name = "One"
t2.name = "Two"
t3.name = "Three"

print('New Names of Threads')
print(t1.name)  # Output: One
print(t2.name)  # Output: Two
print(t3.name)  # Output: Three

print(active_count())  # Output: 1 if none of the threads have been started yet.
                   
