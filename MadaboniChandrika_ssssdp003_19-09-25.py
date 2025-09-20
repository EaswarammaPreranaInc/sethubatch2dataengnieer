#1st program
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random 
for i in range(10):
    t=random.randint(0,999999)
    s=str(t)
    n=len(s)
    print('0'*(6-n)+s)


#2nd program
# Find  outputs
import  os
os . system('dir') #all files and sub directories of cwd
os . system('pause') #stops the execution until a key is pressed
os . system('cls') #screen is cleared
os . system('py  test.py') #executes the test file


#3rd program
# Write  a  program  to  create  a  directory.
# Input  is  directory  name  (or)  path  of  the  directory
import os
d=input("Enter the directory name or path: ")
try:
    os.mkdir(d)
    print(f'created directory {d}')
except FileExistsError:
    print(f'directory {d} already exists')


#4th program
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os
d=input("Enter the path: ")
try:
    os.makedirs(d)
except:
    print("directory already exits")


#5th program
# Write  a  program  to  delete  a  directory.
# Input  is  directory  name  (or)  path  of  the  directory
import os
d=input("Enter the directory or path: ")
try:
    os.rmdir(d)
    print("Directory deleted")
except FileNotFoundError:
    print("file not found")
    exit()
except OSError:
    print("The directory is not empty")
    exit()


#6th program
# Write  a  program  to  delete  a  group  of  directories
# Input  is  directory  path
import os
d=input("Enter the path: ")
try:
    os.removedirs(d)
except FileNotFoundError:
    print("File Not found")


#7th program
# Write  a  program  to  rename  a  file  and  directory
# Input  is  filename  (or)  directory  name
import os
d=input("Enter directory name to be renamed: ")
new_name=input("Enter the new name: ")
try:
    os.rename(d,new_name)
    print("Rename Succesful! ")
except FileNotFoundError:
    print("File not found")
    exit()


#8th program
# Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
# Input :  Directory  (or)  path
# Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
import os 
l1=[]
l2=[]
d=input("Enter directory or path: ")
try:
    for x in os.listdir(d):
        if '.' in x:
            l1.append(x)
        else:
            l2.append(x)
    print(f'Files: {l1}')
    print(f'Directories: {l2}')
except FileNotFoundError:
    print("File not found")


#9th program
# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import os
d=input("Enter directory or path: ")
g=os.walk(d)
try:
    while True:
        tuple=next(g)
        print('Directory path: ',tuple[0], 'Sub Directories: ',tuple[1], 'Files: ',tuple[2])
except:
    print("Fully Iterated")
