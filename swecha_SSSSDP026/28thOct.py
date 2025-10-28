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
end of f1 function
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
#t1 . start() #  What  does  thread  t1  do #execute f1 function and output: prints f1 function 10 times
#t2 . start()  #  What  does  thread  t2  do : executes m1 method of class c1 and output:prints m1 method of class c1
#t3 . start()   #  What  does  thread  t3  do : no target,no run method and no output
#t4 . start()   #  What  does  thread  t4  do : executes run method of Mythread class and output:prints run method 10 times
#t5 . start()   #  What  does  thread  t5  do :MyThread(target=f1)MyThread overrides run so target is ignored → prints "run method of MyThread class" 10 times.
#t6 . start()  #  What  does  thread  t6  do :executes f1 function and output:prints f1 function 10 times
#t7 . start() #  What  does  thread  t7  do : no target, no run method and no output
#t8 . start()   #  What  does  thread  t8  do :executes m1 method of class c1 and output:prints m1 method of class c1
#t9 . start()   #  What  does  thread  t9  do :executes m1 method of class c1 and output: prints m1 method of class c1
#t10 . start()  #  What  does  thread  t10  do :executes run method of class c1 and output:prints run method of MyThread class 10 times
#t11 . start()   #  What  does  thread  t11  do :no run method in class c1 so no output
#t12 . start()  #  What  does  thread  t12  do :executes t4.m1 and output: prints m1 method of MyThread class 10 times
#t13 . start()   #  What  does  thread  t13  do :executes bound t7.m1 and output:prints m1 method of class c1 10 times



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

# output:
# Run Method
# start Method
# Main Thread



from threading import *
# main thread executes all the following statements
main = current_thread()
# print name of main thread
print("Name of main thread:", main.name)
# modify name of main thread to 'Hyd'
main.name = "Hyd"
# print new name of main thread
print("New name of main thread:", main.name)
# create a new child thread with name "Sec"
t = Thread(name="Sec")
# print name of child thread
print("Name of child thread:", t.name)
# modify name of child thread to 'Cyb'
t.name = "Cyb"
# print new name of child thread
print("New name of child thread:", t.name)
# print number of threads under execution
print("Number of threads under execution:", active_count())

# output:
# Name of main thread: MainThread
# New name of main thread: Hyd
# Name of child thread: Sec
# New name of child thread: Cyb
# Number of threads under execution: 1


# # Find  outputs (Home  work)
from threading import *
t1=Thread()
t2=Thread()
t3=Thread()#How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)#How  to  print  name  of  each  thread
t1.name='One'
t2.name='Two'
t3.name='Three'#How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print('number of Threads under execution')#How  to  print  number  of  threads  under  execution   --->  1

# output:
# Names of Threads
# Thread-1
# Thread-2
# Thread-3
# New Names of Threads
# One
# Two
# Three
# number of Threads under execution