#Find  outputs
import  os
os . system('dir') # All the files and sub directories
os . system('pause') # System will pause until we press any key
os . system('cls') # Clears screen 
os . system('mod111.py') # Runs mod111.py



#Write  a  program  to  create  a  directory.Input  is  directory  name  (or)  path  of  the  directory
import os
dir = input("Enter  directory  name  (or) path : ")
try:
    os.mkdir(dir)
    print(f"Directory {dir} created")
except FileExistsError:
    print(f'Directory {dir} already exists')
'''
Enter  directory  name  (or) path : ssssdp2
Directory ssssdp2 created

Enter  directory  name  (or) path : ssssdp2
Directory ssssdp2 already exists

Enter  directory  name  (or) path : ssssdp2/khairtabad
Directory ssssdp2/khairtabad created
'''



# Write  a  program  to  create  a  group  of  directories.Input : a/b/c
import os 
dir = input("Enter  directory  path :  ")
try:
    os.makedirs(dir)
    print(f"Directory  (or) directories created")
except FileExistsError:
    print(f'Directory {dir} already exists')
'''
Enter  directory  path :  ssssdp/khairtabad/pillno176
Directory  (or) directories created
'''


# Write  a  program  to  delete  a  directory.
import os
try:
    dir = input("Enter  directory  name  (or)  path : ")
    os.rmdir(dir)
    print(f"Directory {dir} is removed")
except FileNotFoundError:
    print(f"Directory {dir} does not exist")
except OSError:
    print(f"Directory {dir} is non-empty")
'''
Enter  directory  name  (or)  path :  n1
Directory n1 is  removed

Enter  directory  name  (or)  path :  n1
Directory n1  does  not  exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
'''



# Write  a  program  to  delete  a  group  of  directories

import os 
dir = input("Enter  directory  path :  ")
try:
    os.removedirs(dir)
    print(f"Directory  (or) directories removed")
except FileNotFoundError:
    print(f'Directory {dir} not exists')
except OSError:
    print(f'Directoty {dir} is not empty')
'''
Enter  directory  path :  ssssdp/khairtabad/pillno176
Directory  (or) directories 
'''


# Write  a  program  to  rename  a  file  and  directory
import os
old_dir_or_file = input("Enter Directory or File to be renamed : ")
new_dir_or_file = input("Enter new name : ")
try:
    os.rename(old_dir_or_file,new_dir_or_file)
    print("Renamed")
except FileExistsError:
    print("File or directory with same name is exist")
except FileNotFoundError:
    print("The file or directory which you want to be renamed is not exist")

'''
Enter Directory or File to be renamed : n1
Enter new name : n2
Renamed
'''



# Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
import os
dir = input("Enter  directory  name (or) path : ")
a = []
b = []
try:
    list = os.listdir(dir)
    for i in list:
        if "." in i:
            a.append(i)
        else:
            b.append(i)
    print("List  of  the  files : ", a)
    print()
    print("List  of  the  directories :  ", b)
except FileNotFoundError:
    print("Directory is not found")
'''
Enter  directory  name (or) path : C:\sairam
List  of  the  files :  ['sample.py']

List  of  the  directories :   []
'''


import os
dir = input("Directory Path : ")
for root, dirs, files in os.walk(dir):
    print("Directory Path :", root)
    print("Sub Directories :", dirs)
    print("Files :", files)
    print()
    os.system('pause')
    os.system('cls')