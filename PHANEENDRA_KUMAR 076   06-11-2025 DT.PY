'''
Producer-Consumer  problem  with  synchronization

1) Add  two  more  variables  to  buffer  object  i.e.  write  variable  and  cond  object

2) What  does  buf . write = True  indicate ?  --->  Thread  'p'  can  write  a  value  to  the  buffer  object
     What  does  buf . write = False  indicate ?  ---> Thread  'p'  can  not  write  a  value  to  the  buffer  object

3) Initialize  write  variable  and  cond  object  in  the  constructor  of  buffer  class

4) What  does  thread  'p'  do  (4  events) ?  --->
     a) Write  a  value  to  buf . x  when  buf . write = True
	 b) Modify  buf . write = False  becoz  thread  'p'  can  not  write  another  value  to  object  buf   immediately
	 c) Notify  thread  'c'  that  a  new  value  is  available  in  object   buf
	 d) Thread  'p'  waits  due  to   buf . write = False

5) What  does  thread  'c'  do  (4  events) ?  --->
	 a) Prints  buf . x  when  buf . write = False
	 b) Modify  buf . write = True  becoz  thread  'c'  can  not  print  same  value  again
	 c) Notify  thread  'p'  that  value  is  retrieved  from  object   buf
	 d) Thread  'c'  waits  due  to  buf . write = True

6) Modify  store()  and  ret()  methods  as  indicated  above
    and  also  add  constructor  to  buffer  class

7) Functions  f1() , f2()  and  the  code  outside  remains  same
'''

# Program 
from threading import *
import time
import random

class buffer:
    def __init__(self):
        self.x = None               
        self.write = True           
        self.cond = Condition()      

    def store(self, val):
        self.cond.acquire()          
        while not self.write:
            self.cond.wait()
        self.x = val
        print(f"Producer produced : {val}")
        self.write = False
        self.cond.notify()
        self.cond.release()          

    def ret(self):
        self.cond.acquire()          
        while self.write:
            self.cond.wait()
        print(f"Consumer consumed : {self.x}")
        self.write = True
        self.cond.notify()
        self.cond.release()          
def f1(buf):  
    for i in range(10):
        val = random.randint(1, 100)
        buf.store(val)
        time.sleep(random.uniform(1, 2))
def f2(buf):  
    for i in range(10):
        buf.ret()
        time.sleep(random.uniform(1, 2))
buf = buffer()
t1 = Thread(target=f1, args=(buf,))
t2 = Thread(target=f2, args=(buf,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Producer-Consumer process completed.")

# Output :
Producer produced : 42
Consumer consumed : 42
Producer produced : 90
Consumer consumed : 90
Producer produced : 57
Consumer consumed : 57
Producer produced : 37
Consumer consumed : 37
Producer produced : 57
Consumer consumed : 57
Producer produced : 80
Consumer consumed : 80
Producer produced : 64
Consumer consumed : 64
Producer produced : 19
Consumer consumed : 19
Producer produced : 5
Consumer consumed : 5
Producer produced : 47
Consumer consumed : 47
Producer-Consumer process completed.
