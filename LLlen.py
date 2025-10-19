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
if __name__=='__main__':
    a=sll()
    a.create()
    print("Length of Linked List is : ",a.length())

