#TARUN BANALA            FILE HANDLING    07-11-2025
# Program: Create file using writelines()
def create(f):
    print('Enter text terminated by ctrl+z')
    lines = []                                   # To store all input lines
    try:
        while True:
            line = input()                       # Read line from keyboard
            lines.append(line + '\n')            # Add newline and store
    except EOFError:
        f.writelines(lines)                      # Write list to file
        print(f'File {f.name} is created')       # Output: File sample.txt is created
# End of function

fname = input('Enter filename: ')                # Example input: sample.txt
f = open(fname, 'w')                             # Open file in write mode
create(f)
f.close()
# Output: File sample.txt is created

# Program: Display file data
def disp(f):
    data = f.read()                              # Read entire file
    print(f'Data of the file {f.name}')          # Output: Data of the file sample.txt
    print(data)                                  # Output: (File contents)
# End of function

fname = input('Enter filename: ')                # Example input: sample.txt
f = open(fname, 'r')                             # Open file in read mode
disp(f)
f.close()
# Output:
# Data of the file sample.txt
# Rama Rao
# 9247
# +-$
# Hyd is green city

import os

# Program: Display file pagewise (20 lines per page)
def disp(f):
    count = 0
    line = f.readline()
    while line:
        print(line, end='')                      # Print each line
        count += 1
        if count == 20:                          # After every 20 lines
            os.system('pause')                   # Pause
            os.system('cls')                     # Clear screen
            count = 0
        line = f.readline()
# End of function

fname = input('Enter filename: ')                # Example input: sample.txt
f = open(fname, 'r')                             # Open file in read mode
disp(f)
f.close()
# Output: Displays file data pagewise (pauses after every 20 lines)

