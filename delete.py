#Write  a method  to  delete  ith  node  of  linked  list

from LLlen import *
class N_delete(sll):
    def delete(a,i):
        if i<1 or i>a.length():
            return None
        elif i==1:
            temp=a.first
            x=temp.data
            a.first=a.first.link
            del temp
            return x
        else:
            p=a.first
            for j in range(i-2):
                p=p.link
            temp=p.link
            p.link=temp.link
            x=temp.data
            del temp
            return x
a=N_delete()
a.create()
while True:
    i=int(input("Enter position of i to be deleted : "))
    x=a.delete(i)
    if x==None:
        print("Node {i} does not exist")
    else:
        print('Data  of  deleted  node  is  ' ,  x)
    print('Linked List is : ')
    a.disp()
    ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
    if  ch == 'n'  or  ch=='N':
        break

        
            
        