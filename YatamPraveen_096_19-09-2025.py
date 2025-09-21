# Find  outputs
import  os
os . system('dir')         #all the sub directories and files in the cwd of terminal
os . system('pause')         #pauses the program until any key is pressed
os . system('cls')           #dos command for clear screen 
os . system('py test.py')    #executes tesp.py moudle







'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of the directory

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2 created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already exists


Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad created

'''
import os
dirname = input('Enter  directory  name  (or) path:   ')
try:
    os.mkdir(dirname)
    print(f'Directory {dirname} created')
except FileExistsError:
    print(f'Directory {dirname} already exists')






'''
Write  a  program  to  create  a  group  of  directories.
Input : a/b/c

Enter  directory  path :  a/b/c
Directory  (or) directories created
'''

import os
dirpath = input('Enter  directory  path :  ')
try:
    os.makedirs(dirpath)
    print(f'Directory (or) directories created')
except FileExistsError:
    print(f'Directory (or) directories already exists')






'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of the directory

Enter  directory  name  (or)  path :  temp
Directory  temp is removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does not exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam is non-empty
'''

import os
path = input('Enter  directory  name  (or)  path :  ')
try:
    os.rmdir(path)
    print(f'Directory {path} is removed')
except FileNotFoundError:
    print(f'Directory  {path}  does not exist')
except OSError:
    print(f'Directory {path} is non-empty')







'''
Write  a  program  to  delete  a  group  of  directories
Input  is directory path
'''
import os
path = input('Enter the path to remove directories:  ')
try:
    os.removedirs(path)
    print(f'Directories in {path} removed')
except FileExistsError:
    print(f'Directory {path} already exists')
except OSError:
    print(f'Directory {path} is not empty')






'''
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or) directory name
'''

import os
try:
    os.rename('task1.py', 'task11.py')
    print(f'File rename successful')
except FileNotFoundError:
    print(f'The entered file is not present')







'''
Write  a program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the directories
'''

import os
path = input('Enter Directory (or) path:  ')
try:
    lst = os.listdir(path)
    files = []
    dirs = []
    for x in lst:
        if '.' in x:
            files.append(x)
        else:
            dirs.append(x)
    print(f'List of Files: {files}')
    print(f'List of Directories:  {dirs}')
except FileNotFoundError:
    print(f'The entered Directory (or) path do not exist')







# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

import os
path = input('Enter the Directory (or) Path:  ')
try:
    g = os.walk(path)
    while 1:
        try:
            tp = next(g)
            print(f'Directory path:  {tp[0]}')
            print(f'Sub Directories: {tp[1]}')
            print(f'Files:  {tp[2]}')
            print()
            print()
        except StopIteration:
            break
except FileNotFoundError:
    print(f'The exists Directory (or) path do not exists')