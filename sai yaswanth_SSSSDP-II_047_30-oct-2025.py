from threading import *
import time

def disp():
    for i in range(10):
        print('new thread')
        time.sleep(0.2)

new = Thread(target=disp)
new.start()

for i in range(10):
    print('main thread')
    time.sleep(0.2)

main_thread = current_thread()
for t in enumerate():
    if t is not main_thread:
        t.join()








# Find outputs (Home work)
from threading import *
main = main_thread()
name = main.name                
print(name , ' is started')     #  MainThread is started
main.join()                     
print(name , 'is ended')        # Not executed





from threading import *
import time

def double():
    for i in range(1, 7):
        print('Double :', 2 * i)
        time.sleep(1)

def square():
    for i in range(1, 7):
        print('Square :', i * i)
        time.sleep(1)

# End of the function
t1 = Thread(target=double)
t2 = Thread(target=square)

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()
print(end - start)