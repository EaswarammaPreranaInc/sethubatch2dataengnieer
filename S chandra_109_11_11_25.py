: '''
Repeat  prog6a  with  next()  function.

Reuse  class  c1  defined  in  prog6a  but   donot  rewrite  class  c1  again
'''
#########################
# prog6b
# Repeat prog6a with next() function
# Reuse class c1 defined in prog6a but do not rewrite class c1 again

from prog6a import c1     # reuse previously defined class

# create iterator object
x = c1(5)

# use next() function instead of for loop
while True:
    try:
        print(next(x))
    except StopIteration:
        break





: #  Find  outputs  (Home  work)
f = open('a.txt' , 'w+')
f . write('Hyd is green city.')
f . seek(0)
f . write('Sec')
f . seek(0)
print(f . read())
f . seek(7)
print(f . read(5))
f . seek(0 , 2)
f . write('Hyd is Hitec city.')
f . seek(0)
print(f . read())
f . seek(7)
f . write('red')
f . seek(0)
print(f . read())

############################
| Step | Statement               | Output                                 |
| ---- | ----------------------- | -------------------------------------- |
| 1    | `print(f.read())`       | `Sec is green city.`                   |
| 2    | `print(f.read(5))`      | `green`                                |
| 3    | `print(f.read())`       | `Sec is green city.Hyd is Hitec city.` |
| 4    | Final `print(f.read())` | `Sec is reden city.Hyd is Hitec city.` |








: #  Find  outputs (Home  work)
f = open('a.txt' , 'w+')
print(f . tell())
f . write('Hyd is green city')
print(f . tell())
f . seek(7)
print(f . read(5))
print(f . tell())



'''
H   y    d             i     s          g     r     e      e     n              c      i      t      y     eof
0   1     2     3     4    5    6    7     8     9     10    11    12     13    14    15    16    17
'''
########################
| Statement          | Output |
| ------------------ | ------ |
| `print(f.tell())`  | 0      |
| `print(f.tell())`  | 17     |
| `print(f.read(5))` | green  |
| `print(f.tell())`  | 12     |








: '''
Write  a   program  to  remove  all  the   comments  in  a  python  file

1) Remove  all  single  line  comments  only  but  not   multi-line  comments

2) Do  not  remove  lines  which  starts  with  #
     Eg:  #statement  --->  Do  not  delete

3) Do  not  remove  lines  which  starts  with   <spaces>#
    Eg:  <Spaces>#   comment   --->  Do  not  delete

4) Remove  comments  which  are  at  the  end  of  statement
    Eg:   statement  #   comment  --->  Delete  the  comment

5) Input  is  filename
'''
#####################################
# Program to remove all single-line comments in a Python file
# but not lines starting with # or spaces + #

def remove_comments(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        stripped = line.lstrip()  # remove leading spaces (for checking)

        # 1️⃣ Keep full line if it starts with '#' or spaces + '#'
        if stripped.startswith('#'):
            new_lines.append(line)
            continue

        # 2️⃣ If '#' appears in the middle of the line → remove comment part
        if '#' in line:
            pos = line.find('#')
            line = line[:pos].rstrip() + '\n'

        new_lines.append(line)

    # Write cleaned code to a new file
    with open('output_no_comments.py', 'w') as f:
        f.writelines(new_lines)

    print("Comments removed successfully! New file: output_no_comments.py")


# ---- main code ----
fname = input("Enter Python filename: ")
remove_comments(fname)






: # Write  a  program  to  perform  following  operations  on  binary   file
def menu():
    print('1. Print  binary  file')
    print('2. Print  ith  record  of  the  file')
    print('3. Number  of  records  in  the  file')
    print('4. Append  new  record  to  the  file')
    print('5. Exit')
class  emp:
	def  get(self):
		How  to  read  empno , ename  and  salary  to  the  object  self
	def  disp(self):
		How  to  print  empno , ename  and  salary  in  the  object  self
#  End  of  the  class
def  create_file(f):
	How  to  read  each  employee  object  from  keyboard  and  write  to  the  file
	and  repeat  this  process  until  user  strikes  'n'  (or)  'N'
def  disp_file(f):
	How  to  read  each  object  of  the  file  and  print  until  eof  is  reached			
def  num_records(f):
	How  to  return  number  of   objects  in  the  file
def  display_ith_record(f , i):  #   i = 4
	How  to  print  ith  object  of  the  file  
	and  print  a  msg  when  the  object  does  not  exist
def  append_record(f , e):
    How  to  append  object  'e'  to  the  file
# End  of  the  function
How  to  open  the  file  sairam.txt  in  wb+  mode  when   program  is   executed  for  the   first  time  and 
rb+   mode  when  program  is   executed  subsequently
while True:
	menu()
	ch = int(input('Enter choice: '))
	match  ch:
		case  1:
			How  to  print  the  file
		case  2:
			i = int(input('Enter  record  number : '))
			How  to  print  ith  record  of  the  file
		case  3:
			print('Number  of  records : ' ,  ???)
		case  4:
			How  to  append  a  new  record  (or)  object  to  the  file
		case  5:
			How  to  stop  execution

#########################################################
import pickle
import os

def menu():
    print('\n----- MENU -----')
    print('1. Print binary file')
    print('2. Print ith record of the file')
    print('3. Number of records in the file')
    print('4. Append new record to the file')
    print('5. Exit')

# ------------------------------------------------
class emp:
    def get(self):
        self.empno = int(input('Enter empno: '))
        self.ename = input('Enter ename: ')
        self.salary = float(input('Enter salary: '))

    def disp(self):
        print(f'{self.empno:<10}{self.ename:<15}{self.salary:<10.2f}')
# ------------------------------------------------

def create_file(f):
    print('--- Creating and writing employee records ---')
    while True:
        e = emp()
        e.get()
        pickle.dump(e, f)
        ch = input('Add another record (y/n)? ')
        if ch in ('n', 'N'):
            break
# ------------------------------------------------

def disp_file(f):
    f.seek(0)
    print('\nEmpno     Ename          Salary')
    print('--------------------------------')
    try:
        while True:
            e = pickle.load(f)
            e.disp()
    except EOFError:
        pass
# ------------------------------------------------

def num_records(f):
    f.seek(0)
    count = 0
    try:
        while True:
            pickle.load(f)
            count += 1
    except EOFError:
        pass
    return count
# ------------------------------------------------

def display_ith_record(f, i):
    f.seek(0)
    count = 0
    try:
        while True:
            e = pickle.load(f)
            count += 1
            if count == i:
                print('\nRecord number', i, ':')
                e.disp()
                return
    except EOFError:
        print('Record does not exist!')
# ------------------------------------------------

def append_record(f):
    f.seek(0, 2)   # move to end
    e = emp()
    e.get()
    pickle.dump(e, f)
    print('Record appended successfully!')
# ------------------------------------------------

# Determine file mode
if not os.path.exists('sairam.txt'):
    f = open('sairam.txt', 'wb+')
    print('File created successfully.')
    create_file(f)
else:
    f = open('sairam.txt', 'rb+')
    print('File opened successfully.')

# ------------------------------------------------
while True:
    menu()
    ch = int(input('Enter choice: '))
    match ch:
        case 1:
            disp_file(f)

        case 2:
            i = int(input('Enter record number: '))
            display_ith_record(f, i)

        case 3:
            n = num_records(f)
            print('Number of records:', n)

        case 4:
            append_record(f)

        case 5:
            print('End of program.')
            f.close()
            break

        case _:
            print('Invalid choice!')






: # Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
try:
	How  to  read  zip   filename
	How  to  open  zip  file
	n = int(input('How  many  files ?  : ')
	for  i  in   range(n):
			How  to  read  each   filename
			How  to  write  each  file  to  zip  file
except   FileNotFoundError   as   msg:
	print('File  does  not  exist :  ' , msg)
How  to  close  zip  file
print(F'zip  file  is  created  with  {n}  files')
############################
from zipfile import ZipFile

try:
    # Read zip filename
    zname = input('Enter zip filename (with .zip extension): ')

    # Open zip file in write mode
    zf = ZipFile(zname, 'w')

    n = int(input('How many files? : '))
    for i in range(n):
        fname = input(f'Enter filename {i+1}: ')
        zf.write(fname)      # add file to zip

except FileNotFoundError as msg:
    print('File does not exist :', msg)

else:
    zf.close()
    print(f'Zip file "{zname}" is created successfully with {n} files.')







: '''
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
from  zipfile  import  ZipFile
import  os
def  disp(fname):
	How  to  print  contents  of  the  file
	How  to  execute  file  if  it  is  .py  file
	How  to  close  the  file
def  display(z):
	How  to  obtain  all  the  files  from  zip  file
	How  to  clear  screen
	How  to  print  each  file  of  zip  file  pagewise (use  disp()  function)
# End  of  the  function
How  to  read  zip  file  name
How  to  open  zip  file
How  to  print  zip  file(use  display()  function)
How  to  close  the  zip  file
############################################
from zipfile import ZipFile
import os

def disp(fname):
    # Print file name
    print(f'\n----- {fname} -----')
    
    # Open file and display its contents
    f = open(fname, 'r')
    print(f.read())
    f.close()

    # Execute if it's a Python file
    if fname.endswith('.py'):
        print(f'\nExecuting {fname}...')
        os.system(f'py {fname}')    # run the python file
        print('Execution completed.')

# ---------------------------------------------------

def display(z):
    # Obtain all the files in the zip file
    files = z.namelist()

    os.system('cls' if os.name == 'nt' else 'clear')   # clear screen (works in Windows/Linux)
    
    for fname in files:
        # Extract each file to current directory temporarily
        z.extract(fname)
        disp(fname)
        input('\nPress <Enter> to view next file...')  # pagewise display

# ---------------------------------------------------

# Read zip file name from user
zname = input('Enter zip file name (with .zip extension): ')

# Open the zip file
with ZipFile(zname, 'r') as z:
    display(z)

print('\nAll files displayed successfully.')


