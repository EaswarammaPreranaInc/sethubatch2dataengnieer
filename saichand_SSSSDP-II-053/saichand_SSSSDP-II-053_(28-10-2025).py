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
#Program:
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
t1 . start() #  What  does  thread  t1  do ?    thread t1  executes  f1  function   			# 'f1 function' 10 times
t2 . start()  #  What  does  thread  t2  do ?  thread t2  executes  m1  method  of  class c1		# 'm1 method of class c1' 10 times
t3 . start()   #  What  does  thread  t3  do ? thread t3  executes  run  method  of  Thread  class	# No output
t4 . start()   #  What  does  thread  t4  do ? thread t4  executes  run  method  of  MyThread  class	# 'run   method  of  MyThread  class' 10 times
t5 . start()   #  What  does  thread  t5  do ? thread t5  executes  f1  function			# 'f1 function' 10 times
t6 . start()  #  What  does  thread  t6  do ? thread t6  executes  f1  function				# 'f1 function' 10 times
t7 . start() #  What  does  thread  t7  do ? thread t7  executes  run  method  of  Thread  class	# No output
t8 . start()   #  What  does  thread  t8  do ? thread t8  executes  m1  method  of  class c1		# 'm1 method of class c1' 10 times
t9 . start()   #  What  does  thread  t9  do ? thread t9  executes  m1  method  of  class c1		# 'm1 method of class c1' 10 times
t10 . start()  #  What  does  thread  t10  do ? thread t10  executes  run  method  of  MyThread  class	# 'run   method  of  MyThread  class' 10 times
t11 . start()   #  What  does  thread  t11  do ? thread t11  executes  run  method  of  Thread  class	# No output
t12 . start()  #  What  does  thread  t12  do ? thread t12  executes  m1  method  of  MyThread  class	# 'm1  method  of  MyThread  class' 10 times
t13 . start()   #  What  does  thread  t13  do ? thread t13  executes  f1  method  of  class c1		# 'f1  method  of  class  c1' 10 times







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

#output:
Start Method
Run Method
Main  Thread







# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
#How  to  print  name  of  main  thread
print('Name  of  Main  Thread  :', main.name)
#How  to  modify  name  of  main  thread  to   'Hyd'
main.name = 'Hyd'
#How  to  print  new  name  of  main  thread
print('New  Name  of  Main  Thread  :', main.name)
#How  to  create  a  new  child  thread  with  name  "Sec"
child = Thread(name = 'Sec')
#How  to  print  name  of  child  thread
print('Name  of  Child  Thread  :', child.name)
#How  to  modify  name  of  child  thread  to   'Cyb'
child.name = 'Cyb'
#How  to  print  new  name  of  child  thread
print('New  Name  of  Child  Thread  :', child.name)
#How  to  print  number  of  threads  under  execution
print('Number  of  Threads  under  execution  :', active_count())

#output:
Name  of  Main  Thread  : MainThread
New  Name  of  Main  Thread  : Hyd
Name  of  Child  Thread  : Sec
New  Name  of  Child  Thread  : Cyb
Number  of  Threads  under  execution  : 1








# Find  outputs (Home  work)
from threading import *
#How  to  create  three  new  threads  t1 , t2 , t3
t1 = Thread()
t2 = Thread()
t3 = Thread()
print('Names of Threads')
#How  to  print  name  of  each  thread
print(t1.name)
print(t2.name)
print(t3.name)
#How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three'
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
#How  to  print  number  of  threads  under  execution   --->  1
print('Number  of  Threads  under  execution  :', active_count())

#output:
Names of Threads
Thread-1
Thread-2
Thread-3
New Names of Threads
One
Two
Three
Number  of  Threads  under  execution  : 1
