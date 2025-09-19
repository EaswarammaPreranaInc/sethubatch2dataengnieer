q)Repeat  previous  program  such  that  OTP  can  be  between  000000  and  999999  (may be  000156)
Ans) from random import *
def f1():
    return randint(0,1)
def f2():
    return randint(0,9)
for i in range(10):
    print(f1(),f1(),f1(),f2(),f2(),f2(),sep='')

import os   
os.system('dir')   # shows list of files & folders in current directory
os.system('pause') # waits for user to press any key
os.system('cls')   # clears the screen (in Windows)
os.system('py test.py')  # runs another Python file named test.py

q) Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
Ans) import os 
x = input('enter the name (or)path of the directory to be created : ')
try:
    os.mkdir(x)
    print(f'directory {x} is created.')
except FileExistsError:
    print(f'directory {x} already exists.')

q) Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
Ans) import os 
x = input('enter the group of directories to be created : ')
try:
    os.makedirs(x)
    print(f'directories {x} are created.')
except FileExistsError:
    print(f'directories {x} already exists.')

q) Write  a  program  to  delete  a  directory.	
Input  is  directory  name  (or)  path  of  the  directory
Ans)  import os
x = input('enter the directory name (or) path of the directory to delete: ')
try:
    os.rmdir(x)
    print(f'directory {os.path.basename(x)} is deleted.')
except FileNotFoundError:
    print(f'directory {os.path.basename(x)} does not exist.')

except OSError:
    print(f'directory {os.path.basename(x)} is not empty.')

q) Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
Ans) import os
x = input('enter the path of the directory to delete: ')
try:
    os.removedirs(x)
    print(f'directory {x} is deleted.')
except FileNotFoundError:
    print(f'directory {x} does not exist.')
except OSError:
    print(f'directory {x} is not empty.')

q) Write  a  program  to  rename  a  file  and  directory
Input  is  filename  (or)  directory  name
Ans) import os
x = input('enter the name of file or directory which is to be renamed : ')
y = input('enter the new name of file or directory : ')
if x == y:
    print("old name and new name are same. cannot rename.")
elif os.path.exists(y):
    print(f'directory {y} already exists. please enter a new name.')
else:
    os.rename(x, y)
    print(f'directory {x} is renamed to {y}.')

q) Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
Ans) import os
x = input("Enter directory name (or) path : ")
files = []
dirs = []
try:
    for x in os.listdir(x):
        if "." in x:          
            files.append(x)
        else:                    
            dirs.append(x)
    print("List of the files :", files)
    print("List of the directories :", dirs)
except FileNotFoundError:
    print(f"Directory {x} does not exist.")

q) Write  a  program  to  iterate  thru  a  directory  present  in  current  working  directory
ans)  import os
x = input("Enter the directory name (present in CWD) : ")
try:
    g = os.walk(x)  
    while True:
        dirpath, dirnames, filenames = next(g)  
        print(f"Directory Path : {dirpath}")
        print(f"Sub Directories : {dirnames}")
        print(f"Files : {filenames}\n")
except StopIteration:
    pass  
except FileNotFoundError:
    print(f"Directory {x} does not exist.")
