#Write  a  method  to  insert  a  node  in  the  linked  list
from LLlen import *
class N_insert(sll):
    def insert(self,i,x):
        if i<0 or i>a.length():
            print(f'Node {i} does not exist')
        elif i==0:
            new=node(x)
            new.link=a.first
            a.first=new
        else:
            new=node(x)
            p=a.first
            for x in range(i-1):
                p=p.link
            new.link=p.link
            p.link=new
a=N_insert()
a.create()
while True:
    i=int(input("Enter position of i to be inserted : "))
    x=eval(input("Enter value to be inserted "))
    a.insert(i,x)
    print("Linked List : ")
    a.disp()
    ch=input('Do  you  wish  to  continue (y / n) :  ')
    if  ch == 'N'  or  ch == 'n':
        break
    
            