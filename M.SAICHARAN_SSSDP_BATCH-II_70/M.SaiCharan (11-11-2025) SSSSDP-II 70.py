                                NAME:M.SAICHARAN                   HOMEWORK
                                DATE:11-11-2025

'''
1.#Repeat  prog6a  with  next()  function.

Reuse  class  c1  defined  in  prog6a  but   donot  rewrite  class  c1  again
'''
#Program:
from progb import Remote
import time 
r = Remote()
while True:
	try:
		print(next(r))
		time . sleep(1)
	except:
		break


2.#  Find  outputs  (Home  work)
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

#Output:
Sec is green city.
green
Sec is green city.Hyd is Hitec city.
Sec is reden city.Hyd is Hitec city.



3.#  Find  outputs (Home  work)
f = open('a.txt' , 'w+')
print(f . tell())
f . write('Hyd is green city')
print(f . tell())
f . seek(7)
print(f . read(5))
print(f . tell())

'''
H   y    d      i     s       g     r     e      e     n              c      i      t      y     eof
0   1     2     3     4    5    6    7     8     9     10    11    12     13    14    15    16    17
'''
#Output:
0
17
green
12


'''
4.#Write  a   program  to  remove  all  the   comments  in  a  python  file

1) Remove  all  single  line  comments  only  but  not   multi-line  comments

2) Do  not  remove  lines  which  starts  with  #
     Eg:  #statement  --->  Do  not  delete

3) Do  not  remove  lines  which  starts  with   <spaces>#
    Eg:  <Spaces>#   comment   --->  Do  not  delete

4) Remove  comments  which  are  at  the  end  of  statement
    Eg:   statement  #   comment  --->  Delete  the  comment

5) Input  is  filename
'''
#Program:
def remove_comments(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    new_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            new_lines.append(line)
            continue
        new_line = ""
        in_single = in_double = False
        for i, ch in enumerate(line):
            if ch == "'" and not in_double:
                in_single = not in_single
            elif ch == '"' and not in_single:
                in_double = not in_double
            elif ch == '#' and not in_single and not in_double:
                new_line = line[:i].rstrip() + '\n'
                break
        else:
            new_line = line  
        new_lines.append(new_line)
    f = open('no_comments_' + fname, 'w')
    f.writelines(new_lines)
    f.close()
    print("Comments removed successfully. Output written to: no_comments_" + fname)



5.# Write  a  program  to  perform  following  operations  on  binary   file
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
#Program:
import pickle
import os
def menu():
    print('\n1. Print binary file')
    print('2. Print ith record of the file')
    print('3. Number of records in the file')
    print('4. Append new record to the file')
    print('5. Exit')
class emp:
    def get(self):
        self.empno = int(input('Enter Emp No: '))
        self.ename = input('Enter Emp Name: ')
        self.salary = float(input('Enter Salary: '))
    def disp(self):
        print(f'{self.empno:<10}{self.ename:<15}{self.salary:>10.2f}')
def create_file(f):
    fp = open(f, 'wb')
    while True:
        e = emp()
        e.get()
        pickle.dump(e, fp)
        ch = input('Add another record (y/n)? ')
        if ch.lower() == 'n':
            break
    fp.close()
def disp_file(f):
    try:
        fp = open(f, 'rb')
        print('\nEmpNo     Name            Salary')
        print('-' * 35)
        while True:
            e = pickle.load(fp)
            e.disp()
    except EOFError:
        pass
    except FileNotFoundError:
        print('File not found!')
    finally:
        try:
            fp.close()
        except:
            pass
def num_records(f):
    count = 0
    try:
        fp = open(f, 'rb')
        while True:
            pickle.load(fp)
            count += 1
    except EOFError:
        pass
    except FileNotFoundError:
        count = 0
    finally:
        try:
            fp.close()
        except:
            pass
    return count
def display_ith_record(f, i):
    try:
        fp = open(f, 'rb')
        count = 0
        while True:
            e = pickle.load(fp)
            count += 1
            if count == i:
                print('\nRecord', i, ':')
                e.disp()
                fp.close()
                return
    except EOFError:
        print('Record does not exist!')
    except FileNotFoundError:
        print('File not found!')
    finally:
        try:
            fp.close()
        except:
            pass
def append_record(f):
    try:
        fp = open(f, 'ab')
        e = emp()
        e.get()
        pickle.dump(e, fp)
        print('Record appended successfully.')
    except FileNotFoundError:
        print('File not found!')
    finally:
        try:
            fp.close()
        except:
            pass
filename = 'sairam.txt'
if not os.path.exists(filename):
    print('Creating new binary file...')
    create_file(filename)
while True:
    menu()
    ch = int(input('Enter choice: '))

    match ch:
        case 1:
            disp_file(filename)
        case 2:
            i = int(input('Enter record number: '))
            display_ith_record(filename, i)
        case 3:
            print('Number of records:', num_records(filename))
        case 4:
            append_record(filename)
        case 5:
            print('Exiting program...')
            break
        case _:
            print('Invalid choice!')




6.# Write  a  program  to  create  a  zip  file
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

#Program:
from zipfile import ZipFile
try:
    zname = input('Enter ZIP file name (with .zip extension): ')
    zf = ZipFile(zname, 'w')
    n = int(input('How many files? : '))
    for i in range(n):
        fname = input(f'Enter name of file {i+1}: ')
        zf.write(fname)
        print(f'Added {fname} to {zname}')
except FileNotFoundError as msg:
    print('File does not exist :', msg)
print(f'ZIP file "{zname}" is created with {n} files.')

'''


7.#Write  a  program  to  print  each  file  of  zipfile

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

#Program:
from zipfile import ZipFile
import os
def disp(fname):
    f = open(fname, 'r')
    print(f'\nContents of {fname}:')
    print('-' * 40)
    print(f.read())
    if fname.endswith('.py'):
        print(f'\n--- Executing {fname} ---')
        os.system(f'py {fname}')
        print('--- End of execution ---\n')
    f.close()
def display(z):
    file_list = z.namelist()
    os.system('cls' if os.name == 'nt' else 'clear')
    for fname in file_list:
        z.extract(fname)
        disp(fname)
        input('\nPress <Enter> for next file...')
zname = input('Enter ZIP file name (with .zip extension): ')
z = ZipFile(zname, 'r')
display(z)
z.close()
print('\nAll files displayed successfully.')