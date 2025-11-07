# Program
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

from threading import *
from queue import *
from random import *
import time
q = Queue()
def producer():
    while True:
        num =randint(1, 100)
        q.put(num) 
        print(f"Producer produced: {num}")
        time.sleep(1)  
def consumer():
    while True:
        item = q.get()  
        print(f"Consumer consumed: {item}")
        q.task_done()
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()

# Output :
Producer produced : 94
Consumer consumed : 94
Producer produced : 78
Consumer consumed : 78
Producer produced : 89
Consumer consumed : 89
Producer produced : 11
Consumer consumed : 11
Producer produced : 26
Consumer consumed : 26
Producer produced : 97
Consumer consumed : 97
Producer produced : 87
Consumer consumed : 87
Producer produced : 36
Consumer consumed : 36
Producer produced : 7
Consumer consumed : 7
Producer produced : 86
Consumer consumed : 86

# Program
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

# Output :
Enter  filename :  rishi
Type  text  terminated  by  ctrl+z
^Z
File  rishi  is  created

# Program 3
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
How  to  close  the  file

def create(f):
    print('Enter text terminated by ctrl+z (or press Ctrl+D on Linux/Mac):')
    lines = []  
    try:
        while True:
            line = input()  
            lines.append(line + '\n')  
    except EOFError:  
        pass
    
    f.writelines(lines) 
    print(f'File {f.name} is created')
filename = input('Enter file name: ')
f = open(filename, 'w')   
create(f)
f.close() 

# Output :
Rama Rao
9247
+-$
Hyd is green city


# Program 4
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
How  to  close  the  file

# Program 5
def disp(f):
    data = f.read()  # Read the whole file content
    print(f'Data of the file {f.name}')
    print(data)      # Print file data

# --- main section ---
filename = input('Enter file name: ')
f = open(filename, 'r')  # Open file in read mode
disp(f)
f.close()  # Close the file

# Output :
Enter file name: rishi
Data of the file rishi


# Program 6
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

# Output :
Enter file name: sample.txt
Rama Rao
9247
+-$
Hyd is green city
...
<After 20 lines>
Press any key to continue . . .



# Program 7
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
    count = 0
    line = f.readline()        # Read first line of file
    while line:                # Continue until end of file
        print(line, end='')    # Print each line
        count += 1

        if count == 20:        # After 20 lines
            os.system('pause') # Pause the screen
            os.system('cls')   # Clear the screen
            count = 0          # Reset line count

        line = f.readline()    # Read next line
# End of the function

filename = input('Enter file name: ')
f = open(filename, 'r')        # Open file in read mode
disp(f)                        # Call function
f.close()                      # Close the file

# Output :
Enter file name: sample.txt
Rama Rao
9247
+-$
Hyd is green city
...
<After 20 lines>
Press any key to continue . . .

