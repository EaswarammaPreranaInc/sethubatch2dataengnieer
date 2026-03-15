'''
Producer  Consumer  problem  with  Queue  class  (Home  work)

1) What  does  thread  'p'  do  ?   --->   Inserts  a  random  number  between  1  and  100   into  Queue  object  and  sleeps

2) Why  thread  'p'  sleeps   after  insertion ? --->  So  that  thread  'c'  gets  a  chance  to  remove  the  element

3) What  does  thread  'c'  do ?   --->  Removes  the  element  from  Queue  object  and  prints

4) When  can  thread  'c'  remove  an  element  from  Queue  object ?  --->  When  Queue  object  is  not  empty

5) What  does  thread  'c'  do  when  object  is  empty ?  --->
										 Automatically  waits  as  get()  method  can  not  remove  an  element  empty  Queue

6) How  long  are  the  two  threads   executed ?  --->  Infinite  times
'''

import threading
import queue
import random
import time
q=queue.Queue()
def producer():
    while True:
        num=random.randint(1,100)
        q.put(num)
        print(f'Produced:{num}')
        time.sleep(1)
def consumer():
    while True:
        item=q.get()
        print(f'Consumed:{item}')
        time.sleep(1)
p=threading.Thread(target=producer)
c=threading.Thread(target=consumer)
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
		print('Enter  text  terminated  by  ctrl + z')
		How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+z
		How  to  write  list  to  the  file
		print(F'File  {f.name}  is  created')
#  End  of  the  function
How  to  read  the  filename
How  to  open  the  file
How  to  call  create()  function
How  to  close  the  file

def create():
    print('Enter text terminated by ctrl+z')
    lines=[]
    try:
      while line:=input():
          lines.append(line+'\n')
   except EOFError:
      f.writelines(lines)
      print(f'File {f.name} is created')
fname=input('Enter file name:')
f=open(fname,'w')
create(f)
f.close()

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
	How  to  read  the  whole  file
	print(F'Data  of  the  file  {f . name}')
	How  to  print  the  file
# End  of  the  function
How  to  read  the  filename
How  to  open  the  file
How  to  call  disp()  function
How  to  close  the  file

def disp(f):
     data=f.read()
     print(f'Data of the file {f.name}')
     print(data)
fname=input('Enter file name:')
f=open(fname,'r')
disp(f)
f.close()

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
def  disp(f):
	How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
#  End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  call  disp()  function
How  to  close  the  file

import os
def disp(f):
    count=0
    while True:
        line=f.readline()
        if not line:
            break
        print(line,end='')
        count+=1
        if count%20==0:
            os.system('pause')
            os.system('cls')
fname=input('Enter filename:')
f=open(fname,'r')
disp(f)
f.close()
