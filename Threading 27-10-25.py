#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')

'''
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''


#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
'''
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''

# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')

'''
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''

# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
child . start()
a . m1()
for  i  in  range(10):
	print('main  thread')

'''


child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

output can be any order
'''

# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i  in  range(10):
        print('main  thread')

'''
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''


#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target = c1 . m1) # How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)

'''
Child  Thread  :   1
Child  Thread  :   2
Main Thread :  1
Main Thread :  2
Child  Thread  :   3
Child  Thread  :   4
Child  Thread  :   5
Child  Thread  :   6
Child  Thread  :   7
Child  Thread  :   8
Child  Thread  :   9
Child  Thread  :   10
Main Thread :  3
Main Thread :  4
Main Thread :  5
Main Thread :  6
Main Thread :  7
Main Thread :  8
Main Thread :  9
Main Thread :  10
can be any order
'''

# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start() # error as there is no start method in thread class
for  i  in  range(10):
        print('main  thread')

'''
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''


# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')

'''
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread

'''

# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child . run()
for  i  in  range(10):
        print('main  thread')


'''
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''


# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')

'''
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()
print('Main Thread')

'''
run method
Main thread
'''

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child . start()
for  i  in  range(1 , 11):
	print('Main Thread : ' , i)
'''
f1  function :  1
f1  function :  2
f1  function :  3
f1  function :  4
f1  function :  5
f1  function :  6
f1  function :  7
Main Thread :  1
f1  function :  8
f1  function :  9
f1  function :  10
Main Thread :  2
Main Thread :  3
Main Thread :  4
Main Thread :  5
Main Thread :  6
Main Thread :  7
Main Thread :  8
Main Thread :  9
Main Thread :  10

outputs can be anyorder

'''

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main Thread') # Main Thread



