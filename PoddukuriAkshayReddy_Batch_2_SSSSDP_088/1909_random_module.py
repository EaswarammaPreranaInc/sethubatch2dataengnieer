
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

# import random
# for i in range(10):
#   for j in range(6):
#     print(random.randint(0,9),end='')
#   print()
'''
258447
739842
112185
681428
054290
219889
056740
845508
384423
678123
456789
'''


# Find  outputs
import  os
# os . system('dir')
# os . system('pause')
# os . system('cls')
# os . system('py  test.py')


'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory


Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created


Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists


Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created
'''

# dname=input("Enter directory name (or) path : ")
# try:
#     os.makedirs(dname)
#     print("Directory",dname,"created")
# except FileExistsError:
#     print("Directory",dname,"already exists")
# except Exception as e:
#     print("Error:",e)


'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c

# Enter  directory  path :  a/b/c
# Directory  (or) directories  created
'''


# dname=input("Enter directory path : ")
# try:
#     os.makedirs(dname)
#     print("Directory (or) directories created")
# except FileExistsError:
#     print("Directory",dname,"already exists")
    
'''

Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory


Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed


Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist


Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty

'''  
    
# dname=input("Enter directory name (or) path : ")
# try:
#     os.rmdir(dname)
#     print("Directory",dname,"is removed")
# except FileNotFoundError:
#     print("Directory",dname,"does not exist")
# except OSError:
#     print("Directory",dname,"is non-empty")   
    
    
'''

Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path

Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name
'''

# dname = input("Enter the directory name to be removed:")
# try:
#     os.removedirs(dname)
#     print("Directory (or) directories removed")
# except FileNotFoundError:
#     print("Directory",dname,"does not exist")



'''

Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories


Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']

List  of  the  directories :   ['dir1', 'dir2']

'''

# dname = input("Enter directory name or path: ")
# try:
#     files = []
#     dirs = []
#     for item in os.listdir(dname):
#         if os.path.isfile(os.path.join(dname, item)):
#             files.append(item)
#         elif os.path.isdir(os.path.join(dname, item)):
#             dirs.append(item)
#     print("List of the files :", files)
#     print("List of the directories :", dirs)
# except FileNotFoundError:
#     print("Directory", dname, "does not exist")
    
    
    
'''
# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

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

# dname = input("Enter the directory path: ")
# try:
#     for root, dirs, files in os.walk(dname):
#         print("Directory Path :", root)
#         print("Sub Directories :", dirs)
#         print("Files :", files)
# except FileNotFoundError:
#     print("Directory", dname, "does not exist")
    
    
    
''''
Write a program to rename the file and directory

Input is filename (or) directory name
'''
old_name = input("Enter the old file (or) directory name: ")
new_name = input("Enter the new file (or) directory name: ")
try:
    os.rename(old_name, new_name)
    print("Renamed", old_name, "to", new_name)
except FileNotFoundError:
    print("File (or) Directory", old_name, "does not exist")
except FileExistsError:
    print("File (or) Directory", new_name, "already exists")
except Exception as e:
    print("Error:", e)
    