'''
Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  ---> 10 times f1 function

2) What  are  the  outputs  for  t2 . start() ?  ---> 10 times m1 method of class c1

3) What  are  the  outputs  for  t3 . start() ?  ---> nothing

4) What  are  the  outputs  for  t4 . start() ?  ---> 10 times run   method  of  MyThread  class

5) What  are  the  outputs  for  t5 . start() ?  ---> 10 times run   method  of  MyThread  class

6) What  are  the  outputs  for  t6 . start() ?  ---> 10 times f1 function

7) What  are  the  outputs  for  t7 . start() ?  ---> nothing

8) What  are  the  outputs  for  t8 . start() ?  ---> 10 times run   method  of  MyThread  class

9) What  are  the  outputs  for  t9 . start() ?  ---> 10 times m1 method of class c1

10) What  are  the  outputs  for  t10 . start() ?  ---> 10 times m1 method of class c1

11) What  are  the  outputs  for  t11 . start() ?  ---> nothing

12) What  are  the  outputs  for  t12 . start() ?  ---> 10 times m1 method of MyThread class

13) What  are  the  outputs  for  t13 . start() ?  ---> 10 times f1  method  of  class  c1
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
#t1 . start() #  What  does  thread  t1  do ? executes f1 function
#t2 . start()  #  What  does  thread  t2  do ? executes m1 method of class c1
#t3 . start()   #  What  does  thread  t3  do ? executes empty run method of thread class
#t4 . start()   #  What  does  thread  t4  do ? executes run method of class MyThread
#t5 . start()   #  What  does  thread  t5  do ? executes run method of class MyThread
#t6 . start()  #  What  does  thread  t6  do ? executes f1 function
#t7 . start() #  What  does  thread  t7  do ? executes empty run method of thread class
#t8 . start()   #  What  does  thread  t8  do ? executes run method of class MyThread
#t9 . start()   #  What  does  thread  t9  do ? executes m1 method of class c1
#t10 . start()  #  What  does  thread  t10  do ? executes m1 method of class c1
#t11 . start()   #  What  does  thread  t11  do ? executes empty run method of thread class
#t12 . start()  #  What  does  thread  t12  do ? executes m1 method of MyThread class
#t13 . start()   #  What  does  thread  t13  do ? executes f1 method of class c1


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
print('Main  Thread')

'''
Run method
Start method
Main Thread
'''

# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print(main) # How  to  print  name  of  main  thread
main . name = 'Hyd' # How  to  modify  name  of  main  thread  to   'Hyd'
print(main . name) # How  to  print  new  name  of  main  thread
# How  to  create  a  new  child  thread  with  name  "Sec"
t = Thread(name = 'child')
print(t . name)) # How  to  print  name  of  child  thread
t . name = 'Cyb' # How  to  modify  name  of  child  thread  to   'Cyb'
# How  to  print  new  name  of  child  thread
print(t . name)
print(active_count()) # How  to  print  number  of  threads  under  execution



# Find  outputs (Home  work)
from threading import *
# How  to  create  three  new  threads  t1 , t2 , t3
t1 = Thread()
t2 = Thread()
t3 = Thread()
print('Names of Threads')
# How  to  print  name  of  each  thread
print(t1 . name)
print(t2 . name)
print(t3 . name)
# How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
t1 . name = 'One'
t2 . name = 'Two'
t3 . name = 'Three'
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print(active_count()) # How  to  print  number  of  threads  under  execution 




