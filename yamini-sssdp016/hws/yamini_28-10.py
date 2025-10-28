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
t1 . start() #  What  does  thread  t1  do ?
# executes f1 function and print f1 f1 function 10 times
t2 . start()  #  What  does  thread  t2  do ?
# executes m1 method of class c1 and print m1 method of class c1 10 times
t3 . start()   #  What  does  thread  t3  do ?
# runs empty run method of thread class so no output
t4 . start()   #  What  does  thread  t4  do ?
# executes run method of MyThread class and print run method of MyThread class 10 times
t5 . start()   #  What  does  thread  t5  do ?
# executes run method of mythread class as it has got high priority than target
t6 . start()  #  What  does  thread  t6  do ?
# executes f1 function of c1 class and prints f1 fucntion 
t7 . start() #  What  does  thread  t7  do ?
# as there is no target empty run method of thread class is executed which does nothing
t8 . start()   #  What  does  thread  t8  do ?
# executes run method of mythread class as it has got high priority than target
t9 . start()   #  What  does  thread  t9  do ?
#as there is no run method in c1 class  target m1 method is executed and prints m1 method of class c1 10 times
t10 . start()  #  What  does  thread  t10  do ?
# as there is rum method in mythread class it is executed and prints run method of MyThread class 10 times and target is ignored
t11 . start()   #  What  does  thread  t11  do ?
# as there is no run method in c1 class  target empty run method of thread class is executed
t12 . start()  #  What  does  thread  t12  do ?
# as there is no run method in c1 class  target m1 method of MyThread class is executed
t13 . start()   #  What  does  thread  t13  do ?
# as there is no run method in c1 class  target f1 method of c1 class is executed


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
 new thread is created 
start()  method is called
it is calling parent class start method which registers the child thread and executes run method in the new thread
run method
come back to start method and prints 'Start Method'
come back to main thread and prints 'Main Thread'
'''


# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print(main.name)    #How  to  print  name  of  main  thread
main.name='Hyd'   #How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name)    #How  to  print  new  name  of  main  thread
child=Thread(name='Sec')    #How  to  create  a  new  child  thread  with  name  "Sec"
print(child.name)  #How  to  print  name  of  child  thread
child.name='Cyb'   #How  to  modify  name  of  child  thread  to   'Cyb'
print(child.name)  #How  to  print  new  name  of  child  thread
print(active_count())  #How  to  print  number  of  threads  under  execution

# Find  outputs (Home  work)
from threading import *
t1=Thread()
t2=Thread()
t3=Thread() #How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name) #How  to  print  name  of  each  thread
t1.name='One'
t2.name='Two'
t3.name='Three' #How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print(active_count()) #How  to  print  number  of  threads  under  execution   --->  1

