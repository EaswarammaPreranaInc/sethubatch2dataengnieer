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
from queue import Queue
from threading import *
from random import *
from time import *
q=Queue()
def f1():
    while True:
        x=randint(1,100)
        q.put(x)
        print(f'{x } is inserted to queue')
        sleep(1)
    
def f2():
    while True:
        x=q.get()
        print(f'{x} is deleted from queue')
p=Thread(target=f1)
c=Thread(target=f2)
p.start()
c.start()


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
	list=[]
	print('Enter  text  terminated  by  ctrl + z')
	
	try:
		while  line :=  input():
			list.append(line + '\n')    #How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+
	except  EOFError:
			print(F'File  {f . name}  is  created')

	f.writelines(list)   #How  to  write  list  to  the  file
	print(F'File  {f.name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')
f = open(fname , 'w')
create(f)
f . close()




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
	s=f.read()	#How  to  read  the  whole  file
	print(F'Data  of  the  file  {f . name}')
	print(s)	#How  to  print  the  file
# End  of  the  function
fname = input('Enter  filename :  ')
f = open(fname , 'r')
disp(f)
f . close()

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
import time
def  disp(f):
	i=1
	while s:=f.readline():
		print(s)
		i+=1
		if i%20==0:
			#time.sleep(1)
			os . system('pause')
			os . system('cls')
	#How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
#  End  of  the  function
fname = input('Enter  filename :  ')
f = open(fname , 'r')
disp(f)
f . close()

