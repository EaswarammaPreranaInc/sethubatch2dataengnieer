'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer to prog8
'''
from prog7b import * 
while True:
    try:
        inp = eval(input("Enter number/string/exit:"))
        if inp == 'exit':
            break
        classname = eval(inp)
        a = [classname(), classname(), classname()]
        a[0].get()
        a[1].get()
        a[2].add(a[0], a[1])
        a[2].display()
    except:
        print("Please enter number (or) string:")
print("Good Bye")