#Find  outputs 
from  threading  import  Thread
def  f1():
	for i in range(10):
		print('child  thread')
child = Thread(target = f1)
f1() # only one therad in the program so output can be predicted
for i in range(10):
        print('main  thread')
'''
o/p:
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''


#Find  outputs  
from threading import Thread
def  f1():
        for i in range(10) :
                print('child  thread')
child =Thread(target =  f1()) # executes f1 function and it returns None so. target=None . No child thread is created
child.start() 
for  i  in  range(10):
        print('main  thread')


#Find  outputs  
from  threading  import  *
def   f1():
        for i in range(10):
                print('child  thread')
child =Thread()
child.start() # no target is specified .so, empty run method of thread class is executed 
for i in range(10):
        print('main  thread')
'''
o/p:
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''

#Find  outputs 
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child.start()
for  i  in  range(10):
        print('Main  Thread')
#child.start() error : threads can only be started once



#Find  outputs  
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a.m1)
child.start() # child thread is created and executed prallely with the main thread and output cannot be predicted 
a.m1()
for  i  in  range(10):
	print('main  thread')



#Find  outputs 
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target = a.m1()) # executes m1 method and returns None .so. target=None and output can be predicted
child.start()
for  i  in  range(10):
        print('main  thread')
'''
o/p:
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''



#Find  outputs  
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i in range(1,11):
			print('Child  Thread  :' , i)
child = Thread(target=c1.m1) # How  to  specify  the  target  as  class  method)
child.start() # output cannot be predicted as there are 2 threads in the program that run parallely
for  i  in  range(1,11):
        print('Main  Thread  :  ' , i)



#Identify  error  
from  threading  import  Thread
class   Thread:
        def   run(self):
                for i in range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
#t.start() # error : Thread doesn't have start() method 
for  i  in  range(10):
        print('main  thread')
'''
o/p:
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''



#Find outputs  
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t =Thread()
t.start() # child thread starts and ends immediately
for  i  in  range(10):
        print('Main  Thread')
'''
o/p:
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''



# Find  outputs  
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child.run() # no thread is created only one main thread is created 
for  i  in  range(10):
        print('main  thread')




# Find  outputs 
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child.start() # start() calls thread's run() method .run() does nothing
for  i  in  range(10):
	print('Main  Thread')
'''
o/p:
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
'''



# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child.start()
print('Main  Thread')
'''
o/p:
run method
Main Thread
'''



# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for i in range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child.start() # child thread is created and output cannot be predicted
for i in range(1 , 11):
	print('Main  Thread : ' , i)
 
        

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child.start()
print('Main  Thread') # Main Thread

