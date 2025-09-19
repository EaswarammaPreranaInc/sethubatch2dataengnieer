#1 Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
for i in range(10):
    for i in range(6):
        otp = random.randint(0, 9)  # Random number between 0 and 999999
        print(otp, end = '')  # Printed as a 6-digit number with leading zeros
    print()
'''
815487
481259
737609
937488
540260
103652
383788
739850
840051
063910
'''

#2 Find  outputs
import  os
os . system('dir') # prints files and subdirectories of current working directory
os . system('pause') # Pauses execution of program
os . system('cls') # Clears the screen
os . system('py test.py') # prints the path of test.py 

#3 Write  a  program  to  create  a  directory.
import os
a = input("Enter directory name (or) path:")
try:
    os.mkdir(a)
    print("Directory test1 created")
except FileExistsError:
    print("Directory test1 is already present")
'''
Output:
Enter directory name (or) path:test1
Directory test1 created
Enter directory name (or) path:test1
Directory test1 is already present
'''

#4 Write  a  program  to  create  a  group  of  directories.
import os
n = input("Enter input:")
try:
    os.makedirs(n)
    print("Directory (or) directories created")
except FileExistsError:
    print("Directories are already present")
'''
Enter input:a/b/c
Directory (or) directories created
Enter input:a/b/c
Directories are already present
'''

#5 Write  a  program  to  delete  a  directory.
import os
n = input("Enter directory name (or) path:") 
try:
    os.rmdir(n)
    print("Directory test is removed")
except FileNotFoundError:
    print("Directory test does not exist")
except OSError:
    print("Directory a is non-empty")
'''
Output
Enter directory name (or) path:test
Directory temp is removed
Enter directory name (or) path:test
Directory temp does not exist
Enter directory name (or) path:a
Directory sairam is non-empty
'''

#6 Write  a  program to delete a group of directories
import os
n = input("Enter directiry path:")
try:
    os.removedirs(n)
    print("Directories are deleted")
except FileNotFoundError:
    print("Directories does not exist")
except OSError:
    print("Directory test1 is not empty")
'''
Enter directiry path:a/b/c
Directories are deleted
Enter directiry path:a/b/c
Directories does not exist
Enter directiry path:test1
Directory test1 is not empty
'''

#7 Write a  program to rename a file and directory
import os
n = input("Enter filename (or) directory name:")
try:
    os.rename(n, 'test3')
    print("Directory is renamed")
except FileNotFoundError:
    print("Directory is not present")
'''
Enter filename (or) directory name:test
Directory is renamed
Enter filename (or) directory name:test
Directory is not present
'''

#8 Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
import os
n = input("Enter directory name (or) path:")
a = os.listdir(n)
list1 = []
list2 = []
for i in a:
    if "." in i:
        list1.append(i) 
    else:
        list2.append(i)
print("List of the files:", list1)
print("List of the directories:", list2)
'''
Enter directory name (or) path:test1
List of the files: ['a.txt', 'c.txt']
List of the directories: ['test2']
'''

#9 Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working directory
import os
n = input("Enter directory path: ")
for a, b, c in os.walk(n):
    print("Directory Path:", a)
    print("Sub Directories:", b)
    print("Files:", c)
    print()  
'''
Enter directory path: test1
Directory Path: test1
Sub Directories: ['test2']
Files: ['a.txt', 'c.txt']

Directory Path: test1\test2
Sub Directories: []
Files: ['b']
'''
