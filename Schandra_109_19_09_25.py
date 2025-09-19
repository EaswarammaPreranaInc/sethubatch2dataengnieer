: #  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
: 258447
739842
112185
681428
054290
219889
056740
845508
384423
587572

############
import random

# Generate 10 OTPs between 000000 and 999999
for i in range(10):
    otp = random.randint(0, 999999)   # generate number between 0 and 999999
    print(f"{otp:06d}")              # format as 6-digit with leading zeros







 # Find  outputs
import  os
os . system('dir')
os . system('pause')
os . system('cls')
os . system('py  test.py')

#########################
First shows the file/directory listing (dir).

Then waits for user input (pause).

Clears the screen (cls).

Finally executes and shows output of test.py.


Here’s a simple test.py example:

# test.py
print("Hello from test.py")
print("This file is executed after dir, pause, and cls")

import os

os.system('dir')        # Shows directory listing
os.system('pause')      # Waits for "Press any key to continue . . ."
os.system('cls')        # Clears the screen
os.system('py test.py') # Runs test.py



Expected Execution (Step by Step)

dir runs → you see list of files/folders (example: test.py will also appear).

pause runs →

Press any key to continue . . .


(you press a key)

cls runs → screen becomes blank.

test.py runs → output will be:

Hello from test.py
This file is executed after dir, pause, and cls



: Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
: Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created
: Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists
: Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created

##################
import os

# Take directory name or path from user
dir_name = input("Enter directory name (or) path : ")

# Check if directory exists
if os.path.exists(dir_name):
    print(f"Directory {dir_name} already exists")
else:
    os.makedirs(dir_name)   # creates all intermediate directories if needed
    print(f"Directory {dir_name} created")





: '''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
: Enter  directory  path :  a/b/c
Directory  (or) directories  created
###############
import os

# Take directory path from user
dir_path = input("Enter directory path : ")

try:
    os.makedirs(dir_path, exist_ok=True)  # creates nested directories if needed
    print("Directory (or) directories created")
except Exception as e:
    print("Error:", e)




: Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
: Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed
: Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist
: Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
#####################
import os

# Take directory name or path from user
dir_name = input("Enter directory name (or) path : ")

if not os.path.exists(dir_name):
    print(f"Directory {dir_name} does not exist")
else:
    try:
        os.rmdir(dir_name)   # removes only empty directories
        print(f"Directory {dir_name} is removed")
    except OSError:
        print(f"Directory {dir_name} is non-empty")







: Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path

###################
import os
import shutil

# Take directory path from user
dir_path = input("Enter directory path : ")

if not os.path.exists(dir_path):
    print(f"Directory {dir_path} does not exist")
else:
    try:
        shutil.rmtree(dir_path)   # deletes the whole directory tree
        print(f"Directory path {dir_path} is removed")
    except Exception as e:
        print("Error:", e)


: Write  a  program  to  rename  a  file  and  directory
#####################
import os

# Take old name (file or directory) from user
old_name = input("Enter file (or) directory name : ")

if not os.path.exists(old_name):
    print(f"{old_name} does not exist")
else:
    new_name = input("Enter new name : ")
    try:
        os.rename(old_name, new_name)
        print(f"{old_name} renamed to {new_name}")
    except Exception as e:
        print("Error:", e)


Input  is  filename  (or)  directory  name




: Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
: Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']

##############
import os

# Take directory path from user
dir_path = input("Enter directory name (or) path : ")

if not os.path.exists(dir_path):
    print(f"Directory {dir_path} does not exist")
else:
    files = []
    dirs = []
    
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if os.path.isfile(full_path):
            files.append(item)
        elif os.path.isdir(full_path):
            dirs.append(item)

    print("List of the files :", files)
    print("\nList of the directories :", dirs)





: # Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
: Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']
: Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']
: Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []

#######################

import os

# Starting directory
start_dir = "sairam"

if not os.path.exists(start_dir):
    print(f"Directory {start_dir} does not exist")
else:
    for dirpath, dirnames, filenames in os.walk(start_dir):
        print(f"Directory Path : {dirpath}")
        print("Sub Directories :", dirnames)
        print("Files :", filenames)
        print()
