#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
for i in range(20):
    n=''
    k=random.randrange(000000,999999)
    if(len(str(k))<6):
            n+='0'*(6-len(str(k)))+str(k)
    else:
        n+=str(k)
    print(n)

# Find  outputs
import  os
os . system('dir')  #returns all files and subfiles of the current directory
os . system('pause')    # holds execution until user press any key
os . system('cls')  # clears the terminal
os . system('py  "C:\\Users\\YAMINI\\OneDrive - vitap.ac.in\\Documents\\Yamini-SSSDP-II_16\\test.py"')  # runs the test.py from this program


#Write  a  program  to  create  a  directory.
#Input  is  directory  name  (or)  path  of  the  directory
import os
n=input()
try:
    os.mkdir(n)
    print(f'Directory {n} is created')
except:
    print(f'Directory  {n}  already  exists')

#Write  a  program  to  create  a  group  of  directories

import os
n=input()
try:
    os.makedirs(n)
    print(f'Directories {n} is created')
except:
    print(f'Directories  {n}  already  exists')


#Write  a  program  to  delete  a  directory.
#Input  is  directory  name  (or)  path  of  the  directory
import os
n=input()
try:
    os.rmdir(n)
    print(f'Directory {n} is deleted')
except PermissionError:
    print(f'Directory is not empty')
except FileNotFoundError:
    print(f'Directory {n} doesnt exist')

#Write  a  program  to  delete  a  group  of  directorie
import os
n=input()
try:
    os.removedirs(n)
    print(f'Directory {n} is deleted')
except PermissionError:
    print(f'Directory is not empty')
except FileNotFoundError:
    print(f'Directory {n} doesnt exist')

#Write  a  program  to  rename  a  file  and  directory
import os
n=input()
m=input()
try:
    os.rename(n,m)
    print(f'Directory {n} is renamed')
except FileNotFoundError:
    print(f'Directory {n} doesnt exist')

#Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory

import os
n=input()

try:
    k=os.listdir(n)
    print(f'list of all sub-directories and files {k}')
except FileNotFoundError:
    print(f'Directory {n} doesnt exist')

#Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory

import os
n=input()

try:
    k=os.listdir(n)
    sub=[]
    fil=[]
    for x in k:
        if '.' in x:
            fil.append(x)
        else:
            sub.append(x)
    print(f'list of all sub-director {sub}')
    print()
    print(f'list of all files {fil}')
except FileNotFoundError:
    print(f'Directory {n} doesnt exist')

#W # Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

import os
n=input()
k=os.walk(n)
while(True):
    try:
        print(next(k))
    except:
        break
        
