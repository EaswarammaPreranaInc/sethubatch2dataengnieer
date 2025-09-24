import os
os.system('dir')      # lists current directory contents
os.system('pause')    # waits for user to press a key
os.system('cls')      # clears the screen
os.system('py test.py')  # runs test.py file

import os
dirname = input("Enter directory name (or) path: ")
if not os.path.exists(dirname):
    os.mkdir(dirname)
    print(f"Directory {dirname} created")
else:
    print(f"Directory {dirname} already exists")

"""
Enter directory name (or) path : sssdc2
Directory sssdc2 created

Enter directory name (or) path : sssdc2
Directory sssdc2 already exists

Enter directory name (or) path : sssdc2/khairtabad
Directory sssdc2/khairtabad created
"""

path = input("Enter directory path: ")
os.makedirs(path, exist_ok=True)
print("Directory (or) directories created")

"""
Enter directory path : a/b/c
Directory (or) directories created
"""

# Program: delete a directory
dirname = input("Enter directory name (or) path: ")
if os.path.exists(dirname):
    try:
        os.rmdir(dirname)
        print(f"Directory {dirname} is removed")
    except OSError:
        print(f"Directory {dirname} is non-empty")
else:
    print(f"Directory {dirname} does not exist")

"""
Enter directory name (or) path : temp
Directory temp is removed

Enter directory name (or) path : temp
Directory temp does not exist

Enter directory name (or) path : sairam
Directory sairam is non-empty
"""

path = input("Enter directory path: ")
try:
    os.removedirs(path)
    print("Group of directories removed")
except FileNotFoundError:
    print("Path not found")
except OSError:
    print("Directory not empty or cannot be removed")

src = input("Enter file/directory name to rename: ")
dst = input("Enter new name: ")
if os.path.exists(src):
    os.rename(src, dst)
    print(f"{src} renamed to {dst}")
else:
    print(f"{src} does not exist")

path = input("Enter directory name (or) path: ")
if os.path.exists(path):
    files = []
    dirs = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
        else:
            dirs.append(item)
    print("List of the files :", files)
    print("List of the directories :", dirs)
else:
    print("Directory does not exist")

"""
Enter directory name (or) path : c:\\sssdc2
List of the files : ['file1.txt', 'file2.txt', 'file3.txt']
List of the directories : ['dir1', 'dir2']
"""

path = "sairam"
for dirpath, dirnames, filenames in os.walk(path):
    print("Directory Path :", dirpath)
    print("Sub Directories :", dirnames)
    print("Files :", filenames)
    print()

"""
Directory Path : sairam
Sub Directories : ['karnataka', 'Telangana']
Files : ['file1.txt', 'file2.txt', 'file3.txt']

Directory Path : sairam\\karnataka
Sub Directories : ['banglore']
Files : ['file1.txt']

Directory Path : sairam\\karnataka\\banglore
Sub Directories : []
Files : []
"""
