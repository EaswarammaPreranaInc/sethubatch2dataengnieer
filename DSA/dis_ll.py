
#  Write  destructor  to  delete  whole  linked  list
from single_linked_list import *
class  sll(linked_list):
    def __del__(a):
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
