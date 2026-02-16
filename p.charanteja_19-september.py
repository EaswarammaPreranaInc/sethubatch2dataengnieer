# 6-Digit OTP Generation (with leading zeros)

import random

otp = str(random.randint(0, 999999)).zfill(6)
print("Your OTP is:", otp)
#This ensures the OTP is formatted with six digits, including leading zeros like "000156".







# Directory Creation Program

import os

path = input("Enter directory name (or) path: ")
if not os.path.exists(path):
    os.makedirs(path)
    print(f"Directory {path} created")
else:
    print(f"Directory {path} already exists")

# If the path exists, shows it's already present.








# Group of Directories Creation

import os

path = input("Enter directory path: ")
try:
    os.makedirs(path, exist_ok=True)
    print("Directory (or) directories created")
except Exception as e:
    print("Error:", e)

#Creates nested directory structure "a/b/c" in one step.






# Directory Deletion Program

import os

path = input("Enter directory name (or) path: ")
try:
    os.rmdir(path)
    print(f"Directory {path} is removed")
except FileNotFoundError:
    print(f"Directory {path} does not exist")
except OSError:
    print(f"Directory {path} is non-empty")

#If directory is non-empty, `os.rmdir` raises `OSError`. For recursive deletion, use `shutil.rmtree`.






# Group of Directories Deletion

import shutil

path = input("Enter directory path: ")
try:
    shutil.rmtree(path)
    print("Directory and subdirectories deleted")
except FileNotFoundError:
    print("Directory does not exist")
except Exception as e:
    print("Error:", e)

#Removes a directory and all its contents.






# Rename File or Directory Program

import os

old_name = input("Enter old file/directory name: ")
new_name = input("Enter new file/directory name: ")
try:
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} to {new_name}")
except Exception as e:
    print("Error:", e)

#Handles both file and directory renaming.






# List Files and Subdirectories in a Directory

import os

path = input("Enter directory name (or) path: ")
files = []
dirs = []

with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            files.append(entry.name)
        elif entry.is_dir():
            dirs.append(entry.name)
print("List of the files :", files)
print("List of the directories :", dirs)

#Prints lists of files and directories.







# Iterate Through Directory Tree

import os

def print_tree(path):
    for root, dirs, files in os.walk(path):
        print("Directory Path :", root)
        print("Sub Directories :", dirs)
        print("Files :", files)
        print()

path = input("Enter directory name (or) path: ")
print_tree(path)

#This traverses all subdirectories and lists their contents as described ("sairam", "sairam/karnataka", etc.).

