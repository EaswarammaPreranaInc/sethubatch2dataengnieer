#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
for i in range(10):
    print(random.randint(000000, 999999))

# Find  outputs
import  os
os . system('dir')                         not found
os . system('pause')                       pause not found
os . system('cls')                         not found
os . system('py  test.py')                 not found

Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
import os
dir_name=input('Enter directory name or path:')
try:
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created successfully")
except:
    print('Directory already exist')

Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
import os
path=input('Enter directory path:')
try:
    os.makedirs(path)
    print(f"Directory '{path}' created successfully")
except:
    print('Directory already exist')

Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
import os
dir_name = input("Enter directory name or path: ")
try:
    os.rmdir(dir_name)  
    print(f"Directory '{dir_name}' deleted successfully.")
except FileNotFoundError:
    print("Directory not found.")
except OSError:
    print("Directory is not empty")

Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
import shutil
import os
path = input("Enter directory path: ")   
try:
    if os.path.exists(path):
        shutil.rmtree(path) 
        print(f"Directories at '{path}' deleted successfully.")
    else:
        print("Path not found.")
except:
    print(f"Directory does not exist")

Write  a  program  to  rename  a  file  and  directory
import os
old_name = input("Enter current file/directory name (or path): ")
new_name = input("Enter new name (or path): ")
try:
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}' successfully.")
except FileNotFoundError:
    print("File or directory not found.")
except Exception as e:
    print(f"Error: {e}")

Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
import os
path = input("Enter directory path: ")
try:
    items = os.listdir(path)
    files = [f for f in items if os.path.isfile(os.path.join(path, f))]
    dirs = [d for d in items if os.path.isdir(os.path.join(path, d))]
    print("Files:", files)
    print("Directories:", dirs)
except FileNotFoundError:
    print("Directory not found.")
except NotADirectoryError:
    print("Path entered is not a directory.")
except Exception as e:
    print(f"Error: {e}")

# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import os
dir_name =input('Enter Directory name:')
cwd = os.getcwd()
path = os.path.join(cwd, dir_name)
try:
    print(f"Iterating through directory tree of: {path}\n")
    for root, dirs, files in os.walk(path):
        print("Current directory:", root)
        print("Sub-directories:", dirs)
        print("Files:", files)
        print("-" * 40)
except FileNotFoundError:
    print("not found in current working directory.")
except Exception as e:
    print(f"Error: {e}")
