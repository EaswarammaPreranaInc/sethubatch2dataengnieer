# Bathini  Raju  SSSSDP  103
# Date : 19-09-2023


#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
# program
from random import randint
for x in range(10):
    print(randint(000000,999999))

Output :
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

# Find  outputs
import  os
os . system('dir') # diplay the all the directories and files of current working directory
os . system('pause') # 'pause' function pause excution of the program
os . system('cls') # clears the file 
os . system('py  test.py') # excutes the module or program


'''

Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''

# program
import os 
n=input("Enter  directory  name  (or) path :")
try :
    os.mkdir(n)
    print(F'Directory {n} Created')
except FileExistsError:
    print(F'Directory {n} already  exists')


Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists

Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
# program
import os 
n=input("Enter  directory  name  (or) path :")
try :
    os.makedirs(n)
    print(F'Directory {n} Created')
except FileExistsError:
    print(F'Directory {n} already  exists')

Enter  directory  path :  a/b/c
Directory  (or) directories  created


Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory

# program
import os 
n=input("Enter  directory  name  (or) path :")
try :
    os.rmdir(n)
    print(F'Directory {n} is removed')
except FileNotFoundError:
    print(F"Directory {n}  does  not  exist")
except OSError:
    print(F'Directory {n} is  non-empty')

Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty


Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
# program
import os 
n=input("Enter  directory  name  (or) path :")
try :
    os.removedirs(n)
    print(F'Directory {n} is removed')
except FileNotFoundError:
    print(F"Directory {n}  does  not  exist")
except OSError:
    print(F'Directory {n} is  non-empty')

Write  a  program  to  rename  a  file  and  directory

# program
import os
n=input("Enter Existing  directory  name  (or) path :")
m=input("Enter Rename the directory  name  (or) path :")
os.rename(n,m)
print(F'{n} Directory or file Renamed to {m} ')

Input  is  filename  (or)  directory  name

Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

# program
import os
path = input("Enter directory name (or) path : ").strip()
files_list = []
dirs_list = []
if os.path.exists(path):
    for item in os.listdir(path):
        full_item = os.path.join(path, item)
        if os.path.isfile(full_item):
            files_list.append(item)
        elif os.path.isdir(full_item):
            dirs_list.append(item)
    print("\nList of the files :", files_list)
    print("\nList of the directories :", dirs_list)
else:
    print("Invalid path! Please enter a valid directory.")

Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']

# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

# program
import os
start_dir = "sairam"
if os.path.exists(start_dir):
    for dirpath, dirnames, filenames in os.walk(start_dir):
        print("\nDirectory  Path :", dirpath)
        print("Sub  Directories :", dirnames)
        print("Files :", filenames)
else:
    print("Directory 'sairam' not found in the current working directory.")


Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']

Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']

Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []