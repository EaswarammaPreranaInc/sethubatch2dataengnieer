

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
def f1():
    for i in range(10):
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
# t1 . start() 
''' it  will excute the f1() which is outside of the Class ,  
 print 10 times 'f1  function'
'''

# t2 . start()  # it will excute m1 method of c1 class , and print 10 times 'm1 method of class c1'
# t3 . start()   # it will checks run method  thread class internally ,due to target = none , it won't gives print output
# t4 . start()   # it will excute run method of mythread class, and prints 10 times 'run   method  of  MyThread  class'
# t5 . start()   # it will override the run method of thread class and run th erun method of the mythread class , print 10 times 'run   method  of  MyThread  class'
# t6 . start()  # it will create c1  thread object and stores target as f1, but t6.start() starts new thread and takes f1 as target and excutes the f1 function and print 10 times 'f1 function'
# t7 . start() # it will create class c1 with no target , so it will check run method of thread class internally , due to target = none , it won't gives print output
# t8 . start()   # it will create mythread class object and stores target as m1 method of c1 class , but t8.start() starts new thread and due to overidden run method of mythread class , it will excute the run method of mythread class and print 10 times 'run   method  of  MyThread  class'
# t9 . start()   # it will create c1 class object and stores target as m1 method of c1 class , but t9.start() starts new thread and takes m1 method of c1 class as target and excutes the m1 method of c1 class and print 10 times 'm1  method  of  class  c1'
# t10 . start()  # it will create mythread class object and stores target as run method of mythread class , but t10.start() starts new thread and takes run method of mythread class as target and excutes the run method of mythread class and print 10 times 'run   method  of  MyThread  class'
# t11 . start()   # it will create c1 class object and stores target as run method of c1 class , but t11.start() starts new thread and takes run method of thread class as target and excutes the run method of thread class internally ,due to target = none , it won't gives print output
# t12 . start()  #  it will create c1 class object and stores target as m1 method of mythread class , but t12.start() starts new thread and takes m1 method of mythread class as target and excutes the m1 method of mythread class and print 10 times 'm1  method  of  MyThread  class'
t13 . start()   #  it will create c1 class object and stores target as f1 method of c1 class , but t13.start() starts new thread and takes f1 method of c1 class as target and excutes the f1 method of c1 class and print 10 times 'f1  method  of  class  c1'

    
   
   
    
    
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

# Run Method
# Start Method 
# Main Method    
    
    
    
    
    
# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print('Name of the main thread :',main.name) # How  to  print  name  of  main  thread
main.name = 'Hyd' # How  to  modify  name  of  main  thread  to   'Hyd'
print('NEw Name of the main thread :',main.name) # How  to  print  new  name  of  main  thread
def diaplay(): # How  to  create  a  new  child  thread  with  name  "Sec"
    child = current_thread()
    print('Name of the child thread :',child.name) # How  to  print  name  of  child  thread
    child.name = 'Cyb' # How  to  modify  name  of  child  thread  to   'Cyb'
    print('New Name of the child thread :',child.name) # How  to  print  new  name  of  child  thread
child_thread = Thread(target = diaplay , name = 'Sec')
child_thread . start()
print('Number of threads  under execution :',active_count()) # How  to  print  number  of  threads  under  execution





# Find  outputs (Home  work)
from threading import *
t1 = Thread(name = t1)
t2 = Thread(name = t2)
t3 = Thread(name = t3)  # How  to  create  three  new  threads  t1 , t2 , t3

print('Names of Threads')
# How  to  print  name  of  each  thread
print(t1.name)
print(t2.name)
print(t3.name)

# How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three'

print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)

print('Number of threads  under execution :',active_count()) # How  to  print  number  of  threads  under  execution   --->  1







#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')

# Arithmetic Error




# Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> 



