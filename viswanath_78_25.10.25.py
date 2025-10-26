Q) Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

from abc import *
from prog_7b import number, string   
def menu():
    print('1. Number')
    print('2. String')
    print('3. Exit')
a = []
while True:
    menu()
    choice = int(input('Enter your choice: '))
    if choice == 1:
        c = number()
    elif choice == 2:
        c = string()
    elif choice == 3:
        break
    else:
        print('Invalid choice')
        continue
    c.get()
    c.compute()
    a.append(c)
print('Numbers:')
for i in a:
    if isinstance(i, number):
        i.disp()
print('Strings:')
for i in a:
    if isinstance(i, string):
        i.disp()
print('Good Bye')
