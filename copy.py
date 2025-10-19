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