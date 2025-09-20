from random import *
for i in range(10):
   b=''
   for j in range(6):
      val=randint(0,9)
      b=b+str(val)
   print(b)

 #  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
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


#================================================ # Find  outputs

import  os
os . system('dir')
os . system('pause')
os . system('cls')
os . system('py  cal.py')

# Write  a  program  to  create  a  directory.
import os
dirname = input("(creates)Enter directory name (or) path: ")
try:
    os.mkdir(dirname)
    print(f"Directory {dirname} created")
except FileExistsError:
    print(f"Directory {dirname} already exists")
except Exception as e:
    print("Error:", e)


'''
Input  is  directory  name  (or)  path  of  the  directory

 Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created

 Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists

Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created
'''
#==============================================================
#Write  a  program  to  create  a  group  of  directories.

import os
dirname = input("(create)Enter directory name (or) path: ")
try:
    os.makedirs(dirname, exist_ok=False)
    print(f"Directory {dirname} created")
except FileExistsError:
    print(f"Directory {dirname} already exists")
except Exception as e:
    print("Error:", e)

'''
Input :  a/b/c
'''

#================================================
#Remove sun dir
import os
dirname = input("(remove single)Enter directory name (or path): ")
try:
    os.rmdir(dirname)
    print(f"Directory {dirname} deleted")
except FileNotFoundError:
    print(f"Directory {dirname} does not exist")
except OSError:
    print(f"Directory {dirname} is not empty")
except Exception as e:
    print("Error:", e)

'''
# Enter  directory  path :  a/b/c
# Directory  (or) directories  created

# Write  a  program  to  delete  a  directory
Input  is  directory  name  (or)  path  of  the  directory

# Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed


# Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist

# Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
'''
#================================================
# Write  a  program  to  delete  a  group  of  directories

import os
path = input("(total dir with)Enter directory path : ")
try:
    os.removedirs(path)
    print(f"Directories {path} deleted")
except FileNotFoundError:
    print(f"Directory path {path} does not exist")
except OSError:
    print(f"Cannot delete {path} — one of the directories is not empty")
except Exception as e:
    print("Error:", e)

#================================================
#Write  a  program  to  rename  a  file  and  directory

import os
old_name = input("Enter current file/directory name (or path): ")
new_name = input("Enter new file/directory name (or path): ")

try:
    os.rename(old_name, new_name)
    print(f"{old_name} renamed to {new_name}")
except FileNotFoundError:
    print(f"{old_name} does not exist")
except FileExistsError:
    print(f"{new_name} is already exist")
except Exception as e:
    print("Error:", e)


#================================================
# Write  a  program  to  print  all  the  files  and  sub-directories of  input  directory

import os
path = input("Enter directory name (or) path: ")
try:
    files = []
    dirs = []

    for x in os.listdir(path):
        full_path = os.path.join(path, x)
        if os.path.isfile(full_path):
            files.append(x)
        elif os.path.isdir(full_path):
            dirs.append(x)
    print("List of the files      :", files)
    print("List of the directories:", dirs)
except FileNotFoundError:
    print(f"Directory {path} does not exist")
except Exception as e:
    print("Error:", e)

#OooooooooooooooooRRRrrrrrrrrrrrrrrrrr

import os
dir=input("Enter the path or dir: ")
list=os.listdir(dir)
a=[]
b=[]
try:
   for x in list:
      if '.' in x:
          a.append(x)
      else:
          b.append(x)
   print("list of files: ",a)
   print()
   print("list of dir: ",b)
except FileNotFoundError:
    print(f"Directory {path} does not exist")



'''
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

# Enter  directory  name (or) path :  c:\sssdc2
List  of  the  files :   ['file1.txt', 'file2.txt', 'file3.txt']
List  of  the  directories :   ['dir1', 'dir2']

'''

#================================================
# Write  a  program  to  iterate  thru  sairam  directory  present in  current  working  directory

import os
path = input("Enter directory name (or path): ")
if os.path.exists(path) and os.path.isdir(path):
   for root, dirs, files in os.walk(path):
      print("Directory Path :", root)
      print("Sub Directories:", dirs)
      print("Files          :", files)
      os.system('pause')
      os.system('cls')
else:
   print(f"Directory '{path}' does not exist or is not a directory")

#OoooooooooooooooooRrrrrrrrrrrrrrrrrr

import os
path=input("enter the path or dir : ")
g=os.walk(path)
while True:
   try:
      tpl=next(g)
      print('directory path: ',tpl[0])
      print('sub path: ',tpl[1])
      print('Files : ',tpl[2])
      os.system('pause')
      os.system('cls')
   except :
      break

'''
#================================================
Directory  Path :  sai
Sub  Directories :  ['karnataka', 'Telangana']
Files :  ['file1.txt', 'file2.txt', 'file3.txt']


Directory  Path :  sai\karnataka
Sub  Directories :  ['banglore']
Files :  ['file1.txt']


Directory  Path :  sai\karnataka\banglore
Sub  Directories :  []
Files :  []
'''
