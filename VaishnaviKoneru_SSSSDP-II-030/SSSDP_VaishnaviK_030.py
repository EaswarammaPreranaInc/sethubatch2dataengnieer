# Find  outputs
'''
import  os
os . system('dir')# path of current working directory
os . system('pause')#  
os . system('cls')
os . system('py  test.py')

Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
[11:50, 9/19/2025] +91 99482 50500: Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created
[11:51, 9/19/2025] +91 99482 50500: Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists
[11:52, 9/19/2025] +91 99482 50500: Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created

'''
try:
    import sys
    import os
    s = input("enter directory name : ")
    if s in 'C:\\Users\\User\\Downloads>':
        pass
    else:
        os.mkdir(s)
except:
    print('File Already Exist')

'''
[11:53, 9/19/2025] +91 99482 50500: 
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c

[11:53, 9/19/2025] +91 99482 50500: Enter  directory  path :  a/b/c
Directory  (or) directories  created
[12:01, 9/19/2025] +91 99482 50500: Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
[12:02, 9/19/2025] +91 99482 50500: Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed
[12:03, 9/19/2025] +91 99482 50500: Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist
[12:03, 9/19/2025] +91 99482 50500: Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
[12:04, 9/19/2025] +91 99482 50500: Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
[12:10, 9/19/2025] +91 99482 50500: Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name
[12:14, 9/19/2025] +91 99482 50500: Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
[12:16, 9/19/2025] +91 99482 50500: Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']
[12:32, 9/19/2025] +91 99482 50500: # Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
[12:33, 9/19/2025] +91 99482 50500: Directory  Path :  sairam
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']
[12:34, 9/19/2025] +91 99482 50500: Directory  Path :  sairam\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']
[12:34, 9/19/2025] +91 99482 50500: Directory  Path :  sairam\karnataka\banglore
Sub  Directories :  []
Files :  []
'''