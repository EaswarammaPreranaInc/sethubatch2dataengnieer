-------------------HOME WORKS ON 28/10/2025 -----------------------------


-----------------------------------------------------
'''
Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  ---> Prints 'f1 function' 10 times.

2) What  are  the  outputs  for  t2 . start() ?  ---> Prints 'm1 method of class c1' 10 times.

3) What  are  the  outputs  for  t3 . start() ?  ---> No output.

4) What  are  the  outputs  for  t4 . start() ?  ---> Prints 'run method of MyThread class' 10 times.

5) What  are  the  outputs  for  t5 . start() ?  ---> Prints 'run method of MyThread class' 10 times.

6) What  are  the  outputs  for  t6 . start() ?  ---> Prints 'f1 function' 10 times.

7) What  are  the  outputs  for  t7 . start() ?  ---> No output.

8) What  are  the  outputs  for  t8 . start() ?  ---> Prints 'run method of MyThread class' 10 times.

9) What  are  the  outputs  for  t9 . start() ?  ---> Prints 'm1 method of class c1' 10 times.

10) What  are  the  outputs  for  t10 . start() ?  ---> Prints 'run method of MyThread class' 10 times.

11) What  are  the  outputs  for  t11 . start() ?  ---> No output.

12) What  are  the  outputs  for  t12 . start() ?  ---> Prints 'm1 method of MyThread class' 10 times.

13) What  are  the  outputs  for  t13 . start() ?  ---> Prints 'f1 method of class c1' 10 times.
'''
from  threading  import  *
class  MyThread(Thread):
        def  run(self):
                for  i  in  range(10):
                        print('run   method  of  MyThread  class')
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  MyThread  class')
class  c1(Thread):
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  class  c1')
        def   f1(self):
                 for  i  in  range(10):
                         print('f1  method  of  class  c1')
# end of class
def   f1():
        for  i  in  range(10):
                print('f1  function')
#end of f1 function
t1 = Thread(target = f1)
t2 = Thread(target = c1() . m1)
t3 = Thread()
t4 = MyThread()
t5 = MyThread(target = f1)
t6 = c1(target =  f1)
t7 = c1()
t8 = MyThread(target = c1() . m1)
t9 = c1(target = c1() . m1)
t10 = MyThread(target = t4 . run)
t11 = c1(target = t7 . run)
t12 = c1(target = t4 . m1)
t13 = c1(target = t7 . f1)
# Run  with  any  one  of  the  following  stmts
#t1 . start() #  What  does  thread  t1  do ?  ---> Prints 'f1 function' 10 times.
#t2 . start()  #  What  does  thread  t2  do ? ---> Prints 'm1 method of class c1' 10 times.
#t3 . start()   #  What  does  thread  t3  do ? ---> No output.
#t4 . start()   #  What  does  thread  t4  do ? ---> Prints 'run method of MyThread class' 10 times.
#t5 . start()   #  What  does  thread  t5  do ? ---> Prints 'run method of MyThread class' 10 times.
#t6 . start()  #  What  does  thread  t6  do ? ---> Prints 'f1 function' 10 times.
#t7 . start() #  What  does  thread  t7  do ? ---> No output.
#t8 . start()   #  What  doess  thread  t8  do ? ---> Prints 'run method of MyThread class' 10 times.
#t9 . start()   #  What  does  thread  t9  do ? ---> Prints 'm1 method of class c1' 10 times.
#t10 . start()  #  What  does  thread  t10  do ? ---> Prints 'run method of MyThread class' 10 times.
#t11 . start()   #  What  does  thread  t11  do ? ---> No output.
#t12 . start()  #  Whats  does  thread  t12  do ? ---> Prints 'm1 method of MyThread class' 10 times.
#t13 . start()   #  What  does  thread  t13  do ? ---> Prints 'f1 method of class c1' 10 times.




--------------------------------------------------------------------------------------------------------------


#  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
# ---> Possible Output 1:
# Start Method
# Main Thread
# Run Method
#
# ---> Possible Output 2:
# Start Method
# Run Method
# Main Thread
# (The order of 'Main Thread' and 'Run Method' is not guaranteed)

from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method')
	def   run(self):
		print('Run Method')
child = MyThread()
child . start()
print('Main  Thread')
---------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print(main.name) # ---> MainThread
main.name = 'Hyd'
print(main.name) # ---> Hyd
child = Thread(name="Sec")
print(child.name) # ---> Sec
child.name = 'Cyb'
print(child.name) # ---> Cyb
print(active_count()) # ---> 1

------------------------------------------------------------------------------------------------

# Finds outputs (Home  work)
from threading import *
t1 = Thread()
t2 = Thread()
t3 = Thread()
print('Names of Threads')
print(t1.name) # ---> Thread-1 (or similar, like Thread-N)
print(t2.name) # ---> Thread-2 (or similar, like Thread-N+1)
print(t3.name) # ---> Thread-3 (or similar, like Thread-N+2)
t1.name = "One"
t2.name = "Two"
t3.name = "Three"
print('New Names of Threads')
print(t1.name) # ---> One
print(t2.name) # ---> Two
print(t3.name) # ---> Three
print(active_count()) # ---> 1

---------------------------------------------------------------------------------------------------
