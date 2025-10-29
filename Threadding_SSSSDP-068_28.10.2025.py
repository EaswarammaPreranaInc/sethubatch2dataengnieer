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
t1 . start() #  What  does  thread  t1  do ?  # Register  f1  function to TS and run  it
t2 . start()  #  What  does  thread  t2  do ?  # Register  m1  method  of  c1  class  to TS and run  it
t3 . start()   #  What  does  thread  t3  do ?  # Calls  run  method  of  Thread  class  which  is  empty 
t4 . start()   #  What  does  thread  t4  do ?  # Calls  run  method and m1 methods  of  MyThread  class 
t5 . start()   #  What  does  thread  t5  do ?  #  Register  f1  function  to TS and run  it
t6 . start()  #  What  does  thread  t6  do ?  #  Register  f1  function  to TS and run  it
t7 . start() #  What  does  thread  t7  do ?  #  register  f1  method  of  c1  class  to TS and run  it
t8 . start()   #  What  does  thread  t8  do ?  #  Register  m1  method  of  c1  class  to TS and run  it
t9 . start()   #  What  does  thread  t9  do ?    #  Register  m1  method  of  c1  class  to TS and run  it
t10 . start()  #  What  does  thread  t10  do ?  #  Calls  run  method  of  t4  object  which  is  MyThread  class
t11 . start()   #  What  does  thread  t11  do ?  #  Calls  run  method  of  t7  object  which  is  c1  class
t12 . start()  #  What  does  thread  t12  do ?  #  Calls  m1  method  of  t4  object  which  is  MyThread  class
t13 . start()   #  What  does  thread  t13  do ?  #  Calls  f1  method  of  t7  object  which  is  c1  class



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
Main  Thread
'''


# Find  outputs (Home  work)
from threading import *
main = current_thread()
print("Main Thread Name:", main.name)
main.name = "Hyd"
print("Modified Main Thread Name:", main.name)
def display():
    child = current_thread()
    print("Child Thread Name:", child.name)
    child.name = "Cyb"
    print("Modified Child Thread Name:", child.name)
t = Thread(target=display, name="Sec")
t.start()
print("Number of threads currently active:", active_count())
t.join()


# Find  outputs (Home  work)
from threading import *
def show():
    pass
t1 = Thread(target=show, name="t1")
t2 = Thread(target=show, name="t2")
t3 = Thread(target=show, name="t3")
print("Names of Threads")
print(t1.name)
print(t2.name)
print(t3.name)
t1.name = "One"
t2.name = "Two"
t3.name = "Three"
print("New Names of Threads")
print(t1.name)
print(t2.name)
print(t3.name)
print("Number of threads under execution:", active_count())

