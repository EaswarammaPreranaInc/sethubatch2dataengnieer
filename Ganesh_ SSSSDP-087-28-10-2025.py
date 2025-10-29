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
t1 . start() #  What  does  thread  t1  do ?      # its thread class of target is f1 function  register and exceutes the target of function f1()     # output -> f1 function (10 times)
#t2 . start()  #  What  does  thread  t2  do ?	  # it is thread class of target is method register and exceutes the m1 method of c1 object   # output ->m1 method of class c1 (10 times)
#t3 . start()   #  What  does  thread  t3  do ?	  # it is thread class no target  # output  empty
#t4 . start()   #  What  does  thread  t4  do ?   # mythread class is execute run() method of mythread     # output -> run method of mythread class (10 times)
#t5 . start()   #  What  does  thread  t5  do ?	  # its mythread class override the run() method and target if f1() function executes   # # output -> f1 function   (10 times) 
#t6 . start()  #  What  does  thread  t6  do ?	  # its thread subclass t6.start is register with target executes f1() function     # outout -> f1 function  (10 times)
#t7 . start()  #  What  does  thread  t7  do ?    # its subclass thread is no target  # output -> empty
#t8 . start()   #  What  does  thread  t8  do ?    # mythread class target is register with c1() object of m1() method   # output -> m1 method of class c1 (10 times)
#t9 . start()   #  What  does  thread  t9  do ?    # t9.start is register with target of c1() object m1 method    #output -> m1 metod of class c1  
#t10 . start()  #  What  does  thread  t10  do ?   # t10 start is register with target of run() method of t4 class  # output -> run method of mythread class (10 times)
#t11 . start()   #  What  does  thread  t11  do ?  # t11 start is register with target of t7 thread run method      # output  -> empty
#t12 . start()  #  What  does  thread  t12  do ?    # t12 start is register with target of t4 m1 object of mythread class of m1 method   # output -> m1 method of mythread class (10 times)
t13 . start()   #  What  does  thread  t13  do ?    # t13 start is register with target of t7.f1() method of c1 class    # output -> f1 method of class c1  (10 times)





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
	ouptu
 Run Method
 Start Method
 Main Thread
'''



 # Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print('main thread name: ',main.name)                # How  to  print  name  of  main  thread
print(main.name='Hyd')                               # How  to  modify  name  of  main  thread  to   'Hyd'
print('modified thread name :' , main.name)          # How  to  print  new  name  of  main  thread
def display:
	child=current_thread()          	    
	print('child thread name: ',child.nam )       # How  to  create  a  new  child  thread  with  name  "Sec"

child.name='Cyb'				     # How  to  modify  name  of  child  thread  to   'Cyb'
print('modified child name: ',child.name)	     # How  to  print  new  name  of  child  thread
print((current.count())				     # How  to  print  number  of  threads  under  execution
t.start()
t.join()
print('current.count())




 # Find  outputs (Home  work)
from threading import *
  # How  to  create  three  new  threads  t1 , t2 , t3
t1 = Thread(target=display)
t2 = thread(target=display)
t3 = Thread(target=display)
print('Names of Threads')
  # How  to  print  name  of  each  thread
print(t1.name)
print(t2.name)
print(t3.name)
# How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
t1.name='one
t2.name='Two'
t3.name='Three'
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
# How  to  print  number  of  threads  under  execution   --->  1
print('number od thread under execution: ',active.count())





#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')


'''
Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> 
'''
'''
	output
 Arithmetic Error
 End
'''