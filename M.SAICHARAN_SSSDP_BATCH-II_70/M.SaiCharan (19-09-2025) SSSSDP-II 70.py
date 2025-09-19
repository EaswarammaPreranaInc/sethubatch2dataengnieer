                              NAME:M.SAICHARAN                       HOMEWORK
                              DATE:19-09-2025


1.#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
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

#program:
import random
def generate_otp():
    otp = random.randint(0, 999999)
    return f"{otp:06d}"
for _ in range(10):
    print(generate_otp())






2.# Find  outputs
import  os
os . system('dir')		# it gives all files and subdirectories of cwd
os . system('pause')		# pause the program execution
os . system('cls')		# clear the screen
os . system('py  test.py')	# test.py file is executed through this program




3.Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists

Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created

#program:
import os
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created")
    else:
        print(f"Directory {path} already exists")
path = input("Enter directory name (or path): ")
create_directory(path)






'''
4.Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
Enter  directory  path :  a/b/c
Directory  (or) directories  created

#program:
import os
def create_group_of_directories(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory (or) directories {path} created")
    else:
        print(f"Directory (or) directories {path} already exist")
path = input("Enter directory path: ")
create_group_of_directories(path)






5.Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory

Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty

#program:
import os
import shutil
def delete_directory(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            try:
                os.rmdir(path) 
                print(f"Directory {path} is removed")
            except OSError:
                print(f"Directory {path} is non-empty")
        else:
            print(f"{path} is not a directory")
    else:
        print(f"Directory {path} does not exist")
path = input("Enter directory name (or) path: ")
delete_directory(path)






6.Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path

#Program:
import os
import shutil
def delete_group_of_directories(paths):
    for path in paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                try:
                    os.rmdir(path)  
                    print(f"Directory {path} is removed")
                except OSError:
                    print(f"Directory {path} is non-empty")
            else:
                print(f"{path} is not a directory")
        else:
            print(f"Directory {path} does not exist")

paths = input("Enter directory paths separated by commas: ").split(',')
delete_group_of_directories([path.strip() for path in paths])







7.Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name

#program:
import os
def rename_item(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"{old_name} renamed to {new_name}")
    else:
        print(f"{old_name} does not exist")
old_name = input("Enter old file or directory name: ")
new_name = input("Enter new file or directory name: ")
rename_item(old_name, new_name)






8.Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']

#program:
import os
def list_files_and_dirs(path):
    files = []
    dirs = []
    for root, subdirs, filenames in os.walk(path):
        dirs.extend(subdirs)
        files.extend(filenames)
        break  # Only list top-level files and directories
    print(f"List of the files: {files}")
    print(f"List of the directories: {dirs}")
path = input("Enter directory name (or) path: ")
list_files_and_dirs(path)





9.# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']

Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']

Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []

#program:
import os
def iterate_directory(path):
    for root, dirs, files in os.walk(path):
        print(f"\nDirectory Path: {root}")
        print(f"Sub Directories: {dirs}")
        print(f"Files: {files}")
path = input("Enter directory name (or) path: ")
iterate_directory(path)
