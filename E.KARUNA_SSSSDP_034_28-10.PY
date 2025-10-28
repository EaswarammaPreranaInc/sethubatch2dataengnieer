
#What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()#calling parent thread class
		print('Start Method')
	def   run(self):
		print('Run Method')
child = MyThread()#creates a new thread object
child . start()#calling start method
print('Main  Thread')
'''
o/p:
Run method
start method
main method
'''


# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print("name  of  main  thread:",main.name)#How  to  print  name  of  main  thread
t=Thread(name='mainthread')
main.name='Hyd'#How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name)#How  to  print  new  name  of  main  thread
child=Thread(name='sec')#How  to  create  a  new  child  thread  with  name  "Sec"
print(child.name)#How  to  print  name  of  child  thread
child.name='cyb'#How  to  modify  name  of  child  thread  to   'Cyb'
print(child.name)#How  to  print  new  name  of  child  thread
print("Number of active threads:",active_count())#How  to  print  number  of  threads  under  execution

'''
o/p:
name  of  main  thread: MainThread
Hyd
sec
cyb
Number of active threads: 1
'''


# Find  outputs (Home  work)
from threading import *
t1=Thread()
t2=Thread()
t3=Thread()#How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)#How  to  print  name  of  each  thread
t1.name='one'
t2.name='Two'
t3.name='Three'
#How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print("Number of threads:",active_count())#How  to  print  number  of  threads  under  execution   --->  1

'''
o/p:
Names of Threads
Thread-1
Thread-2
Thread-3
New Names of Threads
one
Two
Three
Number of threads: 1
'''



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
#t1 . start() #  executed f1 () function i.e f1  function  10 times
#t2 . start()  #  class c1 is executed i.e m1  method  of  class  c1 10 times
#t3 . start()   #  empty run()method of thread class is executed i.e nothing
#t4 . start()   # run()method of myThread is executed i.e run   method  of  MyThread  class 10 times
#t5 . start()   #  f1  function 10 times
#t6 . start()  #   f1  function 10 times
#t7 . start() #  empty run() method ofthread class
#t8 . start()   #   executes m1() method of c1 class i.e 'm1  method  of  class  c1 10 times
#t9 . start()   # executes m1() of a new c1 object i.e m1  method  of  class  c1 10 times
#t10 . start()  #  executes t4.run() (the run() of a MyThread instance i.e run   method  of  MyThread  class 10 times
#t11 . start()   #  executes t7.run()but t7 ia a c1 which empty run method i,e nothing
#t12 . start()  #  executes t4.m1(),calls m1() of myThread i.em1  method  of  MyThread  class 10 times
#t13 . start()   #  executes t7.f1() where t7 is c1 so c1.f1 calling i.e f1  method  of  class  c1 10 times 