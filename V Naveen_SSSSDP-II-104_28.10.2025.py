'''
1. Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  ---> 10 times 'f1  function'

2) What  are  the  outputs  for  t2 . start() ?  ---> 10 times 'm1  method  of  class  c1'

3) What  are  the  outputs  for  t3 . start() ?  ---> No output

4) What  are  the  outputs  for  t4 . start() ?  ---> 10 times 'run  method  of  MyThread  class'

5) What  are  the  outputs  for  t5 . start() ?  ---> 10 times 'run  method  of  MyThread  class'

6) What  are  the  outputs  for  t6 . start() ?  ---> 10 times 'f1  function'

7) What  are  the  outputs  for  t7 . start() ?  ---> No output

8) What  are  the  outputs  for  t8 . start() ?  ---> 10 times 'run  method  of  MyThread  class'

9) What  are  the  outputs  for  t9 . start() ?  ---> 10 times 'm1  method  of  class  c1'

10) What  are  the  outputs  for  t10 . start() ?  ---> 10 times 'run  method  of  MyThread  class'

11) What  are  the  outputs  for  t11 . start() ?  ---> No output

12) What  are  the  outputs  for  t12 . start() ?  ---> 10 times 'm1  method  of  MyThread  class'

13) What  are  the  outputs  for  t13 . start() ?  ---> 10 times 'f1  method  of  class  c1'
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
#t1 . start() # it will register 't1' with thread scheduler and executes f1 function #   What  does  thread  t1  do ?
#t2 . start() # it will register 't2' with thread scheduler and executes m1 method  #  What  does  thread  t2  do ?
#t3 . start()  # it will register 't3' with thread scheduler and executes empty run method of Thread class  #  What  does  thread  t3  do ?
#t4 . start()  # it will register 't4' with thread scheduler and executes run method of MyThread class  #  What  does  thread  t4  do ?
#t5 . start()  # it will register 't5' with thread scheduler and executes run method of MyThread class #  What  does  thread  t5  do ?
#t6 . start() # it will register 't6' with thread scheduler and executes f1 function #  What  does  thread  t6  do ?
#t7 . start() # nothing will be printed #  What  does  thread  t7  do ?
#t8 . start() # it will register 't8' with thread scheduler and executes run method of MyThread class  #  What  does  thread  t8  do ?
#t9 . start() # it will register 't9' with thread scheduler and executes m1 method of c1 class  #  What  does  thread  t9  do ?
#t10 . start() # it will register 't10' with thread scheduler and executes run method of MyThread class #  What  does  thread  t10  do ?
#t11 . start() #  it will register 't11' with TS and Nothing will be printed  #  What  does  thread  t11  do ?
#t12 . start() # it will register 't12' with thread scheduler and executes m1 method of MyThread class #  What  does  thread  t12  do ?
t13 . start() # it will register 't13' with thread scheduler and executes f1 method of c1 class  #  What  does  thread  t13  do ?



#2.  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method') # 2nd output
	def   run(self):
		print('Run Method') # 1st output
child = MyThread()
child . start()
print('Main  Thread') # 3rd output





#3. Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print(main.name) # How  to  print  name  of  main  thread
main.name = 'Hyd' # How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name) # How  to  print  new  name  of  main  thread
child = Thread(name = 'Sec') # How  to  create  a  new  child  thread  with  name  "Sec"
print(child.name) # How  to  print  name  of  child  thread
child.name = 'Cyb' # How  to  modify  name  of  child  thread  to   'Cyb'
print(child.name) # How  to  print  new  name  of  child  thread
print(active_count()) # How  to  print  number  of  threads  under  execution






#4. Find  outputs (Home  work)
from threading import *
t1, t2, t3 = Thread(), Thread(), Thread() # How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name, t2.name, t3.name, sep = '\n') # How  to  print  name  of  each  thread
t1.name, t2.name, t3.name = 'One', 'Two', 'Three' # How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print(active_count()) # How  to  print  number  of  threads  under  execution   --->  1