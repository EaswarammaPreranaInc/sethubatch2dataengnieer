
# Q1: Repeat previous program such that OTP can be between 000000 and 999999 (may be 000156)
from random import *
for i in range(10):
    print(f"{randint(0, 999999):06d}")

'''
Sample Output:
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


# Q2: Find outputs
import os
os.system('dir')
os.system('pause')
os.system('cls')
os.system('py test.py')

'''
Sample Output (depends on system):
(Displays directory listing of current folder)
(Waits for user input due to pause)
(Clears screen)
(Runs test.py file if present)
'''


# Q3: Write a program to create a directory
import os
path = input("Enter directory name (or) path : ")
if not os.path.exists(path):
    os.mkdir(path)
    print(f"Directory {path} created")
else:
    print(f"Directory {path} already exists")

'''
Sample Output:
Enter directory name (or) path : sssdc2
Directory sssdc2 created
Enter directory name (or) path : sssdc2
Directory sssdc2 already exists
Enter directory name (or) path : sssdc2/khairtabad
Directory sssdc2/khairtabad created
'''


# Q4: Write a program to create a group of directories
import os
path = input("Enter directory path : ")
os.makedirs(path, exist_ok=True)
print("Directory (or) directories created")

'''
Sample Output:
Enter directory path : a/b/c
Directory (or) directories created
'''


# Q5: Write a program to delete a directory
import os
path = input("Enter directory name (or) path : ")
try:
    os.rmdir(path)
    print(f"Directory {path} is removed")
except FileNotFoundError:
    print(f"Directory {path} does not exist")
except OSError:
    print(f"Directory {path} is non-empty")

'''
Sample Output:
Enter directory name (or) path : temp
Directory temp is removed
Enter directory name (or) path : temp
Directory temp does not exist
Enter directory name (or) path : sairam
Directory sairam is non-empty
'''


# Q6: Write a program to delete a group of directories
import os, shutil
path = input("Enter directory path : ")
if os.path.exists(path):
    shutil.rmtree(path)
    print(f"Directories {path} removed")
else:
    print("Directory does not exist")

'''
Sample Output:
Enter directory path : a/b/c
Directories a/b/c removed
'''


# Q7: Write a program to rename a file and directory
import os
old = input("Enter filename (or) directory name to rename: ")
new = input("Enter new name: ")
if os.path.exists(old):
    os.rename(old, new)
    print(f"{old} renamed to {new}")
else:
    print(f"{old} does not exist")

'''
Sample Output:
Enter filename (or) directory name to rename: old.txt
Enter new name: new.txt
old.txt renamed to new.txt
'''


# Q8: Write a program to print all the files and sub-directories of input directory
import os
path = input("Enter directory name (or) path : ")
files = []
dirs = []
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        files.append(entry)
    else:
        dirs.append(entry)

print("List of the files :", files)
print("List of the directories :", dirs)

'''
Sample Output:
Enter directory name (or) path : c:\sssdc2
List of the files : ['file1.txt', 'file2.txt', 'file3.txt']
List of the directories : ['dir1', 'dir2']
'''

# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
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
path = "saiam"   # root directory
for dirpath, dirnames, filenames in os.walk(path):
    print("Directory Path :", dirpath)
    print("Sub Directories :", dirnames)
    print("Files :", filenames)
    print()

#output
Directory Path : saiam
Sub Directories : ['Karnataka', 'Telangana']
Files : ['file1.txt', 'file2.txt', 'file3.txt']

Directory Path : saiam\Karnataka
Sub Directories : ['bangalore']
Files : ['file1.txt']

Directory Path : saiam\Karnataka\bangalore
Sub Directories : []
Files : []

Directory Path : saiam\Telangana
Sub Directories : ['Hyd', 'Warangal']
Files : ['file1.txt', 'file2.txt']

Directory Path : saiam\Telangana\Hyd
Sub Directories : ['banjara hills']
Files : []

Directory Path : saiam\Telangana\Hyd\banjara hills
Sub Directories : []
Files : []

Directory Path : saiam\Telangana\Warangal
Sub Directories : []
Files : ['file1.txt']
