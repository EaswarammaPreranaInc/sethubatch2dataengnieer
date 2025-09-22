#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156
from random import *
for i in range(11):
    otp = randint(000000,999999)
    print(str(otp).zfill(6))
'''
258447
739842
112185
681428
054290
219889
056740
845508
384423
587572
'''

import os

os.system('dir')   # Executes the 'dir' command in the system shell → lists the files & folders in the current directory.
os.system('pause') # Pauses program execution until user presses a key.
os.system('cls')   # Clears the console screen.
os.system('py test.py')  # Runs the Python program 'test.py'.



'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory



Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists

Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created
'''

import os
try:
    c = input("Enter  directory  name  (or) path : ")
    os.mkdir(f'{c}')
    print(f"Directory {c} Created")
except FileExistsError:
    print(f"Directory {c} already  exists")



'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''

import os
try:
    c = input("Enter  directory  name  (or) path : ")
    os.makedirs(f'{c}')
    print(f"Directory (or) Directories {c} Created")
except FileExistsError:
    print(f"Directory  {c}  already  exists")


'''
Enter  directory  path :  a/b/c
Directory  (or) directories  created
'''


'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
import os
try:
    n = input("Enter  directory  name  (or)  path : ")
    os.rmdir(f"{n}")
    print(f"Directory  {n}  is  removed")
except FileNotFoundError:
    print(f"Directory  {n}  does  not  exist")
except OSError:
    print(f"Directory {n} is  non-empty")

'''
Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
'''


'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''

import os
try:
    n = input("Enter  directory  name  (or)  path : ")
    os.removedirs(f"{n}")
    print(f"Directory or directories  {n}  is  removed")
except FileNotFoundError:
    print(f"Directory  or directories {n}  does  not  exist")
except OSError:
    print(f"Directory or directories {n} is  non-empty")



'''
Write  a  program  to  rename  a  file  and  directorY
Input  is  filename  (or)  directory  name
'''

import os

try:
    n = input("Enter filename (or) directory name: ")
    new_name = input("Enter new name: ")
    os.rename(n, new_name)
    print(f"{n} renamed to {new_name} successfully")

except FileNotFoundError:
    print(f"{n} does not exist")

except PermissionError:
    print("Permission denied! Cannot rename")

except Exception as e:
    print(f"Error: {e}")



'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import os
n = input("Enter Directory  (or)  path: ")
files = []
dirs = []
path = os.listdir(n)
for i in path:
    if '.' in i:
        files.append(i)
    else:
        dirs.append(i)
print(f"Directories : {dirs}")
print(f"Files :{files}")


'''
Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']
'''


'''
Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
'''
import os

n = input("Enter the directory or path: ")

for dirpath, dirnames, filenames in os.walk(n):
    print(f"Directory Path : {dirpath}")
    print(f"Sub Directories : {dirnames}")
    print(f"Files : {filenames}")
    print()

'''
Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']

Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']

Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []
'''