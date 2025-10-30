#1st program
'''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp():
    main=main_thread()
    main.join()
    for  i  in  range(10):
        print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')


#2nd program
# Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name #mainThread
print(name , ' is started')#mainThread is started
#main . join() #Error , main thread cannot wait for main thread to expire 
print(name , 'is ended')#mainThread is ended


#3rd program
'''
Modify  following   program  such  that  t1  should  execute  double()  function  and
t2  should  execute  square()  function
'''
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
#  End  of  the  function
start = time . time()
t1=Thread(target=double)
t2=Thread(target=square)
t1.start()
t2.start()
end = time . time()
print(end - start) #  What  is   the   execution  time ? 0.00047397613525390625