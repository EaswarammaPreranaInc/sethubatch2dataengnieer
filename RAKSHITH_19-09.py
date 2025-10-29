# Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

import random as r
for i in range(10):
    for j in range(6):
        print(r.randrange(0,9),end='')
    print()    
    
'''
output:
564300
208706
217587
235458
285304
656346
038314
782871
031762
817210
'''     


# Find  outputs

import  os
os . system('dir')              # dir is dos command it will return all the files and sub directories of the cwd 
os . system('pause')            # pause is dos command it will pause the program until user presses any key
os . system('cls')              # cls is dos command whice will clears the screen
os . system('py  sample.py')    #  py  sample.py executes  


''' 
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''

import os,sys
n=input('Enter  directory  name  (or) path :  ')
try:
    os.mkdir(n)
    print(F'Directory  {n}  created')
except:
    print(F'Directory  {n}  already  exists')

'''
Enter  directory  name  (or) path :  a
Directory  a  created
Enter  directory  name  (or) path :  b
Directory  b  already  exists
Enter  directory  name  (or) path :  c/d
Directory c/d  created
'''
       
 
''' 
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''

import os
n=input('Enter  directory  path :  ')
try:
    os.makedirs(n)
    print(F'Directory  (or) directories {n}  created')
except:
    print(F'Directory  {n}  already  exists')

'''
Enter  directory  path :  a/b/c
Directory  (or) directories a/b/c  created
Enter  directory  path :  a/b/c
Directory  a/b/c  already  exists
'''


''' 
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''

import os
n=input('Enter  directory  name  (or) path  :  ')
try:
    os.rmdir(n)
    print(F'Directory  {n}  is  removed')
except FileNotFoundError:
    print(F'Directory  {n}  does  not  exist')
except OSError:
    print(F'Directory  {n}  is  non-empty')
'''

Enter  directory  name  (or)  path :  a
Directory  a  is  removed
Enter  directory  name  (or)  path :  ssdc
Directory  ssdc  does  not  exist
Enter  directory  name  (or)  path :  c
Directory  c  is  non-empty
'''


''' 
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''

import os
n=input('Enter  directory  name  (or)  path :  ')
try:
    os.removedirs(n)
    print(F'Directories {n}  is  removed')
except FileNotFoundError:
    print(F'Directories  {n}  does  not  exist')
except OSError:
    print(F'Directory  {n}  is  non-empty')

'''
Enter  directory  name  (or)  path :  a
Directory  a  is  non-empty
Enter  directory  name  (or)  path :  a/b/c
Directories a/b/c  is  removed
Enter  directory  name  (or)  path :  a/b/c
Directories a/b/c  does  not  exist
'''


''' 
Write  a  program  to  rename  a  file  and  directory
Input  is  filename  (or)  directory  name
'''

import os
old_name = input("Enter the old filename or directory name: ")
new_name = input("Enter the new filename or directory name: ")
try:
    os.rename(old_name, new_name)
    print(f'Renamed {old_name} to {new_name}')
except FileNotFoundError:
    print(f'{old_name} does not exist')
except FileExistsError:
    print(f'{new_name} already exists')

'''
output:
Enter the current filename or directory name: c
Enter the new filename or directory name: e
Renamed c to e 
Enter the current filename or directory name: e
Enter the new filename or directory name: b
test already exists
'''


''' 
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''

import os 
n=input('Enter  file (or) directory  name:  ')
list=os.listdir(n)
a=[]
b=[]
for i in list:
    if '.' in i:
        a.append(i)
    else:
        b.append(i) 
print('List  of  the  files :   ',a)
print('List  of  the  directories :   ',b)

'''       
Enter  directory  name (or) path :  c:\sample
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
List  of  the  directories :   ['dir1', 'dir2', 'dir3']    
'''


# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

import os

n = input("Directory path: ")

for dirpath, dirnames, filenames in os.walk(n):
    print(f"Directory Path : {dirpath}")
    print(f"Sub Directories : {dirnames}")
    print(f"Files : {filenames}")
'''

Directory  Path :  sairam
Sub  Directories :  ['hyd', 'sec']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']
Directory  Path :  sairam\hyd
Sub  Directories :  ['khairtabad']
Files :  ['file1.txt']
Directory  Path :  sairam\hyd\khairtabad
Sub  Directories :  []
Files :  []
Directory  Path :  sairam\sec
Sub  Directories :  ['cyb']
Files :  ['file1.txt','file2.txt']
Directory  Path :  sairam\sec\cyb
Sub  Directories :  []
Files :  []
'''