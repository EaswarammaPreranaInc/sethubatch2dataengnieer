
#  Write  a  program   to  determine  length  of  linked  list
from linked_list import *
class sll(linked_list):
    def length(a):
        c=0
        p=a.first
        while p!=None:
            c+=1
            p=p.link
        return c
if _name=='main_':
    a=sll()
    a.create()
    print("Length of Linked List is : ",a.length())

#Write  a  progam  to  determine  data  of  ith  node
from LLlen import *
class s_list(sll):
    def find(a,i):
        p=a.first
        for x in range(i-1):
            p=p.link
        return p.data
a=s_list()
a.create()
while True:
    i=int(input("Enter value of i : "))
    if i<1 or i>a.length():
        print(f"Node {i} does not exist")
    else:
        print("Data of Node {i} is : ",a.find(i))
    ch=input('Do  you  wish  to  continue (y / n) :  ')
    if  ch == 'N'  or  ch == 'n':
        break

#Write  a  method  to  search  for  a  value  in  the  linked  list.   
from linked_list import *
class search_ll(linked_list):
    def search(a,x):
        p=a.first
        while p:
            if p.data==x:
                return p
            p=p.link
        return None
a=search_ll()
a.create()
while True:
    n=int(input("Enter Value to be searched : "))
    x=a.search(n)
    if x==None:
        print(f"{n} is not found ")
    else:
        print(f'{n} is found at address : ',x)
    ch=input('Do  you  wish  to  continue (y / n) :  ')
    if  ch == 'N'  or  ch == 'n':
        break
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

        
            
        
#Write  a  funciton  to  concatenate  two  linked  lists
from linked_list import *
class llist(linked_list):
    def concat(a,b):
        if a.isempty():
            a.first=b.first
        else:
            p=a.first
            while p.link:
                p=p.link
            p.link=b.first
a=llist()
b=llist()
a.create()
b.create()
a.concat(b)
print("Linked List is : ")
a.disp()

    
#  Write  a  method  to  copy  a  linked  list
from linked_list import *
class sll(linked_list):
    def copy(a):
        b=sll()
        p=a.first
        while p:
            new=node(p.data)
            b.append(new) 
            p=p.link
        return b
a=sll()
a.create()
b=a.copy()
print('Original  linked   list  :  ' , end = '')
a.disp()
print('Copied  linked   list  :  ' , end = '')
b.disp()

#  Write  destructor  to  delete  whole  linked  list
from linked_list import *
class  sll(linked_list):
    def _del_(a):
        p=a.first
        while p:
            temp=p.link
            del p
            p=temp
        a.first=None
        print('Linked  list  is  empty')
#  End  of  the  clas
a=sll()
a.create()
del a

#Write  a  method  to  reverse  linked  list
from linked_list import *
class l_reverse(linked_list):
    def reverse(a):
        prev=None
        cur=a.first
        next=a.first.link
        while next!=None:
            cur.link=prev
            prev=cur
            cur=next
            next=next.link
        cur.link=prev
        a.first=cur
a=l_reverse()
a.create()
print('Input  Linked  List')
a.disp()
a.reverse()
print('Reverse  Linked  List')
a.disp()
