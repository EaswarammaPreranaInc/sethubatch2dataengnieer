#Nanda Kishore Vemula
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
t1 . start() #  What  does  thread  t1  do ? 
                #Executes f1 function and output is 10 times f1 function
#t2 . start()  #  What  does  thread  t2  do ?
                # Executes m1 method of c1 class and output is 10 times m1  method  of  class  c1
#t4 . start()   #  What  does  thread  t3  do ? 
            # Executes empty run() method of Thread class and prints nothing
#t4 . start()   #  What  does  thread  t4  do ? 
            # Executes run() method of MyThread class and output is 10 times run   method  of  MyThread  class
#t5 . start()   #  What  does  thread  t5  do ?
        #Executes f1 function and output is 10 times f1 function
#t6 . start()  #  What  does  thread  t6  do ?
        #Executes f1 function and output is 10 times f1 function
#t7 . start() #  What  does  thread  t7  do ?
        # Executes empty run() method of Thread class and prints nothing
#t8 . start()   #  What  does  thread  t8  do ?
        #Executes m1 method of c1 class and output is 10 times m1  method  of  class  c1
#t9 . start()   #  What  does  thread  t9  do ?
        #Executes m1 method of c1 class and output is 10 times m1  method  of  class  c1
#t10 . start()  #  What  does  thread  t10  do ?
        #Executes run() method of MyThread class and output is 10 times run   method  of  MyThread  class
#t11 . start()   #  What  does  thread  t11  do ?
        # Executes empty run() method of Thread class and prints nothing
#t12 . start()  #  What  does  thread  t12  do ?
        #Executes m1 method of MyThread class and output is 10 times m1  method  of  MyThread  class  
t13 . start()   #  What  does  thread  t13  do ?
        #Executes f1 method of c1 class and output is 10 times f1  method  of  class  c1
        
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
Main Method
'''

# Find  outputs (Home  work)
from threading import *
#  main  thread  executes  all  the  following  statements
main = current_thread()
print(main.name) #How  to  print  name  of  main  thread
main.name='Hyd' #How  to  modify  name  of  main  thread  to   'Hyd'
print(main)#How  to  print  new  name  of  main  thread
child=Thread(name='Sec') #How  to  create  a  new  child  thread  with  name  "Sec"
print(child.name) #How  to  print  name  of  child  thread
child.name='Cyb' #How  to  modify  name  of  child  thread  to   'Cyb'
print(child.name) #How  to  print  new  name  of  child  thread
print(active_count()) #How  to  print  number  of  threads  under  execution

# Find  outputs (Home  work)
from threading import *
t1=Thread()#How  to  create  three  new  threads  t1 , t2 , t3
t2=Thread()
t3=Thread()
print('Names of Threads')
print(t1.name) #How  to  print  name  of  each  thread
print(t2.name)
print(t3.name)
t1.name='One' 
t2.name='Two'
t3.name='Three'#How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
print('New Names of Threads')
print(t1.name)
print(t2.name)
print(t3.name)
print(active_count())#How  to  print  number  of  threads  under  execution   --->  1