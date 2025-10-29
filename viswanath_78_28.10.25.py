'''
Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  --->                   f1 function (repeated 10 times)
2) What  are  the  outputs  for  t2 . start() ?  --->                   m1 method of class c1 (repeated 10 times)
3) What  are  the  outputs  for  t3 . start() ?  --->                   No output
4) What  are  the  outputs  for  t4 . start() ?  --->                   run method of MyThread class (repeated 10 times)
5) What  are  the  outputs  for  t5 . start() ?  --->                   run method of MyThread class (repeated 10 times)
6) What  are  the  outputs  for  t6 . start() ?  --->                   f1 function (repeated 10 times)
7) What  are  the  outputs  for  t7 . start() ?  --->                   No output
8) What  are  the  outputs  for  t8 . start() ?  --->                   run method of MyThread class (repeated 10 times)
9) What  are  the  outputs  for  t9 . start() ?  --->                   m1 method of class c1 (repeated 10 times)
10) What  are  the  outputs  for  t10 . start() ?  --->                 run method of MyThread class (repeated 10 times)
11) What  are  the  outputs  for  t11 . start() ?  --->                 No output
12) What  are  the  outputs  for  t12 . start() ?  --->                 m1 method of MyThread class (repeated 10 times)
13) What  are  the  outputs  for  t13 . start() ?  --->                 f1 method of class c1 (repeated 10 times)
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
t1 . start() #  What  does  thread  t1  do ?                                f1 function*10
#t2 . start()  #  What  does  thread  t2  do ?                              m1 method of class c1*10
#t3 . start()   #  What  does  thread  t3  do ?
#t4 . start()   #  What  does  thread  t4  do ?                             run method of MyThread class*10
#t5 . start()   #  What  does  thread  t5  do ?                             run method of MyThread class*10
#t6 . start()  #  What  does  thread  t6  do ?                              f1 function*10
#t7 . start() #  What  does  thread  t7  do ?
#t8 . start()   #  What  does  thread  t8  do ?                             run method of MyThread class*10
#t9 . start()   #  What  does  thread  t9  do ?                             m1 method of class c1*10
#t10 . start()  #  What  does  thread  t10  do ?                            run method of MyThread class*10
#t11 . start()   #  What  does  thread  t11  do ?
#t12 . start()  #  What  does  thread  t12  do ?                            m1 method of MyThread class*10
t13 . start()   #  What  does  thread  t13  do ?                            f1 method of class c1*10

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
outputs :
Run Method
Start Method
Main Method

# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print(main.name) # How  to  print  name  of  main  thread
main.name = 'Hyd' # How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name) # How  to  print  new  name  of  main  thread
child = Thread(name='Sec') # How  to  create  a  new  child  thread  with  name  "Sec"
print(child.name) # How  to  print  name  of  child  thread
child.name = 'Cyb' # How  to  modify  name  of  child  thread  to   'Cyb'
print(child.name) # How  to  print  new  name  of  child  thread
print(active_count()) # How  to  print  number  of  threads  under execution

# Find  outputs (Home  work)
from threading import *
t1 = Thread()
t2 = Thread()
t3 = Thread() # How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name) 
print(t2.name)
print(t3.name) # How  to  print  name  of  each  thread
t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three' # How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name) # One
print(t2.name) # Two
print(t3.name) # Three
print(active_count()) # How  to  print  number  of  threads  under  execution ---> 1

try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')
# Arithmetic Error
# End
