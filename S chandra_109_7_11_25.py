: '''
Producer  Consumer  problem  with  Queue  class  (Home  work)

1) What  does  thread  'p'  do  ?   --->   Inserts  a  random  number  between  1  and  100   into  Queue  object  and  sleeps

2) Why  thread  'p'  sleeps   after  insertion ? --->  So  that  thread  'c'  gets  a  chance  to  remove  the  element

3) What  does  thread  'c'  do ?   --->  Removes  the  element  from  Queue  object  and  prints

4) When  can  thread  'c'  remove  an  element  from  Queue  object ?  --->  When  Queue  object  is  not  empty

5) What  does  thread  'c'  do  when  object  is  empty ?  --->
										 Automatically  waits  as  get()  method  can  not  remove  an  element  empty  Queue

6) How  long  are  the  two  threads   executed ?  --->  Infinite  times
'''
################################################
from threading import Thread
from queue import Queue
import random
import time

q = Queue()   # Create Queue object

# Producer Thread
def producer():
    while True:
        n = random.randint(1, 100)   # generate random number
        q.put(n)                     # insert into queue
        print(f'Producer produced : {n}')
        time.sleep(1)                # sleep so consumer gets chance

# Consumer Thread
def consumer():
    while True:
        n = q.get()                  # removes element (waits if empty)
        print(f'Consumer consumed : {n}')
        time.sleep(1)

# Create threads
p = Thread(target=producer)
c = Thread(target=consumer)

# Start threads
p.start()
c.start()






: def   create(f):
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

###############################
def create(f):
    print('Enter text terminated by ctrl+z')
    lines = []                         # list to store lines
    try:
        while line := input():         # read until Ctrl+Z
            lines.append(line + '\n')  # store each line
    except EOFError:
        f.writelines(lines)            # write list to file
        print(f'File {f.name} is created')
# End of function

fname = input('Enter filename : ')
f = open(fname, 'w')
create(f)
f.close()





: '''
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
How  to  close  the  file
####################################
def create(f):
    print('Enter text terminated by ctrl + z')
    lines = []                          # list to store input lines
    try:
        while line := input():          # read each line until Ctrl+Z
            lines.append(line + '\n')   # add newline and store in list
    except EOFError:
        f.writelines(lines)             # write entire list to file
        print(f'File {f.name} is created')
# End of function

fname = input('Enter filename : ')
f = open(fname, 'w')
create(f)
f.close()







: '''  (Home  work)
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
How  to  close  the  file
##################################
def disp(f):
    data = f.read()                             # read whole file
    print(f'Data of the file {f.name}')
    print(data)                                 # print file content
# End of function

fname = input('Enter filename : ')
f = open(fname, 'r')                            # open file in read mode
disp(f)
f.close()






: '''  (Home  work)
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
##############################################     

import os

def disp(f):
    count = 0
    line = f.readline()              # read first line
    while line:
        print(line, end='')          # print line without extra newline
        count += 1
        if count == 20:              # after 20 lines
            os.system('pause')       # wait for user
            os.system('cls')         # clear screen
            count = 0                # reset counter
        line = f.readline()          # read next line
# End of function

fname = input('Enter filename : ')
f = open(fname, 'r')                 # open in read mode
disp(f)
f.close()







: '''  (Home  work)
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
#######################################
import os

def disp(f):
    count = 0
    line = f.readline()                    # read first line
    while line:                            # repeat until EOF
        print(line, end='')                # print each line
        count += 1
        if count == 20:                    # after 20 lines
            os.system('pause')             # wait for key press
            os.system('cls')               # clear screen
            count = 0                      # reset line counter
        line = f.readline()                # read next line
# End of function

fname = input('Enter filename : ')
f = open(fname, 'r')                       # open in read mode
disp(f)
f.close()
