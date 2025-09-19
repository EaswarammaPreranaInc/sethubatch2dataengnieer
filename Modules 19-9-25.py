#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

from random import *
def f1():
	return randint(0 , 9)
for x in range(10):
	print(f1() , f1() , f1() , f1() , f1() , f1() , sep = '')

# Find  outputs
import  os
os . system('dir') # list of all the files in cwd
os . system('pause') # pause the program execution
os . system('cls') # clears the screen
os . system('py  test.py') # outputs of the test file

'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created
'''
import os
try:
	a = input('Enter a directory name or path : ')
	os.mkdir(a)
	print(f'Directory {a} created')
except FileExistsError:
	print(f'Directory {a} already exists')


'''
Write  a  program  to  create  a  group  of  directories.
Input : a/b/c

Enter  directory  path :  a/b/c
Directory (or) directories created
'''
import os
try:
	a = input('Enter a directory name or path : ')
	os.makedirs(a)
	print(f'Directory {a} created')
except FileExistsError:
	print(f'Directory or directories {a} already exists')


'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
'''
Write  a  program  to  delete  a  directory.
Input is directory name (or) path of the directory
'''
import os
try:
	a = input('Enter a directory name or path : ')
	os.rmdir(a)
	print(f'Directory {a} Deleted')
except FileNotFoundError:
	print(f'Directory {a} is not found')


'''
Write  a  program  to  delete  a  group  of  directories
Input is directory path
'''

import os
try:
	a = input('Enter a directory name or path : ')
	os.removedirs(a)
	print(f'Directory {a} Deleted')
except FileNotFoundError:
	print(f'Directory {a} is not found')


'''
Write  a  program  to  rename  a  file  and  directory
Input is filename (or) directory name
'''
import os
try:
	a = input('Enter a directory name or path : ')
	b = input('Enter another name : ')
	os.rename(a , b)
	print(f'Directory {a} is renamed to {b}')
except FileNotFoundError:
	print(f'Directory {a} is not found')


'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List of the directories : ['dir1', 'dir2']

'''

import os
try:
	a = input('Enter a directory name or path : ')
	b = os.listdir(a)
	c = []
	d = []
	for x in b:
		if '.' in x:
			c . append(x)
		else:
			d . append(x)
	print(f'List of files : {c}')
	print(f'List of directories : {d}')
except FileNotFoundError:
	print(f'Directory {a} is not found')




