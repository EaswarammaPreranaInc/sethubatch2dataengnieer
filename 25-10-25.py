'''Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8


from 24-10-25_abstract_method import number,string

while True:
    x=input('Enter number/ string /exit :').lower()
    if x =='number':
        a = [number(), number(), number()]  
    elif x=='string':
        a = [string(), string(), string()] 
    elif x=='exit':
        print('Good Bye')
        break
    a[0].get()
    a[1].get()
    a[2].add(a[0],a[1])
    a[2].display()

'''                