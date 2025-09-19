#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
############ program ###########
from random import *

for i in range(10):
    print(randrange(000000,999999))

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

# Find  outputs
import  os
os . system('dir') # prints all  the  files  and  folders  in  the  current  directory
os . system('pause') # pauses  the  execution  of  the  program  until  user  presses  any  key
os . system('cls') # clears  the  console  screen
os . system('py  test.py') # executes  the  python  program  named  test.py


Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
######### program ##########
import  os
try:
    a = input('Enter  directory  name  (or) path :')
    b = os.mkdir(a)
    print(F'Directory  {a}  created  successfully')
except FileExistsError:
    print(F'Directory  {a}  already  exists')

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists

Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
############ program ############
import  os
try:
    a = input('Enter  directory path :')
    b = os.makedirs(a)
    print(F'Directory  {a}  created  successfully')
except FileExistsError:
    print(F'Directory  {a}  already  exists')

Enter  directory  path :  a/b/c
Directory  (or) directories  created

Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
########### program #############
import  os
try:
    a = input('Enter  directory  name  (or) path :')
    b = os.rmdir(a)
    print(F'Directory  {a}  removed  successfully')
except FileNotFoundError:
    print(F'Directory  {a}  not  found')
except OSError:
    print(F'Directory  {a}  is  non-empty')


Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty


Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
########### program #############
import  os
try:
    a = input('Enter  directory  name  (or) path :')
    b = os.removedirs(a)
    print(F'Directory  {a}  removed  successfully')
except FileNotFoundError:
    print(F'Directory  {a}  not  found')
except OSError:
    print(F'Directory  {a}  is  not  empty')

Write  a  program  to  rename  a  file  and  directory
Input  is  filename  (or)  directory  name
############# program #############
import  os
try:
    a = input('Enter  filename  (or)  directory  name:')
    c = input('Enter  new  name  of  the  file  (or)  directory  :')
    b = os.rename(a, c)
    print(F'Directory  {a}  renamed  successfully')
except FileNotFoundError:
    print(F'Directory  {a}  not  found')
except FileExistsError:
    print(F'Directory  {c}  already  exists')

Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
############# program ###############
import  os

try:
    a = input('Enter  directory  name (or) path :  ')
    files = []
    dirs = []
    for i in os.listdir(a):
        if '.' in i:
            files.append(i)
        else:
            dirs.append(i)
    print('List  of  the  files :  ' , files)
    print()
    print('List  of  the  directories :  ' , dirs)
except FileNotFoundError:
    print(F'Directory  {a}  not  found')

Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']


# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
############# program ##################
import  os
try:
    a = input('Enter  directory  name (or) path :  ')
    for dirpath, dirnames, filenames in os.walk(a):
        print()
        print('Directory  Path :  ' , dirpath)
        print('Sub  Directories :  ' , dirnames)
        print('Files :  ' , filenames)
except FileNotFoundError:
    print(F'Directory  {a}  not  found')
except Exception as e:
    print(e)

Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']

Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']

Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []