Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
from Addobjects import number, string
if __name__ == '__main__':
    while True:
        data = input('Enter number/string/exit:').lower()
        if data == 'exit':
            break
        elif data == 'number':
            a = [number(), number(), number()]
            a[0].get()
            a[1].get()
            a[2].add(a[0], a[1])
            a[2].display()
        elif data == 'string':
            a = [string(), string(), string()]
            a[0].get()
            a[1].get()
            a[2].add(a[0], a[1])
            a[2].display()
        else:
            print('Invalid input. Please enter number/string/exit:')
    print('Good Bye')
