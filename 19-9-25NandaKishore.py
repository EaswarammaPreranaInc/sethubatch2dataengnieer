#Nanda Kishore Vemula
'''
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
from random import *
'''

for i in range(10):
    for j in range(6):
        print(randint(0,9),end='')
    print()

# Find  outputs
import  os
os . system('dir') #lists all files and folders of CWD
os . system('pause') #waits until you press a key
os . system('cls') #clears the screen
os . system('py  sample.py') #Runs another program from your program

'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory'''

import os
try:
    n=input("Enter  directory  name  (or) path :")
    os.mkdir(n)
    print(F'Directory  {n} created') 
except FileExistsError:
    print(F'Directory  {n}  already exists')
except FileNotFoundError:
    print('The path cannot be found')

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c'''

import os
try:
    n=input("Enter  directory  path : ")
    os.makedirs(n)
    print('Directory  (or) directories created')
except FileExistsError:
    print(F'Directory  {n}  already exists')
except FileNotFoundError:
    print('The path cannot be found')

'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory'''

import os
try:
    n=input("Enter  directory  name  (or)  path : ")
    os.rmdir(n)
    print(F'Directory  {n} is removed')
except FileNotFoundError:
    print(F"Directory  {n}  does not exist")
except OSError:
    print(F'Directory  {n} is non-empty')

'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path'''

import os
try:
    n=input("Enter  directory  name  (or)  path : ")
    os.removedirs(n)
    print(F'Directory  {n} is removed')
except FileNotFoundError:
    print(F"Directory  {n}  does not exist")
except OSError:
    print(F'Directory  {n} is non-empty')
  
'''   
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name'''

import os
try: 
    n=input("Enter  old directory  name  (or)  path : ")
    x=input("Enter new directory name (or) path : ")
    os.rename(n,x)
except FileNotFoundError:
    print(F"Directory  {n}  does not exist")

'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import os
n= input("Enter a directory path: ")
files = []
dirs = []
for i in os.listdir(n):
    full_path = os.path.join(n, i)
    if os.path.isfile(full_path):
        files.append(n)
    elif os.path.isdir(full_path):
        dirs.append(i)
print("Files:", files)
print("Directories:", dirs)


'''
# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working directory
'''
import os
n=input("Enter  old directory  name  (or)  path : ")
for root,dirs,files in os.walk(n):
    print(f"Sub Directories : {dirs}")
    print(f"Files : {files}")
    break
