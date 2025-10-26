'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer to prog8
'''
import prog7b as pro

while True:
    ch = input("Enter number/string/exit : ").lower()

    if ch == "number":
    	a = [pro.number(), pro.number(), pro.number()]    # How to create list of 3 number class objects
    elif ch == "string":
    	a = [pro.string(), pro.string(), pro.string()]    # How to create list of 3 string class objects
    else:
    	break     
                                           
    a[0].get()
    a[1].get()
    a[2].add(a[0], a[1]) 
    a[2].display()                                     
# end of while loop
print("Good Bye")

