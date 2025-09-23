
# Find  outputs
import  os
os . system('dir')
os . system('pause')
os . system('cls')
os . system('python test1.py')
'''
# output
hello from test py
'''
'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
import os
try:
    directory_name=input("Enter a directory name: ")
    os.mkdir('directory_name')
    print(f"{directory_name} is cretaed")
except FileExistsError:
    print(f"{directory_name} already exists.")
'''
# output:
Enter a directory name: dir1
dir1 is cretaed
Enter a directory name: dir1
dir1 already exists.
'''
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os
try:
    path = input("Enter the director path")
    os.makedirs(path)
    print(f"The directoirs {path} were created successfully.")
except  OSError as e:
    print(f"Error creating directories")
'''
# output:
Enter the director path'a/b/c' 
The directoirs 'a/b/c' were created successfully.
'''
'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory.
'''
import os
try:
    name=input("Enter a input: ")
    os.rmdir(name)
    print(f"{name} is deleted")
except FileNotFoundError:
    print(f"Directory '{name}' does not exist.")
except OSError as e:
    print(f"Error deleting directory: {e}")
'''
# output:
Enter a input: 'a/b/c'
'a/b/c' is deleted

Enter a input: 'a/b/c'
Directory ''a/b/c'' does not exist.
'''
'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
import os
try:
    path = input("Enter the directory path: ")
    os.removedirs(path)  
    print(f"The directories '{path}' have been deleted successfully.")
except FileNotFoundError:
    print(f"The path '{path}' does not exist.")
except OSError as e:
    print(f"Error deleting directories: {e}")
'''
# output:
Enter the directory path: hello_world/hello_country/hello_state
The directories 'hello_world/hello_country/hello_state' have been eleted successfully.
'''
'''
Write  a  program  to  rename  a  file  and  directory
Input  is  filename  (or)  directory  name
'''
import os

try:
    old_name = input("Enter the current file : ")
    new_name = input("Enter the new name: ")

    os.rename(old_name, new_name)  
    print(f"{old_name} has been renamed to {new_name}.")
except FileNotFoundError:
    print(f"The file or directory '{old_name}' does not exist.")
except OSError as e:
    print(f"Error renaming: {e}")
'''
# output:
Enter the current file : old.txt
Enter the new name: new.txt 
old.txt has been renamed to new.txt.
'''

#Write a program to print all the files and sub-directories of input directory

import os
try:
    dir=input("Enter directory name or path: ')
    list=os.listdir(dir))
    a=b=[]
    for x in list:
        if '.' in x:
            a.append(x)
        else:
            b.append(x)
    print('List of the files: ',a)
    print()
    print('List of the directories: ',b)
except FileNotFoundError:
    print(F'Directory {dir} does not exist')

'''#output:
Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']'''

# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
    
import os
g=os.walk('sairam')
while True:
    try:
        tpl=next(g)
        print('directory path:',tpl[0])
        print('sub directories:',tpl[1])
        print('File:',tpl[2])
        os.system('pause')
        os.system('cls')
    except StopIteration:
        break
'''#output:
Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']

Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']

Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []'''


























