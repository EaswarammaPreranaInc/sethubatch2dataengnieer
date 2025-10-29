# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(t1 . name) # How  to  print  name  of  child  thread
# main  thread  executes  following  statements
# How  to  create  a  new  thread  with  name  'new'   and  target  f1
t1 = Thread(tagget = f1 , name = 'new')
t1 . start() # How  to  start  the  new  thread
print(current_thread() . name)
# How  to  print  name  of   main  thread

# Find  outputs (Home  work)
from threading import *
# How  to  create  a  thread  t1  with  name  'Hyd'
t1 = Thread(name = 'Hyd')
# How  to  create  another  thread  t2  without  a  name
t2 = Thread()
# How  to  print  name  of  main  thread
print(current_thread() . name)
# How  to  print  name  of  thread  t1
print(t1.name)
# How  to  print  name  of  thread  t2
print(t1.name)
# How  to  modify  name  of  main  thread  to  'India'
current_thread() . name = 'India'
# How  to  modify  name  of  thread  t1  to  'Sec'
t1 . name = 'Sec'
# How  to  modify  name  of  thread  t2  to  'Cyb'
t2 . name = 'Cyb'
print(current_thread() . name) # How  to  print  name  of  main  thread
print(t1 . name) # How  to  print  name  of  thread  t1
print(t2 . name) # How  to  print  name  of  thread  t2
print(active_count())
# How  to  print  number  of  threads  under  execution


# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True:
		print(s , ' : ' , x)
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()
t2 . start()
print(active_count())
print('Press  ctrl + break  or  Fn + b  to  stop ')


'''
1) Which  of  the  following  are  valid ?
    args = [10]  ---> Valid  due  to  sequence
    args = (10,) ---> Valid  due  to  sequence
    args = {10}  --->  Valid  due  to  sequence
    args = 10   ---> 	Invalid  becoz  10  is  not  a  sequence
    args = 10.8 --->	Invalid  becoz  10.8  is  not  a  sequence
    args = '10'  ---> Valid  when  function  has  got  two  arguments  and  invalid  otherwise  becoz  '10'  has  2  characters
    args = (10)  ---> Invalid  becoz  10  is  not  a  sequence

2) In  general,  args  argument  of  Thread  constructor  can  be  any  sequence
'''
'''
Hyd : 10
Sec : 20
infinite times
'''

# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')
# End  of  function   f1()
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start() #   t1  executes  f1(75)
t2 . start()  #   t2  executes  f1(50)

'''
sample outputs
Rama guess 75 in attempt : 1
Rama finish in 1 attempts
Sita guess 50 in attempt : 1
Sita finish in 1 attempts
outputs may vary
'''

#  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread')
		time . sleep(2)
new = Thread(target = disp)
new . start()
new . join(10)
for  i  in  range(10):
	print('main  thread')

'''
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
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
new  thread
new  thread
new  thread
new  thread
'''

# Find  outputs (Home  work)
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
double()
square()
end = time . time()
print(end - start)

'''
Double :  2
Double :  4
Double :  6
Double :  8
Double :  10
Double :  12
Square :  1
Square :  4
Square :  9
Square :  16
Square :  25
Square :  36
12
'''

# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
# End  of  the  function
print(active_count())
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())
t1 . start()
t2 . start()
t3 . start()
print(active_count())
t1 . join()
t2 . join()
t3 . join()
print(active_count())

'''
1
1
One  is  started
Two  is  started
Three  is  started
4
Two  is  ended
One  is  ended
Three  is  ended
1

'''

# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , ' is  started')
	time . sleep(3)
	print(name , '  is  ended')
# End  of  the  function
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
list = enumerate()
for  t  in   list:
	print(t . name)
t1 . join()
t2 . join()
t3 . join()
list = enumerate()
for  t  in  list:
	print(t . name)

'''
One  is  started
Two  is  started
Three  is  started
MainThread
One
Two
Three
One   is  ended
Two   is  ended
Three   is  ended
MainThread

'''

# is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =  current_thread() . name
	print(name , 'is   started')
	time . sleep(3)
	print(name , '   is    ended')
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
print(t1 . is_alive())
print(t2 . is_alive())
print(t3 . is_alive())
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive())
print(t2 . is_alive())
print(t3 . is_alive())

'''
One  is  started
Two  is  started
Three  is  started
True
True
True
One   is  ended
Two   is  ended
Three   is  ended
False
False
False
'''


# Find  outputs (Home  work)
from  threading  import  *
import  time
def   table(n):
	print('Table  :  ' , n)
	for i  in  range(1 , 11):
		print(F'{n}  *  {i}    =   {n * i}')
		time . sleep(1)
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start()

'''
Table  :   7
7  *  1    =   7
7  *  2    =   14
7  *  3    =   21
7  *  4    =   28
7  *  5    =   35
7  *  6    =   42
7  *  7    =   49
7  *  8    =   56
7  *  9    =   63
7  *  10    =   70
Table  :   4
4  *  1    =   4
4  *  2    =   8
4  *  3    =   12
4  *  4    =   16
4  *  5    =   20
4  *  6    =   24
4  *  7    =   28
4  *  8    =   32
4  *  9    =   36
4  *  10    =   40

outputs may vary from run to run

'''


