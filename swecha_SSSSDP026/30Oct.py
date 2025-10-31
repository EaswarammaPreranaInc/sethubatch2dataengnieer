'''
Modify  following  program  such  that  new  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp():
	main = main_thread()
	main.join()
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')



#Find  outputs (Home work)
from  threading  import  *
main = main_thread()
name  =  main . name
print(name , ' is started')#main thread is started
main . join()#error
print(name , 'is ended')


# '''
# Modify  following   program  such  that  t1  should  execute  double()  function  and
#t2  should  execute  square()  function

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
start = time . time()
t1 = Thread(target=double)
t2 = Thread(target=square)
# start threads
t1.start()
t2.start()
t1.join()
t2.join()
end = time . time()
print(end - start) 