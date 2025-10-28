'''
1) What  are  the  outputs  for  t1 . start() ?  ---> 10 times f1 function

2) What  are  the  outputs  for  t2 . start() ?  ---> 10 times m1 method of class c1

3) What  are  the  outputs  for  t3 . start() ?  ---> no output

4) What  are  the  outputs  for  t4 . start() ?  ---> 10 times run method of Mythread class

5) What  are  the  outputs  for  t5 . start() ?  ---> 10 times run method of Mythread class

6) What  are  the  outputs  for  t6 . start() ?  ---> 10 times f1 function

7) What  are  the  outputs  for  t7 . start() ?  ---> no output

8) What  are  the  outputs  for  t8 . start() ?  ---> 10 times run method of Mythread class

9) What  are  the  outputs  for  t9 . start() ?  ---> 10 times m1  method  of  class  c1

10) What  are  the  outputs  for  t10 . start() ?  ---> 10 times run   method  of  MyThread  class

11) What  are  the  outputs  for  t11 . start() ?  ---> no output

12) What  are  the  outputs  for  t12 . start() ?  ---> 10 times m1  method  of  MyThread  class

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
#t1.start() #  What  does  thread  t1  do ? as target=f1 function main thread creates a new thread and executes f1 function
#t2.start()  #  What  does  thread  t2  do ? executes m1 method of c1 class
#t3.start()   #  What  does  thread  t3  do ? creates thread and does nothing because no target is specified
#t4.start()   #  What  does  thread  t4  do ? as no target is specified executes run method of MyThread class
#t5.start()   #  What  does  thread  t5  do ? executes run method of MyThread class because run method has higher priority than the target
#t6.start()  #  What  does  thread  t6  do ? executes f1 function
#t7.start() #  What  does  thread  t7  do ? does nothing as there is no run() method and target 
#t8.start()   #  What  does  thread  t8  do ? executes m1 method of MyThread class
#t9.start()   #  What  does  thread  t9  do ? executes m1 method of c1 class
#t10.start()  #  What  does  thread  t10  do ? executes run method of MyThread class
#t11.start()   #  What  does  thread  t11  do ? no run method in c1 class
#t12.start()  #  What  does  thread  t12  do ? executes m1 method of MyThread class
#t13.start()   #  What  does  thread  t13  do ? executes f1 method of c1 class



#  What  are  the  outputs  when  start()  method  is  overridden  ?  
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super().start() # creates a new thread and executes run method 
		print('Start Method')
	def   run(self):
		print('Run Method')
child = MyThread()
child.start() # executes start method of MyThread class
print('Main  Thread')
'''
o/p:
Run method
start method
Main Thread
'''



# Find  outputs 
from threading import *
# main thread executes all  the  following  statements
main = current_thread()
print(main.name) #  print  name  of  main  thread
main.name='Hyd' #  modify  name  of  main  thread  to 'Hyd'
print(main.name) #  print  new  name  of  main  thread
child=Thread(name='sec') #  create  a  new  child  thread with name "Sec"
print(child.name) #  print  name  of  child  thread
child.name='cyb' #  modify  name  of  child  thread  to 'Cyb'
print(child.name) #  print  new  name  of  child  thread
print(active_count()) #  print  number  of  threads  under execution



# Find  outputs 
from threading import *
t1=Thread()
t2=Thread()
t3=Thread() # create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name) 
print(t2.name) 
print(t3.name) # print  name  of  each  thread
t1.name='one'
t2.name='Two'
t3.name='Three' # modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print(active_count()) # print  number  of  threads  under  execution   --->  1
