# Find  outputs
import  os
os . system('dir')#list directory contents
os . system('pause')#pause until user enter any key
os . system('cls')#clear the terminal
os . system('py  test.py')#run test.py with python3

Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory

import os
a = input("enter directory name:")
os.mkdir(a)
print(f"directory '{a}' created sucessfully")

output:enter directory name:sssdc2
directory 'sssdc2' created sucessfully

enter directory name:sssdc2
FileExistsError: [Errno 17] File exists: 'sssdc2'

enter directory name:sssdc2/khairthabad
directory 'sssdc2/khairthabad' created sucessfully


Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c

import os 
try:
   file = input("enter directory name or path of the directory:").strip()
   os.makedirs(file)
   print(f"{file} directory is created ")

except FileExistsError:
   print(f"{file} directory already there")

output:
enter group of directories:a/b/c
directory a/b/c created sucessfully

Write  a  program  to  delete  a  directory.

Input  is  directory  name  (or)  path  of  the  directory
Enter  directory  name  (or)  path :  temp
Directory  temp  is  remove
# Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist
Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty

import os 
try:
    file = input("enter directory name or path of the directory:").strip()
    os.rmdir(file)
    print(f"{file} directory is removed ")
except FileNotFoundError:
    print(f"{file} is not exist")
except OSError:
    print(f"{file} is non empty")

output:
enter directory name or path of the directory:sairam
sairam directory is removed   

Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path

import os 
try:
    file = input("enter directory name or path of the directory:").strip()
    os.removedirs(file)
    print(f"{file} directory is removed ")
except FileNotFoundError:
    print(f"{file} is not exist")
except OSError:
    print(f"{file} is non empty")

output:enter directory name or path of the directory:a/b/c
a/b/c directory is removed 


Write  a  program  to  rename  a  file  and  directory
Input  is  filename  (or)  directory  name

import os
old_name = input("Enter the current file or folder name: ")
new_name = input("Enter the new name : ")

old_path = os.path.abspath(old_name)
new_path = os.path.abspath(new_name)

try:

    if not os.path.exists(old_path):
        raise FileNotFoundError(f"'{old_path}' does not exist.")
    
    if os.path.exists(new_path):
        raise FileExistsError(f"Cannot rename. '{new_path}' already exists.")
    os.rename(old_path, new_path)
    print(f"Renamed from '{old_path}' to '{new_path}'.")

except FileNotFoundError as fnf:
    print(f"Error: {fnf}")
except FileExistsError as Fee:
    print(f"Error: {Fee}")

Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

import os 
files = input("enter directory name:")
lst=os.listdir(files)
l1=[]
l2=[]
for file in lst:
   
   if '.' in file:
      l1.append(file)
   else:
      l2.append(file)
print("list of the files:",l1)
print("list of the directories:",l2)

Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']
Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']
Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []

import os
def iterate_directory(file):
    for path, dirs, files in os.walk(file):
        print(f"Directory Path: {path}")
        print(f"Sub Directories: {dirs}")
        print(f"Files: {files}")
file= input("Enter directory name (or) path: ")
iterate_directory(file)
