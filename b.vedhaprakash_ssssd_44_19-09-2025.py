# home works question on 19/09/2025
1
--------------
# Generate 10 OTPs (6-digit, including leading zeros)
import random

for _ in range(10):
    otp = random.randint(0, 999999)
    print(f"{otp:06d}")

# Sample Output:
# 258447
# 739842
# 112185
# 681428
# 054290
# 219889
# 056740
# 845508
# 384423
# 587572

2
--------------
# Find outputs – using os.system()
import os

os.system('dir')
os.system('pause')
os.system('cls')
os.system('py test.py')

3
--------------
# Create a Directory
import os

dir_name = input("Enter directory name (or) path : ")
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} created")
else:
    print(f"Directory {dir_name} already exists")

# Sample Runs:
# Enter directory name (or) path : sssdc2
# Directory sssdc2 created
# Enter directory name (or) path : sssdc2
# Directory sssdc2 already exists
# Enter directory name (or) path : sssdc2/khairtabad
# Directory sssdc2/khairtabad created

4
--------------
# Create a Group of Directories
import os

dir_path = input("Enter directory path : ")
os.makedirs(dir_path, exist_ok=True)
print("Directory (or) directories created")

# Sample Run:
# Enter directory path : a/b/c
# Directory (or) directories created

5
--------------
# Delete a Directory
import os
import shutil

dir_name = input("Enter directory name (or) path : ")
if os.path.exists(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"Directory {dir_name} is removed")
    except OSError:
        print(f"Directory {dir_name} is non-empty")
else:
    print(f"Directory {dir_name} does not exist")

# Sample Runs:
# Enter directory name (or) path : temp
# Directory temp is removed
# Enter directory name (or) path : temp
# Directory temp does not exist
# Enter directory name (or) path : sairam
# Directory sairam is non-empty

6
--------------
# Delete a Group of Directories
import shutil
import os

dir_path = input("Enter directory path : ")
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
    print(f"Directory {dir_path} and all sub-directories removed")
else:
    print(f"Directory {dir_path} does not exist")

7
--------------
# Rename a File or Directory
import os

old_name = input("Enter filename (or) directory name to rename: ")
new_name = input("Enter new name: ")
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"{old_name} renamed to {new_name}")
else:
    print(f"{old_name} does not exist")

8
--------------
# Print All Files and Sub-directories of Input Directory
import os

dir_path = input("Enter directory name (or) path : ")
all_files = []
all_dirs = []

for item in os.listdir(dir_path):
    full_path = os.path.join(dir_path, item)
    if os.path.isfile(full_path):
        all_files.append(item)
    elif os.path.isdir(full_path):
        all_dirs.append(item)

print("List of the files : ", all_files)
print("List of the directories : ", all_dirs)

# Sample Output:
# Enter directory name (or) path : c:\sssdc2
# List of the files :   ['file1.txt', 'file2.txt', 'file3.txt']
# List of the directories :   ['dir1', 'dir2']

9
--------------
# Iterate Through a Directory (sairam)
import os

def iterate_dir(path):
    print(f"Directory Path : {path}")
    sub_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Sub Directories : ", sub_dirs)
    print("Files : ", files)
    for d in sub_dirs:
        iterate_dir(os.path.join(path, d))

iterate_dir("sairam")

# Sample Output:
# Directory Path : sairam
# Sub Directories :  ['karnataka', 'Telangana']
# Files :  ['file1.txt', 'file2.txt', 'file3.txt']
# Directory Path : sairam\karnataka
# Sub Directories :  ['banglore']
# Files :  ['file1.txt']
# Directory Path : sairam\karnataka\banglore
# Sub Directories :  []
# Files :  []
