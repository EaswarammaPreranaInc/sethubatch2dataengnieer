#Tarun Banala       19-09-2025
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
from random import *
for i in range(10):
    print(randint(000000,999999))

# Find  outputs
import  os
os . system('dir')  # get all subdirectiories and files in CWD
os . system('pause') # pause until press a key
os . system('cls') # clear screen
os . system('py  test.py') # run the file of text.py

# Write  a  program  to  create  a  directory.
# Input  is  directory  name  (or)  path  of  the  directory
# Write  a  program  to  create  a  directory.
# Input  is  directory  name  (or)  path  of  the  directory
import os
n=input("Enter  directory  name  (or) path :")
try:
    os.makedirs(n)
    print(f"Directory {n} created successfully")
except FileExistsError:
    print(f"Directory {n} already exists")
except Exception as e:
    print(f"Error {e}")

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os
n=input("Enter  directory  name  (or) path :")
try:
    os.makedirs(n)
    print(f"Directory  (or) directories  created successfully")
except FileExistsError:
    print(f"Directory {n} already exists")
except Exception as e:
    print(f"Error {e}")

Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
# Write  a  program  to  delete  a  directory.
# Input  is  directory  name  (or)  path  of  the  directory
import os
try:
    n=input("Enter  directory  name  (or)  path :")
    os.rmdir(n)
    print(f"Directory  {n}  is  removed")
except FileNotFoundError:
    print(f"Directory  {n}  does  not  exist")
except OSError as e:
    print(f"Directory {n} is non-empty")

Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
import os
try:
    n=input("Enter  directory  name  (or)  path :")
    os.removedirs(n)
    print(f"Directory  {n}  is  removed")
except FileNotFoundError:
    print(f"Directory  {n}  does  not  exist")
except OSError as e:
    print(f"Directory {n} is non-empty")

# Write  a  program  to  rename  a  file  and  directory

# Input  is  filename  (or)  directory  name
import os
m=input("enter original file name:")
n=input("enter a  change name :")
try:
    os.rename(m,n)
    print(f"directory {m} to {n} successfully")
except FileNotFoundError:
    print(f"directory {m} not found")
except FileExistsError:
     print(f"directory {n} already exists")
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
import os

n = input("Enter directory name (or) path : ")

try:
    items = os.listdir(n)   # get all files + subdirs
    files = []
    dirs = []

    for item in items:
        path = os.path.join(n, item)
        if os.path.isfile(path):
            files.append(item)
        elif os.path.isdir(path):
            dirs.append(item)

    print("List of the files :", files)
    print("\nList of the directories :", dirs)

except FileNotFoundError:
    print(f"Directory {n} does not exist")
except Exception as e:
    print("Error:", e)
# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import os

# directory to iterate
n = "sairam"   # or input("Enter directory name (or) path : ")

for dirpath, dirnames, filenames in os.walk(n):
    print(f"Directory Path : {dirpath}")
    print("Sub Directories :", dirnames)
    print("Files :", filenames)
    print()
