
'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''


from Tarun_Banala import datatype,number,string 
while True:
    try:
        ch=eval(input("Enter number/string/exit: "))
        obj1=ch()
        obj2=ch()
        # ch.get()
        obj1.get()
        obj2.get()
        obj3=ch()
        obj3.add(obj1,obj2)
        obj3.display()
    except:
        break
print("Good Bye")
