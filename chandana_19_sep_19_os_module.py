#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
a='0123456789'
for i in range(10):
    for j in range(6):
        print(random.choice(a),end='')
    print()
'''
o/p:
256427
015758
346437
305467
803055
233977
296190
764192
818519
142724
'''



# Find  outputs
import  os
os . system('dir')  #  list all files and folders in the current working directory
os . system('pause')  # pause the execution of the current program 
os . system('cls') # clears the command prompt window
os . system('py  test.py') # runs the  python interpreter with the file test.py



# Write  a  program  to  create  a  directory. Input  is  directory  name  (or)  path  of  the  directory
import os
try:
    x=input("enter directory name (or) path : ")
    os.mkdir(x)
    print(f'Directory {x} created')
except FileExistsError:
    print(f'Directory {x} already exists')

'''
o/p:
enter directory name (or) path : s
Directory s created

enter directory name (or) path : s
Directory s already exists
'''


# Write  a  program  to  create  a  group  of  directories. Input :  a/b/c
import os
try:
    x=input("enter directory name (or) path : ")
    os.makedirs(x)
    print(f'Directory {x} created')
except FileExistsError:
    print(f'Directory {x} already exists')
'''
o/p:
enter directory name (or) path : a/b/c
Directory a/b/c created

enter directory name (or) path : a/b/c
Directory a/b/c already exists
'''



# Write  a  program  to  delete  a  directory. Input  is  directory  name  (or)  path  of  the  directory
import os
try:
    x=input("Enter directory name (or) path :")
    os.rmdir(x)
    print(f'Directory {x} is removed')
except FileNotFoundError:
    print(f'Directory {x} does not exist')
'''
o/p:
Enter directory name (or) path :s
Directory s is removed
'''


# Write  a  program  to  delete  a  group  of  directories. Input  is  directory  path
import os
try:
    x=input("Enter directory name (or) path :")
    os.removedirs(x)
    print(f'Directory {x} is removed')
except FileNotFoundError:
    print(f'Directory {x} does not exist')
'''
o/p:
Enter directory name (or) path :a/b/c
Directory a/b/c is removed
'''



# Write  a  program  to  rename  a  file  and  directory. Input  is  filename  (or)  directory  name
import os
x=input("Enter the file/directory name (or path) to rename: ")
y=input("Enter the new name (or path): ")
try:
    os.rename(x,y)
    print(f"Renamed '{x}' to '{y}' successfully.")
except FileNotFoundError:
    print(f"'{x}' does not exist.")
    
'''
o/p:
Enter the file/directory name (or path) to rename: file1
Enter the new name (or path): file2
Renamed 'file1' to 'file2' successfully.
'''


'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import os
x=input("Enter directory name (or) path: ")
try:
    y=os.listdir(x)
    a=[]
    b=[]
    for i in y:
        if '.' in i:
            a.append(i)
        else:
            b.append(i)
    print("list of files: ",a)
    print("list of directories: ",b)
except FileNotFoundError:
    print(f"Directory '{x}' does not exist.")
'''
o/p:
Enter directory name (or) path: a/b
list of files:  ['ab.text']
list of directories:  ['a']
'''


# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import os
x=input("Enter a directory (or) path: ")
g=os.walk(x)
try:
    while True:
        tup=next(g)
        print('Directory path: ',tup[0])
        print('Sub Directories: ',tup[1])
        print('Files: ',tup[2])
        input('Enter any key to see next iteration...')
        print()
except:
    print("completely Iterated")
