# Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread() . join(10)           # Child waits 10 sec for main thread (times out)
	for  i  in  range(10):
		print('new  thread')            # Output: 10 times 'new thread' after timeout
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')               # Output: 10 times 'main thread' (with 2 sec delays)
	time . sleep(2)
# Final output order: ~5 'main thread' -> 10 'new thread' -> ~5 'main thread'

#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join()              # Child waits for main thread forever (DEADLOCK)
	for  i  in  range(10):
		print('child  thread')           # NEVER REACHED due to deadlock
child = Thread(target = disp)
child . start()
child . join()                          # Main waits for child forever (DEADLOCK)
for  i  in  range(10):
	  print('main  thread')              # NEVER REACHED due to deadlock
# Final output: Program hangs indefinitely with no output after start
