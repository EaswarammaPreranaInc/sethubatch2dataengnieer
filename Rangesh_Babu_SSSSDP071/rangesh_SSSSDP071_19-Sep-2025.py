#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
from random import choice
lst = []
for i in range(1000000):
    lst.append(str(i).zfill(6)) 
for j in range(10):
    print(choice(lst[j]))  

# Find  outputs
import  os
os . system('dir')# Lists files and folders in current directory
os . system('pause')# Pauses the program until user presses a key
os . system('cls')# Clears the screen
os . system('py  test.py')# Runs test.py program

#Write  a  program  to  create  a  directory.
#Input  is  directory  name  (or)  path  of  the  directory
import os
dname = input("Enter directory name or path: ") 
os.mkdir(dname)
print(f"Directory {dname} created")  

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os
dname = input("Enter directory name or path: ")
os.makedirs(dname)
print(f"Directories {dname} created")

'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
import os
dname = input("Enter directory name or path: ")
os.rmdir(dname)
print(f"Directory {dname} is removed")

'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path '''
import os
dname = input("Enter directory name or path: ")
os.removedirs(dname)
print(f"Directories {dname} are removed")

'''
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name
'''
import os
oldname = input("Enter old file/directory name: ")
newname = input("Enter new file/directory name: ")
os.rename(oldname, newname)
print(f"{oldname} is renamed as {newname}")

'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import os
dname = input("Enter directory name or path: ")
files = []
dirs = []
for i in dname:
    if i in '.':
        files.append(i)
    else:
        dirs.append(i)
print("Files:", files)
print("Directories:", dirs)

# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory recursively.
import os
dname = r"c:\sairam"
for foldername, subfolders, filenames in os.walk(dname):
    print(f"Folder: {foldername}")
    for subfolder in subfolders:
        print(f"Subfolder: {subfolder}")
    for filename in filenames:
        print(f"File: {filename}")
    input("Press any key to continue...")