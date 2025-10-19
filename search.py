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