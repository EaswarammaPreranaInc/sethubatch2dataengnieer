#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
for i in range(10):
 k=random.randint(0,999999)
 s=str(k)
 n=len(s)
 print('0'*(6-n)+s)

'''
297856
152860
024216
347578
775685
222711
960704
488187
783901
093577
'''

# Find  outputs
import  os
os . system('dir')#it prints the all files and subfiles of cwd
os . system('pause')#It's the dos command which pause the program
os . system('cls')#its clears the screen
os . system('py  test.py')#executes the test file


'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''

import os
a= input("enter the directory name:")
try:
  os.mkdir(a)
except FileExistsError:
  print(f'directory {a} already exists')
print(f'created directory {a}')

'''
o/p:
enter the directory name:kv
created directory kv
'''


'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''

import os
a=input ("enter directory path:")
try:
  os.makedirs(a)
except:
  print("direcctory already exits")



'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''

import os 
a =input("enter directory name or path:")
try:
  os.rmdir(a)
except FileNotFoundError:
  print("file is not found")
  exit()
except OSError:
  print("The directory is not empty")
  exit()
print("Directory deleted")  

'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''

import os
a=input("enter directory path:")
try:
 os.removedirs(a)
except FileNotFoundError:
  print("file not found")


'''
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name

'''   

import os
n= input("enter file name or directory name:")
new_name=input("Enter the new name: ")
try:
    os.rename(n,new_name)
except FileNotFoundError:
    print("File not found")
    exit()
print("Rename Succesful! ")

'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''

import os
n=input("enter directory or path:")
a=[]
b=[]
try:
  for x in os.listdir(n):
    if'.' in x:
      a.append(x)
    else:
      b.append(x)
  print(f'files:{a}')      
  print(f'Directories:{b}') 
except FileNotFoundError:
  print("File not found")  



'''
rite  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
'''

import os
d=input("Enter directory or path: ")
g=os.walk(d)
try:
    while True:
        tuple=next(g)
        print('Directory path: ',tuple[0], 'Sub Directories: ',tuple[1], 'Files: ',tuple[2])
except:
    print("Fully Iterated")