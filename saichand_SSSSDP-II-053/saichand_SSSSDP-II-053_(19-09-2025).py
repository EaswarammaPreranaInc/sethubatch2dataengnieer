'''
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
#Sample output:
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

#program:
import random
for i in range(10):
    otp = random.randint(000000, 999999)
    print( f"{otp:06d}")






# Find  outputs
import  os
os . system('dir')		# It gives all the files and sub-directories of the CurrentWorkingDirectory
os . system('pause')		# Pause the program execution until user press any key
os . system('cls')		# clear the screen
os . system('py  test.py')	# test.py file is executed through this python program




'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory

#Sample output:
Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists

Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created
'''
#program:
import os
def create_directory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory {path} created")
        else:
            print(f"Directory {path} already exists")
    except Exception as e:
        print(f"Error creating directory: {e}")

path = input("Enter directory name (or path): ")
create_directory(path)






'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c

#Sample output:
Enter  directory  path :  a/b/c
Directory  (or) directories  created
'''
#program:
import os
def create_group_of_directories(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory (or) directories {path} created")
        else:
            print(f"Directory (or) directories {path} already exists")
    except Exception as e:
        print(f"Error creating directories: {e}")

path = input("Enter directory path: ")
create_group_of_directories(path)






'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory

#Sample output:
Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
'''

#program:
import os
import shutil

def delete_directory(path):
    try:
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
    except Exception as e:
        print(f"Error deleting directory: {e}")

path = input("Enter directory name (or) path: ")
delete_directory(path)






'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
#Program:
import os
import shutil
def delete_group_of_directories(paths):
    for path in paths:
        try:
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
        except Exception as e:
            print(f"Error processing {path}: {e}")

paths = input("Enter directory paths separated by commas: ").split(',')
delete_group_of_directories([path.strip() for path in paths])







'''
Write  a  program  to  rename  a  file  and  directory
Input  is  filename  (or)  directory  name
'''

#Program:
import os
def rename_item(old_name, new_name):
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"{old_name} renamed to {new_name}")
        else:
            print(f"{old_name} does not exist")
    except FileNotFoundError:
        print(f"File or directory {old_name} not found")
    except PermissionError:
        print(f"Permission denied while renaming {old_name}")
    except Exception as e:
        print(f"Error renaming {old_name} to {new_name}: {e}")

old_name = input("Enter old file or directory name: ")
new_name = input("Enter new file or directory name: ")
rename_item(old_name, new_name)





'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

#Sample output:
Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']
'''

#program:
import os
def list_files_and_dirs(path):
    try:
        files = []
        dirs = []
        if os.path.exists(path):
            for root, subdirs, filenames in os.walk(path):
                dirs.extend(subdirs)
                files.extend(filenames)
                break
            print(f"List of the files: {files}")
            print(f"List of the directories: {dirs}")
        else:
            print(f"Path {path} does not exist")
    except Exception as e:
        print(f"Error reading directory {path}: {e}")

path = input("Enter directory name (or) path: ")
list_files_and_dirs(path)




'''
# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

#Sample output:
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

#program:
import os
def iterate_directory(path):
    try:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                print(f"\nDirectory Path: {root}")
                print(f"Sub Directories: {dirs}")
                print(f"Files: {files}")
        else:
            print(f"Path {path} does not exist")
    except Exception as e:
        print(f"Error iterating through directory {path}: {e}")
path = input("Enter directory name (or) path: ")
iterate_directory(path)
