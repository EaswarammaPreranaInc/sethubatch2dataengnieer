#Write  a  program  to  create  a  directory.
#Input  is  directory  name  (or)  path  of  the  directory
import os 
a=input("enter directory name to create:")
os.mkdir(a)
print("directory created")

#Write  a  program  to  create  a  group  of  directories
import os 
a=input("enter directory name to delete:")
os.makedirs(a)
print("directories created")


#Write  a  program  to  delete  a  directories.
#Input  is  directory  name  (or)  path  of  the  directory
import os
a=input("enter directory name to delete:")
os.removedirs(a)
print("directory deleted")


import os

print("Current working directory:", os.getcwd())



#Write  a  program  to  rename  a  file  and  directory
import os
a= input("enter old filename :")
b=input("enter new filename:")
os.rename(a,b)
print("new filename is updated")

enter old filename :sairam
enter new filename:sairam1
new filename is updated



#Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
import os
a=[]
b=""
path=input("enter directory name or path: ")
s=os.listdir(path)
for i in s:
  if i.endswith(".txt") or i.endswith(".py"):
      a.append(i)
  else: 
      b+=i
print("textfiles-",a)
print()
print("directories-",b)
enter directory name or path: c:\\learnpython
textfiles- ['class and without class.py', 'GSurya_Sravani_12_04th_August.py', 'GSurya_Sravani_12_04th_july.py', 'GSurya_Sravani_12_06th_August.py', 'GSurya_Sravani_12_07th_August.py', 'GSurya_Sravani_12_15th_july.py', 'GSurya_Sravani_12_16th_july.py', 'GSurya_Sravani_12_17th_july.py', 'GSurya_Sravani_12_18th_july.py', 'GSurya_Sravani_12_19th_july.py', 'GSurya_Sravani_12_21st_july.py', 'GSurya_Sravani_12_22nd_july.py', 'GSurya_Sravani_12_23rd_july.py', 'GSurya_Sravani_12_24th_july.py', 'GSurya_Sravani_12_30th_july.py', 'interview_questions.txt', 'mypython.py']

directories- .ideaclass and objects





# Find  outputs
import os

os.system('dir')        # Lists all files and directories in the current folder 
os.system('pause')      # Pauses execution, waits for user to "Press any key to continue..."
os.system('cls')        # Clears the terminal/command prompt screen
os.system('py test.py') # Runs the Python file test.py

