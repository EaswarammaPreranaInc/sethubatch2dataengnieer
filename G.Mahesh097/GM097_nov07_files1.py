
'''
Producer  Consumer  problem  with  Queue  class  (Home  work)

1) What  does  thread  'p'  do  ?   --->   Inserts  a  random  number  between  1  and  100   into  Queue  object  and  sleeps

2) Why  thread  'p'  sleeps   after  insertion ? --->  So  that  thread  'c'  gets  a  chance  to  remove  the  element

3) What  does  thread  'c'  do ?   --->  Removes  the  element  from  Queue  object  and  prints

4) When  can  thread  'c'  remove  an  element  from  Queue  object ?  --->  When  Queue  object  is  not  empty

5) What  does  thread  'c'  do  when  object  is  empty ?  --->
										 Automatically  waits  as  get()  method  can  not  remove  an  element  empty  Queue

6) How  long  are  the  two  threads   executed ?  --->  Infinite  times


'''
from queue import *
from threading import Thread
from random import randint
import time
def producer(q):
    n=randint(1,100)
    q.put(n)
    print('Producer stores',n)
    time.sleep(1)

def consumer(q):
    while True:
        n=q.get()
        print('Consumer retrieves', n)
        time.sleep(1)
q = Queue()                            
p = Thread(target=producer, args=(q,))     
c = Thread(target=consumer, args=(q,))   
p.start()
c.start()
print("Press Ctrl + Break or Fn + B to stop")    
    
    
    
    
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')
f = open(fname , 'w')
create(f)
f . close()




'''
Repeat  prog5b(File-Create)  with  writelines()  method

1) Let  input  be
    Rama  Rao
    9247
    +-$
    Hyd is green city
    ctrl+z
'''
def  create(f):
		try:
			print('Enter  text  terminated  by  ctrl + z')
			a=[]
			while True:
				line= input()
				a.append(line+'\n')
		# How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+z
		# How  to  write  list  to  the  file
		except EOFError:
			f.writelines(a)
			print(F'File  {f . name}  is  created')
		print(F'File  {f.name}  is  created')
#  End  of  the  function
filename=input('Enter the filename to create:') #How  to  read  the  filename
f=open(filename,'w')    #How  to  open  the  file
create(f)   #How  to  call  create()  function
f.close()   #How  to  close  the  file






'''  (Home  work)
Write  a  program  to  print  data  of  the  file

File
-----
Rama  Rao
9247
+-$
Hyd is green city

1) Which  method  is  used  to  read  data  of  the  file  ?  ---> read()

2) Which  function  is  used  to  print  whole  data  of  the  file ?  --->  print()

3) In  which  mode  is  file  opened ?  --->  read  mode
'''
def  disp(f):
	data=f.read()	#How  to  read  the  whole  file
	print(F'Data  of  the  file  {f . name}')
	print(data)	#How  to  print  the  file
# End  of  the  function
name=input('Enter the filename to read:')	#How  to  read  the  filename
f=open(filename,'r') 	#How  to  open  the  file
disp(f)	#How  to  call  disp()  function
f.close()	#How  to  close  the  file





'''  (Home  work)
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city


1) Which  function  is  used  to  read  each  line  of  the  file  ?  --->  readline()

3) Which  function  is  used  to  print  each  line ?  ---> print()

3) How  long  is  the  procedure  repeated ?  --->  Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  --->  read  mode

5) How  to  pause  execution  for  every  20  lines ?  --->  os . system('pause')  where  pause  is  a  dos  command

6) How  to  clear  the  20  lines   before  printing   next  20  lines ?  ---> os . system('cls')  where  cls  is  a  dos  command


'''
import os
def  disp(f):
	# How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
    c=0
    while True:
        line=f.readline()
        if not line:
            break
        print(line,end='')
        c+=1
        if c==20:
            os.system('pause')
            os.system('cls')
            c=0
#  End  of  the  function
fname=input('Enter filename to read: ')	#How  to  read  filename
f=open(fname,'r')	#How  to  open  the  file
disp(f)	#How  to  call  disp()  function
f.close()	#How  to  close  the  file