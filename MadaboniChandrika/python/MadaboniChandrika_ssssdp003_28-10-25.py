#1st program
#Tricky  program
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
t1 . start() #  What  does  thread  t1  do ? prints f1 function 10 times
t2 . start()  #  What  does  thread  t2  do ?prints m1 method of class c1 10 times
t3 . start()   #  What  does  thread  t3  do ?does nothing as no target and executes empty run method of Thread class
t4 . start()   #  What  does  thread  t4  do ?prints run method of MyThread class 10 times
t5 . start()   #  What  does  thread  t5  do ?prints run method of MyThread class 10 times
t6 . start()  #  What  does  thread  t6  do ?prints f1 method of class c1 10 times
t7 . start() #  What  does  thread  t7  do ?prints nothing as it executes empty run method of Thread class
t8 . start()   #  What  does  thread  t8  do ?prints run method of MyThread class 10 times
t9 . start()   #  What  does  thread  t9  do ?prints m1 method of class c1 10 times
t10 . start()  #  What  does  thread  t10  do ?prints run method of MyThread class 10 times
t11 . start()   #  What  does  thread  t11  do ?executes empty run method of Thread class so prints nothing
t12 . start()  #  What  does  thread  t12  do ?prints m1 method of MyThread class 10 times
t13 . start()   #  What  does  thread  t13  do ?prints f1 method of class c1 10 times


#2nd program
#  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()#Registers child with thread scheduler
		print('Start Method')#Start Method(2)
	def   run(self):
		print('Run Method')#Run Method (1)
child = MyThread()
child . start()
print('Main  Thread')#Main Thread (3)


#3rd program
# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
from threading import *
main = current_thread()
print(main.name)#How  to  print  name  of  main  thread
main.name="Hyd"#How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name)#How  to  print  new  name  of  main  thread
new=Thread(name="Sec")#How  to  create  a  new  child  thread  with  name  "Sec"
print(new.name)#How  to  print  name  of  child  thread
new.name="Cyb" #How  to  modify  name  of  child  thread  to   'Cyb'
print(new.name)#How  to  print  new  name  of  child  thread
print(active_count())#How  to  print  number  of  threads  under  execution


#4th program
# Find  outputs (Home  work)
from threading import *
t1=Thread()
t2=Thread()
t3=Thread()#How  to  create  three  new  threads  t1 , t2 , t3
print('Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)#How  to  print  name  of  each  thread
t1.name="One"
t2.name="Two"
t3.name="Three"#How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print(active_count())#How  to  print  number  of  threads  under  execution   --->  1
