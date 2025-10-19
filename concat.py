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

    