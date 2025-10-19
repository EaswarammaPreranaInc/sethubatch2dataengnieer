
#Write  a  method  to  reverse  linked  list
from single_linked_list import *
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
